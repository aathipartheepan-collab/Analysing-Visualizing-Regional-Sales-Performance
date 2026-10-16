"""
Regional Sales Performance Analysis
Run from the project root:
    python src/analyze_sales.py
"""
from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sales_performance_cleaned.csv"
OUT = ROOT / "outputs"
CHARTS = OUT / "charts"
OUT.mkdir(exist_ok=True)
CHARTS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["Order Date"])
df = df.dropna(how="all")
df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)
df["Profit Margin (%)"] = (df["Profit"] / df["Sales Amount"] * 100).round(2)

region = df.groupby("Region", as_index=False).agg(
    Orders=("Order ID", "count"),
    Total_Sales=("Sales Amount", "sum"),
    Total_Profit=("Profit", "sum"),
    Units_Sold=("Quantity Sold", "sum"),
    Average_Discount=("Discount (%)", "mean"),
).sort_values("Total_Sales", ascending=False)
category = df.groupby("Product Category", as_index=False).agg(
    Orders=("Order ID", "count"),
    Total_Sales=("Sales Amount", "sum"),
    Total_Profit=("Profit", "sum"),
    Units_Sold=("Quantity Sold", "sum"),
).sort_values("Total_Sales", ascending=False)
monthly = df.groupby("Order Month", as_index=False).agg(
    Total_Sales=("Sales Amount", "sum"),
    Total_Profit=("Profit", "sum"),
    Orders=("Order ID", "count"),
)

region.to_csv(OUT / "sales_by_region.csv", index=False)
category.to_csv(OUT / "sales_by_category.csv", index=False)
monthly.to_csv(OUT / "monthly_sales_trend.csv", index=False)

kpis = {
    "total_orders": int(len(df)),
    "total_sales": round(float(df["Sales Amount"].sum()), 2),
    "total_profit": round(float(df["Profit"].sum()), 2),
    "total_units_sold": int(df["Quantity Sold"].sum()),
    "average_discount_percent": round(float(df["Discount (%)"].mean()), 2),
    "average_profit_margin_percent": round(float((df["Profit"].sum() / df["Sales Amount"].sum()) * 100), 2),
    "top_region_by_sales": str(region.iloc[0]["Region"]),
    "top_category_by_sales": str(category.iloc[0]["Product Category"]),
}
(OUT / "kpis.json").write_text(json.dumps(kpis, indent=2), encoding="utf-8")

def save_bar(x, y, title, xlabel, filename, rotate=0):
    plt.figure(figsize=(8, 5))
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Sales Amount")
    if rotate:
        plt.xticks(rotation=rotate, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS / filename, dpi=160)
    plt.close()

save_bar(region["Region"], region["Total_Sales"], "Total Sales by Region", "Region", "sales_by_region.png")
save_bar(category["Product Category"], category["Total_Sales"], "Total Sales by Product Category", "Product Category", "sales_by_category.png", 20)

plt.figure(figsize=(9, 5))
plt.plot(monthly["Order Month"], monthly["Total_Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Order Month")
plt.ylabel("Sales Amount")
plt.xticks(rotation=60, ha="right")
plt.tight_layout()
plt.savefig(CHARTS / "monthly_sales_trend.png", dpi=160)
plt.close()

print("Analysis completed.")
print(json.dumps(kpis, indent=2))
