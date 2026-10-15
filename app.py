import streamlit as st

st.set_page_config(page_title="BRODIX HARAYA - ICC $5K", page_icon="🔮", layout="wide")

# ===== MAGANDANG DESIGN WITH BACKGROUND =====
st.markdown("""
<style>
/* BACKGROUND GRADIENT */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    background-attachment: fixed;
}
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at 20% 30%, rgba(255,45,149,0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 70%, rgba(123,45,255,0.15) 0%, transparent 50%),
                radial-gradient(circle at 40% 80%, rgba(45,255,201,0.1) 0%, transparent 50%);
    pointer-events: none;
    z-index: -1;
}

/* TITLE */
.big-title {
    font-size: 52px; font-weight: 900;
    background: linear-gradient(90deg, #FF2D95, #FF8A2D, #2DFFC9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-align: center; letter-spacing: 2px;
    text-shadow: 0 0 30px rgba(255,45,149,0.5);
}
.sub {
    text-align: center; color: #ccc; font-size: 14px; margin-bottom: 20px;
}

/* CARDS */
.metric-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 20px; border-radius: 20px; text-align: center;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    transition: transform 0.3s;
}
.metric-card:hover { transform: translateY(-5px); }
.metric-number {
    font-size: 36px; font-weight: 900; color: #FF2D95;
}
.metric-label { font-size: 12px; color: #aaa; text-transform: uppercase; letter-spacing: 1px; }
.metric-sub { font-size: 11px; color: #2DFFC9; background: rgba(45,255,201,0.15); padding: 4px 8px; border-radius: 10px; display: inline-block; margin-top: 8px; }

/* TABS */
.stTabs [data-baseweb="tab-list"] { background: rgba(255,255,255,0.05); border-radius: 15px; padding: 5px; }
.stTabs [data-baseweb="tab"] { color: #ccc; }
.stTabs [aria-selected="true"] { background: linear-gradient(90deg, #FF2D95, #7B2DFF) !important; color: white !important; border-radius: 10px; }

/* INPUTS */
.stTextInput>div>div>input, .stTextArea>div>div>textarea {
    background: rgba(255,255,255,0.08) !important; color: white !important;
    border: 1px solid rgba(255,255,255,0.2) !important; border-radius: 12px !important;
}
.stSlider>div>div>div { background: linear-gradient(90deg, #FF2D95, #FF8A2D) !important; }

/* BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #FF2D95, #FF2D2D) !important;
    color: white !important; border: none !important;
    border-radius: 12px !important; font-weight: 700 !important;
    padding: 12px 24px !important; box-shadow: 0 4px 15px rgba(255,45,149,0.4);
}
.stButton>button:hover { transform: scale(1.05); box-shadow: 0 6px 20px rgba(255,45,149,0.6); }

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown('<div class="big-title">BRODIX HARAYA 🔮</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">The Invisible Scoreboard | ICC x Ignyte $5K | Dubai AI Festival<br>Measures what patriarchy tried to erase</div>', unsafe_allow_html=True)

# SESSION
if 'bloodline_count' not in st.session_state:
    st.session_state.bloodline_count = 1247
if 'permission_slips' not in st.session_state:
    st.session_state.permission_slips = 892
if 'cycle_sync' not in st.session_state:
    st.session_state.cycle_sync = 63

# METRICS WITH BACKGROUND CARDS
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="metric-card"><div class="metric-label">🩸 Bloodline Wall</div><div class="metric-number">{st.session_state.bloodline_count}+</div><div class="metric-sub">Women never got to play</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-card"><div class="metric-label">💌 Permission Slips</div><div class="metric-number">{st.session_state.permission_slips}</div><div class="metric-sub">Girls allowed to dream</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="metric-card"><div class="metric-label">🌙 Cycle Sync</div><div class="metric-number">{st.session_state.cycle_sync}%</div><div class="metric-sub">Resilience linked</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# TABS
tab1, tab2, tab3, tab4 = st.tabs(["🔮 BLOODLINE", "💌 PERMISSION", "🌙 CYCLE SYNC", "📊 INVISIBLE SCOREBOARD"])

with tab1:
    st.markdown("### 🔮 Lola What-If - Bloodline Wall")
    st.write("Upload Lola/Nanay na pinagbawalang maglaro. AI creates 'What If She Played?'")
    c_a, c_b = st.columns(2)
    with c_a:
        lola_name = st.text_input("Pangalan ni Lola", "Lola Nena")
        year = st.slider("Year pinagbawalan", 1960, 2010, 1975)
        sport = st.selectbox("Sport sana?", ["Cricket", "Football", "Basketball", "Volleyball"])
    with c_b:
        dream = st.text_area("Pangarap nya dati?", "Gusto maging batter - 340 runs sana", height=100)
        st.file_uploader("Photo (optional)", type=['jpg','png'])
    
    if st.button("🔮 GENERATE HARAYA STORY", key="bloodline"):
        st.session_state.bloodline_count += 1
        st.balloons()
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(255,45,149,0.2), rgba(123,45,255,0.2)); padding: 20px; border-radius: 15px; border: 1px solid #FF2D95; color: white;">
        <h3>✨ HARAYA STORY: {lola_name.upper()}</h3>
        <b>Year {year}:</b> Si {lola_name} pinagbawalang mag-{sport.lower()}.<br>
        <i>"Babae ka, hindi pwede."</i><br><br>
        <b>What If She Played?</b><br>
        Kung pinayagan sya, {340+year%100} runs sana. Opening batter ng PH.<br>
        Pero hindi nangyari. Kaya apo nya maglalaro para sa kanya.<br><br>
        <b>Dream:</b> {dream}<br>
        <b>Invisible Score: +1 girl who will NOT be erased again.</b>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 💌 Permission Slip")
    st.write("Watch women's match = 1 Permission Slip. Gift to a girl.")
    girl = st.text_input("Batang babae", "Mika, 9yo - Talisay Elementary", key="girl")
    msg = st.text_area("Permission Message", "Pinapayagan kitang mangarap maging cricketer. Hindi ka na magde-delete ng pangarap. - Haraya Guardian", key="msg")
    if st.button("💌 SEND PERMISSION SLIP", key="perm"):
        st.session_state.permission_slips += 1
        st.success(f"Sent to {girl}! Slip #{st.session_state.permission_slips}")
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.95); color: #333; padding: 25px; border-radius: 15px; border: 3px dashed #FF2D95; text-align: center;">
        <h3 style="color: #FF2D95;">💌 PERMISSION SLIP #{st.session_state.permission_slips}</h3>
        <b>To:</b> {girl}<br><br>
        <i>"{msg}"</i><br><br>
        <b>From:</b> Haraya Guardian (You)<br>
        <b>Valid:</b> Forever - Hindi na mabubura<br>
        <b>Powered by:</b> ICC Women's Cricket x BRODIX HARAYA
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### 🌙 Cycle Sync - First in Sports!")
    st.write("Female fan + Female athlete = shared resilience")
    mood = st.select_slider("Kumusta ka today?", ["Pagod na pagod", "Laban lang", "Lakas pa", "Palaban", "HARAYA MODE 🔥"], key="mood")
    period = st.selectbox("Cycle status (anonymous)", ["Prefer not to say", "Menstruation", "Follicular - Energy up", "Luteal - Pagod", "Ovulation - Lakas"], key="per")
    watch = st.checkbox("Nanonood ng ICC Women's match kahit pagod / may period", key="watch")
    support = st.text_area("Message sa athlete", "Kahit pagod ka, lumalaban ka. Kahit pagod ako, nanonood ako. Hindi tayo nag-iisa.", key="sup")
    if st.button("🌙 SEND RESILIENCE PACK", key="cycle"):
        st.session_state.cycle_sync = min(100, st.session_state.cycle_sync+1)
        st.snow()
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(45,255,201,0.15), rgba(45,156,255,0.15)); padding: 20px; border-radius: 15px; border: 1px solid #2DFFC9; color: white;">
        ✅ <b>RESILIENCE PACK SENT TO ATHLETE IN DUGOUT!</b><br><br>
        <b>Anonymous fan from Talisay:</b><br>
        Mood={mood}, Cycle={period}, Still watching={watch}<br><br>
        <i>"{support}"</i><br><br>
        <b>Performance boost:</b> +2% mental resilience - collective strength of women who bleed and still fight.
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("### 📊 The Invisible Scoreboard - AR Stadium")
    st.markdown("""
    <div style="background: rgba(0,0,0,0.4); padding: 20px; border-radius: 15px; color: white;">
    <b>Today's Visible:</b> 142/6 (ICC Women's T20)<br>
    <b>Today's INVISIBLE (mas importante):</b><br>
    • 👩‍👧 <b>1,203 mothers</b> allowed daughters to play after watching<br>
    • 👨 <b>847 fathers</b> clapped for woman athlete first time<br>
    • 👧 <b>2,341 girls</b> did NOT delete dream today<br>
    • 💌 <b>892 Permission Slips</b> sent in Talisay, Cebu<br>
    • 🌙 <b>63% Cycle Sync</b> - fans bleeding but still supporting<br><br>
    <b>Real Winner:</b> Not team with most runs. Real winner is barangay with most girls who stayed.
    </div>
    """, unsafe_allow_html=True)
    score = int(st.session_state.bloodline_count*0.47 + st.session_state.permission_slips*0.22 + st.session_state.cycle_sync*0.31) % 100
    if score < 50: score += 42
    st.markdown("<br>", unsafe_allow_html=True)
    col_m1, col_m2 = st.columns([1,2])
    col_m1.metric("HARAYA SCORE", f"{score}/100", "+12 today")
    col_m2.progress(score)

st.markdown("---")
st.caption("🔮 Built by brodix0028-netizen | Talisay PH | ICC Global Hackathon $5K | Sister: brodix-fan-compass-laliga $10K | Dubai AI Festival Oct 2026")
