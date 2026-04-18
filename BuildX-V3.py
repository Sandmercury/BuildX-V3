import streamlit as st
import re

# საიტის კონფიგურაცია
st.set_page_config(page_title="BuildX | Construction", page_icon="🏗️", layout="centered")

# --- CUSTOM CSS (მაქსიმალური კონტრასტი და ფოკუსი) ---
st.markdown("""
    <style>
    /* მთლიანი საიტის ფონი */
    .stApp { background-color: #FFFFFF; }
    
    /* ტექსტების ფერი - სუფთა შავი */
    h1, h2, h3, h4, p, label, .stMarkdown { 
        color: #000000 !important; 
        font-weight: 600 !important; 
    }

    /* ინპუტების სტილი */
    input { 
        color: #000000 !important; 
        background-color: #FFFFFF !important;
        -webkit-text-fill-color: #000000 !important;
    }
    
    /* ველების ჩარჩოები */
    .stTextInput div[data-baseweb="input"], 
    .stNumberInput div[data-baseweb="input"], 
    .stSelectbox div[data-baseweb="select"] {
        border: 2px solid #1A1A1A !important;
        border-radius: 8px !important;
        background-color: #FFFFFF !important;
    }

    /* აქტიური ველის კონტრასტი (ციმციმა ხაზი და შავი ჩარჩო) */
    .stTextInput div[data-baseweb="input"]:focus-within,
    .stNumberInput div[data-baseweb="input"]:focus-within {
        border: 2px solid #2E86C1 !important;
        box-shadow: 0 0 0 2px rgba(46, 134, 193, 0.2) !important;
    }

    /* ღილაკის მუდმივი კონტრასტული სტილი */
    .stButton>button {
        background-color: #2E86C1 !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        width: 100% !important;
        display: block !important;
        opacity: 1 !important;
    }
    .stButton>button:hover {
        background-color: #1B4F72 !important;
        color: #FFFFFF !important;
    }

    /* მეტრიკის ციფრების ფერი */
    [data-testid="stMetricValue"] {
        color: #2E86C1 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ლოგო ---
col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
with col_l2:
    try:
        st.image("Screenshot_2026-04-19_at_01.31.05-removebg-preview.png", use_container_width=True)
    except:
        st.title("🏗️ BUILDX")

st.markdown("---")

# --- ნაბიჯი 1: საკონტაქტო ინფორმაცია ---
st.markdown("### 👤 საკონტაქტო ინფორმაცია")
c_name, c_mail, c_phone = st.columns(3)

with c_name:
    full_name = st.text_input("სახელი, გვარი", placeholder="მაგ: სანდრო მერკვილიშვილი")

with c_mail:
    email = st.text_input("Mail", placeholder="example@mail.com")

with c_phone:
    phone = st.text_input("ტელეფონის ნომერი", placeholder="5XXXXXXXX")

location = st.selectbox(
    "აირჩიეთ რაიონი:", 
    ["არჩიეთ რაიონი...", "თბილისი", "მცხეთა", "თეთრიწყარო"],
    index=0
)

# ვალიდაციის ფუნქციები
def is_valid_email(e):
    return re.match(r"[^@]+@[^@]+\.[^@]+", e)

def is_valid_phone(p):
    return p.isdigit() and len(p) >= 9

st.markdown("---")

# --- ნაბიჯი 2: კალკულატორი (ჩნდება მხოლოდ ვალიდაციის შემდეგ) ---
if full_name and is_valid_email(email) and is_valid_phone(phone) and location != "არჩიეთ რაიონი...":
    
    # 🏠 პროექტის ზოგადი პარამეტრები
    st.markdown("### 🏠 პროექტის ზოგადი პარამეტრები")
    area = st.number_input("სახლის საერთო ფართობი (კვ.მ):", min_value=1, step=1, value=150)
    floors = st.selectbox("სართულების რაოდენობა:", [1, 2, 3])
    
    # 🏗️ კონსტრუქციული დეტალები
    st.markdown("### 🏗️ კონსტრუქციული დეტალები")
    concrete_grade = st.selectbox("ბეტონის მარკა:", ["B20 (M250)", "B25 (M350)"])
    wall_material = st.selectbox("კედლის მასალა:", ["პემზის ბლოკი", "აგური", "გაზბლოკი"])
    
    # 🏠 ექსტერიერი
    st.markdown("### 🏠 ექსტერიერი")
    roof_type = st.selectbox("სახურავის ტიპი:", ["თუნუქი (Classic)", "ბრტყელი გადახურვა"])
    window_type = st.selectbox("ფანჯარა:", ["სტანდარტული მეტალოპლასტმასი", "პრემიუმ ალუმინი"])
    door_type = st.selectbox("კარი:", ["რკინა", "ხე"])

    # --- გაანგარიშების ლოგიკა ---
    p_const, p_roof, p_facade, p_comm = 280, 85, 120, 60
    if floors > 1: p_const *= 1.15
    if wall_material == "აგური": p_const += 45
    if concrete_grade == "B25 (M350)": p_const += 15
    if roof_type == "ბრტყელი გადახურვა": p_roof = 145
    if window_type == "პრემიუმ ალუმინი": p_facade += 160
    if door_type == "ხე": p_facade += 25

    val_const = area * p_const
    val_roof = area * p_roof
    val_facade = area * p_facade
    val_comm = area * p_comm
    total_cost = val_const + val_roof + val_facade + val_comm

    st.markdown("---")
    st.metric(label="ჯამური სავარაუდო ბიუჯეტი", value=f"${total_cost:,.0f}")

    with st.expander("🔍 იხილეთ დეტალური განაწილება"):
        st.write(f"🔹 **კონსტრუქციული ნაწილი:** ${val_const:,.0f}")
        st.write(f"🔹 **გადახურვა:** ${val_roof:,.0f}")
        st.write(f"🔹 **ფასადი და კარ-ფანჯარა:** ${val_facade:,.0f}")
        st.write(f"🔹 **კომუნიკაციები:** ${val_comm:,.0f}")

    st.markdown("---")
    st.subheader("📁 ნახაზის ატვირთვა (AI ანალიზი)")
    st.file_uploader("ატვირთეთ კონსტრუქციული ნახაზი", type=['png', 'jpg', 'pdf'])
    
    if st.button("მონაცემების გაგზავნა 🚀"):
        st.success(f"მადლობა {full_name}, თქვენი მონაცემები წარმატებით გაიგზავნა!")

else:
    # შეცდომების ჩვენება
    if not full_name:
        st.info("ℹ️ კალკულატორის გასააქტიურებლად შეიყვანეთ სახელი და გვარი.")
    elif not is_valid_email(email):
        st.error("📧 გთხოვთ, შეიყვანოთ მეილი სწორი ფორმატით (@-ის ჩათვლით).")
    elif not is_valid_phone(phone):
        st.error("📞 ნომერი უნდა შეიცავდეს მხოლოდ ციფრებს (მინ. 9 სიმბოლო).")
    elif location == "არჩიეთ რაიონი...":
        st.warning("📍 გთხოვთ, აირჩიოთ მშენებლობის რაიონი.")

st.markdown("---")
st.caption("© 2026 BuildX Construction Company | All Rights Reserved")
