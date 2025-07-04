import streamlit as st

# 1. Dark mode toggle at top
dark_mode = st.checkbox("🌙 Dark Mode")

if dark_mode:
    st.markdown(
        """
        <style>
        .main { background-color: #0E1117; color: #D9D9D9; }
        a { color: #58a6ff; }
        .css-1d391kg { background-color: #0E1117; }
        </style>
        """, unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .main { background-color: white; color: black; }
        a { color: #0078d7; }
        .css-1d391kg { background-color: white; }
        </style>
        """, unsafe_allow_html=True
    )

st.set_page_config(page_title="Anupama | Portfolio", page_icon="🌸", layout="centered")

# --- Header Section ---
st.title("👩‍💻 Anupama Chaudhary")
st.write("Dark mode toggle test")

st.subheader("Data Science | Python Developer | IT Enthusiast")

st.markdown("""
Welcome to my portfolio! I'm passionate about transforming data into actionable insights using machine learning and Python.
""")

# --- About Section ---
st.header("📘 About Me")
st.markdown("""
I’m an aspiring data scientist and software developer from Nepal with hands-on experience in building ML-powered apps and Python tools.

**Skills**:
- Python, Pandas, Scikit-learn, Streamlit
- Data Analysis, ML Algorithms
- HTML/CSS, Git/GitHub
""")

# --- Projects Section ---

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
