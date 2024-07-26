import streamlit as st
import pandas as pd

with st.sidebar:
    st.image("https://static.streamlit.io/examples/cat.jpg", width=100)
    st.title("AutoSTREAMml")
    choice = st.radio("Select a page", ["Upload", "Profiling", "ML", "Download"])
    st.info("This application allows you to build a machine learning model with a few clicks.")
st.write("Welcome to AutoSTREAMml!")

if choice == "Upload":
    st.title("Upload your data for modelling")
    file = st.file_uploader("Upload a CSV file")
    if file:
        try:
            df = pd.read_csv(file)
            st.dataframe(df)
        except pd.errors.ParserError:
            st.error("There was an error parsing the CSV file.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

elif choice == "Profiling":
    pass
elif choice == "ML":
    pass
elif choice == "Download":
    pass
