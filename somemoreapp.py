import streamlit as st
import math
#from zxcvbn import zxcvbn
from pass_analyzer import analyze_password

# --- PAGE CONFIG ---
st.set_page_config(page_title="Password Analyzer | Team Ve", layout="centered")

# --- CUSTOM STYLING (The Pink/Dark Theme) ---
st.markdown("""
    <style>
    /* main content background - deep charcoal-blue */
    .main, body, [data-testid="stAppViewContainer"], .css-18e3th9 { 
        background-color: #0F0F1A !important; 
        color: #FFFFFF; 
        font-family: 'Segoe UI', sans-serif; 
    }
    /* card/background containers use lighter navy for depth */
    .window-box {
        background-color: #1A1A2E;
        border: 3px solid #FF4B91;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(255, 75, 145, 0.2);
    }
    /* ensure any default text (like inputs) stays white */
    .stTextInput>div>div>input, .stText, .stMarkdown, .stButton>button {
        color: #FFFFFF !important;
    }
    /* make sidebar radio labels white so modes aren't black */
    [data-testid="stSidebar"] .css-1aumxhk label, [data-testid="stSidebar"] .css-ckOyDo {
        color: #FFFFFF !important;
    }
    /* ensure any text under navigation (titles, info, etc.) is white */
    [data-testid="stSidebar"] *,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span {
        color: #FFFFFF !important;
    }

    /* sidebar set to left dark shade */
    [data-testid="stSidebar"] {
        background-color: #1C1A26 !important;
        color: #FFFFFF;
    }
    [data-testid="stSidebar"] .css-1d391kg {
        background-color: #1C1A26 !important;
    }

    .header { text-align: center; padding: 20px 0; color: #FF4B91; font-size: 2.5rem; font-weight: 800; }
    
    /* Box styling to mimic the "Windows" in your drawing */
    .window-box {
        background-color: #1E1E1E;
        border: 3px solid #FF4B91;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(255, 75, 145, 0.2);
    }
    
    .stProgress>div>div>div>div { background-color: #FF4B91; }
    .stTextInput>div>div>input { background-color: #2D2D2D; color: #FF4B91; border: 2px solid #FF4B91; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='header'>🔐 PASSWORD ANALYZER</div>", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Select Mode")
mode = st.sidebar.radio("Navigation", ["(A) LEARN", "(B) QUICK CHECK", "(C) DEEP ANALYSIS"])

# --- MODE A: LEARN ---
if mode == "(A) LEARN":
    st.markdown("<div class='window-box'>", unsafe_allow_html=True)
    st.title("🎓 LEARN MODE")
    st.write("Can you guess the password based on these personas?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
        st.info("**Persona:** John Doe\n\n**DOB:** 15/05/1990\n\n**Pet:** Rex")
    with col2:
        guess = st.text_input("Guess John's password:")
        if guess:
            if any(word in guess.lower() for word in ["rex", "1990", "john"]):
                st.error("Too Easy! Most hackers use personal info first.")
            else:
                st.success("Not bad! But most users use 'Rex1990' or 'John1505'.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- MODE B: QUICK CHECK (Integrated with Color Bar) ---
elif mode == "(B) QUICK CHECK":
    st.markdown("<div class='window-box'>", unsafe_allow_html=True)
    st.title("⚡ QUICK CHECK")
    pwd = st.text_input("Enter password to test", type="password")
    
    if pwd:
        results = analyze_password(pwd)  # Using the custom analysis function from pass_analyzer.py
        final_score = results['final_security_score'] # 0 to 4
        
        score = min(int(final_score * 3), 4)  # Scale to 0-4 for color mapping
        # Determine Color and Label based on score
        # 0=Red, 1=Orange, 2=Yellow, 3/4=Green
        strength_map = {
            0: ("#FF0000", "WEAK!", 0.1),
            1: ("#FF4500", "STILL WEAK", 0.3),
            2: ("#FFCC00", "FAIR", 0.6),
            3: ("#ADFF2F", "GOOD", 0.8),
            4: ("#00FF00", "STRONG!", 1.0)
        }
        
        color, label, progress = strength_map[score]
        
        # Display the custom colored strength bar
        st.markdown(f"<h2 style='color:{color}; text-align:center;'>{label}</h2>", unsafe_allow_html=True)
        st.progress(progress)
        
        # Suggestions Section (from 2nd code)
        if results['feedback']['suggestions'] or results['feedback']['warning']:
            st.markdown("---")
            st.subheader("💡 Suggestions")
            if results['feedback']['warning']:
                st.warning(f"**Warning:** {results['feedback']['warning']}")
            for s in results['feedback']['suggestions']:
                st.write(f"• {s}")
    else:
        st.info("Start typing a password to see its strength bar.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- MODE C: DEEP ANALYSIS ---
elif mode == "(C) DEEP ANALYSIS":
    st.markdown("<div class='window-box'>", unsafe_allow_html=True)
    st.title("🔬 DEEP ANALYSIS")
    target_pwd = st.text_input("Enter password for full breakdown", type="default")
    
    if target_pwd:
        results = zxcvbn(target_pwd)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Score", f"{results['score']}/4")
            st.write(f"⏱️ **Time to crack:** {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
        with col2:
            st.write("**Vulnerabilities:**")
            # Shows what sequences were found (like '123' or dictionary words)
            for match in results['sequence']:
                st.write(f"- Found: `{match['token']}` ({match['pattern']})")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Powered by Team Ve Analysis Engine")
