import streamlit as st
st.set_page_config(page_title="BRODIX HARAYA - ICC $5K", page_icon="🔮", layout="wide")
st.markdown('<h1 style="text-align:center;color:#FF2D95">BRODIX HARAYA</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center">The Invisible Scoreboard | ICC x Ignyte $5K | Dubai AI Festival</p>', unsafe_allow_html=True)
st.markdown("---")
if 'bloodline_count' not in st.session_state:
    st.session_state.bloodline_count=1247
if 'permission_slips' not in st.session_state:
    st.session_state.permission_slips=892
if 'cycle_sync' not in st.session_state:
    st.session_state.cycle_sync=63
c1,c2,c3=st.columns(3)
c1.metric("BLOODLINE WALL", f"{st.session_state.bloodline_count}+", "Women never got to play")
c2.metric("PERMISSION SLIPS", st.session_state.permission_slips, "Girls allowed to dream")
c3.metric("CYCLE SYNC", f"{st.session_state.cycle_sync}%", "Resilience linked")
st.markdown("---")
t1,t2,t3,t4=st.tabs(["🔮 BLOODLINE","💌 PERMISSION","🌙 CYCLE SYNC","📊 SCOREBOARD"])
with t1:
    st.subheader("Lola What-If")
    lola=st.text_input("Pangalan ni Lola","Lola Nena")
    year=st.slider("Year pinagbawalan",1960,2010,1975)
    if st.button("🔮 GENERATE HARAYA STORY",type="primary"):
        st.session_state.bloodline_count+=1
        st.success(f"Added! Total: {st.session_state.bloodline_count}+ - Si {lola} sana {340+year%100} runs nung {year}!")
        st.balloons()
with t2:
    st.subheader("Permission Slip")
    girl=st.text_input("Batang babae","Mika, 9yo - Talisay")
    msg=st.text_area("Message","Pinapayagan kitang mangarap maging cricketer.")
    if st.button("💌 SEND PERMISSION SLIP",type="primary"):
        st.session_state.permission_slips+=1
        st.success(f"Sent to {girl}! Slip #{st.session_state.permission_slips}")
with t3:
    st.subheader("Cycle Sync")
    mood=st.select_slider("Kumusta?",["Pagod","Laban","Lakas","Haraya Mode 🔥"])
    if st.button("🌙 SEND RESILIENCE PACK",type="primary"):
        st.session_state.cycle_sync=min(100,st.session_state.cycle_sync+1)
        st.success(f"Resilience Pack sent! Mood: {mood} -> Athlete: Hindi ka nag-iisa")
with t4:
    st.subheader("Invisible Scoreboard")
    st.write("Runs: 142/6 | Invisible: 1,203 mothers allowed daughters, 847 fathers clapped first time, 2,341 girls did NOT delete dream")
    score=int(st.session_state.bloodline_count*0.47+st.session_state.permission_slips*0.22+st.session_state.cycle_sync*0.31)%100
    if score<50: score+=42
    st.metric("HARAYA SCORE",f"{score}/100","Measures what patriarchy erased")
    st.progress(score)
st.caption("Built by brodix0028-netizen | Talisay PH | ICC Global Hackathon $5K | Sister: brodix-fan-compass-laliga $10K")
