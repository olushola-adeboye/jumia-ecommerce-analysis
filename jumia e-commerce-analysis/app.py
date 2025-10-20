import streamlit as st
import pandas as pd
import plotly.express as px

# page setup
st.set_page_config(page_title="Jumia E-commerce Data Analysis", layout='wide')

# title
st.title("Jumia E-commerce Data Analysis Dashboard")

# load data
@st.cache_data
def load_data():
    df = pd.read_csv("jumia_cleaned.csv")
    return df

df = load_data()

# Sidebar filters
category = st.sidebar.multiselect("Select Category", df['Category'].unique())

if category:
    df = df[df['Category'].isin(category)]
    
# Dataset Overview
st.markdown('### Dataset Overview')
st.dataframe(df.head())

# Quick Summary Metric
st.markdown('### Key Metrics')
col1, col2, col3 = st.columns(3)
col1.metric('Total Products', len(df))
col2.metric('Average Price(₦)', round(df['Price'].mean(), 2))
col3.metric('Average Discount(%)', round(df['Discount'].mean(), 2))

# Price Distribution
st.markdown('### Price Distribution')
fig = px.histogram(df, x='Price', nbins=50, title='Product Price Distribution')
st.plotly_chart(fig, use_container_width=True)

# Discount Distribution
st.markdown('### Discount Analysis')
fig2 = px.histogram(df, x='Discount', nbins=50, title='Discount Percentage Distribution')
st.plotly_chart(fig2, use_container_width=True)

# Rating Distribution
st.markdown('### Rating Distribution')
fig3 = px.histogram(df, x='Rating', nbins=50, title=' Product Rating Distribution')
st.plotly_chart(fig3, use_container_width=True)

# Average Price by Category
st.markdown('### Average Price by Category')
avg_price = df.groupby('Category')['Price'].mean().reset_index()
fig4 = px.bar(avg_price, x='Category', y='Price', title='Average Product Price by Category', color='Price')
st.plotly_chart(fig4, use_container_width=True)

# Average Discount by Category
st.markdown('### Average Discount by Category')
avg_price = df.groupby('Category')['Discount'].mean().reset_index()
fig5 = px.bar(avg_price, x='Category', y='Discount', title='Average Discount by Category', color='Discount')
st.plotly_chart(fig5, use_container_width=True)

# Average Rating by Category
st.markdown('### Average Rating by Category')

# Calculate averages per category
avg_stats = df.groupby('Category')[['Rating', 'Price']].mean().reset_index()
# Create bar chart
fig6 = px.bar(
    avg_stats,
    x='Category',
    y='Rating',
    title='Average Rating by Category',
    color='Price',          # Color by average Price
    color_continuous_scale='Viridis'  # Optional: nice color gradient
)
fig6.show()
st.plotly_chart(fig6, use_container_width=True)

# Correlation Heatmap
st.markdown('### Correlation Analysis')
corr = df.corr(numeric_only=True)
st.dataframe(corr.style.background_gradient(cmap='coolwarm'))

# Footer
st.markdown('---')

st.caption('Developed by Olushola Adeboye | Data sourced from Jumia Nigeria')
