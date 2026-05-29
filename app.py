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

st.subheader("Penguin Species Count")

fig1, ax1 = plt.subplots()

df['species'].value_counts().plot(
    kind='bar',
    ax=ax1
)

ax1.set_xlabel("Species")
ax1.set_ylabel("Count")

st.pyplot(fig1)
