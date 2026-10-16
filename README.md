# Regional Sales Performance Analysis

**Mini Project | Data Analytics | Microsoft Excel + Python**

## Project Overview
This project analyzes retail sales performance for ABC Electronics across regions and product categories. The objective is to understand sales and profit patterns, compare regional performance, review category contribution, and prepare data-backed business recommendations.

## Business Questions
- Which region contributes the most sales?
- Which product category has the highest sales?
- How do monthly sales change over time?
- What are the overall sales, profit, units sold, average discount, and profit margin?
- Are there missing or duplicate records that should be checked before analysis?

## Tools Used
- **Microsoft Excel:** PivotTables, dashboard, charts, conditional formatting
- **Python:** pandas for data preparation and aggregation; matplotlib for charts
- **GitHub:** project version control and portfolio sharing

## Project Structure
```text
Regional-Sales-Performance/
├── data/
│   └── sales_performance_cleaned.csv
├── excel/
│   └── Analysing Visualizing Regional Sales Performance.xlsx
├── outputs/
│   ├── charts/
│   │   ├── sales_by_region.png
│   │   ├── sales_by_category.png
│   │   └── monthly_sales_trend.png
│   ├── data_quality_report.json
│   ├── sales_by_region.csv
│   ├── sales_by_category.csv
│   └── monthly_sales_trend.csv
├── src/
│   └── analyze_sales.py
├── requirements.txt
└── README.md
```

## Dataset
The source workbook contains sales records with these main fields: Order ID, Order Date, Region, Product Category, Sales Amount, Quantity Sold, Discount (%), and Profit.

The cleaned CSV removes fully blank rows and records missing any required analysis fields. See `outputs/data_quality_report.json` for the row counts and validation summary.

## Key Findings
Based on the valid records extracted from the supplied workbook:

- **Total sales:** ₹10,109,783.69
- **Total profit:** ₹4,032,552.62
- **Valid sales records:** 4,000
- **Top region by sales:** East (₹2,595,496.48)
- **Top product category by sales:** Clothing (₹2,156,007.58)
- **Average discount:** 24.78%

These are descriptive findings, not proof that discounts cause changes in sales or profit.

## How to Run the Python Analysis
1. Install Python 3.10 or newer.
2. Open a terminal in the project folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python src/analyze_sales.py
   ```
5. Updated summary CSV files, KPI JSON, and charts will be saved in `outputs/`.

## Excel Analysis
Open the workbook in the `excel/` folder. It contains the supplied source workbook, including its Pivot and dashboard sheets. In Excel, refresh PivotTables if prompted and verify that the dashboard reflects the latest data.

## Data Quality Notes
- Completely blank rows are excluded from the cleaned CSV.
- Rows with missing required fields are excluded from the analysis-ready dataset.
- Duplicate Order IDs are flagged in the data quality report for review; repeated IDs should not automatically be deleted without confirming the business meaning.
- Check the source data and business definitions before drawing conclusions about unusual profit, discount, or quantity values.

## Suggested Business Recommendations
1. Review the top-performing region and identify which products and customer segments drive its sales.
2. Investigate the lowest-performing region for product mix, pricing, and distribution opportunities.
3. Monitor monthly sales trends and compare them with campaign or seasonal activity where that information is available.
4. Review discount levels alongside profit and margin, rather than using sales alone to judge performance.



## Author
**Partheepan** — Data Analyst Portfolio Project
