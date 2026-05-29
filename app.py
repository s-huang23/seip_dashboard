import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

st.set_page_config(
    page_title="Penguins Dashboard",
    layout="wide"
)

st.title("Penguins Dataset Dashboard")

@st.cache_data
def load_data():
    df = sns.load_dataset("penguins")
    return df

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.sidebar.header("Filters")

species = st.sidebar.multiselect(
    "Select Species",
    options=df['species'].dropna().unique(),
    default=df['species'].dropna().unique()
)

filtered_df = df[df['species'].isin(species)]

st.subheader("Penguin Species Count")

fig1, ax1 = plt.subplots()

df['species'].value_counts().plot(
    kind='bar',
    ax=ax1
)

st.subheader("Bill Length vs Flipper Length")

fig3, ax3 = plt.subplots()

ax3.scatter(
    filtered_df['bill_length_mm'],
    filtered_df['flipper_length_mm']
)

ax3.set_xlabel("Bill Length (mm)")
ax3.set_ylabel("Flipper Length (mm)")

st.pyplot(fig3)


ax1.set_xlabel("Species")
ax1.set_ylabel("Count")

st.pyplot(fig1)
