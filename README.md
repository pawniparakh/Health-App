# 🏥 Digital Health Record System

A secure and user-friendly web application that allows patients to store, manage, and access their complete medical history in one place.

Built using **Python + Streamlit**, this project simulates an Aadhaar-linked health record system where patients can upload reports, scan documents, and maintain a digital medical profile.

---

## 🚀 Features

* 🔐 Secure Login & Registration (Aadhaar-based ID simulation)
* 📂 Upload Medical Records (PDF/Image)
* 📷 Scan Documents using Camera
* 📜 View Complete Medical History
* ⬇️ Download Uploaded Reports
* 🧠 Organized patient-wise storage system
* 🔒 Password hashing for basic security

---

## 🛠️ Tech Stack

* **Frontend & Backend:** Streamlit
* **Database:** SQLite3
* **File Handling:** OS + Local Storage
* **Libraries:** pandas, PyPDF2, pillow

---

## 📁 Project Structure

```
health_app/
│
├── app.py          # Main application
├── auth.py         # Authentication logic
├── utils.py        # Database operations
├── database.db     # SQLite database
├── uploads/        # Stored medical files
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/health_app.git
cd health_app
```

### 2. Install dependencies

```
pip install streamlit pandas PyPDF2 pillow
```

### 3. Run the application

```
streamlit run app.py
```

---

## 🧪 Usage

1. Register using Name, Aadhaar (12-digit), and Password
2. Login to access your dashboard
3. Upload medical reports or scan documents
4. View and download your records anytime

---

## ⚠️ Disclaimer

This project simulates Aadhaar-based authentication and is intended for educational purposes only. It is not connected to any official government system.

---

## 🌟 Future Enhancements

* 👨‍⚕️ Doctor Dashboard (view patient records)
* ☁️ Cloud Storage Integration (AWS S3)
* 📊 AI-based medical report summarization
* 📅 Appointment & Medicine Reminder System
* 🔐 Advanced Encryption & OTP Authentication

---

## 🙌 Contributing

Contributions are welcome! Feel free to fork this repo and improve the project.

---

## 📌 Author

**Pawni Parakh**
**Raghav Sharma**
**Sanskriti Jha**
**Voduri Haasitha**

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
