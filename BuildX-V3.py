import streamlit as st
import re

st.set_page_config(
    page_title="BuildX | Smart Construction",
    page_icon="🏗️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Playfair+Display:wght@600&display=swap');

/* ===== BASE RESET ===== */
html, body, .stApp {
    background-color: #F5F3EE !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* ===== HIDE STREAMLIT CHROME ===== */
#MainMenu, footer, header { visibility: hidden !important; }
.block-container {
    padding-top: 48px !important;
    padding-bottom: 60px !important;
    max-width: 780px !important;
}

/* ===== GLOBAL TEXT ===== */
h1, h2, h3, h4, h5, h6, p, label, span, div,
.stMarkdown, .stText {
    font-family: 'DM Sans', sans-serif !important;
    color: #1C1B18 !important;
}

/* ===== CARD WRAPPER ===== */
.bx-card {
    background: #FFFFFF;
    border-radius: 20px;
    border: 1px solid #E8E5DF;
    padding: 28px;
    margin-bottom: 16px;
}

.bx-card-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding-bottom: 20px;
    border-bottom: 1px solid #F0EDE7;
    margin-bottom: 24px;
}

.bx-step {
    width: 28px; height: 28px;
    background: #1C1B18;
    color: #F5F3EE;
    border-radius: 8px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: 600;
    flex-shrink: 0;
}

.bx-step.done { background: #2D7A5A; }

.bx-section-title {
    font-size: 15px !important;
    font-weight: 600 !important;
    color: #1C1B18 !important;
    margin: 0 !important;
}

/* ===== FORM FIELDS ===== */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div:first-child {
    border: 1.5px solid #E8E5DF !important;
    border-radius: 10px !important;
    background-color: #FAFAF8 !important;
    transition: all 0.2s ease !important;
    height: 44px !important;
}

div[data-baseweb="input"]:focus-within > div,
div[data-baseweb="select"]:focus-within > div:first-child {
    border-color: #C8A96E !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 0 0 3px rgba(200,169,110,0.12) !important;
}

input, select, textarea {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    color: #1C1B18 !important;
}

/* Input label style */
.stTextInput label, .stSelectbox label, .stNumberInput label {
    font-size: 11px !important;
    font-weight: 600 !important;
    color: #9A9790 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

/* ===== PARAM GROUP LABEL ===== */
.bx-group-label {
    font-size: 10px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #B5B2AB !important;
    margin-bottom: 12px !important;
    display: block !important;
}

/* ===== RESULT PANEL ===== */
.bx-result {
    background: #1C1B18;
    border-radius: 16px;
    padding: 28px;
    margin-top: 20px;
}

.bx-result-label {
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #6B6963 !important;
    margin-bottom: 6px !important;
}

.bx-result-amount {
    font-family: 'Playfair Display', serif !important;
    font-size: 42px !important;
    font-weight: 600 !important;
    color: #F5F3EE !important;
    letter-spacing: -1px !important;
    line-height: 1.1 !important;
}

.bx-result-currency {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 22px !important;
    color: #C8A96E !important;
    margin-right: 4px !important;
}

.bx-breakdown {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-top: 20px;
}

.bx-breakdown-item {
    background: #272724;
    border-radius: 10px;
    padding: 14px;
}

.bx-breakdown-item-label {
    font-size: 10px !important;
    color: #6B6963 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    margin-bottom: 4px !important;
}

.bx-breakdown-item-value {
    font-size: 16px !important;
    font-weight: 600 !important;
    color: #E8E5DF !important;
}

/* ===== INFO NOTE ===== */
.bx-info {
    display: flex;
    gap: 10px;
    padding: 14px 16px;
    background: #FAFAF8;
    border: 1px solid #E8E5DF;
    border-radius: 10px;
    font-size: 12px !important;
    color: #8A8880 !important;
    line-height: 1.6 !important;
    margin-top: 12px;
}

.bx-info-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #C8A96E;
    margin-top: 5px;
    flex-shrink: 0;
}

/* ===== UPLOAD ZONE ===== */
section[data-testid="stFileUploadDropzone"] {
    background: #FAFAF8 !important;
    border: 1.5px dashed #D4D0C8 !important;
    border-radius: 12px !important;
    transition: all 0.2s !important;
}

section[data-testid="stFileUploadDropzone"]:hover {
    border-color: #C8A96E !important;
    background: #FDFCF9 !important;
}

/* ===== SUBMIT BUTTON ===== */
.stButton > button {
    width: 100% !important;
    height: 52px !important;
    background: #1C1B18 !important;
    color: #F5F3EE !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    transition: all 0.25s !important;
    box-shadow: none !important;
}

.stButton > button:hover {
    background: #2D2C28 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(28,27,24,0.18) !important;
}

/* ===== TRUST BAR ===== */
.bx-trust {
    display: flex;
    justify-content: center;
    gap: 24px;
    flex-wrap: wrap;
    margin-bottom: 32px;
    padding: 13px 24px;
    background: #FFFFFF;
    border-radius: 50px;
    border: 1px solid #E8E5DF;
    width: fit-content;
    margin-left: auto;
    margin-right: auto;
}

.bx-trust-item {
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 12px;
    color: #6B6963;
    font-weight: 500;
    white-space: nowrap;
}

.bx-trust-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #C8A96E;
    flex-shrink: 0;
}

/* ===== LOGO / HEADER ===== */
.bx-logo-mark {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-bottom: 10px;
}

.bx-logo-icon {
    width: 44px; height: 44px;
    background: #1C1B18;
    border-radius: 11px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.bx-logo-text {
    font-family: 'Playfair Display', serif !important;
    font-size: 28px !important;
    font-weight: 600 !important;
    letter-spacing: 3px !important;
    color: #1C1B18 !important;
}

.bx-tagline {
    text-align: center;
    font-size: 12px;
    color: #9A9790;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 24px;
}

/* ===== METRIC OVERRIDE ===== */
div[data-testid="stMetric"] {
    display: none !important;
}

/* ===== DIVIDER ===== */
hr {
    border: none !important;
    border-top: 1px solid #E8E5DF !important;
    margin: 20px 0 !important;
}

/* ===== ERROR / SUCCESS ===== */
.stAlert {
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
}

/* ===== CAPTION ===== */
.stCaption {
    text-align: center !important;
    font-size: 11px !important;
    color: #B5B2AB !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Validation helpers ───────────────────────────────────────────────
def is_valid_email(e):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", e)) if e else True

def is_valid_phone(p):
    if not p: return True
    return bool(re.match(r"^\+?[0-9\s]*$", p))

# ─── HEADER ──────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-bottom:8px;">
  <div class="bx-logo-mark">
    <div class="bx-logo-icon">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M3 21H21M3 18H21M6 18V10M10 18V10M14 18V10M18 18V10M12 3L21 8H3L12 3Z"
              stroke="#F5F3EE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <span class="bx-logo-text">BUILDX</span>
  </div>
</div>
<div class="bx-tagline">Smart Construction Estimator</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="bx-trust">
  <div class="bx-trust-item"><div class="bx-trust-dot"></div>პროფესიონალური შეფასება</div>
  <div class="bx-trust-item"><div class="bx-trust-dot"></div>200+ განხორციელებული პროექტი</div>
  <div class="bx-trust-item"><div class="bx-trust-dot"></div>24/7 კონსულტაცია</div>
</div>
""", unsafe_allow_html=True)

# ─── STEP 1 : Contact ────────────────────────────────────────────────
contact_complete = False

st.markdown("""
<div class="bx-card">
  <div class="bx-card-header">
    <div class="bx-step">1</div>
    <span class="bx-section-title">საკონტაქტო ინფორმაცია</span>
  </div>
</div>
""", unsafe_allow_html=True)

with st.container():
    c1, c2 = st.columns(2)
    with c1:
        full_name = st.text_input("სახელი, გვარი", placeholder="ლაშა ჯაკობია", label_visibility="visible")
        phone     = st.text_input("ტელეფონი", placeholder="+995 5XX XXX XXX")
    with c2:
        email    = st.text_input("Email", placeholder="example@email.com")
        location = st.selectbox("მშენებლობის რაიონი",
                                ["— აირჩიეთ რაიონი —", "თბილისი", "მცხეთა", "თეთრიწყარო"])

if email and not is_valid_email(email):
    st.error("📧 ჩაწერეთ სწორი Email ფორმატი")
if phone and not is_valid_phone(phone):
    st.error("📞 ნომერი უნდა შეიცავდეს მხოლოდ ციფრებს")

email_ok   = bool(email) and is_valid_email(email)
phone_ok   = bool(phone) and is_valid_phone(phone) and len(phone.replace(" ", "").replace("+", "")) >= 9
contact_complete = bool(full_name) and email_ok and phone_ok and location != "— აირჩიეთ რაიონი —"

st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

# ─── STEP 2 : Parameters + Estimate ─────────────────────────────────
if contact_complete:

    st.markdown("""
    <div class="bx-card">
      <div class="bx-card-header">
        <div class="bx-step">2</div>
        <span class="bx-section-title">პროექტის პარამეტრები</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown('<span class="bx-group-label">ზოგადი</span>', unsafe_allow_html=True)
        area      = st.number_input("ფართობი (კვ.მ)", min_value=1, step=1,
                                    value=None, placeholder="მაგ: 150")
        floors    = st.selectbox("სართულები", [1, 2, 3])
        roof_type = st.selectbox("სახურავი", ["თუნუქი (Classic)", "ბრტყელი გადახურვა"])

    with col_b:
        st.markdown('<span class="bx-group-label">მასალები</span>', unsafe_allow_html=True)
        concrete_grade = st.selectbox("ბეტონის მარკა", ["B20 (M250)", "B25 (M350)"])
        wall_material  = st.selectbox("კედლის მასალა", ["პემზის ბლოკი", "აგური", "გაზბლოკი"])
        window_type    = st.selectbox("ფანჯარა", ["სტანდარტული", "პრემიუმ ალუმინი"])

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    if area:
        # Calculation
        p_const, p_roof, p_facade, p_comm = 280, 85, 120, 60
        if floors > 1:                          p_const  = int(p_const * 1.15)
        if wall_material == "აგური":            p_const += 45
        if roof_type == "ბრტყელი გადახურვა":   p_roof   = 145
        if window_type == "პრემიუმ ალუმინი":    p_facade += 160

        c_const  = area * p_const
        c_roof   = area * p_roof
        c_facade = area * p_facade
        c_comm   = area * p_comm
        total    = c_const + c_roof + c_facade + c_comm

        st.markdown(f"""
        <div class="bx-result">
          <div class="bx-result-label">სავარაუდო ბიუჯეტი</div>
          <div class="bx-result-amount">
            <span class="bx-result-currency">$</span>{total:,.0f}
          </div>
          <div class="bx-breakdown">
            <div class="bx-breakdown-item">
              <div class="bx-breakdown-item-label">კონსტრუქცია</div>
              <div class="bx-breakdown-item-value">${c_const:,.0f}</div>
            </div>
            <div class="bx-breakdown-item">
              <div class="bx-breakdown-item-label">გადახურვა</div>
              <div class="bx-breakdown-item-value">${c_roof:,.0f}</div>
            </div>
            <div class="bx-breakdown-item">
              <div class="bx-breakdown-item-label">ფასადი</div>
              <div class="bx-breakdown-item-value">${c_facade:,.0f}</div>
            </div>
            <div class="bx-breakdown-item">
              <div class="bx-breakdown-item-label">კომუნიკაციები</div>
              <div class="bx-breakdown-item-value">${c_comm:,.0f}</div>
            </div>
          </div>
        </div>
        <div class="bx-info">
          <div class="bx-info-dot"></div>
          შეფასება სავარაუდოა და შეიძლება განსხვავდებოდეს ადგილზე დათვალიერების შემდეგ.
          ჩვენი სპეციალისტი დაგიკავშირდებათ დეტალური კონსულტაციისთვის.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="bx-info">
          <div class="bx-info-dot"></div>
          შეიყვანეთ ფართობი კვ.მ-ში სავარაუდო ბიუჯეტის სანახავად.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    # ─── STEP 3 : Upload ─────────────────────────────────────────────
    st.markdown("""
    <div class="bx-card">
      <div class="bx-card-header">
        <div class="bx-step">3</div>
        <span class="bx-section-title">ნახაზის ატვირთვა
          <span style="font-size:11px; color:#9A9790; font-weight:400; margin-left:8px">— სურვილისამებრ</span>
        </span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.file_uploader(
        "ატვირთეთ ნახაზი ან გეგმა AI ანალიზისთვის",
        type=["png", "jpg", "pdf"],
        label_visibility="visible"
    )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    # ─── SUBMIT ───────────────────────────────────────────────────────
    if st.button("→  მოთხოვნის გაგზავნა"):
        st.success(f"✓  მადლობა, {full_name}! თქვენი მოთხოვნა მიღებულია. მალე დაგიკავშირდებით.")

else:
    st.markdown("""
    <div class="bx-info" style="margin-top:4px;">
      <div class="bx-info-dot"></div>
      გთხოვთ, შეავსოთ საკონტაქტო მონაცემები კალკულატორის გასააქტიურებლად.
    </div>
    """, unsafe_allow_html=True)

# ─── FOOTER ──────────────────────────────────────────────────────────
st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)
st.caption("© 2026 BuildX Construction Company")
