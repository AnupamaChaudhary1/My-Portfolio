import streamlit as st

st.set_page_config(page_title="Anupama | Portfolio", page_icon="🌸", layout="centered")

# --- Header Section ---
st.title("👩‍💻 Anupama Chaudhary")
st.subheader("Data Science | Python Developer | IT Enthusiast")

st.header("📁 My Projects")

st.markdown("""
### 1. 🎓 School Fee Analysis App  
A Streamlit-based tool that predicts school fees and visualizes trends using ML.  
[🔗 View on GitHub](https://github.com/AnupamaChaudhary1/School_feeAnalysis)  
[🔗 View live](https://schoolfeeanalysis-anupamax.streamlit.app/)

### 2. 💬 Sentiment Analysis with FastAPI  
A simple text classifier to detect sentiment using FastAPI.  
[🔗 GitHub Repo](https://github.com/AnupamaChaudhary1/fee_app)  
[🔗 View live](https://feeapp-anu.streamlit.app/)

### 3. 🔢 Clustering Student Performance  
KMeans clustering to group students based on academic performance.  
[🔗 View Project](https://github.com/AnupamaChaudhary1/student-performance-predictor)  
[🔗 View live](https://student-performance-predictor-anupama.streamlit.app/)
""")


# --- Contact Section ---
st.header("📬 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Send Message")

    if submitted:
        if name and email and message:
            st.success(f"Thank you, {name}! Your message has been recorded. 📬")
        else:
            st.error("Please complete all fields before sending.")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 Anupama Chaudhary | Built with ❤️ using Streamlit")
