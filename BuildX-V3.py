import streamlit as st
import re

# საიტის კონფიგურაცია
st.set_page_config(page_title="BuildX | Construction", page_icon="🏗️", layout="centered")

# --- CUSTOM CSS (ვიზუალური სრულყოფილება) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    
    /* ტექსტების ფერი */
    h1, h2, h3, h4, p, label, .stMarkdown { 
        color: #000000 !important; 
        font-weight: 600 !important; 
    }

    /* ველების ერთნაირი ვიზუალი */
    .stTextInput > div > div, 
    .stNumberInput > div > div, 
    .stSelectbox > div > div,
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        background-color: #FFFFFF !important;
        border: 2px solid #1A1A1A !important;
        border-radius: 8px !important;
        min-height: 45px !important;
    }

    /* ტექსტი ველებში */
    input, .stSelectbox span, div[role="listbox"] {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* Autofill ფიქსაცია */
    input:-webkit-autofill {
        -webkit-box-shadow: 0 0 0px 1000px #FFFFFF inset !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* ღილაკის სტილი */
    .stButton > button {
        background-color: #2E86C1 !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        width: 100% !important;
        border-radius: 8px !important;
        height: 50px;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ვალიდაციის ფუნქციები
def is_valid_email(e):
    return re.match(r"[^@]+@[^@]+\.[^@]+", e) if e else True

def is_valid_phone(p):
    if not p: return True
    return bool(re.match(r"^\+?[0-9]*$", p))

# --- LOGO სექცია ---
# დარწმუნდი, რომ ფაილი "Screenshot_2026-04-19_at_01.31.05-removebg-preview.png" დევს BuildX-V3 საქაღალდეში
col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
with col_l2:
    try:
        st.image("BuildX.png", use_container_width=True)
    except:
        st.error("🏗️ BuildX")

st.markdown("---")

# --- ნაბიჯი 1: საკონტაქტო ინფორმაცია ---
st.markdown("### 👤 საკონტაქტო ინფორმაცია")
c_name, c_mail, c_phone = st.columns(3)

with c_name:
    full_name = st.text_input("სახელი, გვარი", placeholder="მაგ: ლაშა ჯაკობია")

with c_mail:
    email = st.text_input("Email", placeholder="example@Email.com")
    if email and not is_valid_email(email):
        st.caption(" :red[გთხოვთ ჩაწერეთ სწორ ფორმატში]")

with c_phone:
    phone = st.text_input("ტელეფონის ნომერი", placeholder="5XXXXXXXX")
    if phone and not is_valid_phone(phone):
        st.caption(" :red[გთხოვთ ჩაწერეთ სწორ ფორმატში (დასაშვებია მხოლოდ ციფრები და +)]")

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
        # ფასების ლოგიკა
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
        st.subheader("📁 ნახაზის ატვირთვა (AI ანალიზი)")
        st.file_uploader("ატვირთეთ კონსტრუქციული ნახაზი", type=['png', 'jpg', 'pdf'])
        
        if st.button("მონაცემების გაგზავნა 🚀"):
            st.success(f"მადლობა {full_name}, მონაცემები გაგზავნილია!")
    else:
        st.info("💡 შეიყვანეთ ფართობი კალკულაციისთვის.")
else:
    st.warning("📍 გთხოვთ სრულად შეავსოთ საკონტაქტო ინფორმაცია.")

st.caption("© 2026 BuildX Construction Company")
