import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from data_management import get_data

def main():
    st.title("Data Visualization with Plotly and Streamlit")

    st.write("This is a simple Streamlit app to visualize data using Plotly.")

    df = get_data()
    st.write("Data loaded successfully!")
    st.dataframe(df)

if __name__ == "__main__":
    main()
