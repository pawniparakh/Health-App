import streamlit as st
import os
from utils import create_tables, add_record, get_records
from auth import register_user, login_user

create_tables()

st.set_page_config(page_title="Health App", layout="centered")

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- MENU ----------------
menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- REGISTER ----------------
if choice == "Register":
    st.title("📝 Register")

    name = st.text_input("Full Name")
    aadhaar = st.text_input("Aadhaar (12 digits)")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if register_user(name, aadhaar, password):
            os.makedirs(f"uploads/{aadhaar}", exist_ok=True)
            st.success("Account created!")
        else:
            st.error("Aadhaar already exists")

# ---------------- LOGIN ----------------
elif choice == "Login":
    st.title("🔐 Login")

    aadhaar = st.text_input("Aadhaar")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login_user(aadhaar, password)

        if user:
            st.session_state.logged_in = True
            st.session_state.aadhaar = aadhaar
            st.success("Logged in!")
        else:
            st.error("Invalid credentials")

# ---------------- DASHBOARD ----------------
if st.session_state.logged_in:

    st.title("🏥 Patient Dashboard")

    aadhaar = st.session_state.aadhaar
    user_folder = f"uploads/{aadhaar}"

    st.subheader("📤 Upload Medical Record")

    uploaded_file = st.file_uploader("Upload PDF or Image")

    description = st.text_input("Description")

    if st.button("Upload"):
        if uploaded_file:
            file_path = os.path.join(user_folder, uploaded_file.name)

            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            add_record(aadhaar, uploaded_file.name, description)
            st.success("Uploaded successfully!")

    # ---------------- VIEW RECORDS ----------------
    st.subheader("📜 Your Medical History")

    records = get_records(aadhaar)

    if records:
        for file_name, desc in records:
            file_path = os.path.join(user_folder, file_name)

            st.write(f"📄 {file_name} - {desc}")

            with open(file_path, "rb") as f:
                st.download_button(
                    label="Download",
                    data=f,
                    file_name=file_name
                )
    else:
        st.info("No records yet")

    # ---------------- CAMERA SCANNER ----------------
    st.subheader("📷 Scan Document")

    image = st.camera_input("Take a photo")

    if image:
        img_path = os.path.join(user_folder, "scan.png")

        with open(img_path, "wb") as f:
            f.write(image.getbuffer())

        add_record(aadhaar, "scan.png", "Scanned Report")
        st.success("Scanned and saved!")

    # ---------------- LOGOUT ----------------
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()