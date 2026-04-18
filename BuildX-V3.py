import streamlit as st
import re

# საიტის კონფიგურაცია
st.set_page_config(page_title="BuildX | Construction", page_icon="🏗️", layout="centered")

# --- CUSTOM CSS (კონტრასტი, ფოკუსი და დიზაინი) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* ტექსტის ფერები */
    h1, h2, h3, h4, p, label { color: #1A1A1A !important; font-weight: 500; }

    /* ინპუტების სტილი და ფოკუსი (ციმციმა ხაზი) */
    input { color: #1A1A1A !important; }
    .stTextInput div[data-baseweb="input"], .stNumberInput div[data-baseweb="input"], .stSelectbox div[data-baseweb="select"] {
        border: 1px solid #D1D5DB !important;
        border-radius: 8px !important;
    }
    /* აქტიური ველის კონტრასტი (როცა აჭერ) */
    .stTextInput div[data-baseweb="input"]:focus-within, 
    .stNumberInput div[data-baseweb="input"]:focus-within {
        border: 2px solid #2E86C1 !important;
        box-shadow: 0 0 0 2px rgba(46, 134, 193, 0.2) !important;
    }

    /* ღილაკის სტილი (რომ მუდამ ჩანდეს) */
    .stButton>button {
        background-color: #2E86C1 !important;
        color: white !important;
        border: None !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        width: 100% !important;
        display: block !important;
    }
    .stButton>button:hover {
        background-color: #21618C !important;
        border: None !important;
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

# --- ნაბიჯი 1: საკონტაქტო ინფორმაცია ---
st.markdown("### 👤 საკონტაქტო ინფორმაცია")
c_name, c_mail, c_phone = st.columns(3)

with c_name:
    full_name = st.text_input("სახელი, გვარი", placeholder="მაგ: დავით ბერიძე")

with c_mail:
    email = st.text_input("Mail", placeholder="example@mail.com")

with c_phone:
    phone = st.text_input("ტელეფონის ნომერი", placeholder="5XXXXXXXX")

# რაიონის არჩევანი დიფოლტის გარეშე
location = st.selectbox(
    "აირჩიეთ რაიონი:", 
    ["არჩიეთ რაიონი...", "თბილისი", "მცხეთა", "თეთრიწყარო"],
    index=0
)

# ვალიდაციის ფუნქციები
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 9

st.markdown("---")

# --- ნაბიჯი 2: კალკულატორი (ჩნდება მხოლოდ ვალიდაციის შემდეგ) ---
# ვამოწმებთ: შევსებულია თუ არა ველები, არის თუ არა @ მეილში, არის თუ არა მხოლოდ ციფრები ნომერში და არჩეულია თუ არა რაიონი
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

    # --- გაანგარიშება ---
    p_const, p_roof, p_facade, p_comm = 280, 85, 120, 60
    if floors > 1: p_const *= 1.15
    if wall_material == "აგური": p_const += 45
    if roof_type == "ბრტყელი გადახურვა": p_roof = 140
    if window_type == "პრემიუმ ალუმინი": p_facade += 150

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
        st.success(f"მადლობა {full_name}, ინფორმაცია წარმატებით გაიგზავნა!")

else:
    # შეცდომების შეტყობინებები დინამიურად
    if not full_name:
        st.info("ℹ️ კალკულატორის გასააქტიურებლად შეიყვანეთ სახელი და გვარი.")
    elif not is_valid_email(email):
        st.error("📧 გთხოვთ, შეიყვანოთ მეილი სწორი ფორმატით (უნდა შეიცავდეს @).")
    elif not is_valid_phone(phone):
        st.error("📞 ტელეფონის ნომერი უნდა შეიცავდეს მხოლოდ ციფრებს (მინ. 9 სიმბოლო).")
    elif location == "არჩიეთ რაიონი...":
        st.warning("📍 გთხოვთ, აირჩიოთ მშენებლობის რაიონი.")

st.caption("© 2026 BuildX Construction Company")
