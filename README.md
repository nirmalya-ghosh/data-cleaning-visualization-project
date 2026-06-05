# Data Cleaning & Visualization Project

This project demonstrates a full beginner-friendly data workflow:

- create a messy raw dataset
- handle duplicates, missing values, invalid values, and outliers
- clean and process the data with Pandas
- visualize insights with Matplotlib
- generate a simple HTML dashboard/report

## Project Structure

```text
data/
  raw_sales_data.csv       # generated messy source data
  clean_sales_data.csv     # cleaned output data
outputs/
  *.png                    # generated charts
  cleaning_summary.csv     # cleaning audit metrics
  sales_data_report.html   # visual report
src/
  clean_visualize.py       # main project script
```

## Run

```powershell
python src/clean_visualize.py
```

Then open:

```text
outputs/sales_data_report.html
```

## What The Cleaning Pipeline Does

1. Removes exact duplicate rows.
2. Standardizes categorical text like region and status.
3. Converts dates and removes invalid date rows.
4. Converts numeric fields safely.
5. Imputes missing values with mode, median, or a clear placeholder.
6. Recalculates revenue from quantity, unit price, and discount.
7. Caps quantity and revenue outliers using the IQR method.

## Storytelling Questions Answered

- Which category generates the most revenue?
- Which region performs best?
- How does revenue trend by month?
- Which sales channel has the most orders?
- Which products drive the largest share of revenue?
