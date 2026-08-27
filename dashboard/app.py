import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent.parent

rfm = pd.read_csv(
    BASE_DIR / "data" / "processed" / "rfm_customers.csv"
)

st.set_page_config(
    page_title="Customer Segmentation & Retention",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Segmentation & Retention Dashboard")

st.write(
    "Interactive analysis of customer behavior, retention, "
    "RFM segmentation, and K-Means clustering."
)

st.subheader("Customer Data")
st.dataframe(rfm.head())
st.subheader("Key Performance Indicators")

total_customers = rfm["CustomerID"].nunique()
total_revenue = rfm["Monetary"].sum()
avg_frequency = rfm["Frequency"].mean()
avg_customer_value = rfm["Monetary"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Total Revenue", f"${total_revenue:,.2f}")
col3.metric("Avg. Purchase Frequency", f"{avg_frequency:.2f}")
col4.metric("Avg. Customer Value", f"${avg_customer_value:,.2f}")

st.subheader("Explore Customer Clusters")

selected_cluster = st.selectbox(
    "Select a customer cluster",
    [
        "All",
        "Regular Customers",
        "Inactive Customers",
        "Loyal High-Value Customers",
        "VIP Customers"
    ]
)

if selected_cluster == "All":
    filtered_rfm = rfm.copy()
else:
    filtered_rfm = rfm[
        rfm["Cluster_Name"] == selected_cluster
    ]

st.write(f"Customers displayed: {len(filtered_rfm):,}")
st.subheader("Top Customers")

st.subheader("Business Recommendations")

recommendations = {
    "VIP Customers": [
        "Protect and retain these high-value customers.",
        "Offer personalized rewards and exclusive benefits.",
        "Provide priority customer support.",
        "Avoid aggressive discounting that could reduce margin."
    ],
    "Loyal High-Value Customers": [
        "Strengthen loyalty with premium rewards.",
        "Offer early access to new products.",
        "Use personalized cross-sell and upsell campaigns.",
        "Monitor for any drop in purchase frequency."
    ],
    "Regular Customers": [
        "Encourage more frequent purchases.",
        "Use product recommendations and cross-selling.",
        "Promote loyalty programs.",
        "Create campaigns to move them toward high-value segments."
    ],
    "Inactive Customers": [
        "Launch win-back and reactivation campaigns.",
        "Send personalized reminders or limited-time offers.",
        "Investigate why customers stopped purchasing.",
        "Prioritize customers with historically higher Monetary value."
    ]
}
if selected_cluster == "All":
    st.info(
        "Select a customer cluster above to view targeted business recommendations."
    )
else:
    for recommendation in recommendations[selected_cluster]:
        st.write(f"• {recommendation}")

        st.divider()

st.subheader("Key Business Insights")

st.write("""
- The customer base is dominated by Regular Customers.
- Inactive Customers represent an important opportunity for reactivation.
- A small group of VIP Customers generates exceptionally high customer value.
- Loyal High-Value Customers should be prioritized for retention.
- RFM analysis combined with K-Means helps identify actionable customer behavior patterns.
""")

top_customers = (
    filtered_rfm[
        ["CustomerID", "Recency", "Frequency", "Monetary", "Cluster_Name"]
    ]
    .sort_values("Monetary", ascending=False)
    .head(10)
)

st.dataframe(top_customers)
st.subheader("RFM Customer Segmentation")

segment_counts = rfm["Segment"].value_counts()

st.bar_chart(segment_counts)
st.subheader("K-Means Customer Clusters")

cluster_counts = rfm["Cluster_Name"].value_counts()

st.bar_chart(cluster_counts)
st.subheader("Cluster Profiles")

cluster_profile = (
    rfm.groupby("Cluster_Name")[
        ["Recency", "Frequency", "Monetary"]
    ]
    .mean()
    .round(2)
)

st.dataframe(cluster_profile)

retention = pd.read_csv(
    BASE_DIR / "data" / "processed" / "retention_matrix.csv",
    index_col=0
)
st.subheader("Customer Retention by Cohort")

st.dataframe(
    retention.style.format("{:.1%}")
)
st.subheader("Customer Retention Heatmap")

fig, ax = plt.subplots(figsize=(14, 7))

sns.heatmap(
    retention,
    annot=True,
    fmt=".0%",
    cmap="YlGnBu",
    ax=ax
)

ax.set_title("Customer Retention by Cohort")
ax.set_xlabel("Months Since First Purchase")
ax.set_ylabel("Cohort Month")

st.pyplot(fig)