import streamlit as st
import base64

# საიტის კონფიგურაცია - ნათელი თემა
st.set_page_config(page_title="BuildX | Construction", page_icon="🏗️", layout="centered")

# --- CUSTOM CSS დიზაინისთვის ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #2e86c1;
        color: white;
        border-radius: 8px;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO ---
# შეცვალე 'logo.png' შენი ფაილის რეალური სახელით
try:
    st.image("logo.png", width=250)
except:
    st.title("BX BUILDX") # თუ ლოგო არ მოიძებნა

st.subheader("მშენებლობის დაგეგმვა და კალკულაცია")

# --- ნაბიჯი 1: მომხმარებლის ინფორმაცია ---
st.markdown("### 👤 საკონტაქტო ინფორმაცია")
col_info1, col_info2 = st.columns(2)

with col_info1:
    full_name = st.text_input("სახელი, გვარი *")
    email = st.text_input("Mail *")

with col_info2:
    phone = st.text_input("ტელეფონის ნომერი *")
    location = st.selectbox("აირჩიეთ რაიონი:", ["თბილისი", "მცხეთა", "თეთრიწყარო"])

st.divider()

# --- ნაბიჯი 2: მშენებლობის დეტალები ---
if full_name and email and phone:
    st.markdown("### 🏠 მშენებლობის დეტალები")
    
    col1, col2 = st.columns(2)
    
    with col1:
        area = st.number_input("სახლის საერთო ფართობი (კვ.მ):", min_value=10, value=150)
        floors = st.selectbox("სართულიანობა:", [1, 2, 3])
        material = st.selectbox("კედლის მასალა:", ["პემზის ბლოკი 20სმ", "აგური", "გაზობლოკი"])

    with col2:
        st.write("#### 💰 სავარაუდო ბიუჯეტი")
        
        # საბაზისო ლოგიკა
        base_price = 300
        if location == "თბილისი": base_price += 20 # ტრანსპორტირების/ლოკაციის დანამატი
        if floors > 1: base_price += 50
        if material == "აგური": base_price += 40
        
        total_cost = area * base_price
        
        st.metric(label="ჯამური ღირებულება", value=f"${total_cost:,.0f}")
        st.info(f"ლოკაცია: {location}")

    st.divider()
    
    # ნახაზის ატვირთვა
    st.subheader("📁 ნახაზის ანალიზი (AI)")
    uploaded_file = st.file_uploader("ატვირთეთ კონსტრუქციული ნახაზი", type=['png', 'jpg', 'pdf'])
    
    if st.button("მონაცემების გაგზავნა"):
        st.success(f"მადლობა {full_name}, თქვენი მოთხოვნა რეგისტრირებულია!")
else:
    st.warning("გთხოვთ, შეავსოთ საკონტაქტო ინფორმაცია კალკულატორის გასააქტიურებლად.")

st.caption("© 2026 BuildX Construction Company")