import streamlit as st
from flight_dashboard import Db
import plotly.graph_objects as go

# creating the db object
db = Db()

st.sidebar.title("Flights Analytics")

user_options = st.sidebar.selectbox(
    "Menu", ["Select One", "Check_Flights", "Analytics"]
)

if user_options == "Check_Flights":
    st.title("Check Flights")

    col1, col2 = st.columns(2)

    city = db.fetch_city_name()
    with col1:
        source = st.selectbox("Source", sorted(city))
    with col2:
        destination = st.selectbox("Destination", sorted(city))

    if st.button("Search"):
        results = db.fetch_all_cities(source, destination)
        if isinstance(results, str):
            st.warning(results)
        else:
            st.dataframe(results)


elif user_options == "Analytics":
    st.title("Analytics")
    airline, frequency = db.airline_freq()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value",
        )
    )

    st.header("Pie chart")
    st.plotly_chart(fig)
else:
    st.title("Tell about the project")
