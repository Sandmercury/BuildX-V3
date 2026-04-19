import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="BuildiX | Smart Construction",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Strip all Streamlit chrome and match dark bg
st.markdown("""
<style>
.stApp, section.main, .block-container,
.stApp > div, section.main > div {
    background: #0A0A0A !important;
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}
#MainMenu, footer, header { visibility: hidden !important; }
div[data-testid="stVerticalBlock"] { gap: 0 !important; }
iframe { display: block !important; }
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="ka">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=DM+Serif+Display&family=Noto+Sans+Georgian:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; }

body {
    background: #0A0A0A;
    font-family: 'Noto Sans Georgian', 'Inter', sans-serif;
    color: #F0EDE7;
    padding: 48px 20px 72px;
}

.wrap { max-width: 660px; margin: 0 auto; }

/* ─── HEADER ─── */
.hdr { text-align:center; margin-bottom:40px; }

.tagline {
    font-size: 10px;
    color: #555;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 22px;
}
.badges {
    display: flex;
    gap: 8px;
    justify-content: center;
    flex-wrap: wrap;
}
.badge {
    padding: 5px 14px;
    background: #161616;
    border: 1px solid #262626;
    border-radius: 100px;
    font-size: 11px;
    color: #666;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}
.badge::before {
    content: '';
    width: 5px; height: 5px;
    border-radius: 50%;
    background: #C8A96E;
    flex-shrink: 0;
}

/* ─── CARD ─── */
.card {
    background: #161616;
    border: 1px solid #242424;
    border-radius: 20px;
    padding: 28px 28px 30px;
    margin-bottom: 12px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.5);
}
.card-hdr {
    display: flex;
    align-items: center;
    gap: 14px;
    padding-bottom: 20px;
    border-bottom: 1px solid #222;
    margin: 0 -28px 24px;
    padding: 0 28px 20px;
}
.step-n {
    width: 30px; height: 30px;
    background: linear-gradient(135deg, #C8A96E, #9A6F30);
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 700; color: #111;
    flex-shrink: 0;
    box-shadow: 0 3px 14px rgba(200,169,110,0.4);
}
.card-title { font-size: 15px; font-weight: 600; color: #F0EDE7; }
.card-opt   { font-size: 11px; color: #555; font-weight: 400; margin-left: 5px; }

/* ─── GRID ─── */
.g2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

/* ─── FIELDS ─── */
.f { margin-bottom: 14px; }
.f:last-child { margin-bottom: 0; }

.f label {
    display: block;
    font-size: 10px;
    font-weight: 700;
    color: #555;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    margin-bottom: 7px;
}
.f input, .f select {
    width: 100%;
    height: 46px;
    background: #0F0F0F;
    border: 1.5px solid #2E2E2E;
    border-radius: 10px;
    padding: 0 14px;
    font-size: 14px;
    color: #F0EDE7;
    font-family: 'Noto Sans Georgian', 'Inter', sans-serif;
    outline: none;
    transition: border-color .2s, box-shadow .2s, background .2s;
    -webkit-appearance: none;
    appearance: none;
}
.f input::placeholder { color: #333; }
.f input:focus, .f select:focus {
    border-color: #C8A96E;
    background: #131313;
    box-shadow: 0 0 0 3px rgba(200,169,110,0.13);
}
.f input.err { border-color: #7A2020 !important; box-shadow: 0 0 0 3px rgba(122,32,32,.12) !important; }

.f select {
    cursor: pointer;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='11' height='7' viewBox='0 0 11 7'%3E%3Cpath d='M1 1l4.5 4.5L10 1' stroke='%23555' stroke-width='1.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 14px center;
    padding-right: 38px;
}
.f select option { background: #1E1E1E; color: #F0EDE7; }

.err-msg { font-size: 11px; color: #F87171; margin-top: 5px; display: none; }

/* ─── SECTION LABEL ─── */
.sec-lbl {
    font-size: 9px; font-weight: 700;
    letter-spacing: 2.5px; text-transform: uppercase;
    color: #383838; display: block;
    margin-bottom: 10px; margin-top: 2px;
}

/* ─── RESULT PANEL ─── */
.result {
    background: #0C0C0C;
    border: 1px solid #212121;
    border-radius: 16px;
    padding: 24px 26px 22px;
    margin-top: 18px;
    position: relative;
    overflow: hidden;
    display: none;
}
.result.on { display: block; }
.result::before {
    content: '';
    position: absolute; top:0; left:0; right:0; height:2px;
    background: linear-gradient(90deg, #C8A96E, #6B4A1E);
}
.r-lbl {
    font-size: 10px; font-weight: 700;
    letter-spacing: 3px; text-transform: uppercase;
    color: #444; margin-bottom: 8px;
}
.r-amt {
    font-family: 'DM Serif Display', serif;
    font-size: 50px; color: #F0EDE7;
    line-height: 1; letter-spacing: -1px;
}
.r-cur {
    font-family: 'Inter', sans-serif;
    font-size: 28px; color: #C8A96E;
    margin-right: 4px; font-weight: 300;
}
.bkdn {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px; margin-top: 20px;
}
.bi {
    background: #080808;
    border: 1px solid #1C1C1C;
    border-radius: 10px;
    padding: 12px 14px;
}
.bi-lbl { font-size: 9px; color: #444; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 5px; }
.bi-val { font-size: 15px; font-weight: 600; color: #C0BDB6; display: flex; align-items: center; gap: 8px; }
.bi-acc { width:3px; height:14px; background:#C8A96E; border-radius:2px; flex-shrink:0; }

/* ─── INFO / HINT BOX ─── */
.hint {
    display: flex; gap: 10px;
    padding: 13px 15px; margin-top: 14px;
    background: #111; border: 1px solid #1E1E1E;
    border-radius: 10px;
    font-size: 12px; color: #4A4A4A; line-height: 1.7;
}
.hint .dot { opacity:.35; flex-shrink:0; margin-top:1px; }

/* ─── FILE DROP ─── */
.file-drop {
    border: 1.5px dashed #282828;
    border-radius: 12px;
    padding: 28px 20px;
    text-align: center;
    cursor: pointer;
    transition: border-color .2s, background .2s;
    background: #0F0F0F;
    position: relative;
}
.file-drop:hover, .file-drop.over { border-color: #C8A96E; background: #131313; }
.file-drop input[type=file] {
    position: absolute; inset: 0;
    opacity: 0; cursor: pointer;
    height: 100%; border: none; background: none;
}
.fd-icon { font-size: 22px; margin-bottom: 8px; opacity: .25; }
.fd-txt  { font-size: 12px; color: #444; }
.fd-hint { font-size: 10px; color: #303030; margin-top: 4px; letter-spacing:1px; text-transform:uppercase; }
.fd-name { font-size: 12px; color: #C8A96E; margin-top: 8px; display: none; }

/* ─── BUTTON ─── */
.btn {
    width: 100%; height: 54px;
    background: linear-gradient(135deg, #C8A96E, #9A6F30);
    color: #111; border: none; border-radius: 12px;
    font-size: 12px; font-weight: 700;
    letter-spacing: 2.5px; text-transform: uppercase;
    cursor: pointer;
    box-shadow: 0 4px 24px rgba(200,169,110,0.32);
    transition: all .2s;
    font-family: 'Noto Sans Georgian', 'Inter', sans-serif;
    margin-top: 10px;
}
.btn:hover { background: linear-gradient(135deg, #D4B87A, #C8A96E); box-shadow: 0 8px 32px rgba(200,169,110,0.5); transform: translateY(-1px); }
.btn:active { transform: translateY(0); }

/* ─── SUCCESS ─── */
.success {
    background: #091A0F; border: 1px solid #174D28;
    border-radius: 12px; padding: 16px 20px;
    font-size: 13px; color: #4ADE80; font-weight: 500;
    display: none; margin-top: 10px;
}
.success.on { display: block; }

/* ─── LOCKED ─── */
.locked {
    display: flex; gap: 12px;
    padding: 15px 18px; margin-top: 4px;
    background: #111; border: 1px solid #1E1E1E;
    border-radius: 12px; align-items: center;
    font-size: 12px; color: #404040; line-height: 1.6;
}

/* ─── STEPS 2-3 (hidden) ─── */
.s23 { display: none; }
.s23.on { display: block; }

/* ─── FOOTER ─── */
.footer {
    text-align: center; font-size: 10px;
    color: #262626; letter-spacing: 2px;
    text-transform: uppercase; margin-top: 40px;
}
</style>
</head>
<body>
<div class="wrap">

  <!-- HEADER -->
  <div class="hdr">
    <img src="https://raw.githubusercontent.com/Sandmercury/BuildX-V3/main/BuildiX-logo.png"
         alt="BuildiX" style="height:200px;width:auto;margin-bottom:18px;">
    <div class="tagline">Smart Construction Estimator</div>
    <div class="badges">
      <span class="badge">პროფესიონალური შეფასება</span>
      <span class="badge">200+ პროექტი</span>
      <span class="badge">24/7 კონსულტაცია</span>
    </div>
  </div>

  <!-- STEP 1 -->
  <div class="card">
    <div class="card-hdr">
      <div class="step-n">1</div>
      <span class="card-title">საკონტაქტო ინფორმაცია</span>
    </div>
    <div class="g2">
      <div>
        <div class="f">
          <label>სახელი, გვარი</label>
          <input id="iName" type="text" placeholder="მაგ: ლაშა ჯაკობია" oninput="chk()">
        </div>
        <div class="f">
          <label>ტელეფონი</label>
          <input id="iPhone" type="tel" placeholder="+995 5XX XXX XXX" oninput="chk()">
          <div class="err-msg" id="ePhone">სწორი ნომერი შეიყვანეთ</div>
        </div>
      </div>
      <div>
        <div class="f">
          <label>Email</label>
          <input id="iEmail" type="email" placeholder="example@email.com" oninput="chk()">
          <div class="err-msg" id="eEmail">სწორი Email ფორმატი</div>
        </div>
        <div class="f">
          <label>მშენებლობის რაიონი</label>
          <select id="iLoc" onchange="chk()">
            <option value="">— აირჩიეთ რაიონი —</option>
            <option>თბილისი</option>
            <option>მცხეთა</option>
            <option>თეთრიწყარო</option>
          </select>
        </div>
      </div>
    </div>
  </div>

  <!-- LOCKED hint -->
  <div class="locked" id="locked">
    <span style="font-size:17px;opacity:.2">🔒</span>
    <span>გთხოვთ, შეავსოთ საკონტაქტო მონაცემები კალკულატორის გასააქტიურებლად.</span>
  </div>

  <!-- STEPS 2 & 3 -->
  <div class="s23" id="s23">

    <!-- STEP 2 -->
    <div class="card">
      <div class="card-hdr">
        <div class="step-n">2</div>
        <span class="card-title">პროექტის პარამეტრები</span>
      </div>
      <div class="g2">
        <div>
          <span class="sec-lbl">ზოგადი</span>
          <div class="f">
            <label>ფართობი (კვ.მ)</label>
            <input id="iArea" type="number" min="1" placeholder="მაგ: 150" oninput="calc()">
          </div>
          <div class="f">
            <label>სართულები</label>
            <select id="iFloors" onchange="calc()">
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
            </select>
          </div>
          <div class="f">
            <label>სახურავი</label>
            <select id="iRoof" onchange="calc()">
              <option value="tin">თუნუქი (Classic)</option>
              <option value="flat">ბრტყელი გადახურვა</option>
            </select>
          </div>
        </div>
        <div>
          <span class="sec-lbl">მასალები</span>
          <div class="f">
            <label>ბეტონის მარკა</label>
            <select id="iConcrete">
              <option>B20 (M250)</option>
              <option>B25 (M350)</option>
            </select>
          </div>
          <div class="f">
            <label>კედლის მასალა</label>
            <select id="iWall" onchange="calc()">
              <option value="pemza">პემზის ბლოკი</option>
              <option value="aguri">აგური</option>
              <option value="gazbloki">გაზბლოკი</option>
            </select>
          </div>
          <div class="f">
            <label>ფანჯარა</label>
            <select id="iWin" onchange="calc()">
              <option value="std">სტანდარტული</option>
              <option value="prem">პრემიუმ ალუმინი</option>
            </select>
          </div>
        </div>
      </div>

      <div class="hint" id="hintArea">
        <span class="dot">↑</span>
        <span>შეიყვანეთ ფართობი კვ.მ-ში სავარაუდო ბიუჯეტის სანახავად.</span>
      </div>

      <div class="result" id="result">
        <div class="r-lbl">სავარაუდო ბიუჯეტი</div>
        <div class="r-amt"><span class="r-cur">$</span><span id="aTotal">0</span></div>
        <div class="bkdn">
          <div class="bi"><div class="bi-lbl">კონსტრუქცია</div><div class="bi-val"><span class="bi-acc"></span><span id="aCC">—</span></div></div>
          <div class="bi"><div class="bi-lbl">გადახურვა</div><div class="bi-val"><span class="bi-acc"></span><span id="aCR">—</span></div></div>
          <div class="bi"><div class="bi-lbl">ფასადი</div><div class="bi-val"><span class="bi-acc"></span><span id="aCF">—</span></div></div>
          <div class="bi"><div class="bi-lbl">კომუნიკაციები</div><div class="bi-val"><span class="bi-acc"></span><span id="aCM">—</span></div></div>
        </div>
        <div class="hint" style="margin-top:16px">
          <span class="dot">ℹ</span>
          <span>შეფასება სავარაუდოა და შეიძლება განსხვავდებოდეს ადგილზე დათვალიერების შემდეგ. ჩვენი სპეციალისტი დაგიკავშირდებათ კონსულტაციისთვის.</span>
        </div>
      </div>
    </div>

    <!-- STEP 3 -->
    <div class="card">
      <div class="card-hdr">
        <div class="step-n">3</div>
        <span class="card-title">ნახაზის ატვირთვა<span class="card-opt">— სურვილისამებრ</span></span>
      </div>
      <div class="file-drop" id="fdrop">
        <input type="file" id="fInput" accept=".png,.jpg,.jpeg,.pdf" onchange="onFile(this)">
        <div class="fd-icon">📎</div>
        <div class="fd-txt">ჩააგდეთ ფაილი ან დააჭირეთ ასატვირთად</div>
        <div class="fd-hint">PNG · JPG · PDF</div>
        <div class="fd-name" id="fdName"></div>
      </div>
    </div>

    <button class="btn" onclick="submit()">მოთხოვნის გაგზავნა &nbsp;→</button>
    <div class="success" id="successBox"></div>

  </div>

  <div class="footer">© 2026 BuildiX Construction · All rights reserved</div>
</div>

<script>
const $ = id => document.getElementById(id);

function fmt(n) { return '$' + Math.round(n).toLocaleString('en-US'); }

function validEmail(e) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e); }
function validPhone(p) {
  const digits = p.replace(/[^\d]/g, '');
  return digits.length >= 9 && /^\+?[\d\s\-()+]+$/.test(p);
}

function chk() {
  const name  = $('iName').value.trim();
  const phone = $('iPhone').value.trim();
  const email = $('iEmail').value.trim();
  const loc   = $('iLoc').value;

  const phoneOk = !phone || validPhone(phone);
  const emailOk = !email || validEmail(email);

  $('ePhone').style.display = (phone && !phoneOk) ? 'block' : 'none';
  $('eEmail').style.display = (email && !emailOk) ? 'block' : 'none';
  $('iPhone').classList.toggle('err', !!(phone && !phoneOk));
  $('iEmail').classList.toggle('err', !!(email && !emailOk));

  const ok = name && validEmail(email) && validPhone(phone) && loc;

  $('locked').style.display = ok ? 'none' : 'flex';
  $('s23').classList.toggle('on', !!ok);
  resize();
}

function calc() {
  const area = parseFloat($('iArea').value);
  const hint = $('hintArea');
  const res  = $('result');

  if (!area || area <= 0) {
    hint.style.display = 'flex';
    res.classList.remove('on');
    resize();
    return;
  }

  hint.style.display = 'none';

  let pc = 280, pr = 85, pf = 120, pm = 60;
  if (parseInt($('iFloors').value) > 1) pc = Math.round(pc * 1.15);
  if ($('iWall').value  === 'aguri')     pc += 45;
  if ($('iRoof').value  === 'flat')      pr  = 145;
  if ($('iWin').value   === 'prem')      pf += 160;

  const cc = area * pc, cr = area * pr, cf = area * pf, cm = area * pm;
  const total = cc + cr + cf + cm;

  $('aTotal').textContent = Math.round(total).toLocaleString('en-US');
  $('aCC').textContent = fmt(cc);
  $('aCR').textContent = fmt(cr);
  $('aCF').textContent = fmt(cf);
  $('aCM').textContent = fmt(cm);
  res.classList.add('on');
  resize();
}

function onFile(inp) {
  if (inp.files && inp.files[0]) {
    $('fdName').textContent = '✓  ' + inp.files[0].name;
    $('fdName').style.display = 'block';
  }
}

const fdrop = $('fdrop');
fdrop.addEventListener('dragover',  e => { e.preventDefault(); fdrop.classList.add('over'); });
fdrop.addEventListener('dragleave', () => fdrop.classList.remove('over'));
fdrop.addEventListener('drop', e => {
  e.preventDefault(); fdrop.classList.remove('over');
  const f = e.dataTransfer.files[0];
  if (f) { $('fdName').textContent = '✓  ' + f.name; $('fdName').style.display = 'block'; }
});

function submit() {
  const name = $('iName').value.trim();
  const box  = $('successBox');
  box.textContent = '✓  მადლობა, ' + name + '! მოთხოვნა მიღებულია. მალე დაგიკავშირდებით.';
  box.classList.add('on');
  box.scrollIntoView({ behavior: 'smooth', block: 'center' });
  resize();
}

// Tell Streamlit how tall this iframe needs to be
function resize() {
  const h = document.body.scrollHeight + 30;
  window.parent.postMessage({ type: 'streamlit:setFrameHeight', height: h }, '*');
}

window.addEventListener('load', () => { chk(); resize(); });
window.addEventListener('resize', resize);
</script>
</body>
</html>"""

components.html(HTML, height=2200, scrolling=False)
