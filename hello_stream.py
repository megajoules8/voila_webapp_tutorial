#pip install streamlit

#streamlit run app.py
#cntrl c to stop

#Here is a simple template demonstrating some of Streamlit's essential components:
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Title and Text
st.title("Welcome to My First Streamlit App")
st.write("This is a simple app demonstrating Streamlit's main features.")

# Sidebar
st.sidebar.header("Sidebar")
st.sidebar.write("This is a sidebar for additional settings.")

# Number Input
user_input = st.sidebar.number_input("Choose a number", 0, 100, 25)
st.write(f"You selected: {user_input}")

# Data Display
st.subheader("Dataframe Example")
data = pd.DataFrame({
    'Column 1': np.random.randn(10),
    'Column 2': np.random.randn(10)
})
st.write("Here is a sample dataframe:", data)

# Charts
st.subheader("Simple Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# User Input
if st.checkbox("Show Line Chart Data"):
    st.write("Chart Data:", chart_data)

# Interactive Widgets
user_name = st.text_input("Enter your name", "Guest")
st.write(f"Hello, {user_name}!")

# Button
if st.button("Say Hello"):
    st.write("Hello there! Streamlit is fun to use.")
else:
    st.write("Press the button to see a greeting.")

# File Upload
st.subheader("File Uploader")
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploaded_file is not None:
    file_data = pd.read_csv(uploaded_file)
    st.write("File contents:", file_data)
#After running this command, a local URL (usually http://localhost:8501) will open where you can see your app.

#some extras for sliders and widgets
# Slider for selecting a number with custom range and step
age = st.slider("Select your age", min_value=0, max_value=100, value=25, step=1)
st.write(f"You selected: {age}")

# Dropdown select box with custom options
favorite_fruit = st.selectbox("Pick your favorite fruit", options=["Apple", "Banana", "Cherry"], index=1)
st.write(f"Your favorite fruit is: {favorite_fruit}")

# Multi-select box for choosing multiple items
hobbies = st.multiselect("Select your hobbies", options=["Reading", "Traveling", "Swimming", "Cooking"])
st.write("You selected:", hobbies)

# Date input with a default date
birthday = st.date_input("When is your birthday?", value=pd.Timestamp("2000-01-01"))
st.write("Your birthday is:", birthday)


# File uploader allowing only CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:", data)

#charts
#Streamlit has built-in charting functions that work well 
#for simple data visualizations, but it also integrates with libraries like Matplotlib, Altair, and Plotly for more control.

# Simple line chart with random data, automatically infers x axis
import numpy as np
import pandas as pd

line_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(line_data)

# Simple bar chart
bar_data = pd.DataFrame(np.random.randn(10, 3), columns=['X', 'Y', 'Z'])
st.bar_chart(bar_data)

# Simple area chart
area_data = pd.DataFrame(np.random.randn(20, 3), columns=['M', 'N', 'O'])
st.area_chart(area_data)


# Altair bar chart with custom colors and labels
alt_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [3, 7, 5, 4]
})

alt_chart = alt.Chart(alt_data).mark_bar(color='teal').encode(
    x='Category',
    y='Values'
)
st.altair_chart(alt_chart, use_container_width=True)

import plotly.express as px

# Sample Plotly line chart
plotly_data = pd.DataFrame({
    'x': range(10),
    'y': np.random.randn(10)
})

fig = px.line(plotly_data, x='x', y='y', title="Interactive Plotly Line Chart")
st.plotly_chart(fig)

#combine widgets and charts
# Using a slider to dynamically filter data for a chart
import numpy as np

data = pd.DataFrame({
    'x': range(100),
    'y': np.random.randn(100).cumsum()
})

# Slider to select data range
range_selection = st.slider("Select range", 0, 99, (0, 50))
filtered_data = data[(data['x'] >= range_selection[0]) & (data['x'] <= range_selection[1])]

# Plot filtered data
st.line_chart(filtered_data)
#customise
with st.expander("See explanation"):
    st.write("This is some additional information.")
