import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Walmart Sales Forecast",
    page_icon="📈",
    layout="wide"
)

# ---------------- TITLE ---------------- #
st.title("📈 Walmart Sales Forecast Dashboard")
st.subheader("use XGBoost to predict Walmart sales")
st.markdown(
    """
    This dashboard shows:
    - Train predictions
    - Test predictions
    - Forecasts for Store Types A, B, and C
    """
)

# ---------------- HELPER FUNCTION ---------------- #
def show_section(title, image_path, caption, csv_path):
    st.subheader(title)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image(
            image_path,
            caption=caption,
            width="stretch"
        )

    with col2:
        df = pd.read_csv(csv_path)

        st.metric("Rows", len(df))
        st.metric("Columns", len(df.columns))

        st.dataframe(
            df,
            use_container_width=True,
            height=350
        )

    st.divider()


# ---------------- MAIN SECTIONS ---------------- #

show_section(
    "📊 All Stores - Train Prediction",
    "predicted vs actual all store.png",
    "Prediction on training data",
    "data.csv"
)

show_section(
    "🧪 All Stores - Test Prediction",
    "prediction of all stores on unseen data.png",
    "Prediction on unseen test data",
    "prediction.csv"
)

show_section(
    "🏪 Type A Stores - Test Forecast",
    "Type A unseen Data.png",
    "Forecast for Type A stores",
    "forecasted_sales_of_A.csv"
)

show_section(
    "🏪 Type B Stores - Test Forecast",
    "Type B unseen Data.png",
    "Forecast for Type B stores",
    "forecasted_sales_of_B.csv"
)

show_section(
    "🏪 Type C Stores - Test Forecast",
    "Type C unseen Data.png",
    "Forecast for Type C stores",
    "forecasted_sales_of_C.csv"
)

show_section(
    "📉 Type A Stores - Train Prediction",
    "preicted vs actual type A.png",
    "Train prediction for Type A stores",
    "prediction_store_A.csv"
)

show_section(
    "📉 Type B Stores - Train Prediction",
    "preicted vs actual type B.png",
    "Train prediction for Type B stores",
    "prediction_store_B.csv"
)

show_section(
    "📉 Type C Stores - Train Prediction",
    "preicted vs actual type C.png",
    "Train prediction for Type C stores",
    "prediction_store_C.csv"
)

# ---------------- FOOTER ---------------- #
st.markdown("---")

st.markdown(
    """
    📂 Dataset:  
    [Walmart Sales Forecast Dataset](https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast?select=train.csv)
    """
)