import streamlit as st
import pandas as pd
import plotly.express as px

st.title("CSV File Extractor")

# Upload csv file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    st.success("File successfully extracted!")
    
    # Show the DataFrame
    st.write(df)

    # Show first 5 rows
    st.subheader("Preview (first 5 rows)")
    st.dataframe(df.head())

    # Sidebar Selectbox
    option = st.sidebar.selectbox(
        "Select a Category",
        ["Films", "Genre", "CriticRating", "AudienceRating", "BudgetMillions", "Year"]
    )

    # ---- Page: Films ----
    if option == "Films":
        st.header("Films List")
        st.write(df["Film"])
        st.dataframe(df[["Film", "Genre", "Year"]])

    # ---- Page: Genre ----
    elif option == "Genre":
        st.header("Genre Distribution")
        fig = px.bar(df, x="Genre", title="Genre Count")
        st.plotly_chart(fig, use_container_width=True)

    # ---- Page: Critic Rating ----
    elif option == "CriticRating":
        st.header("Critic Ratings Overview")
        fig = px.histogram(df, x="CriticRating", nbins=20)
        st.plotly_chart(fig, use_container_width=True)

    # ---- Page: Audience Rating ----
    elif option == "AudienceRating":
        st.header("Audience Ratings Overview")
        st.write(df["AudienceRating"])
        fig = px.histogram(df, x="AudienceRating", nbins=20)
        st.plotly_chart(fig, use_container_width=True)

    # ---- Page: Budget ----
    elif option == "BudgetMillions":
        st.header("Movie Budget (in Millions)")
        fig = px.box(df, x="BudgetMillions")
        st.plotly_chart(fig, use_container_width=True)

    # ---- Page: Year ----
    elif option == "Year":
        st.header("Movies per Year")
        fig = px.histogram(df, x="Year")
        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Please upload a CSV file to continue.")