import streamlit as st
import re

# 1. გვერდის კონფიგურაცია (Light Mode-ის იძულება)
st.set_page_config(
    page_title="BuildX | Smart Construction",
    page_icon="🏗️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. ULTRA-CLEAN UI CSS
st.markdown("""
    <style>
    /* ბრაუზერის თემის იგნორირება და გათეთრება */
    :root { --primary-color: #2E86C1; }
    .stApp { background-color: #FFFFFF !important; }
    
    /* ტექსტის სტილი */
    h1, h2, h3, h4, label, p, .stMarkdown {
        color: #1A1A1A !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }

    /* ველების კონტეინერები - შევიწროებული და დახვეწილი */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        border: 1.5px solid #E2E8F0 !important;
        border-radius: 10px !important;
        background-color: #F8FAFC !important;
        transition: all 0.2s ease;
    }
    
    /* ფოკუსის ეფექტი */
    div[data-baseweb="input"]:focus-within, div[data-baseweb="select"]:focus-within {
        border-color: #2E86C1 !important;
        background-color: #FFFFFF !important;
        box-shadow: 0 0 0 3px rgba(46, 134, 193, 0.1) !important;
    }

    /* ტექსტი ველებში */
    input { color: #1A1A1A !important; font-size: 16px !important; }

    /* ღილაკის დიზაინი */
    .stButton > button {
        width: 100% !important;
        background: linear-gradient(90deg, #2E86C1 0%, #2471A3 100%) !important;
        color: white !important;
        border: none !important;
        padding: 12px !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 18px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    
    /* Metric Card */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 15px !important;
        padding: 20px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
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
col_logo1, col_logo2, col_logo3 = st.columns([1, 1, 1])
with col_logo2:
    try:
        st.image("BuildX.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align: center;'>🏗️ BUILDX</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #64748b !important;'>Smart Construction Estimator</p>", unsafe_allow_html=True)
st.markdown("---")

# --- ნაბიჯი 1: საკონტაქტო ბლოკი ---
st.subheader("👤 საკონტაქტო ინფორმაცია")
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    full_name = st.text_input("სახელი, გვარი", placeholder="მაგ: ლაშა ჯაკობია")
    phone = st.text_input("ტელეფონის ნომერი", placeholder="5XXXXXXXX")

with row1_col2:
    email = st.text_input("Email", placeholder="example@email.com")
    location = st.selectbox("მშენებლობის რაიონი", ["არჩიეთ რაიონი...", "თბილისი", "მცხეთა", "თეთრიწყარო"])

# ვალიდაციის შეტყობინებები
if email and not is_valid_email(email): st.error("📧 ჩაწერეთ სწორი Email ფორმატი")
if phone and not is_valid_phone(phone): st.error("📞 ნომერი უნდა შეიცავდეს მხოლოდ ციფრებს")

st.markdown("<br>", unsafe_allow_html=True)

# ვალიდაციის ლოგიკა
email_ok = email and is_valid_email(email)
phone_ok = phone and is_valid_phone(phone) and len(phone) >= 9

if full_name and email_ok and phone_ok and location != "არჩიეთ რაიონი...":
    
    st.markdown("---")
    
    # --- ნაბიჯი 2: კალკულატორი ორ სვეტად ---
    st.subheader("🏠 პროექტის პარამეტრები")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("**ზოგადი**")
        area = st.number_input("ფართობი (კვ.მ):", min_value=1, step=1, value=None, placeholder="მაგ: 150")
        floors = st.selectbox("სართულები:", [1, 2, 3])
        roof_type = st.selectbox("სახურავი:", ["თუნუქი (Classic)", "ბრტყელი გადახურვა"])

    with col_b:
        st.markdown("**მასალები**")
        concrete_grade = st.selectbox("ბეტონის მარკა:", ["B20 (M250)", "B25 (M350)"])
        wall_material = st.selectbox("კედლის მასალა:", ["პემზის ბლოკი", "აგური", "გაზბლოკი"])
        window_type = st.selectbox("ფანჯარა:", ["სტანდარტული", "პრემიუმ ალუმინი"])

    st.markdown("<br>", unsafe_allow_html=True)

    if area:
        # ლოგიკა
        p_const, p_roof, p_facade, p_comm = 280, 85, 120, 60
        if floors > 1: p_const *= 1.15
        if wall_material == "აგური": p_const += 45
        if roof_type == "ბრტყელი გადახურვა": p_roof = 145
        if window_type == "პრემიუმ ალუმინი": p_facade += 160

        total_cost = area * (p_const + p_roof + p_facade + p_comm)

        # ფასის ბლოკი
        st.metric(label="სავარაუდო ბიუჯეტი (ჯამში)", value=f"${total_cost:,.0f}")

        with st.expander("🔍 იხილეთ ხარჯების ჩაშლა"):
            res_col1, res_col2 = st.columns(2)
            res_col1.write(f"🔹 კონსტრუქცია: **${area * p_const:,.0f}**")
            res_col1.write(f"🔹 გადახურვა: **${area * p_roof:,.0f}**")
            res_col2.write(f"🔹 ფასადი: **${area * p_facade:,.0f}**")
            res_col2.write(f"🔹 კომუნიკაციები: **${area * p_comm:,.0f}**")

        st.markdown("---")
        st.subheader("📁 ნახაზის ატვირთვა")
        st.file_uploader("ატვირთეთ ფაილი AI ანალიზისთვის", type=['png', 'jpg', 'pdf'])
        
        if st.button("მონაცემების გაგზავნა 🚀"):
            st.success(f"მადლობა {full_name}, მოთხოვნა გაგზავნილია!")
    else:
        st.info("💡 შეიყვანეთ ფართობი კალკულაციის სანახავად")

else:
    st.info("📍 გთხოვთ, შეავსოთ საკონტაქტო მონაცემები კალკულატორის გასააქტიურებლად.")

st.caption("© 2026 BuildX Construction Company")
