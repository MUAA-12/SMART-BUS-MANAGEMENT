import streamlit as st
from data import routes, bookings

st.set_page_config(
    page_title="Smart Bus Booking System",
    page_icon="🚌",
    layout="wide"
)

st.title("🚌 Smart Bus Ticket Booking System")
st.write("Welcome! Book your bus tickets easily.")

menu = st.sidebar.selectbox(
    "Choose an Option",
    [
        "View Available Routes",
        "Search Route",
        "Book Ticket",
        "View My Bookings",
        "Cancel Booking",
        "Seat Availability",
        "Booking Report"
    ]
)

if menu == "View Available Routes":
    st.subheader("Available Bus Routes")
    st.dataframe(routes, use_container_width=True)