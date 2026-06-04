import pandas as pd
import matplotlib.pyplot as plt
from connector import conn, cursor

query = 'SELECT * FROM Sales'
df_sql = pd.read_sql(query, conn)
print(df_sql)


df = pd.read_excel('sales_data.xlsx', sheet_name='data')
df['Total'] = df['Quantity'] * df['Price']
print(df.columns)

print('\nSales Data')
print(df)

total_revenue = df['Total'].sum()
print('\nTotal Revenue')
print(total_revenue)

product_sales = df.groupby('Product')['Total'].sum()
print('\nRevenue by product')
print(product_sales)

city_sales = df.groupby('City')['Total'].sum()
print('\nRevenue by city')
print(city_sales)

customer_sales = df.groupby('Customer')['Total'].sum()
print('\nCustomer Spending')
print(customer_sales.sort_values(ascending=False))

df.to_excel('sales_data.xlsx', sheet_name='data',index=False)
print('\nReport saved succesfuly')

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby('Month')['Total'].sum()
print(monthly_sales)

#Created product sales chart
product_sales.plot(
    kind='bar'
)

plt.title('Product Sales')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.show()

#Created city sales pie chart
city_sales.plot(
    kind='pie',
    autopct = '%1.1f%%'
)
plt.title('Sales by city')
plt.ylabel('')
plt.show()

monthly_sales.plot(
    kind='line',
    marker = 'o'
)
plt.title('Monthly sales Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.show()