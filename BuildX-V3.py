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
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600&family=Playfair+Display:wght@600&display=swap');

/* ── 1. APP SHELL ── */
.stApp,
.stApp > div,
section.main,
section.main > div,
.block-container {
    background-color: #F5F3EE !important;
}
.block-container {
    max-width: 760px !important;
    padding-top: 40px !important;
    padding-bottom: 80px !important;
}
#MainMenu, footer, header { visibility: hidden !important; }

/* ── 2. FONT — override Source Sans ── */
html, body,
.stApp *:not(.bx-logo-text):not(.bx-result-amount) {
    font-family: 'DM Sans', sans-serif !important;
}

/* ── 3. CARD — target Streamlit's border container wrapper ──
   st.container(border=True) renders:
   div[data-testid="stVerticalBlockBorderWrapper"]
     └─ div  ← this inner div gets the card style             */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF !important;
    border: 1px solid #E2DFD8 !important;
    border-radius: 18px !important;
    overflow: hidden !important;
    margin-bottom: 12px !important;
}
/* Remove the inner div's own padding so we control it */
div[data-testid="stVerticalBlockBorderWrapper"] > div {
    padding: 24px 26px 26px !important;
    background: #FFFFFF !important;
    border: none !important;
    border-radius: 0 !important;
}

/* ── 4. INPUT LABELS ── */
.stTextInput > label,
.stSelectbox > label,
.stNumberInput > label,
.stFileUploader > label {
    font-size: 11px !important;
    font-weight: 600 !important;
    color: #9A9790 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
    margin-bottom: 4px !important;
}

/* ── 5. INPUT BOXES ──
   Target every possible Streamlit version's wrapper         */
div[data-baseweb="input"],
div[data-baseweb="input"] > div,
div[data-baseweb="base-input"] {
    border-radius: 10px !important;
}
div[data-baseweb="input"] > div {
    background-color: #F7F6F3 !important;
    border: 1.5px solid #E2DFD8 !important;
    box-shadow: none !important;
}
/* Kill the red invalid border Streamlit adds on first load */
div[data-baseweb="input"] > div,
div[data-baseweb="input"] > div[aria-invalid],
div[data-baseweb="input"] > div[aria-invalid="true"],
div[data-baseweb="input"] > div[class*="error"] {
    border-color: #E2DFD8 !important;
    box-shadow: none !important;
    outline: none !important;
}
div[data-baseweb="input"]:focus-within > div {
    border-color: #C8A96E !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 0 0 3px rgba(200,169,110,0.13) !important;
}
div[data-baseweb="input"] input {
    color: #1C1B18 !important;
    font-size: 14px !important;
    background: transparent !important;
}

/* ── 6. SELECT BOXES ── */
div[data-baseweb="select"] > div:first-child {
    background-color: #F7F6F3 !important;
    border: 1.5px solid #E2DFD8 !important;
    border-radius: 10px !important;
    box-shadow: none !important;
}
div[data-baseweb="select"]:focus-within > div:first-child {
    border-color: #C8A96E !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 0 0 3px rgba(200,169,110,0.13) !important;
}
div[data-baseweb="select"] span,
div[data-baseweb="select"] [data-id="select"] {
    color: #1C1B18 !important;
    font-size: 14px !important;
}

/* ── 7. NUMBER INPUT ── */
div[data-testid="stNumberInput"] div[data-baseweb="input"] > div {
    background-color: #F7F6F3 !important;
    border: 1.5px solid #E2DFD8 !important;
    border-radius: 10px !important;
    box-shadow: none !important;
}
div[data-testid="stNumberInput"] div[data-baseweb="input"]:focus-within > div {
    border-color: #C8A96E !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 0 0 3px rgba(200,169,110,0.13) !important;
}

/* ── 8. BUTTON ── */
.stButton > button {
    width: 100% !important;
    height: 52px !important;
    background: #1C1B18 !important;
    color: #F5F3EE !important;
    border: none !important;
    border-radius: 12px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    box-shadow: none !important;
}
.stButton > button:hover {
    background: #2D2C28 !important;
    box-shadow: 0 6px 20px rgba(28,27,24,0.18) !important;
}
.stButton > button p { color: #F5F3EE !important; }

/* ── 9. FILE UPLOADER ── */
section[data-testid="stFileUploadDropzone"] {
    background: #F7F6F3 !important;
    border: 1.5px dashed #D4D0C8 !important;
    border-radius: 12px !important;
}
section[data-testid="stFileUploadDropzone"]:hover {
    border-color: #C8A96E !important;
}

/* ── 10. SUCCESS / ERROR ── */
div[data-testid="stSuccessMessage"] {
    background: #EAF5EE !important;
    border-color: #2D7A5A !important;
    border-radius: 12px !important;
}
div[data-testid="stSuccessMessage"] p { color: #1A4D35 !important; font-weight: 500 !important; }
div[data-testid="stErrorMessage"] { border-radius: 10px !important; }

/* ── 11. CAPTION ── */
.stCaption p {
    text-align: center !important;
    font-size: 11px !important;
    color: #B5B2AB !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* ── 12. COLUMNS ── */
div[data-testid="stHorizontalBlock"] { gap: 14px !important; }

/* ── 13. PURE HTML CLASSES ── */
.bx-logo-wrap {
    display:flex; align-items:center; justify-content:center;
    gap:13px; margin-bottom:10px;
}
.bx-logo-icon {
    width:46px; height:46px; background:#1C1B18; border-radius:12px;
    display:flex; align-items:center; justify-content:center;
}
.bx-logo-text {
    font-family:'Playfair Display',serif !important;
    font-size:28px; font-weight:600; letter-spacing:4px; color:#1C1B18;
}
.bx-tagline {
    text-align:center; font-size:11px; color:#9A9790;
    letter-spacing:3.5px; text-transform:uppercase; margin-bottom:20px;
}
.bx-trust {
    display:flex; justify-content:center; gap:20px; flex-wrap:wrap;
    margin:0 auto 24px; padding:11px 20px;
    background:#FFFFFF; border-radius:50px; border:1px solid #E2DFD8;
    width:fit-content;
}
.bx-trust-item {
    display:flex; align-items:center; gap:7px;
    font-size:12px; font-weight:500; color:#6B6963; white-space:nowrap;
}
.bx-trust-dot {
    width:6px; height:6px; border-radius:50%;
    background:#C8A96E; flex-shrink:0;
}
/* Card header — rendered with st.markdown inside the container */
.bx-card-hdr {
    display:flex; align-items:center; gap:12px;
    padding-bottom:16px; border-bottom:1px solid #EDEAE3;
    margin-bottom:20px; margin-left:-26px; margin-right:-26px;
    padding-left:26px; padding-right:26px;
}
.bx-step {
    width:28px; height:28px; background:#1C1B18; color:#F5F3EE;
    border-radius:8px; display:inline-flex; align-items:center;
    justify-content:center; font-size:12px; font-weight:700; flex-shrink:0;
}
.bx-title { font-size:15px; font-weight:600; color:#1C1B18; }
.bx-opt   { font-size:11px; color:#9A9790; font-weight:400; margin-left:8px; }
.bx-grp   {
    font-size:10px; font-weight:700; letter-spacing:2px;
    text-transform:uppercase; color:#B5B2AB; display:block;
    margin-bottom:6px; margin-top:2px;
}
/* Result panel — ALL colours explicit, never inherited */
.bx-result {
    background:#1C1B18; border-radius:14px;
    padding:24px 26px 20px; margin-top:10px;
}
.bx-rlabel {
    font-family:'DM Sans',sans-serif; font-size:10px; font-weight:700;
    letter-spacing:2.5px; text-transform:uppercase; color:#6B6963;
    margin-bottom:5px;
}
.bx-ramt {
    font-family:'Playfair Display',serif; font-size:42px; font-weight:600;
    color:#F0EDE7; letter-spacing:-1px; line-height:1;
}
.bx-rcur { font-family:'DM Sans',sans-serif; font-size:22px; color:#C8A96E; margin-right:3px; }
.bx-bkdn { display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:16px; }
.bx-bitem { background:#272724; border-radius:10px; padding:12px 14px; }
.bx-blbl  {
    font-family:'DM Sans',sans-serif; font-size:10px; color:#706D66;
    letter-spacing:1.2px; text-transform:uppercase; margin-bottom:4px;
}
.bx-bval  {
    font-family:'DM Sans',sans-serif; font-size:15px;
    font-weight:600; color:#E0DDD6;
}
.bx-info {
    display:flex; gap:10px; padding:12px 15px; margin-top:10px;
    background:#F7F6F3; border:1px solid #E2DFD8; border-radius:10px;
}
.bx-ispan { font-family:'DM Sans',sans-serif; font-size:12px; color:#8A8880; line-height:1.65; }
.bx-idot  {
    width:6px; height:6px; border-radius:50%;
    background:#C8A96E; margin-top:6px; flex-shrink:0;
}
</style>
""", unsafe_allow_html=True)

# ── helpers ──────────────────────────────────────────────────
def valid_email(e): return bool(re.match(r"[^@]+@[^@]+\.[^@]+", e)) if e else True
def valid_phone(p):
    if not p: return True
    return bool(re.match(r"^\+?[\d\s\-()+]*$", p))

# ── HEADER ───────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;margin-bottom:6px">
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
<div class="bx-trust">
  <div class="bx-trust-item"><span class="bx-trust-dot"></span>პროფესიონალური შეფასება</div>
  <div class="bx-trust-item"><span class="bx-trust-dot"></span>200+ განხორციელებული პროექტი</div>
  <div class="bx-trust-item"><span class="bx-trust-dot"></span>24/7 კონსულტაცია</div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════
# STEP 1 — everything inside one container
# ════════════════════════════════════
with st.container(border=True):
    st.markdown("""
    <div class="bx-card-hdr">
      <div class="bx-step">1</div>
      <span class="bx-title">საკონტაქტო ინფორმაცია</span>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        full_name = st.text_input("სახელი, გვარი", placeholder="ლაშა ჯაკობია")
        phone     = st.text_input("ტელეფონი",      placeholder="+995 5XX XXX XXX")
    with c2:
        email    = st.text_input("Email", placeholder="example@email.com")
        location = st.selectbox("მშენებლობის რაიონი",
                                ["— აირჩიეთ რაიონი —","თბილისი","მცხეთა","თეთრიწყარო"])

# validation (below the card)
if email and not valid_email(email):
    st.error("📧 ჩაწერეთ სწორი Email ფორმატი")
if phone and not valid_phone(phone):
    st.error("📞 ნომერი უნდა შეიცავდეს მხოლოდ ციფრებს")

email_ok   = bool(email) and valid_email(email)
phone_ok   = bool(phone) and valid_phone(phone) and len(re.sub(r"[\s+\-()+]","",phone)) >= 9
contact_ok = bool(full_name) and email_ok and phone_ok and location != "— აირჩიეთ რაიონი —"

# ════════════════════════════════════
# STEP 2
# ════════════════════════════════════
if contact_ok:
    with st.container(border=True):
        st.markdown("""
        <div class="bx-card-hdr">
          <div class="bx-step">2</div>
          <span class="bx-title">პროექტის პარამეტრები</span>
        </div>
        """, unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<span class="bx-grp">ზოგადი</span>', unsafe_allow_html=True)
            area      = st.number_input("ფართობი (კვ.მ)", min_value=1, step=1,
                                        value=None, placeholder="მაგ: 150")
            floors    = st.selectbox("სართულები", [1, 2, 3])
            roof_type = st.selectbox("სახურავი", ["თუნუქი (Classic)","ბრტყელი გადახურვა"])
        with col_b:
            st.markdown('<span class="bx-grp">მასალები</span>', unsafe_allow_html=True)
            _          = st.selectbox("ბეტონის მარკა",  ["B20 (M250)","B25 (M350)"])
            wall_mat   = st.selectbox("კედლის მასალა",  ["პემზის ბლოკი","აგური","გაზბლოკი"])
            window_tp  = st.selectbox("ფანჯარა",        ["სტანდარტული","პრემიუმ ალუმინი"])

        # estimate
        if area:
            pc, pr, pf, pm = 280, 85, 120, 60
            if floors > 1:                     pc = int(pc * 1.15)
            if wall_mat  == "აგური":           pc += 45
            if roof_type == "ბრტყელი გადახურვა": pr = 145
            if window_tp == "პრემიუმ ალუმინი":  pf += 160

            cc, cr, cf, cm = area*pc, area*pr, area*pf, area*pm
            total = cc + cr + cf + cm

            st.markdown(f"""
            <div class="bx-result">
              <div class="bx-rlabel">სავარაუდო ბიუჯეტი</div>
              <div class="bx-ramt"><span class="bx-rcur">$</span>{total:,.0f}</div>
              <div class="bx-bkdn">
                <div class="bx-bitem"><div class="bx-blbl">კონსტრუქცია</div><div class="bx-bval">${cc:,.0f}</div></div>
                <div class="bx-bitem"><div class="bx-blbl">გადახურვა</div><div class="bx-bval">${cr:,.0f}</div></div>
                <div class="bx-bitem"><div class="bx-blbl">ფასადი</div><div class="bx-bval">${cf:,.0f}</div></div>
                <div class="bx-bitem"><div class="bx-blbl">კომუნიკაციები</div><div class="bx-bval">${cm:,.0f}</div></div>
              </div>
            </div>
            <div class="bx-info">
              <div class="bx-idot"></div>
              <span class="bx-ispan">შეფასება სავარაუდოა და შეიძლება განსხვავდებოდეს ადგილზე
              დათვალიერების შემდეგ. ჩვენი სპეციალისტი დაგიკავშირდებათ კონსულტაციისთვის.</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="bx-info">
              <div class="bx-idot"></div>
              <span class="bx-ispan">შეიყვანეთ ფართობი კვ.მ-ში სავარაუდო ბიუჯეტის სანახავად.</span>
            </div>
            """, unsafe_allow_html=True)

    # ════════════════════════════════════
    # STEP 3
    # ════════════════════════════════════
    with st.container(border=True):
        st.markdown("""
        <div class="bx-card-hdr">
          <div class="bx-step">3</div>
          <span class="bx-title">ნახაზის ატვირთვა
            <span class="bx-opt">— სურვილისამებრ</span>
          </span>
        </div>
        """, unsafe_allow_html=True)

        st.file_uploader("ატვირთეთ ნახაზი ან გეგმა AI ანალიზისთვის",
                         type=["png","jpg","pdf"],
                         label_visibility="visible")

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    if st.button("→  მოთხოვნის გაგზავნა"):
        st.success(f"✓  მადლობა, {full_name}! მოთხოვნა მიღებულია. მალე დაგიკავშირდებით.")

else:
    st.markdown("""
    <div class="bx-info" style="margin-top:4px">
      <div class="bx-idot"></div>
      <span class="bx-ispan">გთხოვთ, შეავსოთ საკონტაქტო მონაცემები კალკულატორის გასააქტიურებლად.</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)
st.caption("© 2026 BuildX Construction Company")
