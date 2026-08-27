# Customer Segmentation & Retention Analysis

## Project Overview
End-to-end Data Science project analyzing retail customer behavior to identify valuable customer groups, understand retention, and support targeted marketing decisions.

The project combines **EDA, RFM segmentation, cohort analysis, K-Means clustering, and an interactive Streamlit dashboard**.

## Business Questions
- Who are the most valuable customers?
- Which customers are becoming inactive?
- How well are customers retained over time?
- Can Machine Learning identify natural customer groups?
- What strategy should be used for each customer segment?

## Dataset
The **Online Retail dataset** contains more than 500,000 transactions with customer, product, quantity, price, date, and country information.

Data preparation included missing-value handling, duplicate removal, datetime conversion, transaction validation, and creation of:

`TotalPrice = Quantity × UnitPrice`

## Key Results

| Metric | Result |
|---|---:|
| Unique Customers | **4,338** |
| Total Revenue | **~$8.89M** |
| Avg. Purchase Frequency | **4.27 orders** |
| Avg. Customer Value | **~$2,048.69** |
| Highest Revenue Month | **November 2011** |

## RFM & Retention Analysis
Customers were evaluated using **Recency, Frequency, and Monetary value** and classified into segments including Champions, Loyal Customers, Potential Loyalists, At Risk, and Lost Customers.

Cohort analysis measured customer retention after the first purchase and revealed substantial opportunities for **retention, loyalty, and reactivation campaigns**.

## Machine Learning — K-Means
K-Means clustering was applied to standardized RFM features.

**Elbow Method** and **Silhouette Score** were used to evaluate K. The final model uses **K = 4**, with a Silhouette Score of approximately **0.616**.

A log-transformed model was also tested but performed worse (~0.433), so the original standardized RFM model was retained.

## Final Customer Clusters

| Segment | Customers | Recency | Frequency | Monetary |
|---|---:|---:|---:|---:|
| Regular | 3,054 | 43.7 | 3.68 | $1,354 |
| Inactive | 1,067 | 248.1 | 1.55 | $479 |
| Loyal High-Value | 204 | 15.5 | 22.33 | $12,691 |
| VIP | 13 | 7.4 | 82.54 | $127,188 |

## Business Recommendations
- **VIP:** Protect and retain with personalized service and exclusive benefits.
- **Loyal High-Value:** Strengthen loyalty and cross-sell relevant products.
- **Regular:** Increase purchase frequency through targeted recommendations.
- **Inactive:** Use personalized win-back and reactivation campaigns.

## Streamlit Dashboard
The interactive dashboard includes **KPIs, RFM segments, K-Means clusters, cohort retention, customer filtering, top customers, and targeted business recommendations**.

## Technologies
**Python • Pandas • NumPy • Matplotlib • Seaborn • Scikit-learn • Streamlit • Jupyter • Git/GitHub**

## Project Structure
```text
├── dashboard/app.py
├── data/
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_data_analysis.ipynb
│   ├── 04_rfm_segmentation.ipynb
│   ├── 05_retention_cohort_analysis.ipynb
│   └── 06_customer_segmentation_ml.ipynb
├── README.md
└── requirements.txt
```

## Run the Dashboard
```bash
pip install -r requirements.txt
python -m streamlit run dashboard/app.py
```

## Conclusion
This project demonstrates an end-to-end customer analytics workflow combining **data analysis, retention analytics, unsupervised Machine Learning, business interpretation, and interactive dashboard development**.