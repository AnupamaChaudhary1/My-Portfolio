# import streamlit as st

# # Set wide layout at start
# st.set_page_config(page_title="Anupama | Portfolio", page_icon="🌸", layout="wide")

# # Initialize session state for dark_mode if not exists
# if "dark_mode" not in st.session_state:
#     st.session_state.dark_mode = False

# # Sidebar with toggle so it stays visible and separate
# with st.sidebar:
#     st.title("Settings")
#     toggle = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
#     st.session_state.dark_mode = toggle

# # CSS strings for dark and light mode
# dark_css = """
# <style>
# html, body, #root {
#   height: 100% !important;
#   margin: 0; padding: 0;
#   background-color: #000 !important;
#   color: #fff !important;
#   overflow-x: hidden;
# }
# .block-container {
#   min-height: 100vh !important;
#   background-color: #000 !important;
#   color: #fff !important;
#   padding-top: 1rem !important;
#   padding-bottom: 1rem !important;
#   display: flex !important;
#   flex-direction: column !important;
# }
# .css-1d391kg, .css-1v3fvcr {
#   background-color: #000 !important;
#   color: #fff !important;
# }
# footer {
#   position: fixed !important;
#   bottom: 0;
#   width: 100%;
#   background-color: #000 !important;
#   color: #fff !important;
#   border-top: 1px solid #222 !important;
#   padding: 0.5rem 1rem !important;
# }
# a {
#   color: #3399FF !important;
# }
# ::-webkit-scrollbar {
#   width: 8px;
# }
# ::-webkit-scrollbar-track {
#   background: #000;
# }
# ::-webkit-scrollbar-thumb {
#   background-color: #555;
#   border-radius: 20px;
#   border: 3px solid #000;
# }
# </style>
# """

# light_css = """
# <style>
# html, body, #root {
#   height: 100% !important;
#   margin: 0; padding: 0;
#   background-color: white !important;
#   color: black !important;
#   overflow-x: hidden;
# }
# .block-container {
#   min-height: 100vh !important;
#   background-color: white !important;
#   color: black !important;
#   padding-top: 1rem !important;
#   padding-bottom: 1rem !important;
#   display: flex !important;
#   flex-direction: column !important;
# }
# .css-1d391kg, .css-1v3fvcr {
#   background-color: white !important;
#   color: black !important;
# }
# footer {
#   position: fixed !important;
#   bottom: 0;
#   width: 100%;
#   background-color: white !important;
#   color: black !important;
#   border-top: 1px solid #ddd !important;
#   padding: 0.5rem 1rem !important;
# }
# a {
#   color: #0078d7 !important;
# }
# ::-webkit-scrollbar {
#   width: 8px;
# }
# ::-webkit-scrollbar-track {
#   background: white;
# }
# ::-webkit-scrollbar-thumb {
#   background-color: #ccc;
#   border-radius: 20px;
#   border: 3px solid white;
# }
# </style>
# """

# # Apply CSS
# if st.session_state.dark_mode:
#     st.markdown(dark_css, unsafe_allow_html=True)
# else:
#     st.markdown(light_css, unsafe_allow_html=True)

# # Your portfolio content below
# st.title("👩‍💻 Anupama Chaudhary")
# st.subheader("Data Science | Python Developer | IT Enthusiast")

# st.markdown("""
# Welcome to my portfolio! I'm passionate about transforming data into actionable insights using machine learning and Python.
# """)

# st.header("📘 About Me")
# st.markdown("""
# I’m an aspiring data scientist and software developer from Nepal with hands-on experience in building ML-powered apps and Python tools.

# **Skills**:
# - Python, Pandas, Scikit-learn, Streamlit
# - Data Analysis, ML Algorithms
# - HTML/CSS, Git/GitHub
# """)

# st.header("📁 My Projects")
# st.markdown("""
# ### 1. 🎓 School Fee Analysis App  
# A Streamlit-based tool that predicts school fees and visualizes trends using ML.  
# [🔗 GitHub](https://github.com/AnupamaChaudhary1/School_feeAnalysis) | [🔗 Live](https://schoolfeeanalysis-anupamax.streamlit.app/)

# ### 2. 💬 Sentiment Analysis with FastAPI  
# A simple text classifier to detect sentiment using FastAPI.  
# [🔗 GitHub](https://github.com/AnupamaChaudhary1/fee_app) | [🔗 Live](https://feeapp-anu.streamlit.app/)

# ### 3. 🔢 Clustering Student Performance  
# KMeans clustering to group students based on academic performance.  
# [🔗 GitHub](https://github.com/AnupamaChaudhary1/student-performance-predictor) | [🔗 Live](https://student-performance-predictor-anupama.streamlit.app/)
# """)

# st.header("📬 Contact Me")

# with st.form("contact_form"):
#     name = st.text_input("Your Name")
#     email = st.text_input("Your Email")
#     message = st.text_area("Your Message")
#     submitted = st.form_submit_button("Send Message")

#     if submitted:
#         if name and email and message:
#             st.success(f"Thank you, {name}! Your message has been recorded. 📬")
#         else:
#             st.error("Please complete all fields before sending.")

# st.markdown("---")
# st.caption("© 2025 Anupama Chaudhary | Built with ❤️ using Streamlit")



import streamlit as st

# Set wide layout first
st.set_page_config(page_title="Anupama | Portfolio", page_icon="🌸", layout="wide")

# Initialize dark mode in session state if not set
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Place the toggle button fixed at top right
toggle = st.checkbox("🌙 Dark Mode", key="dark_mode")

# CSS for dark and light mode (cover all containers and sidebar)
dark_css = """
<style>
html, body, #root, .main, .block-container, .css-1d391kg, .css-1v3fvcr, footer {
    background-color: #000 !important;
    color: #fff !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}
a, a:visited {
    color: #3399FF !important;
}
footer {
    position: fixed !important;
    bottom: 0;
    width: 100%;
    background-color: #000 !important;
    color: #fff !important;
    border-top: 1px solid #222 !important;
    padding: 0.5rem 1rem !important;
}
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-track {
    background: #000;
}
::-webkit-scrollbar-thumb {
    background-color: #555;
    border-radius: 20px;
    border: 3px solid #000;
}
</style>
"""

light_css = """
<style>
html, body, #root, .main, .block-container, .css-1d391kg, .css-1v3fvcr, footer {
    background-color: white !important;
    color: black !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}
a, a:visited {
    color: #0078d7 !important;
}
footer {
    position: fixed !important;
    bottom: 0;
    width: 100%;
    background-color: white !important;
    color: black !important;
    border-top: 1px solid #ddd !important;
    padding: 0.5rem 1rem !important;
}
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-track {
    background: white;
}
::-webkit-scrollbar-thumb {
    background-color: #ccc;
    border-radius: 20px;
    border: 3px solid white;
}
</style>
"""

# Apply CSS
st.markdown(dark_css if toggle else light_css, unsafe_allow_html=True)

# --- Your portfolio content below ---

st.title("👩‍💻 Anupama Chaudhary")
st.subheader("Data Science | Python Developer | IT Enthusiast")

st.markdown("""
Welcome to my portfolio! I'm passionate about transforming data into actionable insights using machine learning and Python.
""")

st.header("📘 About Me")
st.markdown("""
I’m an aspiring data scientist and software developer from Nepal with hands-on experience in building ML-powered apps and Python tools.

**Skills**:
- Python, Pandas, Scikit-learn, Streamlit
- Data Analysis, ML Algorithms
- HTML/CSS, Git/GitHub
""")

st.header("📁 My Projects")
st.markdown("""
### 1. 🎓 School Fee Analysis App  
A Streamlit-based tool that predicts school fees and visualizes trends using ML.  
[🔗 GitHub](https://github.com/AnupamaChaudhary1/School_feeAnalysis) | [🔗 Live](https://schoolfeeanalysis-anupamax.streamlit.app/)

### 2. 💬 Sentiment Analysis with FastAPI  
A simple text classifier to detect sentiment using FastAPI.  
[🔗 GitHub](https://github.com/AnupamaChaudhary1/fee_app) | [🔗 Live](https://feeapp-anu.streamlit.app/)

### 3. 🔢 Clustering Student Performance  
KMeans clustering to group students based on academic performance.  
[🔗 GitHub](https://github.com/AnupamaChaudhary1/student-performance-predictor) | [🔗 Live](https://student-performance-predictor-anupama.streamlit.app/)
""")

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

st.markdown("---")
st.caption("© 2025 Anupama Chaudhary | Built with ❤️ using Streamlit")
