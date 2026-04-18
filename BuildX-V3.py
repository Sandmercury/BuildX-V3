import streamlit as st
import re

# საიტის კონფიგურაცია
st.set_page_config(page_title="BuildX | Premium Construction", page_icon="🏗️", layout="centered")

# --- ULTRA MODERN PREMIUM CSS ---
st.markdown("""
    <style>
    /* მთლიანი ფონი - ძალიან ნათელი რუხი/თეთრი */
    .stApp {
        background: linear-gradient(135deg, #ffffff 0%, #f0f2f5 100%) !important;
    }

    /* შრიფტები და ტექსტები */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif !important;
        color: #1e293b !important;
    }

    /* სათაურები */
    h1, h2, h3 {
        color: #0f172a !important;
        letter-spacing: -0.5px !important;
    }

    /* ბარათების სტილი (Card UI) */
    div[data-testid="stVerticalBlock"] > div > div {
        background: rgba(255, 255, 255, 0.8);
        # backdrop-filter: blur(10px);
        # border-radius: 20px !important;
        # border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* ველების (Inputs) პრემიუმ სტილი */
    .stTextInput div[data-baseweb="input"], 
    .stNumberInput div[data-baseweb="input"], 
    .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        transition: all 0.3s ease-in-out !important;
        padding: 4px 8px !important;
    }

    /* ფოკუსის ეფექტი ველებზე */
    .stTextInput div[data-baseweb="input"]:focus-within,
    .stNumberInput div[data-baseweb="input"]:focus-within {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1) !important;
    }

    /* ტექსტის ფერი ველებში (შენი მოთხოვნა) */
    input, .stSelectbox span, div[data-baseweb="select"] div {
        color: #0f172a !important;
        font-weight: 500 !important;
    }

    /* პრემიუმ ლურჯი ღილაკი Gradient-ით */
    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 16px 32px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3) !important;
        height: auto !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 20px 25px -5px rgba(37, 99, 235, 0.4) !important;
    }

    /* Metric-ის სტილი */
    div[data-testid="stMetric"] {
        background: #ffffff !important;
        padding: 20px !important;
        border-radius: 16px !important;
        border: 1px solid #f1f5f9 !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
    }

    /* Dropdown ფიქსაცია */
    div[data-baseweb="popover"] ul {
        background-color: #ffffff !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="popover"] li {
        color: #1e293b !important;
        transition: background 0.2s !important;
    }
    div[data-baseweb="popover"] li:hover {
        background-color: #f8fafc !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ვალიდაციის ფუნქციები
def is_valid_email(e):
    return re.match(r"[^@]+@[^@]+\.[^@]+", e) if e else True

def is_valid_phone(p):
    if not p: return True
    return bool(re.match(r"^\+?[0-9]*$", p))

# --- HEADER / LOGO ---
col_l1, col_l2, col_l3 = st.columns([1, 1.5, 1])
with col_l2:
    try:
        st.image("BuildX.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center;'>🏗️ BUILDX</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #64748b !important; font-weight: 400;'>Premium Construction Estimator</h3>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- STEP 1: CONTACT ---
st.markdown("#### 👤 საკონტაქტო ინფორმაცია")
c_name, c_mail, c_phone = st.columns(3)

with c_name:
    full_name = st.text_input("სახელი, გვარი", placeholder="მაგ: ლაშა ჯაკობია")

with c_mail:
    email = st.text_input("Email", placeholder="example@email.com")
    if email and not is_valid_email(email):
        st.caption(" :red[⚠️ ჩაწერეთ სწორ ფორმატში]")

with c_phone:
    phone = st.text_input("ტელეფონის ნომერი", placeholder="5XXXXXXXX")
    if phone and not is_valid_phone(phone):
        st.caption(" :red[⚠️ დასაშვებია მხოლოდ ციფრები და +]")

location = st.selectbox(
    "აირჩიეთ რაიონი:", 
    ["არჩიეთ რაიონი...", "თბილისი", "მცხეთა", "თეთრიწყარო"],
    index=0
)

st.markdown("<br>", unsafe_allow_html=True)

# ვალიდაცია
email_ok = email and is_valid_email(email)
phone_ok = phone and is_valid_phone(phone) and len(phone) >= 9

if full_name and email_ok and phone_ok and location != "არჩიეთ რაიონი...":
    
    # --- STEP 2: CALCULATOR ---
    st.markdown("<hr style='border: 0.5px solid #e2e8f0;'>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("#### 🏠 პროექტის ზოგადი პარამეტრები")
        area = st.number_input("სახლის საერთო ფართობი (კვ.მ):", min_value=1, step=1, value=None, placeholder="მაგ: 150")
        floors = st.selectbox("სართულების რაოდენობა:", [1, 2, 3])
        
        st.markdown("#### 🏗️ კონსტრუქციული დეტალები")
        concrete_grade = st.selectbox("ბეტონის მარკა:", ["B20 (M250)", "B25 (M350)"])
        wall_material = st.selectbox("კედლის მასალა:", ["პემზის ბლოკი", "აგური", "გაზბლოკი"])
        
        st.markdown("#### 🏠 ექსტერიერი")
        roof_type = st.selectbox("სახურავის ტიპი:", ["თუნუქი (Classic)", "ბრტყელი გადახურვა"])
        window_type = st.selectbox("ფანჯარა:", ["სტანდარტული მეტალოპლასტმასი", "პრემიუმ ალუმინი"])
        door_type = st.selectbox("კარი:", ["რკინა", "ხე"])

    st.markdown("<br>", unsafe_allow_html=True)

    if area:
        # ფასების ლოგიკა
        p_const, p_roof, p_facade, p_comm = 280, 85, 120, 60
        if floors > 1: p_const *= 1.15
        if wall_material == "აგური": p_const += 45
        if roof_type == "ბრტყელი გადახურვა": p_roof = 145
        if window_type == "პრემიუმ ალუმინი": p_facade += 160

        total_cost = area * (p_const + p_roof + p_facade + p_comm)

        st.metric(label="ჯამური სავარაუდო ბიუჯეტი", value=f"${total_cost:,.0f}")

        with st.expander("🔍 ხარჯების დეტალური ჩაშლა"):
            st.write(f"🔹 **კონსტრუქციული ნაწილი:** ${area * p_const:,.0f}")
            st.write(f"🔹 **გადახურვა:** ${area * p_roof:,.0f}")
            st.write(f"🔹 **ფასადი და კარ-ფანჯარა:** ${area * p_facade:,.0f}")
            st.write(f"🔹 **კომუნიკაციები:** ${area * p_comm:,.0f}")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📁 ნახაზის ატვირთვა")
        st.file_uploader("ატვირთეთ ფაილი (AI Vision ანალიზისთვის)", type=['png', 'jpg', 'pdf'])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("მონაცემების გაგზავნა 🚀"):
            st.balloons()
            st.success(f"მადლობა {full_name}, თქვენი მოთხოვნა მიღებულია!")
    else:
        st.info("💡 შეიყვანეთ ფართობი ხარჯთაღრიცხვის საჩვენებლად.")
else:
    st.markdown("<div style='background-color: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; color: #64748b;'>📍 კალკულატორის გამოსაყენებლად შეავსეთ საკონტაქტო მონაცემები.</div>", unsafe_allow_html=True)

st.markdown("<br><hr style='border: 0.5px solid #e2e8f0;'>", unsafe_allow_html=True)
st.caption("© 2026 BuildX Construction Company | Premium Build Solutions")
