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
        concrete_grade = st.selectbox
