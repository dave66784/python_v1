import streamlit as st
import pandas as pd
import plotly.express as px

# Define the data
data = [
    {
        "Type": "Tx1",
        "TotalCount": 100,
        "TimeStamp": "2023-01-01T10:10:45",
        "OutCome": [
            {"Decision": "ACCEPT", "Count": 60},
            {"Decision": "REJECT", "Count": 20},
            {"Decision": "WAIVE", "Count": 20},
        ],
    },
    {
        "Type": "Tx2",
        "TotalCount": 100,
        "TimeStamp": "2023-01-01T11:10:45",
        "OutCome": [
            {"Decision": "ACCEPT", "Count": 40},
            {"Decision": "REJECT", "Count": 20},
            {"Decision": "WAIVE", "Count": 40},
        ],
    },
    {
        "Type": "Tx3",
        "TotalCount": 100,
        "TimeStamp": "2023-01-01T12:10:45",
        "OutCome": [
            {"Decision": "ACCEPT", "Count": 60},
            {"Decision": "REJECT", "Count": 20},
            {"Decision": "WAIVE", "Count": 20},
        ],
    },
    {
        "Type": "Tx4",
        "TotalCount": 100,
        "TimeStamp": "2023-01-01T09:10:45",
        "OutCome": [
            {"Decision": "ACCEPT", "Count": 60},
            {"Decision": "REJECT", "Count": 20},
            {"Decision": "WAIVE", "Count": 20},
        ],
    },
]

# Prepare the data for bar chart
bar_data = []
for item in data:
    bar_data.append({
        "Type": item["Type"],
        "TotalCount": item["TotalCount"]
    })

df_bar = pd.DataFrame(bar_data)


# Create the bar chart
def create_bar_chart():
    fig = px.bar(df_bar, x="Type", y="TotalCount")
    fig.update_layout(xaxis_title="Transaction Type", yaxis_title="Total Count")
    return fig


# Prepare the data for pie chart
pie_data = []
for item in data:
    for outcome in item["OutCome"]:
        pie_data.append({
            "Type": item["Type"],
            "Decision": outcome["Decision"],
            "Count": outcome["Count"]
        })

df_pie = pd.DataFrame(pie_data)


# Create the pie chart
def create_pie_chart():
    fig = px.pie(df_pie, names="Decision", values="Count", color="Type", title="Outcome Distribution")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


# Main app
def main():
    st.title("Data Visualization")

    st.subheader("Transaction Type and Total Count")
    bar_chart = create_bar_chart()
    st.plotly_chart(bar_chart)

    st.subheader("Outcome Distribution")
    pie_chart = create_pie_chart()
    st.plotly_chart(pie_chart)


if __name__ == "__main__":
    main()
