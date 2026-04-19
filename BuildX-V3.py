import streamlit as st

st.set_page_config(page_title="BuildX-V2 | Construction Pro", page_icon="🏗️", layout="wide")

# საიტის ვიზუალური ნაწილი
st.title("🏗️ BuildX - ვერსია 2.0")
st.subheader("დეტალური სამშენებლო კალკულატორი")

# სვეტებად დაყოფა უკეთესი ვიზუალისთვის
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📋 პროექტის პარამეტრები")
    area = st.number_input("სახლის საერთო ფართობი (კვ.მ):", min_value=10, value=150)
    floors = st.selectbox("სართულიანობა:", [1, 2, 3])
    
    st.divider()
    
    st.write("### 🏗️ კონსტრუქციული დეტალები")
    concrete_grade = st.selectbox("ბეტონის მარკა:", ["B20 (M250)", "B25 (M350)"])
    wall_material = st.selectbox("კედლის მასალა:", ["პემზის ბლოკი 20სმ", "აგური", "გაზობლოკი"])
    
    st.write("### 🏠 ექსტერიერი")
    roof_type = st.selectbox("სახურავის ტიპი:", ["თუნუქი (Classic)", "ბრტყელი გადახურვა", "კრამიტი"])
    windows_type = st.radio("კარ-ფანჯარა:", ["სტანდარტული მეტალოპლასტმასი", "პრემიუმ ალუმინი"])

# გამოთვლის ლოგიკა (შენი ექსელის ფასებზე დაყრდნობით)
with col2:
    st.header("💰 ხარჯთაღრიცხვა")
    
    # სატესტო ერთეულის ფასები (შენი ფაილიდან აღებული ლოგიკით)
    prices = {
        "კარკასი": 280,   # საშუალო $ კვ.მ-ზე
        "სახურავი": 85,
        "ფასადი": 120,
        "კომუნიკაციები": 60
    }
    
    # კოეფიციენტები შერჩეული პარამეტრების მიხედვით
    if floors > 1: prices["კარკასი"] *= 1.15
    if wall_material == "აგური": prices["კარკასი"] += 40
    if roof_type == "ბრტყელი გადახურვა": prices["სახურავი"] = 140
    if windows_type == "პრემიუმ ალუმინი": prices["ფასადი"] += 150

    # ჯამების დათვლა
    cost_structure = area * prices["კარკასი"]
    cost_roof = area * prices["სახურავი"]
    cost_facade = area * prices["ფასადი"]
    cost_engineering = area * prices["კომუნიკაციები"]
    
    total_cost = cost_structure + cost_roof + cost_facade + cost_engineering

    # შედეგების ჩვენება
    st.metric(label="ჯამური სავარაუდო ბიუჯეტი", value=f"${total_cost:,.0f}")
    
    with st.expander("იხილეთ დეტალური განაწილება"):
        st.write(f"🔹 **კონსტრუქციული ნაწილი:** ${cost_structure:,.0f}")
        st.write(f"🔹 **გადახურვა:** ${cost_roof:,.0f}")
        st.write(f"🔹 **ფასადი და კარ-ფანჯარა:** ${cost_facade:,.0f}")
        st.write(f"🔹 **კომუნიკაციები:** ${cost_engineering:,.0f}")

st.divider()

# ფაილის ატვირთვის სექცია (მომავალი AI-სთვის)
st.subheader("📁 ნახაზის ატვირთვა (AI ანალიზი)")
uploaded_file = st.file_uploader("ატვირთეთ კონსტრუქციული ნახაზი ზუსტი დათვლისთვის", type=['pdf', 'png', 'jpg'])

if uploaded_file:
    st.success("ნახაზი მიღებულია! შემდეგ ეტაპზე AI დაამუშავებს მონაცემებს.")
