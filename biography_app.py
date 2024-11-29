import streamlit as st
import pandas as pd

if "biographies" not in st.session_state:
    st.session_state.biographies = []

st.set_page_config(page_title="Biography Website", layout="centered")

st.title("Biography Website")

menu = st.sidebar.selectbox("Menu", ["Home", "Add Biography", "View Biographies", "Search Biography"])

if menu == "Home":
    st.header("Welcome to the Biography Website")
    st.write("This app allows you to add, view, and search for biographies easily.")
    st.image("https://via.placeholder.com/600x200", caption="Biography Management")

elif menu == "Add Biography":
    st.header("Add a New Biography")
    with st.form("add_bio_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, step=1)
        address = st.text_area("Address")
        contact = st.text_input("Contact Number")
        email = st.text_input("Email Address")
        education = st.text_area("Educational Background")
        skills = st.text_area("Skills and Hobbies")
        submitted = st.form_submit_button("Add Biography")
    
    if submitted:
        if name and contact:
            st.session_state.biographies.append({
                "Name": name,
                "Age": age,
                "Address": address,
                "Contact": contact,
                "Email": email,
                "Education": education,
                "Skills": skills
            })
            st.success(f"Biography for {name} added successfully!")
        else:
            st.error("Name and Contact fields are required.")

elif menu == "View Biographies":
    st.header("All Biographies")
    if st.session_state.biographies:
        df = pd.DataFrame(st.session_state.biographies)
        st.dataframe(df)
    else:
        st.warning("No biographies found. Please add some first.")

elif menu == "Search Biography":
    st.header("Search for a Biography")
    search_query = st.text_input("Enter a name to search for")
    if search_query:
        results = [bio for bio in st.session_state.biographies if search_query.lower() in bio["Name"].lower()]
        if results:
            for bio in results:
                st.subheader(bio["Name"])
                st.write(f"**Age:** {bio['Age']}")
                st.write(f"**Address:** {bio['Address']}")
                st.write(f"**Contact:** {bio['Contact']}")
                st.write(f"**Email:** {bio['Email']}")
                st.write(f"**Education:** {bio['Education']}")
                st.write(f"**Skills:** {bio['Skills']}")
        else:
            st.warning("No matching biographies found.")
