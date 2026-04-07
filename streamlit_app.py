import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#get the data
def get_data():
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv")
    st.write("Dataset import done")
    return df
    
df =get_data()

#Display the data
st.dataframe(df.head(5))

#select option
option = st.selectbox("Select column", ("survived","sex","class"))
#Display selected column
st.write(option)
#Count values in the column
selected_count =df[option].value_counts()
survival_counts = df['survived'].value_counts()
st.write(selected_count)
st.bar_chart(selected_count, horizontal=True)
#st.write(survival_counts)
#st.bar_chart(survival_counts, horizontal=True)

# Select numeric columns only
numeric_df = df.select_dtypes(include='number')

# Create pairplot
sns.pairplot(numeric_df)
st.pyplot(plt)


st.line_chart(df[["fare"]])


