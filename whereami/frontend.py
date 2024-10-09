import streamlit as st
import requests

st.title("API Info")

api_url = "https://api.fda.gov/food/enforcement.json?limit=1"  # Generic OPEN API

try:
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for bad status codes
data = response.json()
    enforcement_details = data.get("results", [])

    if enforcement_details:
        # Extract the data for the table
        table_data = [
            {
                "Status": detail.get("status", "N/A"),
                "City": detail.get("city", "N/A"),
                "State": detail.get("state", "N/A"),
                "Country": detail.get("country", "N/A"),
                "Product Type": detail.get("product_type", "N/A"),
                "Reason for Recall": detail.get("reason_for_recall", "N/A"),
                "Recall Initiation Date": detail.get("recall_initiation_date", "N/A"),
            }
            for detail in enforcement_details
        ]

        # Display the data in a tabular format
        st.table(table_data)
    else:
        st.write("No enforcement details found.")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data: {e}")
 