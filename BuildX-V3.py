import streamlit as st
import re

# საიტის კონფიგურაცია
st.set_page_config(page_title="BuildX | Construction", page_icon="🏗️", layout="centered")

# --- CUSTOM CSS (მაქსიმალური კონტრასტი და ფონის ფიქსაცია) ---
st.markdown("""
    <style>
    /* მთლიანი საიტის ფონი */
    .stApp { background-color: #FFFFFF !important; }
    
    /* ტექსტების ფერი */
    h1, h2, h3, h4, p, label, .stMarkdown { 
        color: #000000 !important; 
        font-weight: 600 !important; 
    }

    /* ველების ერთნაირი ვიზუალი და თეთრი ფონი */
    .stTextInput div[data-baseweb="input"], 
    .stNumberInput div[data-baseweb="input"], 
    .stSelectbox div[data-baseweb="select"],
    .stSelectbox [data-baseweb="select"] > div {
        border: 2px solid #1A1A1A !important;
        border-radius: 8px !important;
        background-color: #FFFFFF !important;
        min-height: 45px !important;
    }

    /* ტექსტის ფერი ველების შიგნით - ძალდატანებით თეთრი ფონი და შავი ასოები */
    input { 
        color: #000000 !important; 
        background-color: #FFFFFF !important;
        -webkit-text-fill-color: #000000 !important;
        caret-color: #000000 !important; /* კურსორის ფერი */
    }

    /* ბრაუზერის Autofill-ის ფონის ფიქსაცია (რომ არ გაშავდეს) */
    input:-webkit-autofill,
    input:-webkit-autofill:hover, 
    input:-webkit-autofill:focus {
        -webkit-box-shadow: 0 0 0px 1000px #FFFFFF inset !important;
        -webkit-text-fill-color: #000000 !important;
    }
    
    /* ფოკუსის სტილი */
    .stTextInput div[data-baseweb="input"]:focus-within,
    .stNumberInput div[data-baseweb="input"]:focus-within,
    .stSelectbox div[data-baseweb="select"]:focus-within {
        border: 2px solid #2E86C1 !important;
        box-shadow: 0 0 0 2px rgba(46, 134, 193, 0.2) !important;
    }

    /* ღილაკის სტილი */
    .stButton>button {
        background-color: #2E86C1 !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        width: 100% !important;
        border-radius: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ვალიდაციის ფუნქციები
def is_valid_email(e):
    return re.match(r"[^@]+@[^@]+\.[^@]+", e) if e else True

def is_valid_phone(p):
    if not p: return True
    pattern = r"^\+?[0-9]*$"
    return bool(re.match(pattern, p))

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
    if email and not is_valid_email(email):
        st.caption(" :red[გთხოვთ ჩაწერეთ სწორ ფორმატში]")

with c_phone:
    phone = st.text_input("ტელეფონის ნომერი", placeholder="+995XXXXXXXXX")
    if phone and not is_valid_phone(phone):
        st.caption(" :red[გთხოვთ ჩაწერეთ სწორ ფორმატში (დასაშვებია მხოლოდ ციფრები და +)]")

location = st.selectbox(
    "აირჩიეთ რაიონი:", 
    ["არჩიეთ რაიონი...", "თბილისი", "მცხეთა", "თეთრიწყარო"],
    index=0
)

st.markdown("---")

# --- ნაბიჯი 2: კალკულატორი ---
email_ok = email and is_valid_email(email)
phone_ok = phone and is_valid_phone(phone) and len(phone) >= 9

if full_name and email_ok and phone_ok and location != "არჩიეთ რაიონი...":
    
    st.markdown("### 🏠 პროექტის ზოგადი პარამეტრები")
    area = st.number_input("სახლის საერთო ფართობი (კვ.მ):", min_value=1, step=1, value=150)
    floors = st.selectbox("სართულების რაოდენობა:", [1, 2, 3])
    
    st.markdown("### 🏗️ კონსტრუქციული დეტალები")
    concrete_grade = st.selectbox("ბეტონის მარკა:", ["B20 (M250)", "B25 (M350)"])
    wall_material = st.selectbox("კედლის მასალა:", ["პემზის ბლოკი", "აგური", "გაზბლოკი"])
    
    st.markdown("### 🏠 ექსტერიერი")
    roof_type = st.selectbox("სახურავის ტიპი:", ["თუნუქი (Classic)", "ბრტყელი გადახურვა"])
    window_type = st.selectbox("ფანჯარა:", ["სტანდარტული მეტალოპლასტმასი", "პრემიუმ ალუმინი"])
    door_type = st.selectbox("კარი:", ["რკინა", "ხე"])

    # გაანგარიშება
    p_const, p_roof, p_facade, p_comm = 280, 85, 120, 60
    if floors > 1: p_const *= 1.15
    if wall_material == "აგური": p_const += 45
    if concrete_grade == "B25 (M350)": p_const += 15
    if roof_type == "ბრტყელი გადახურვა": p_roof = 145
    if window_type == "პრემიუმ ალუმინი": p_facade += 160
    if door_type == "ხე": p_facade += 25

    val_const, val_roof, val_facade, val_comm = area*p_const, area*p_roof, area*p_facade, area*p_comm
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
        st.success(f"მადლობა {full_name}, მონაცემები გაგზავნილია!")

else:
    if not full_name:
        st.info("ℹ️ შეიყვანეთ სახელი და გვარი.")
    elif not email_ok:
        st.warning("📧 გთხოვთ მიუთითოთ მეილი სწორი ფორმატით.")
    elif not phone_ok:
        st.warning("📞 გთხოვთ მიუთითოთ ვალიდური ტელეფონის ნომერი.")
    elif location == "არჩიეთ რაიონი...":
        st.warning("📍 აირჩიეთ მშენებლობის რაიონი.")

st.caption("© 2026 BuildX Construction Company")
