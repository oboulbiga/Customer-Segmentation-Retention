# Customer Segmentation & Retention Analysis

## Project Overview
End-to-end **Data Science & Machine Learning project** analyzing retail customer behavior to identify valuable customers, measure retention, and support targeted marketing decisions.

The project combines **EDA, SQL, RFM segmentation, cohort analysis, K-Means clustering, Streamlit, Docker, and AWS deployment**.

## Business Questions
- Who are the most valuable customers?
- Which customers are becoming inactive?
- How well are customers retained over time?
- Can Machine Learning identify natural customer groups?
- What strategy should be used for each customer segment?

## Dataset & Analysis
The **Online Retail dataset** contains 500,000+ transactions. Data preparation included missing-value handling, duplicate removal, transaction validation, datetime conversion, and feature engineering.

`TotalPrice = Quantity × UnitPrice`

| Metric | Result |
|---|---:|
| Unique Customers | **4,338** |
| Total Revenue | **~$8.89M** |
| Avg. Purchase Frequency | **4.27 orders** |
| Highest Revenue Month | **November 2011** |

## RFM, Retention & Machine Learning
Customers were analyzed using **Recency, Frequency, and Monetary Value (RFM)**. Cohort analysis measured customer retention over time.

K-Means clustering was applied to standardized RFM features. The **Elbow Method** and **Silhouette Score** were used for model selection.

**Final model: K = 4 | Silhouette Score ≈ 0.616**

| Segment | Customers | Recency | Frequency | Monetary |
|---|---:|---:|---:|---:|
| Regular | 3,054 | 43.7 | 3.68 | $1,354 |
| Inactive | 1,067 | 248.1 | 1.55 | $479 |
| Loyal High-Value | 204 | 15.5 | 22.33 | $12,691 |
| VIP | 13 | 7.4 | 82.54 | $127,188 |

## Business Recommendations
- **VIP:** Personalized service and exclusive benefits.
- **Loyal High-Value:** Loyalty programs and cross-selling.
- **Regular:** Targeted recommendations to increase purchase frequency.
- **Inactive:** Personalized win-back and reactivation campaigns.

## Dashboard & Cloud Deployment
The Streamlit dashboard provides **KPIs, RFM segments, K-Means clusters, cohort retention, customer filtering, and business recommendations**.

`Streamlit → Docker → Amazon ECR → Amazon ECS → Public AWS Application`

## Technologies
**Python • SQL • SQLite • Pandas • NumPy • Scikit-learn • Matplotlib • Seaborn • Streamlit • Docker • AWS ECR • AWS ECS • Jupyter • Git/GitHub**

## Run Locally
```bash
pip install -r requirements.txt
python -m streamlit run dashboard/app.py
```

## Docker
```bash
docker build -t customer-segmentation-app .
docker run -p 8501:8501 customer-segmentation-app
```

## Conclusion
An end-to-end customer analytics project demonstrating **data analysis, SQL, retention analytics, unsupervised Machine Learning, business interpretation, dashboard development, containerization, and AWS cloud deployment**.
