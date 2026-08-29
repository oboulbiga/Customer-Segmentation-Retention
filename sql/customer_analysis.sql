-- ============================================================
-- CUSTOMER SEGMENTATION & RETENTION ANALYSIS
-- SQL Business Analysis
-- ============================================================


-- 1. TOTAL REVENUE
SELECT
    ROUND(SUM(TotalPrice), 2) AS Total_Revenue
FROM online_retail;


-- 2. TOP 10 COUNTRIES BY REVENUE
SELECT
    Country,
    ROUND(SUM(TotalPrice), 2) AS Total_Revenue
FROM online_retail
GROUP BY Country
ORDER BY Total_Revenue DESC
LIMIT 10;


-- 3. TOP 10 CUSTOMERS BY REVENUE
SELECT
    CustomerID,
    ROUND(SUM(TotalPrice), 2) AS Total_Revenue
FROM online_retail
GROUP BY CustomerID
ORDER BY Total_Revenue DESC
LIMIT 10;


-- 4. TOP 10 CUSTOMERS BY NUMBER OF ORDERS
SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Number_of_Orders
FROM online_retail
GROUP BY CustomerID
ORDER BY Number_of_Orders DESC
LIMIT 10;


-- 5. AVERAGE CUSTOMER VALUE
SELECT
    ROUND(AVG(Customer_Revenue), 2) AS Average_Customer_Value
FROM (
    SELECT
        CustomerID,
        SUM(TotalPrice) AS Customer_Revenue
    FROM online_retail
    GROUP BY CustomerID
);


-- 6. MONTHLY REVENUE
SELECT
    strftime('%Y-%m', InvoiceDate) AS Month,
    ROUND(SUM(TotalPrice), 2) AS Monthly_Revenue
FROM online_retail
GROUP BY Month
ORDER BY Month;


-- 7. TOP 10 PRODUCTS BY QUANTITY SOLD
SELECT
    Description,
    SUM(Quantity) AS Total_Quantity
FROM online_retail
GROUP BY Description
ORDER BY Total_Quantity DESC
LIMIT 10;


-- 8. TOP 10 PRODUCTS BY REVENUE
SELECT
    Description,
    ROUND(SUM(TotalPrice), 2) AS Product_Revenue
FROM online_retail
GROUP BY Description
ORDER BY Product_Revenue DESC
LIMIT 10;


-- 9. NUMBER OF UNIQUE CUSTOMERS BY COUNTRY
SELECT
    Country,
    COUNT(DISTINCT CustomerID) AS Unique_Customers
FROM online_retail
GROUP BY Country
ORDER BY Unique_Customers DESC
LIMIT 10;


-- 10. REVENUE AND CUSTOMERS BY COUNTRY
SELECT
    Country,
    COUNT(DISTINCT CustomerID) AS Unique_Customers,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders,
    ROUND(SUM(TotalPrice), 2) AS Total_Revenue
FROM online_retail
GROUP BY Country
ORDER BY Total_Revenue DESC
LIMIT 10;


-- ============================================================
-- ADVANCED SQL
-- ============================================================


-- 11. CUSTOMER REVENUE RANKING USING A WINDOW FUNCTION
WITH CustomerRevenue AS (
    SELECT
        CustomerID,
        ROUND(SUM(TotalPrice), 2) AS Total_Revenue
    FROM online_retail
    GROUP BY CustomerID
)

SELECT
    CustomerID,
    Total_Revenue,
    RANK() OVER (
        ORDER BY Total_Revenue DESC
    ) AS Revenue_Rank
FROM CustomerRevenue
ORDER BY Revenue_Rank
LIMIT 10;


-- 12. MONTHLY REVENUE WITH RUNNING TOTAL
WITH MonthlyRevenue AS (
    SELECT
        strftime('%Y-%m', InvoiceDate) AS Month,
        SUM(TotalPrice) AS Revenue
    FROM online_retail
    GROUP BY Month
)

SELECT
    Month,
    ROUND(Revenue, 2) AS Monthly_Revenue,

    ROUND(
        SUM(Revenue) OVER (
            ORDER BY Month
        ),
        2
    ) AS Cumulative_Revenue

FROM MonthlyRevenue
ORDER BY Month;


-- 13. CUSTOMER SUMMARY
SELECT
    CustomerID,

    COUNT(DISTINCT InvoiceNo) AS Frequency,

    ROUND(
        SUM(TotalPrice),
        2
    ) AS Monetary,

    MAX(InvoiceDate) AS Last_Purchase

FROM online_retail

GROUP BY CustomerID

ORDER BY Monetary DESC

LIMIT 20;