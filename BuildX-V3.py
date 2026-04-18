import streamlit as st
import re

# საიტის კონფიგურაცია
st.set_page_config(page_title="BuildX | Premium", page_icon="🏗️", layout="centered")

# --- აბსოლუტური კონტროლი ვიზუალზე (ყველა ხვრელის ამოვსება) ---
st.markdown("""
    <style>
    /* 1. მთლიანი საიტის იძულებითი გათეთრება */
    html, body, .stApp, [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
    }

    /* 2. ტექსტების სრული გაშავება */
    h1, h2, h3, h4, p, label, span, div, .stMarkdown {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* 3. ყველა ველის (Input/Select) ფიქსაცია */
    div[data-baseweb="input"], 
    div[data-baseweb="select"], 
    .stTextInput input, 
    .stNumberInput input,
    div[role="combobox"] {
        background-color: #FFFFFF !important;
        background: #FFFFFF !important;
        border: 2px solid #000000 !important;
        border-radius: 10px !important;
        color: #000000 !important;
        opacity: 1 !important;
    }

    /* 4. არჩეული ტექსტის ხილვადობა */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        color: #000000 !important;
        background-color: #FFFFFF !important;
    }

    /* 5. ჩამოსაშლელი სიის (Dropdown) ფიქსაცია */
    div[data-baseweb="popover"] {
        background-color: #FFFFFF !important;
    }
    div[data-baseweb="popover"] li {
        color: #000000 !important;
        background-color: #FFFFFF !important;
    }
    div[data-baseweb="popover"] li:hover {
        background-color: #F0F2F6 !important;
    }

    /* 6. Autofill-ის (დამახსოვრებული მონაცემების) გათეთრება */
    input:-webkit-autofill,
    input:-webkit-autofill:hover, 
    input:-webkit-autofill:focus {
        -webkit-box-shadow: 0 0 0px 1000px #FFFFFF inset !important;
        -webkit-text-fill-color: #000000 !important;
        transition: background-color 5000s ease-in-out 0s;
    }

    /* 7. ღილაკის სტილი */
    .stButton > button {
        background: linear-gradient(90deg, #2E86C1 0%, #3498DB 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 50px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(46, 134, 193, 0.3) !important;
    }
    
    /* 8. Metric ბლოკის გათეთრება */
    div[data-testid="stMetric"] {
        background-color: #F8F9FA !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 15px !important;
        padding: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ვალიდაციის ფუნქციები
def is_valid_email(e):
    return re.match(r"[^@]+@[^@]+\.[^@]+", e) if e else True

def is_valid_phone(p):
    if not p: return True
    return bool(re.match(r"^\+?[0-9]*$", p))

# --- LOGO ---
col_l1, col_l2, col_l3 = st.columns([1, 1.5, 1])
with col_l2:
    try:
        st.image("BuildX.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center; color: black;'>🏗️ BUILDX</h1>", unsafe_allow_html=True)

st.markdown("---")

# --- STEP 1: CONTACT ---
st.markdown("### 👤 საკონტაქტო ინფორმაცია")
c_name, c_mail, c_phone = st.columns(3)

with c_name:
    full_name = st.text_input("სახელი, გვარი", placeholder="მაგ: ლაშა ჯაკობია")

with c_mail:
    email = st.text_input("Email", placeholder="example@email.com")
    if email and not is_valid_email(email):
        st.caption(" :red[გთხოვთ ჩაწერეთ სწორ ფორმატში]")

with c_phone:
    phone = st.text_input("ტელეფონის ნომერი", placeholder="5XXXXXXXX")
    if phone and not is_valid_phone(phone):
        st.caption(" :red[გთხოვთ ჩაწერეთ სწორ ფორმატში]")

location = st.selectbox(
    "აირჩიეთ რაიონი:", 
    ["არჩიეთ რაიონი...", "თბილისი", "მცხეთა", "თეთრიწყარო"],
    index=0
)

st.markdown("---")

# ვალიდაცია
email_ok = email and is_valid_email(email)
phone_ok = phone and is_valid_phone(phone) and len(phone) >= 9

if full_name and email_ok and phone_ok and location != "არჩიეთ რაიონი...":
    
    st.markdown("### 🏠 პროექტის ზოგადი პარამეტრები")
    area = st.number_input("სახლის საერთო ფართობი (კვ.მ):", min_value=1, step=1, value=None, placeholder="ჩაწერეთ ციფრები...")
    floors = st.selectbox("სართულების რაოდენობა:", [1, 2, 3])
    
    st.markdown("### 🏗️ კონსტრუქციული დეტალები")
    concrete_grade = st.selectbox("ბეტონის მარკა:", ["B20 (M250)", "B25 (M350)"])
    wall_material = st.selectbox("კედლის მასალა:", ["პემზის ბლოკი", "აგური", "გაზბლოკი"])
    
    st.markdown("### 🏠 ექსტერიერი")
    roof_type = st.selectbox("სახურავის ტიპი:", ["თუნუქი (Classic)", "ბრტყელი გადახურვა"])
    window_type = st.selectbox("ფანჯარა:", ["სტანდარტული მეტალოპლასტმასი", "პრემიუმ ალუმინი"])
    door_type = st.selectbox("კარი:", ["რკინა", "ხე"])

    st.markdown("---")

    if area:
        p_const, p_roof, p_facade, p_comm = 280, 85, 120, 60
        if floors > 1: p_const *= 1.15
        if wall_material == "აგური": p_const += 45
        if roof_type == "ბრტყელი გადახურვა": p_roof = 145
        if window_type == "პრემიუმ ალუმინი": p_facade += 160

        total_cost = area * (p_const + p_roof + p_facade + p_comm)

        st.metric(label="ჯამური სავარაუდო ბიუჯეტი", value=f"${total_cost:,.0f}")

        with st.expander("🔍 იხილეთ დეტალური განაწილება"):
            st.write(f"🔹 **კონსტრუქციული ნაწილი:** ${area * p_const:,.0f}")
            st.write(f"🔹 **გადახურვა:** ${area * p_roof:,.0f}")
            st.write(f"🔹 **ფასადი და კარ-ფანჯარა:** ${area * p_facade:,.0f}")
            st.write(f"🔹 **კომუნიკაციები:** ${area * p_comm:,.0f}")

        st.markdown("---")
        st.subheader("📁 ნახაზის ატვირთვა")
        st.file_uploader("ატვირთეთ ფაილი (AI Vision ანალიზი)", type=['png', 'jpg', 'pdf'])
        
        if st.button("მონაცემების გაგზავნა 🚀"):
            st.balloons()
            st.success(f"მადლობა {full_name}, მონაცემები გაგზავნილია!")
    else:
        st.info("💡 შეიყვანეთ ფართობი კალკულაციისთვის.")
else:
    st.warning("📍 გთხოვთ სრულად შეავსოთ საკონტაქტო ინფორმაცია.")

st.caption("© 2026 BuildX Construction Company")
