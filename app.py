import streamlit as st
import pandas as pd

st.header('Effect of Fuel and Mileage on Price')
import plotly.express as px

df= pd.read_csv('vehicles_us.csv')
columns_kept= ['price', 'fuel', 'odometer']
filtered_df= df[columns_kept]

#First histogram, Price vs. fuel type
uf= df['fuel'].unique()

first_columns= ['price', 'fuel']
first_df= df[first_columns]
cleaned_df1= first_df[['price', 'fuel']].drop_duplicates().dropna()

selected_fuel = []
for fuel in uf:
    if st.checkbox(fuel):
        selected_fuel.append(fuel)

if selected_fuel:
    filtered_data= cleaned_df1[cleaned_df1['fuel'].isin(selected_fuel)]
    fig= px.histogram(filtered_data, x='price', color='fuel', title='Price Distribution by Fuel Type', barmode='overlay')
    st.plotly_chart(fig)
else:
    st.warning('Please select a fuel type.')

#Second plot, Price vs. Odometer
second_columns= ['price', 'odometer']
second_df= df[second_columns]
cleaned_df2= second_df[['price', 'odometer']].drop_duplicates().dropna()
fig = px.scatter(cleaned_df2, x='odometer', y='price', title='Price vs Odometer', labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'})
st.write(fig)