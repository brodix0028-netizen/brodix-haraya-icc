import streamlit as st
st.set_page_config(page_title="BRODIX HARAYA", page_icon="🔮", layout="wide")
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #FF2D95, #24243e);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.big-title {
    font-size: 60px; font-weight: 900;
    background: linear-gradient(90deg, #FF2D95, #FFD700, #2DFFC9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-align: center; filter: drop-shadow(0 0 20px #FF2D95);
    animation: glow 2s ease-in-out infinite alternate;
}
@keyframes glow { from { filter: drop-shadow(0 0 10px #FF2D95); } to { filter: drop-shadow(0 0 30px #FF2D95); } }
.metric-card {
    background: rgba(255,255,255,0.1); backdrop-filter: blur(15px);
    border: 2px solid rgba(255,45,149,0.3); padding: 25px; border-radius: 25px;
    text-align: center; box-shadow: 0 0 30px rgba(255,45,149,0.2);
}
.metric-number { font-size: 42px; font-weight: 900; color: #FFD700; text-shadow: 0 0 10px #FFD700; }
.stButton>button {
    background: linear-gradient(90deg, #FF2D95, #FFD700) !important;
    color: black !important; font-weight: 900 !important;
    border-radius: 15px !important; font-size: 16px !important;
    box-shadow: 0 0 20px #FF2D95; animation: pulse 2s infinite;
}
@keyframes pulse { 0% {transform: scale(1);} 50% {transform: scale(1.05);} 100% {transform: scale(1);} }
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="big-title">BRODIX HARAYA 🔮</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:white;">✨ THE INVISIBLE SCOREBOARD ✨<br>ICC x Ignyte $5K | Dubai AI Festival | PINAKA ANGKAS EDITION</p>', unsafe_allow_html=True)
if 'bloodline_count' not in st.session_state:
    st.session_state.bloodline_count=1247
if 'permission_slips' not in st.session_state:
    st.session_state.permission_slips=892
if 'cycle_sync' not in st.session_state:
    st.session_state.cycle_sync=63
c1,c2,c3=st.columns(3)
c1.markdown(f'<div class="metric-card"><div style="color:#aaa;font-size:12px">🩸 BLOODLINE WALL</div><div class="metric-number">{st.session_state.bloodline_count}+</div><div style="color:#2DFFC9;font-size:11px">Women never got to play</div></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="metric-card"><div style="color:#aaa;font-size:12px">💌 PERMISSION SLIPS</div><div class="metric-number">{st.session_state.permission_slips}</div><div style="color:#2DFFC9;font-size:11px">Girls allowed to dream</div></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="metric-card"><div style="color:#aaa;font-size:12px">🌙 CYCLE SYNC</div><div class="metric-number">{st.session_state.cycle_sync}%</div><div style="color:#2DFFC9;font-size:11px">Resilience linked</div></div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
t1,t2,t3,t4=st.tabs(["🔮 BLOODLINE","💌 PERMISSION","🌙 CYCLE SYNC","📊 SCOREBOARD"])
with t1:
    lola=st.text_input("Pangalan ni Lola","Lola Nena")
    year=st.slider("Year pinagbawalan",1960,2010,1975)
    if st.button("🔮 GENERATE HARAYA STORY - ANGKAS MODE"):
        st.session_state.bloodline_count+=1
        st.balloons()
        st.success(f"🔥 BOOM! {lola} ADDED! Total: {st.session_state.bloodline_count}+ - PINAKA ANGKAS!")
with t2:
    girl=st.text_input("Batang babae","Mika, 9yo - Talisay")
    if st.button("💌 SEND PERMISSION SLIP - ANGKAS"):
        st.session_state.permission_slips+=1
        st.success(f"🔥 ANGKAS SLIP SENT TO {girl}!")
with t3:
    mood=st.select_slider("Kumusta?","Pagod,Laban,Lakas,Haraya Mode 🔥".split(","))
    if st.button("🌙 SEND RESILIENCE - ANGKAS"):
        st.session_state.cycle_sync=min(100,st.session_state.cycle_sync+1)
        st.snow()
        st.success(f"🔥 ANGKAS RESILIENCE SENT! Mood: {mood}")
with t4:
    st.markdown(f'<div class="metric-card"><h3>📊 INVISIBLE SCOREBOARD</h3>Runs: 142/6<br>INVISIBLE: 1,203 mothers allowed daughters, 847 fathers clapped, 2,341 girls did NOT delete dream<br><br><h2 style="color:#FFD700">HARAYA SCORE: {st.session_state.bloodline_count%100+42}/100 🔥 PINAKA ANGKAS!</h2></div>', unsafe_allow_html=True)
st.caption("🔥 PINAKA ANGKAS EDITION | Built by brodix0028-netizen | Talisay PH | ICC $5K | Dubai AI Festival")
    
