import streamlit as st

# Set page config for a clean look
st.set_page_config(page_title="Password Analyzer | Team Ve", layout="centered")

# --- CSS STYLING ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Delicious+Handrawn&display=swap" rel="stylesheet">
    <style>
        /* Target the main container */
        .main {
            background-color: #120d1a !important;
        }
        
        /* Container and Text styling */
        .custom-container {
            text-align: center;
            border: 4px solid #FF4B91;
            padding: 60px 40px;
            border-radius: 20px;
            background-color: #1e1e1e;
            box-shadow: 0 0 30px rgba(255, 75, 145, 0.2);
            font-family: 'Delicious Handrawn', cursive;
            margin-top: 50px;
        }

        .custom-container h1 {
            font-size: 3.5rem;
            font-weight: 900;
            letter-spacing: 8px;
            margin: 0;
            text-transform: uppercase;
            color: #ffffff;
            white-space: nowrap;
        }

        .custom-container h3 {
            font-size: 1.2rem;
            font-weight: 400;
            color: #FF4B91;
            margin-top: 10px;
            letter-spacing: 2px;
            opacity: 0.9;
        }

        .input-simulation {
            background: #111;
            border: 2px solid #444;
            padding: 15px;
            margin: 40px auto;
            width: 250px;
            font-size: 1.5rem;
            color: #FF4B91;
            letter-spacing: 5px;
            text-align: center;
        }

        /* Styling the actual Streamlit Button to match your UI */
        div.stButton > button {
            background-color: #d1d1d1 !important;
            color: #121212 !important;
            border: none !important;
            padding: 15px 50px !important;
            font-size: 1.5rem !important;
            font-weight: 800 !important;
            border-radius: 5px !important;
            transition: all 0.2s ease !important;
            box-shadow: 6px 6px 0px #666 !important;
            text-transform: uppercase !important;
            font-family: 'Delicious Handrawn', cursive !important;
            display: block;
            margin: 0 auto;
        }

        div.stButton > button:hover {
            background-color: #ffffff !important;
            box-shadow: 8px 8px 0px #FF4B91 !important;
            transform: translate(-2px, -2px);
        }

        div.stButton > button:active {
            transform: translate(4px, 4px) !important;
            box-shadow: 0px 0px 0px #666 !important;
        }
        
        /* Hide default streamlit elements for a cleaner look */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- UI STRUCTURE ---
st.markdown(f"""
    <div class="custom-container">
        <h1>PASSWORD <span style="color:#FF4B91">*</span> ANALYZER</h1>
        <h3>By Team Ve</h3>
        <div class="input-simulation">*******</div>
    </div>
    """, unsafe_allow_html=True)

# Spacing to place the button correctly
st.write("##") 

# --- NAVIGATION LOGIC ---
if st.button("ANALYZE"):
    # This logic tells Streamlit to run the content of newapp.py
    # In a real multipage app, you'd use st.switch_page("pages/newapp.py")
    try:
        st.switch_page("newapp.py")
    except Exception:
        st.error("Make sure 'newapp.py' exists in the same directory!")