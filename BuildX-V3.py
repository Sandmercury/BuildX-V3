import streamlit as st

# საიტის კონფიგურაცია
st.set_page_config(page_title="BuildX | Construction Estimator", page_icon="🏗️", layout="centered")

# --- CUSTOM CSS (თეთრი ფონი და მუქი ტექსტი) ---
st.markdown("""
    <style>
    /* მთლიანი საიტის ფონი */
    .stApp {
        background-color: #FFFFFF;
    }
    /* ყველა ტექსტის ფერი */
    h1, h2, h3, h4, p, label, .stMarkdown {
        color: #1A1A1A !important;
    }
    /* კალკულატორის ველების ფონი */
    .stNumberInput input, .stSelectbox div, .stTextInput input {
        background-color: #F0F2F6 !important;
        color: #1A1A1A !important;
    }
    /* Metric-ის ვიზუალი */
    [data-testid="stMetricValue"] {
        color: #2E86C1 !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ლოგოს ცენტრირება ---
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
    try:
        # დარწმუნდი რომ ფაილს ზუსტად ეს სახელი ჰქვია
        st.image("Screenshot_2026-04-19_at_01.31.05-removebg-preview.png", use_container_width=True)
    except:
        st.title("🏗️ BUILDX")

st.markdown("---")

# --- ნაბიჯი 1: მომხმარებლის ინფორმაცია ---
st.markdown("### 👤 საკონტაქტო ინფორმაცია")
c_name, c_mail, c_phone = st.columns(3)
with c_name:
    full_name = st.text_input("სახელი, გვარი *")
with c_mail:
    email = st.text_input("Mail *")
with c_phone:
    phone = st.text_input("ტელეფონის ნომერი *")

location = st.selectbox("აირჩიეთ რაიონი:", ["თბილისი", "მცხეთა", "თეთრიწყარო"])

st.markdown("---")

# --- ნაბიჯი 2: კალკულატორი ---
if full_name and email and phone:
    st.markdown("### 🏠 პროექტის ზოგადი პარამეტრები")
    col1, col2 = st.columns(2)
    
    with col1:
        area = st.number_input("სახლის საერთო ფართობი (კვ.მ):", min_value=1, value=150)
        floors = st.selectbox("სართულების რაოდენობა:", [1, 2, 3])
        
        st.markdown("### 🏗️ კონსტრუქციული დეტალები")
        concrete_grade = st.selectbox("ბეტონის მარკა:", ["B20 (M250)", "B25 (M350)"])
        wall_material = st.selectbox("კედლის მასალა:", ["პემზის ბლოკი", "აგური", "გაზბლოკი"])

    with col2:
        st.markdown("### 🏠 ექსტერიერი")
        roof_type = st.selectbox("სახურავის ტიპი:", ["თუნუქი (Classic)", "ბრტყელი გადახურვა"])
        window_type = st.selectbox("ფანჯარა:", ["სტანდარტული მეტალოპლასტმასი", "პრემიუმ ალუმინი"])
        door_type = st.selectbox("კარი:", ["რკინა", "ხე"])

    st.markdown("---")

    # --- გაანგარიშების ლოგიკა ---
    # ფასები (შეგიძლია შეცვალო შენი ექსელის მიხედვით)
    p_const = 280
    p_roof = 85
    p_facade = 120
    p_comm = 60

    if floors > 1: p_const *= 1.15
    if wall_material == "აგური": p_const += 45
    if concrete_grade == "B25 (M350)": p_const += 15
    if roof_type == "ბრტყელი გადახურვა": p_roof = 140
    if window_type == "პრემიუმ ალუმინი": p_facade += 150
    if door_type == "ხე": p_facade += 20

    # ჯამები
    val_const = area * p_const
    val_roof = area * p_roof
    val_facade = area * p_facade
    val_comm = area * p_comm
    total_cost = val_const + val_roof + val_facade + val_comm

    # შედეგების ჩვენება
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
        st.success(f"მადლობა {full_name}, ინფორმაცია შენახულია!")

else:
    st.warning("⚠️ გთხოვთ, შეავსოთ საკონტაქტო ინფორმაცია კალკულატორის გასააქტიურებლად.")

st.caption("© 2026 BuildX Construction Company")
