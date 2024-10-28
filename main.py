import pandas as pd
import seaborn as sns
import streamlit as st

st.write("Testing streamlit package")

#To capture the customer input
input = st.text_input("Whats your favorite Movie?")
st.write(f"Your favourite movie is: {input}")

click_btn1 = st.button("Click Me !")


data= pd.read_csv("Practice 1.csv")
st.write(data)

gender_counts = data['gender'].value_counts()
st.write("Gender Distribution:", gender_counts)

# Plot gender distribution using seaborn
sns_plot = sns.barplot(x=gender_counts.index, y=gender_counts.values)
st.pyplot(sns_plot.figure)