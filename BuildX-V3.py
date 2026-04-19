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
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600&family=Playfair+Display:wght@600&display=swap');

/* ── BASE ── */
html, body, [class*="st-"], .stApp {
    font-family: 'DM Sans', sans-serif !important;
}
.stApp, .stApp > div {
    background-color: #F5F3EE !important;
}
#MainMenu, footer, header { visibility: hidden !important; }
.block-container {
    padding-top: 44px !important;
    padding-bottom: 64px !important;
    max-width: 800px !important;
}

/* ── FIELD LABELS (scoped — NOT inside dark panels) ── */
.stTextInput label p,
.stSelectbox label p,
.stNumberInput label p,
.stFileUploader label p {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    color: #9A9790 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
}

/* ── INPUTS — border & background ── */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div:first-child {
    border: 1.5px solid #E0DDD6 !important;
    border-radius: 10px !important;
    background-color: #FAFAF8 !important;
    box-shadow: none !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
div[data-baseweb="input"]:focus-within > div,
div[data-baseweb="select"]:focus-within > div:first-child {
    border-color: #C8A96E !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 0 0 3px rgba(200,169,110,0.13) !important;
}
/* kill Streamlit red invalid border */
div[data-baseweb="input"] > div[aria-invalid="true"],
div[data-baseweb="input"]:focus-within > div[aria-invalid="true"] {
    border-color: #E0DDD6 !important;
    box-shadow: none !important;
}
/* input text colour */
div[data-baseweb="input"] input,
div[data-baseweb="select"] [data-id="select"] {
    color: #1C1B18 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
}

/* ── BUTTON ── */
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
    box-shadow: none !important;
}
.stButton > button:hover {
    background: #2D2C28 !important;
    box-shadow: 0 6px 20px rgba(28,27,24,0.16) !important;
}
/* button text inside <p> */
.stButton > button p { color: #F5F3EE !important; font-family: 'DM Sans', sans-serif !important; }

/* ── FILE UPLOADER ── */
section[data-testid="stFileUploadDropzone"] {
    background: #FAFAF8 !important;
    border: 1.5px dashed #D4D0C8 !important;
    border-radius: 12px !important;
}
section[data-testid="stFileUploadDropzone"]:hover {
    border-color: #C8A96E !important;
    background: #FDFCF9 !important;
}

/* ── SUCCESS / ERROR ── */
.stAlert { border-radius: 10px !important; }
div[data-testid="stSuccessMessage"] {
    background: #EAF5EE !important;
    border-color: #2D7A5A !important;
    border-radius: 12px !important;
}
div[data-testid="stSuccessMessage"] p { color: #1A4D35 !important; font-weight: 500 !important; }

/* ── CAPTION ── */
.stCaption p {
    text-align: center !important;
    font-size: 11px !important;
    color: #B5B2AB !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* ── COLUMN GAP ── */
div[data-testid="stHorizontalBlock"] { gap: 16px !important; }

/* ════════════════════════════════════
   CUSTOM COMPONENTS (pure HTML/CSS)
   ════════════════════════════════════ */

/* Card header bar */
.bx-card {
    background: #FFFFFF;
    border-radius: 20px 20px 0 0;
    border: 1px solid #E8E5DF;
    border-bottom: none;
    padding: 20px 26px;
}
.bx-card-header {
    display: flex;
    align-items: center;
    gap: 12px;
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
    font-weight: 700;
    flex-shrink: 0;
    font-family: 'DM Sans', sans-serif;
}
.bx-section-title {
    font-size: 15px;
    font-weight: 600;
    color: #1C1B18;
    font-family: 'DM Sans', sans-serif;
}
.bx-optional {
    font-size: 11px;
    color: #9A9790;
    font-weight: 400;
    margin-left: 8px;
}

/* White field zone — sits below the header card, rounds at bottom */
.bx-fields-top {
    background: #FFFFFF;
    border-left: 1px solid #E8E5DF;
    border-right: 1px solid #E8E5DF;
    padding: 0 26px;
}
.bx-fields-top-rule {
    border-top: 1px solid #F0EDE7;
    margin-bottom: 18px;
}
.bx-fields-bottom {
    background: #FFFFFF;
    border: 1px solid #E8E5DF;
    border-top: none;
    border-radius: 0 0 20px 20px;
    padding: 0 26px 24px;
    margin-bottom: 16px;
}

/* Group label */
.bx-group-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #B5B2AB;
    display: block;
    margin-bottom: 10px;
    font-family: 'DM Sans', sans-serif;
}

/* Trust bar */
.bx-trust {
    display: flex;
    justify-content: center;
    gap: 22px;
    flex-wrap: wrap;
    margin: 0 auto 30px;
    padding: 12px 22px;
    background: #FFFFFF;
    border-radius: 50px;
    border: 1px solid #E8E5DF;
    width: fit-content;
}
.bx-trust-item {
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 12px;
    font-weight: 500;
    color: #6B6963;
    white-space: nowrap;
    font-family: 'DM Sans', sans-serif;
}
.bx-trust-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #C8A96E;
    flex-shrink: 0;
    display: inline-block;
}

/* Result panel — MUST use explicit colours, not inherit */
.bx-result {
    background: #1C1B18;
    border-radius: 16px;
    padding: 26px 28px 22px;
    margin-top: 18px;
    margin-bottom: 12px;
}
.bx-result-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #6B6963;
    margin-bottom: 6px;
}
.bx-result-amount {
    font-family: 'Playfair Display', serif;
    font-size: 44px;
    font-weight: 600;
    color: #F0EDE7;
    letter-spacing: -1px;
    line-height: 1;
}
.bx-result-currency {
    font-family: 'DM Sans', sans-serif;
    font-size: 24px;
    color: #C8A96E;
    margin-right: 3px;
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
    padding: 13px 15px;
}
.bx-bd-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 10px;
    color: #706D66;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 5px;
}
.bx-bd-value {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    font-weight: 600;
    color: #E0DDD6;
}

/* Info note */
.bx-info {
    display: flex;
    gap: 10px;
    padding: 13px 16px;
    background: #FAFAF8;
    border: 1px solid #E8E5DF;
    border-radius: 10px;
    margin-top: 12px;
}
.bx-info span {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    color: #8A8880;
    line-height: 1.65;
}
.bx-info-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #C8A96E;
    margin-top: 6px;
    flex-shrink: 0;
}

/* Logo */
.bx-logo-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 13px;
    margin-bottom: 10px;
}
.bx-logo-icon {
    width: 46px; height: 46px;
    background: #1C1B18;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.bx-logo-text {
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    font-weight: 600;
    letter-spacing: 4px;
    color: #1C1B18;
}
.bx-tagline {
    text-align: center;
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    color: #9A9790;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    margin-bottom: 22px;
}
</style>
""", unsafe_allow_html=True)

# ─── Helpers ─────────────────────────────────────────────────────────
def is_valid_email(e):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", e)) if e else True

def is_valid_phone(p):
    if not p: return True
    return bool(re.match(r"^\+?[\d\s\-()]*$", p))

# ─── HEADER ──────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-bottom:6px;">
  <div class="bx-logo-wrap">
    <div class="bx-logo-icon">
      <svg width="23" height="23" viewBox="0 0 24 24" fill="none">
        <path d="M3 21H21M3 18H21M6 18V10M10 18V10M14 18V10M18 18V10M12 3L21 8H3L12 3Z"
              stroke="#F5F3EE" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </div>
    <span class="bx-logo-text">BUILDX</span>
  </div>
</div>
<div class="bx-tagline">Smart Construction Estimator</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="bx-trust">
  <div class="bx-trust-item"><span class="bx-trust-dot"></span>პროფესიონალური შეფასება</div>
  <div class="bx-trust-item"><span class="bx-trust-dot"></span>200+ განხორციელებული პროექტი</div>
  <div class="bx-trust-item"><span class="bx-trust-dot"></span>24/7 კონსულტაცია</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# STEP 1 — Contact
# ══════════════════════════════════════════════════════════════
# Header card (top rounded, no bottom border)
st.markdown("""
<div class="bx-card">
  <div class="bx-card-header">
    <div class="bx-step">1</div>
    <span class="bx-section-title">საკონტაქტო ინფორმაცია</span>
  </div>
</div>
<div class="bx-fields-top"><div class="bx-fields-top-rule"></div></div>
""", unsafe_allow_html=True)

# Streamlit widgets — they render inside the white zone thanks to the
# cascading background set on .bx-fields-top / .bx-fields-bottom
c1, c2 = st.columns(2)
with c1:
    full_name = st.text_input("სახელი, გვარი", placeholder="ლაშა ჯაკობია")
    phone     = st.text_input("ტელეფონი", placeholder="+995 5XX XXX XXX")
with c2:
    email    = st.text_input("Email", placeholder="example@email.com")
    location = st.selectbox("მშენებლობის რაიონი",
                            ["— აირჩიეთ რაიონი —", "თბილისი", "მცხეთა", "თეთრიწყარო"])

# Close card visually
st.markdown('<div class="bx-fields-bottom"></div>', unsafe_allow_html=True)

# Validation
if email and not is_valid_email(email):
    st.error("📧 ჩაწერეთ სწორი Email ფორმატი")
if phone and not is_valid_phone(phone):
    st.error("📞 ნომერი უნდა შეიცავდეს მხოლოდ ციფრებს")

email_ok   = bool(email) and is_valid_email(email)
phone_ok   = bool(phone) and is_valid_phone(phone) and len(re.sub(r"[\s\+\-()]", "", phone)) >= 9
contact_ok = bool(full_name) and email_ok and phone_ok and location != "— აირჩიეთ რაიონი —"

# ══════════════════════════════════════════════════════════════
# STEP 2 — Parameters
# ══════════════════════════════════════════════════════════════
if contact_ok:
    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bx-card">
      <div class="bx-card-header">
        <div class="bx-step">2</div>
        <span class="bx-section-title">პროექტის პარამეტრები</span>
      </div>
    </div>
    <div class="bx-fields-top"><div class="bx-fields-top-rule"></div></div>
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

    st.markdown('<div class="bx-fields-bottom"></div>', unsafe_allow_html=True)

    # ── Estimate ─────────────────────────────────────────────
    if area:
        p_const, p_roof, p_facade, p_comm = 280, 85, 120, 60
        if floors > 1:                         p_const  = int(p_const * 1.15)
        if wall_material == "აგური":           p_const += 45
        if roof_type == "ბრტყელი გადახურვა":  p_roof   = 145
        if window_type == "პრემიუმ ალუმინი":   p_facade += 160

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
              <div class="bx-bd-label">კონსტრუქცია</div>
              <div class="bx-bd-value">${c_const:,.0f}</div>
            </div>
            <div class="bx-breakdown-item">
              <div class="bx-bd-label">გადახურვა</div>
              <div class="bx-bd-value">${c_roof:,.0f}</div>
            </div>
            <div class="bx-breakdown-item">
              <div class="bx-bd-label">ფასადი</div>
              <div class="bx-bd-value">${c_facade:,.0f}</div>
            </div>
            <div class="bx-breakdown-item">
              <div class="bx-bd-label">კომუნიკაციები</div>
              <div class="bx-bd-value">${c_comm:,.0f}</div>
            </div>
          </div>
        </div>
        <div class="bx-info">
          <div class="bx-info-dot"></div>
          <span>შეფასება სავარაუდოა და შეიძლება განსხვავდებოდეს ადგილზე დათვალიერების შემდეგ.
          ჩვენი სპეციალისტი დაგიკავშირდებათ დეტალური კონსულტაციისთვის.</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="bx-info">
          <div class="bx-info-dot"></div>
          <span>შეიყვანეთ ფართობი კვ.მ-ში სავარაუდო ბიუჯეტის სანახავად.</span>
        </div>
        """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════
    # STEP 3 — Upload
    # ══════════════════════════════════════════════════════════
    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bx-card">
      <div class="bx-card-header">
        <div class="bx-step">3</div>
        <span class="bx-section-title">
          ნახაზის ატვირთვა
          <span class="bx-optional">— სურვილისამებრ</span>
        </span>
      </div>
    </div>
    <div class="bx-fields-top"><div class="bx-fields-top-rule"></div></div>
    """, unsafe_allow_html=True)

    st.file_uploader(
        "ატვირთეთ ნახაზი ან გეგმა AI ანალიზისთვის",
        type=["png", "jpg", "pdf"],
        label_visibility="visible"
    )

    st.markdown('<div class="bx-fields-bottom"></div>', unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    if st.button("→  მოთხოვნის გაგზავნა"):
        st.success(f"✓  მადლობა, {full_name}! თქვენი მოთხოვნა მიღებულია. მალე დაგიკავშირდებით.")

else:
    st.markdown("""
    <div class="bx-info" style="margin-top:8px;">
      <div class="bx-info-dot"></div>
      <span>გთხოვთ, შეავსოთ საკონტაქტო მონაცემები კალკულატორის გასააქტიურებლად.</span>
    </div>
    """, unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────
st.markdown("<div style='height:36px'></div>", unsafe_allow_html=True)
st.caption("© 2026 BuildX Construction Company")
