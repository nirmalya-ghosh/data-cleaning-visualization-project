from __future__ import annotations

import html
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
RAW_PATH = DATA_DIR / "raw_sales_data.csv"
CLEAN_PATH = DATA_DIR / "clean_sales_data.csv"
SUMMARY_PATH = OUTPUT_DIR / "cleaning_summary.csv"
REPORT_PATH = OUTPUT_DIR / "sales_data_report.html"


RAW_ROWS = [
    ["ORD-1001", "2026-01-03", "North", "Laptop", "Electronics", 2, 799.0, 0.05, "Online", "Delivered", 1518.10],
    ["ORD-1002", "2026-01-04", "south", "Office Chair", "Furniture", 5, 120.0, 0.10, "Retail", "Delivered", 540.00],
    ["ORD-1003", "2026-01-06", "East", "Notebook", "Stationery", 40, 2.5, 0.00, "Online", "Delivered", 100.00],
    ["ORD-1004", "2026-01-08", "West", "Printer", "Electronics", 1, 185.0, 0.00, "Partner", "Returned", 185.00],
    ["ORD-1005", "2026-01-10", "North", "Standing Desk", "Furniture", 2, 310.0, 0.08, "Retail", "Delivered", 570.40],
    ["ORD-1006", "2026-01-12", "East", "Pen Set", "Stationery", 20, 6.0, 0.05, "Online", "Delivered", 114.00],
    ["ORD-1007", "2026-01-13", "West", "Monitor", "Electronics", 3, 210.0, 0.12, "Online", "Delivered", 554.40],
    ["ORD-1008", "2026-01-15", "South", "Filing Cabinet", "Furniture", 1, 180.0, 0.00, "Retail", "Delivered", 180.00],
    ["ORD-1009", "2026-01-16", "North", "USB Cable", "Electronics", 15, 8.0, 0.00, "Online", "Delivered", 120.00],
    ["ORD-1010", "2026-01-18", "East", "Desk Lamp", "Furniture", 4, 35.0, 0.05, "Partner", "Delivered", 133.00],
    ["ORD-1011", "2026-01-20", "West", "Keyboard", "Electronics", 6, 45.0, 0.07, "Online", "Delivered", 251.10],
    ["ORD-1012", "2026-01-22", "South", "Copy Paper", "Stationery", 10, 11.0, 0.03, "Retail", "Delivered", 106.70],
    ["ORD-1013", "2026-01-25", "North", "Tablet", "Electronics", 2, 260.0, 0.00, "Online", "Delivered", 520.00],
    ["ORD-1014", "2026-01-27", "East", "Bookshelf", "Furniture", 1, 150.0, 0.10, "Partner", "Delivered", 135.00],
    ["ORD-1015", "2026-02-01", "West", "Markers", "Stationery", 30, 1.8, 0.00, "Retail", "Delivered", 54.00],
    ["ORD-1016", "2026-02-03", "South", "Laptop", "Electronics", 1, 820.0, 0.05, "Online", "Delivered", 779.00],
    ["ORD-1017", "2026-02-04", "North", "Office Chair", "Furniture", 3, 115.0, 0.00, "Retail", "Delivered", 345.00],
    ["ORD-1018", "2026-02-07", "East", "Notebook", "Stationery", 50, 2.4, 0.05, "Online", "Delivered", 114.00],
    ["ORD-1019", "2026-02-09", "West", "Printer", "Electronics", 2, 190.0, 0.08, "Partner", "Delivered", 349.60],
    ["ORD-1020", "2026-02-11", "South", "Standing Desk", "Furniture", 1, 330.0, 0.00, "Retail", "Delivered", 330.00],
    ["ORD-1021", "2026-02-14", "North", "Pen Set", "Stationery", 25, 5.5, 0.00, "Online", "Delivered", 137.50],
    ["ORD-1022", "2026-02-15", "East", "Monitor", "Electronics", 4, 205.0, 0.10, "Online", "Delivered", 738.00],
    ["ORD-1023", "2026-02-16", "West", "Filing Cabinet", "Furniture", 2, 175.0, 0.04, "Retail", "Delivered", 336.00],
    ["ORD-1024", "2026-02-18", "South", "USB Cable", "Electronics", 18, 7.5, 0.00, "Online", "Delivered", 135.00],
    ["ORD-1025", "2026-02-20", "North", "Desk Lamp", "Furniture", 5, 34.0, 0.06, "Partner", "Delivered", 159.80],
    ["ORD-1026", "2026-02-22", "East", "Keyboard", "Electronics", 7, 47.0, 0.05, "Online", "Delivered", 312.55],
    ["ORD-1027", "2026-02-25", "West", "Copy Paper", "Stationery", 12, 10.5, 0.00, "Retail", "Delivered", 126.00],
    ["ORD-1028", "2026-02-26", "South", "Tablet", "Electronics", 3, 255.0, 0.08, "Online", "Delivered", 703.80],
    ["ORD-1029", "2026-03-01", "North", "Bookshelf", "Furniture", 2, 148.0, 0.05, "Partner", "Returned", 281.20],
    ["ORD-1030", "2026-03-03", "East", "Markers", "Stationery", 45, 1.7, 0.00, "Retail", "Delivered", 76.50],
    ["ORD-1031", "2026-03-05", "West", "Laptop", "Electronics", 2, 805.0, 0.04, "Online", "Delivered", 1545.60],
    ["ORD-1032", "2026-03-07", "South", "Office Chair", "Furniture", 4, 118.0, 0.10, "Retail", "Delivered", 424.80],
    ["ORD-1033", "2026-03-09", "North", "Notebook", "Stationery", 55, 2.3, 0.00, "Online", "Delivered", 126.50],
    ["ORD-1034", "2026-03-10", "East", "Printer", "Electronics", 1, 188.0, 0.05, "Partner", "Delivered", 178.60],
    ["ORD-1035", "2026-03-12", "West", "Standing Desk", "Furniture", 2, 325.0, 0.12, "Retail", "Delivered", 572.00],
    ["ORD-1036", "2026-03-14", "South", "Pen Set", "Stationery", 35, 5.8, 0.03, "Online", "Delivered", 196.91],
    ["ORD-1037", "2026-03-16", "North", "Monitor", "Electronics", 5, 215.0, 0.10, "Online", "Delivered", 967.50],
    ["ORD-1038", "2026-03-18", "East", "Filing Cabinet", "Furniture", 1, 170.0, 0.00, "Retail", "Delivered", 170.00],
    ["ORD-1039", "2026-03-20", "West", "USB Cable", "Electronics", 20, 7.9, 0.05, "Online", "Delivered", 150.10],
    ["ORD-1040", "2026-03-22", "South", "Desk Lamp", "Furniture", 6, 33.0, 0.00, "Partner", "Delivered", 198.00],
    ["ORD-1041", "2026-03-24", "North", "Keyboard", "Electronics", 8, 46.0, 0.04, "Online", "Delivered", 353.28],
    ["ORD-1042", "2026-03-25", "East", "Copy Paper", "Stationery", 15, 10.0, 0.05, "Retail", "Delivered", 142.50],
    ["ORD-1043", "2026-03-27", "West", "Tablet", "Electronics", 4, 250.0, 0.08, "Online", "Delivered", 920.00],
    ["ORD-1044", "2026-03-29", "South", "Bookshelf", "Furniture", 3, 145.0, 0.00, "Partner", "Delivered", 435.00],
    ["ORD-1045", "2026-03-30", "North", "Markers", "Stationery", 60, 1.6, 0.00, "Retail", "Delivered", 96.00],
    ["ORD-1046", "2026-04-02", "East", "Laptop", "Electronics", 2, 815.0, 0.06, "Online", "Delivered", 1532.20],
    ["ORD-1047", "2026-04-04", "West", "Office Chair", "Furniture", 5, 116.0, 0.05, "Retail", "Delivered", 551.00],
    ["ORD-1048", "2026-04-06", "South", "Notebook", "Stationery", 65, 2.2, 0.00, "Online", "Delivered", 143.00],
    ["ORD-1049", "2026-04-07", "North", "Printer", "Electronics", 1, 192.0, 0.04, "Partner", "Delivered", 184.32],
    ["ORD-1050", "2026-04-09", "East", "Standing Desk", "Furniture", 2, 320.0, 0.10, "Retail", "Delivered", 576.00],
    ["ORD-1051", "2026-04-10", "West", "Pen Set", "Stationery", 30, 5.6, 0.02, "Online", "Delivered", 164.64],
    ["ORD-1052", "2026-04-12", "South", "Monitor", "Electronics", 3, 212.0, 0.08, "Online", "Delivered", 585.12],
    ["ORD-1053", "2026-04-13", "North", "Filing Cabinet", "Furniture", 2, 172.0, 0.03, "Retail", "Delivered", 333.68],
    ["ORD-1054", "2026-04-15", "East", "USB Cable", "Electronics", 25, 7.7, 0.00, "Online", "Delivered", 192.50],
    ["ORD-1055", "2026-04-17", "West", "Desk Lamp", "Furniture", 7, 32.0, 0.00, "Partner", "Delivered", 224.00],
    ["ORD-1056", "2026-04-19", "South", "Keyboard", "Electronics", 6, 48.0, 0.05, "Online", "Delivered", 273.60],
    ["ORD-1057", "2026-04-21", "North", "Copy Paper", "Stationery", 18, 10.2, 0.00, "Retail", "Delivered", 183.60],
    ["ORD-1058", "2026-04-22", "East", "Tablet", "Electronics", 5, 248.0, 0.10, "Online", "Delivered", 1116.00],
    ["ORD-1059", "2026-04-24", "West", "Bookshelf", "Furniture", 2, 152.0, 0.04, "Partner", "Delivered", 291.84],
    ["ORD-1060", "2026-04-26", "South", "Markers", "Stationery", 70, 1.5, 0.00, "Retail", "Delivered", 105.00],
    ["ORD-1061", "2026-04-28", "North", "Laptop", "Electronics", 1, 810.0, 0.00, "Online", "Delivered", 810.00],
    ["ORD-1062", "2026-04-29", "East", "Office Chair", "Furniture", 6, 119.0, 0.08, "Retail", "Delivered", 656.88],
    ["ORD-1063", "2026-05-01", "West", "Notebook", "Stationery", 70, 2.1, 0.03, "Online", "Delivered", 142.59],
    ["ORD-1064", "2026-05-03", "South", "Printer", "Electronics", 1, 186.0, 0.00, "Partner", "Delivered", 186.00],
    ["ORD-1065", "2026-05-05", "North", "Standing Desk", "Furniture", 2, 335.0, 0.08, "Retail", "Delivered", 616.40],
    ["ORD-1066", "2026-05-07", "East", "Pen Set", "Stationery", 40, 5.4, 0.00, "Online", "Delivered", 216.00],
    ["ORD-1067", "2026-05-09", "West", "Monitor", "Electronics", 2, 218.0, 0.04, "Online", "Delivered", 418.56],
    ["ORD-1068", "2026-05-10", "South", "Filing Cabinet", "Furniture", 3, 174.0, 0.05, "Retail", "Delivered", 495.90],
    ["ORD-1069", "2026-05-12", "North", "USB Cable", "Electronics", 30, 7.6, 0.00, "Online", "Delivered", 228.00],
    ["ORD-1070", "2026-05-14", "East", "Desk Lamp", "Furniture", 8, 31.5, 0.04, "Partner", "Delivered", 241.92],
    ["ORD-1071", "2026-05-16", "West", "Keyboard", "Electronics", 9, 49.0, 0.05, "Online", "Delivered", 418.95],
    ["ORD-1072", "2026-05-18", "South", "Copy Paper", "Stationery", 20, 9.8, 0.00, "Retail", "Delivered", 196.00],
    ["ORD-1073", "2026-05-20", "North", "Tablet", "Electronics", 3, 252.0, 0.06, "Online", "Delivered", 710.64],
    ["ORD-1074", "2026-05-22", "East", "Bookshelf", "Furniture", 1, 155.0, 0.00, "Partner", "Returned", 155.00],
    ["ORD-1075", "2026-05-24", "West", "Markers", "Stationery", 75, 1.4, 0.00, "Retail", "Delivered", 105.00],
    ["ORD-1076", "2026-05-26", "South", "Laptop", "Electronics", 2, 830.0, 0.10, "Online", "Delivered", 1494.00],
    ["ORD-1077", "2026-05-28", "North", "Office Chair", "Furniture", 4, 121.0, 0.05, "Retail", "Delivered", 459.80],
    ["ORD-1078", "2026-05-29", "East", "Notebook", "Stationery", 80, 2.0, 0.00, "Online", "Delivered", 160.00],
    ["ORD-1079", "2026-05-30", "West", "Printer", "Electronics", 2, 195.0, 0.08, "Partner", "Delivered", 358.80],
    ["ORD-1080", "2026-06-01", "South", "Standing Desk", "Furniture", 1, 340.0, 0.04, "Retail", "Delivered", 326.40],
    # Duplicate, missing values, invalid values, and outliers below.
    ["ORD-1007", "2026-01-13", "West", "Monitor", "Electronics", 3, 210.0, 0.12, "Online", "Delivered", 554.40],
    ["ORD-1081", "not a date", "north", "Laptop", "Electronics", 1, 800.0, 0.00, "Online", "Delivered", 800.00],
    ["ORD-1082", "2026-06-02", "", "Desk Lamp", "Furniture", 3, 31.0, 0.00, "Partner", "Delivered", 93.00],
    ["ORD-1083", "2026-06-03", "East", "Tablet", "", 2, 249.0, 0.05, "Online", "Delivered", 473.10],
    ["ORD-1084", "2026-06-03", "West", "USB Cable", "Electronics", "", 7.5, 0.00, "Online", "Delivered", 0.00],
    ["ORD-1085", "2026-06-04", "South", "Office Chair", "Furniture", 500, 120.0, 0.00, "Retail", "Delivered", 60000.00],
    ["ORD-1086", "2026-06-04", "North", "Notebook", "Stationery", 35, -2.5, 0.00, "Online", "Delivered", -87.50],
    ["ORD-1087", "2026-06-05", "East", "Printer", "Electronics", 1, 189.0, 1.50, "Partner", "Delivered", -94.50],
]


def generate_raw_dataset() -> pd.DataFrame:
    columns = [
        "order_id",
        "order_date",
        "region",
        "product",
        "category",
        "quantity",
        "unit_price",
        "discount",
        "sales_channel",
        "order_status",
        "revenue",
    ]
    raw = pd.DataFrame(RAW_ROWS, columns=columns)
    DATA_DIR.mkdir(exist_ok=True)
    raw.to_csv(RAW_PATH, index=False)
    return raw


def clip_outliers_iqr(series: pd.Series) -> tuple[pd.Series, int, float, float]:
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = max(0, q1 - 1.5 * iqr)
    upper = q3 + 1.5 * iqr
    mask = (series < lower) | (series > upper)
    return series.clip(lower, upper), int(mask.sum()), float(lower), float(upper)


def clean_dataset(raw: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = raw.copy()
    start_rows = len(df)
    duplicate_rows = int(df.duplicated().sum())
    df = df.drop_duplicates()

    missing_before = int(df.isna().sum().sum() + df.astype("string").eq("").sum().sum())
    df = df.replace("", pd.NA)

    for col in ["region", "category", "sales_channel", "order_status"]:
        df[col] = df[col].astype("string").str.strip().str.title()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    bad_dates = int(df["order_date"].isna().sum())
    df = df.dropna(subset=["order_date"])

    for col in ["quantity", "unit_price", "discount", "revenue"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    invalid_numeric = int(
        (df["quantity"].le(0) | df["unit_price"].le(0) | df["discount"].lt(0) | df["discount"].gt(0.9)).sum()
    )
    df.loc[df["quantity"].le(0), "quantity"] = pd.NA
    df.loc[df["unit_price"].le(0), "unit_price"] = pd.NA
    df.loc[df["discount"].lt(0) | df["discount"].gt(0.9), "discount"] = pd.NA

    df["region"] = df["region"].fillna(df["region"].mode().iat[0])
    df["category"] = df["category"].fillna("Unknown")
    df["quantity"] = df["quantity"].fillna(df["quantity"].median()).round().astype(int)
    df["unit_price"] = df.groupby("product")["unit_price"].transform(lambda s: s.fillna(s.median()))
    df["discount"] = df["discount"].fillna(df["discount"].median())

    df["gross_revenue"] = df["quantity"] * df["unit_price"]
    df["revenue"] = df["gross_revenue"] * (1 - df["discount"])

    df["quantity"], quantity_outliers, quantity_lower, quantity_upper = clip_outliers_iqr(df["quantity"])
    df["revenue"], revenue_outliers, revenue_lower, revenue_upper = clip_outliers_iqr(df["revenue"])
    df["quantity"] = df["quantity"].round().astype(int)
    df["revenue"] = df["revenue"].round(2)
    df["month"] = df["order_date"].dt.to_period("M").astype(str)

    clean = df.sort_values(["order_date", "order_id"]).reset_index(drop=True)
    summary = pd.DataFrame(
        [
            ["raw_rows", start_rows],
            ["duplicate_rows_removed", duplicate_rows],
            ["missing_or_blank_values_before_cleaning", missing_before],
            ["invalid_dates_removed", bad_dates],
            ["invalid_numeric_values_imputed", invalid_numeric],
            ["quantity_outliers_capped", quantity_outliers],
            ["quantity_iqr_lower_cap", round(quantity_lower, 2)],
            ["quantity_iqr_upper_cap", round(quantity_upper, 2)],
            ["revenue_outliers_capped", revenue_outliers],
            ["revenue_iqr_lower_cap", round(revenue_lower, 2)],
            ["revenue_iqr_upper_cap", round(revenue_upper, 2)],
            ["clean_rows", len(clean)],
        ],
        columns=["metric", "value"],
    )
    return clean, summary


def save_bar(series: pd.Series, title: str, ylabel: str, filename: str, color: str) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    series.plot(kind="bar", ax=ax, color=color, edgecolor="#222222")
    ax.set_title(title, pad=14)
    ax.set_xlabel("")
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=25)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=160)
    plt.close(fig)


def save_line(series: pd.Series, title: str, ylabel: str, filename: str) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    series.plot(kind="line", marker="o", ax=ax, color="#1f77b4", linewidth=2.5)
    ax.set_title(title, pad=14)
    ax.set_xlabel("")
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=160)
    plt.close(fig)


def save_scatter(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    categories = sorted(df["category"].unique())
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd"]
    for category, color in zip(categories, colors, strict=False):
        subset = df[df["category"] == category]
        ax.scatter(subset["quantity"], subset["revenue"], label=category, s=48, alpha=0.78, color=color)
    ax.set_title("Quantity vs Revenue", pad=14)
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Revenue")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "quantity_vs_revenue.png", dpi=160)
    plt.close(fig)


def build_visuals(clean: pd.DataFrame) -> dict[str, pd.DataFrame | pd.Series]:
    OUTPUT_DIR.mkdir(exist_ok=True)
    revenue_by_category = clean.groupby("category")["revenue"].sum().sort_values(ascending=False)
    revenue_by_region = clean.groupby("region")["revenue"].sum().sort_values(ascending=False)
    monthly_revenue = clean.groupby("month")["revenue"].sum()
    channel_orders = clean["sales_channel"].value_counts()
    top_products = clean.groupby("product")["revenue"].sum().sort_values(ascending=False).head(8)

    save_bar(revenue_by_category, "Revenue by Category", "Revenue", "revenue_by_category.png", "#1f77b4")
    save_bar(revenue_by_region, "Revenue by Region", "Revenue", "revenue_by_region.png", "#2ca02c")
    save_bar(channel_orders, "Orders by Sales Channel", "Orders", "orders_by_channel.png", "#ff7f0e")
    save_bar(top_products, "Top Products by Revenue", "Revenue", "top_products.png", "#9467bd")
    save_line(monthly_revenue, "Monthly Revenue Trend", "Revenue", "monthly_revenue.png")
    save_scatter(clean)

    return {
        "revenue_by_category": revenue_by_category,
        "revenue_by_region": revenue_by_region,
        "monthly_revenue": monthly_revenue,
        "channel_orders": channel_orders,
        "top_products": top_products,
    }


def fmt_money(value: float) -> str:
    return f"${value:,.2f}"


def table_html(frame: pd.DataFrame) -> str:
    return frame.to_html(index=False, border=0, classes="data-table")


def series_table(series: pd.Series, value_name: str) -> pd.DataFrame:
    frame = series.reset_index()
    frame.columns = [series.index.name or "segment", value_name]
    if pd.api.types.is_numeric_dtype(frame[value_name]):
        frame[value_name] = frame[value_name].round(2)
    return frame


def build_report(clean: pd.DataFrame, summary: pd.DataFrame, views: dict[str, pd.Series]) -> None:
    total_revenue = clean["revenue"].sum()
    total_orders = clean["order_id"].nunique()
    avg_order_value = total_revenue / total_orders
    best_category = views["revenue_by_category"].idxmax()
    best_region = views["revenue_by_region"].idxmax()
    best_month = views["monthly_revenue"].idxmax()

    report = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sales Data Cleaning & Visualization Report</title>
  <style>
    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      color: #1f2933;
      background: #f7f9fb;
    }}
    header {{
      background: #203040;
      color: white;
      padding: 32px 40px;
    }}
    main {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 28px 20px 48px;
    }}
    h1, h2 {{
      margin: 0 0 12px;
    }}
    p {{
      line-height: 1.55;
    }}
    .kpis {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
      margin: 22px 0;
    }}
    .kpi {{
      background: white;
      border: 1px solid #d7dee8;
      border-radius: 8px;
      padding: 18px;
    }}
    .kpi span {{
      display: block;
      color: #52616f;
      font-size: 13px;
      margin-bottom: 8px;
    }}
    .kpi strong {{
      font-size: 24px;
    }}
    section {{
      margin-top: 32px;
    }}
    .charts {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 18px;
    }}
    figure {{
      margin: 0;
      background: white;
      border: 1px solid #d7dee8;
      border-radius: 8px;
      padding: 12px;
    }}
    img {{
      width: 100%;
      height: auto;
      display: block;
    }}
    .data-table {{
      border-collapse: collapse;
      width: 100%;
      background: white;
      margin-top: 12px;
    }}
    .data-table th, .data-table td {{
      border: 1px solid #d7dee8;
      padding: 9px 10px;
      text-align: left;
      font-size: 14px;
    }}
    .data-table th {{
      background: #edf2f7;
    }}
    .insights li {{
      margin-bottom: 8px;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Sales Data Cleaning & Visualization Report</h1>
    <p>A compact portfolio-style project showing preprocessing, quality checks, and business storytelling.</p>
  </header>
  <main>
    <div class="kpis">
      <div class="kpi"><span>Total Revenue</span><strong>{html.escape(fmt_money(total_revenue))}</strong></div>
      <div class="kpi"><span>Clean Orders</span><strong>{total_orders:,}</strong></div>
      <div class="kpi"><span>Average Order Value</span><strong>{html.escape(fmt_money(avg_order_value))}</strong></div>
      <div class="kpi"><span>Top Region</span><strong>{html.escape(str(best_region))}</strong></div>
    </div>

    <section>
      <h2>Cleaning Summary</h2>
      <p>The raw file includes duplicates, blank fields, invalid dates, invalid numeric values, and extreme values. The pipeline standardizes text, removes exact duplicates, imputes recoverable fields, recalculates revenue, and caps outliers with the IQR method.</p>
      {table_html(summary)}
    </section>

    <section>
      <h2>Key Findings</h2>
      <ul class="insights">
        <li><strong>{html.escape(str(best_category))}</strong> generated the highest revenue by category.</li>
        <li><strong>{html.escape(str(best_region))}</strong> led regional revenue after cleaning.</li>
        <li><strong>{html.escape(str(best_month))}</strong> was the strongest month in the dataset.</li>
        <li>Online orders dominate volume, while higher-ticket products drive most revenue.</li>
      </ul>
    </section>

    <section>
      <h2>Visual Dashboard</h2>
      <div class="charts">
        <figure><img src="revenue_by_category.png" alt="Revenue by category"></figure>
        <figure><img src="revenue_by_region.png" alt="Revenue by region"></figure>
        <figure><img src="monthly_revenue.png" alt="Monthly revenue trend"></figure>
        <figure><img src="orders_by_channel.png" alt="Orders by channel"></figure>
        <figure><img src="top_products.png" alt="Top products by revenue"></figure>
        <figure><img src="quantity_vs_revenue.png" alt="Quantity versus revenue scatter plot"></figure>
      </div>
    </section>

    <section>
      <h2>Top Products</h2>
      {table_html(series_table(views["top_products"], "revenue"))}
    </section>
  </main>
</body>
</html>
"""
    REPORT_PATH.write_text(report, encoding="utf-8")


def main() -> None:
    raw = generate_raw_dataset()
    clean, summary = clean_dataset(raw)
    DATA_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    clean.to_csv(CLEAN_PATH, index=False)
    summary.to_csv(SUMMARY_PATH, index=False)
    views = build_visuals(clean)
    build_report(clean, summary, views)

    print(f"Raw data: {RAW_PATH}")
    print(f"Clean data: {CLEAN_PATH}")
    print(f"Cleaning summary: {SUMMARY_PATH}")
    print(f"HTML report: {REPORT_PATH}")


if __name__ == "__main__":
    main()
