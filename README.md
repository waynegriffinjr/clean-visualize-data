**Clean & Visualize Sales Data**
A Python project that cleans messy sales data, standardizes fields, handles invalid values, and generates clear visualizations for stakeholder reporting.

**Overview**
This project demonstrates a full data‑cleaning and visualization pipeline using Pandas, NumPy, and Matplotlib.
It transforms inconsistent, messy input data into an analysis‑ready dataset and produces three charts:

Sales by Product (bar chart)

Daily Sales Trend (line chart)

Sales Distribution (histogram)

**Data Cleaning Steps**
Standardize product and region names

Convert sales to numeric and date to datetime

Replace invalid sales (e.g., "abc", negative values)

Fill missing sales with the median

Drop rows with missing product names

Store final cleaned dataset in cleaned_df

**Visualizations**
Bar Chart: Total sales by product

Line Chart: Daily sales trend

Histogram: Distribution of sales values
Charts are saved as PNG files for reporting.

**Requirements**
Code
python3
pip install pandas matplotlib numpy

**How to Run**
Code
python3 clean_visualize_data.py
This will clean the data, generate charts, and save sales-by-product.png.

**Project Structure**
Code
clean-visualize-data/
├── clean_visualize_data.py
├── sales-by-product.png
├── daily-trend.png
├── sales-distribution.png
└── README.md

**Contact**
Created by Wayne Griffin Jr.
