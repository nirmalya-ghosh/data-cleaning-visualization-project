# Data Cleaning & Visualization Project

An end-to-end data preprocessing and visual reporting project built around a deliberately messy sales dataset. The project demonstrates how raw operational data becomes analysis-ready data, audit evidence, and an executive-style report.

## Project Objective

Clean a raw sales dataset, document every important quality issue, transform the data into reliable analytical fields, and communicate the cleaned business story with charts and a self-contained HTML report.

## What This Project Demonstrates

- Missing value detection and imputation
- Duplicate record removal
- Invalid date handling
- Invalid numeric value repair
- Categorical text standardization
- Revenue recalculation from source fields
- IQR-based outlier capping
- Data quality audit trail
- Business visualization and storytelling

## Repository Structure

```text
data/
  raw_sales_data.csv
  clean_sales_data.csv
outputs/
  cleaning_summary.csv
  sales_data_report.html
  revenue_by_category.png
  revenue_by_region.png
  monthly_revenue.png
  orders_by_channel.png
  top_products.png
  quantity_vs_revenue.png
src/
  clean_visualize.py
requirements.txt
README.md
```

## Run The Project

```powershell
python src\clean_visualize.py
```

Open the generated report:

```text
outputs\sales_data_report.html
```

## Pipeline Design

1. Generate a realistic raw sales CSV with duplicates, blanks, invalid dates, negative prices, excessive discounts, and extreme order quantities.
2. Standardize text categories such as region, status, and sales channel.
3. Convert dates and numeric columns using safe parsing.
4. Remove unrecoverable invalid rows.
5. Impute recoverable missing values using mode or median strategies.
6. Recalculate revenue from quantity, unit price, and discount.
7. Cap outliers using the IQR method.
8. Export cleaned data, audit metrics, charts, and an HTML report.

## Outputs

- `data/clean_sales_data.csv`: cleaned analysis-ready dataset
- `outputs/cleaning_summary.csv`: audit table of cleaning actions
- `outputs/sales_data_report.html`: final report
- `outputs/*.png`: visual evidence for business findings

## Key Analysis Questions

- Which product categories generate the most revenue?
- Which region performs best?
- How does revenue trend over time?
- Which sales channel receives the most orders?
- Which products are the strongest revenue contributors?

## Portfolio Value

This project is useful as a foundation piece because it shows the practical work that happens before modeling: validating raw data, building trust in derived fields, and making analysis reproducible.
