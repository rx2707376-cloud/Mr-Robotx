# -*- coding: utf-8 -*-
"""
🤖 Mr Robot X — Interactive Demo Website
Versi: 2.0 | Mode Simulasi Interaktif
"""

import streamlit as st
import time
import pandas as pd
from datetime import datetime

# ============= 1. KONFIGURASI HALAMAN =============
st.set_page_config(
    page_title="Mr Robot X // LIVE DEMO",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Warna tema terminal
DARK_BG = "#0c0c0c"
GREEN_TERM = "#33ff33"

# ============= 2. TAMPILAN CSS KUSTOM =============
st.markdown(f"""
<style>
    .main {{ background-color: {DARK_BG}; color: {GREEN_TERM}; }}
    h1, h2, h3, h4 {{ color: {GREEN_TERM}; font-family: 'Courier New', monospace; }}
    .stButton>button {{ background: #1a1a1a; color: {GREEN_TERM}; border: 1px solid {GREEN_TERM}; width: 100%; }}
    .stTextInput>div>div>input {{ background: #1a1a1a; color: {GREEN_TERM}; font-family: 'Courier New', monospace; }}
    .terminal {{
        background-color: #000;
        border: 1px solid #33ff33;
        border-radius: 6px;
        padding: 15px;
        font-family: 'Courier New', monospace;
        color: {GREEN_TERM};
        font-size: 14px;
        line-height: 1.6;
        margin-bottom: 10px;
    }}
    .glitch {{
        animation: glitch 1s infinite;
        text-shadow: 0 0 10px #33ff33;
    }}
    @keyframes glitch {{
        0% {{ transform: translate(0) skew(0deg); }}
        20% {{ transform: translate(-1px, 1px) skew(-0.5deg); }}
        40% {{ transform: translate(-1px, -1px) skew(0.5deg); }}
        60% {{ transform: translate(1px, 1px) skew(0deg); }}
        100% {{ transform: translate(0) skew(0deg); }}
    }}
</style>
""", unsafe_allow_html=True)

# ============= 3. INISIALISASI SESSION STATE =============
if 'terminal_logs' not in st.session_state:
    st.session_state.terminal_logs = [
        "╔══════════════════════════════════════════════════════════╗",
        "║  MR ROBOT X SYSTEM v2.0.0 — ONLINE ENVIRONMENT           ║",
        "║  STATUS: CORE INITIALIZED SUCCESSFULLY                   ║",
        f"║  TIME SYSTEM: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                         ║",
        "╚══════════════════════════════════════════════════════════╝",
        "Ketik 'help' untuk melihat daftar perintah simulasi yang tersedia."
    ]

# ============= 4. PANEL KONTROL (SIDEBAR) =============
with st.sidebar:
    st.markdown("### 🛠️ PANEL KONTROL")
    st.markdown("Gunakan panel ini untuk memanipulasi data simulasi secara real-time.")
    
    # Input interaktif
    jumlah_node = st.slider("Jumlah Node Aktif", min_value=5, max_value=100, value=42)
    status_jaringan = st.selectbox("Status Enkripsi", ["SECURE (SIMULASI)", "BYPASS MODE", "MAINTENANCE"])
    
    st.divider()
    st.caption("Aplikasi ini berjalan sepenuhnya di cloud server sebagai media demonstrasi visual.")

# ============= 5. HALAMAN UTAMA =============
st.markdown("""
<h1 style='text-align: center;' class='glitch'>🤖 MR ROBOT X</h1>
<h4 style='text-align: center; color: #666;'>LIVE ONLINE DEMO — INTERACTIVE SIMULATION</h4>
<hr style='border-color: #333;'>
""", unsafe_allow_html=True)

# Komponen Terminal Interaktif
st.subheader("📟 Terminal Sistem")

# Tampilkan riwayat log terminal
log_text = "<br>".join(st.session_state.terminal_logs)
st.markdown(f"<div class='terminal'>{log_text}</div>", unsafe_allow_html=True)

# Form input untuk mengetikkan perintah perintah terminal
with st.form(key='cmd_form', clear_on_submit=True):
    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_cmd = st.text_input("user@mrrobotx:~$", placeholder="Ketik sesuatu di sini (contoh: help, status, diag)...")
    with col_btn:
        submit_btn = st.form_submit_submit = st.form_submit_button(label="Kirim")

# Logika respon terminal dari input pengguna
if submit_btn and user_cmd:
    cmd_clean = user_cmd.strip().lower()
    st.session_state.terminal_logs.append(f"<span style='color:#888;'>user@mrrobotx:~$</span> <span style='color:#fff;'>{user_cmd}</span>")
    
    if cmd_clean == 'help':
        st.session_state.terminal_logs.extend([
            "Perintah yang tersedia:",
            " - <b>status</b> : Memeriksa kondisi ringkasan server saat ini.",
            " - <b>diag</b>   : Menjalankan simulasi diagnosis pada modul.",
            " - <b>clear</b>  : Membersihkan riwayat layar terminal."
        ])
    elif cmd_clean == 'status':
        st.session_state.terminal_logs.extend([
            f"💻 Jaringan: {status_jaringan}",
            f"📡 Total Node Terdeteksi: {jumlah_node} unit",
            "🛡️ Firewall Level: MAXIMUM (Virtual Mock)"
        ])
    elif cmd_clean == 'diag':
        st.session_state.terminal_logs.extend([
            "⚙️ Memulai pemindaian sektor virtual...",
            "✅ Modul Database: OKE",
            "✅ Modul Enkripsi: BERJALAN",
            "⚠️ Koneksi Eksternal: DISOLASI (Mode Demo Aman)"
        ])
    elif cmd_clean == 'clear':
        st.session_state.terminal_logs = ["Terminal dibersihkan. Ketik 'help' untuk panduan."]
    else:
        st.session_state.terminal_logs.append(f"❌ Perintah '{user_cmd}' tidak dikenal. Ketik 'help' untuk bantuan.")
    
    st.rerun()

# Navigasi Tab Data & Informasi
st.divider()
tab1, tab2, tab3 = st.tabs(["📊 Data Node", "🔐 Modul Jaringan", "ℹ️ Tentang Aplikasi"])

with tab1:
    st.markdown("### 📊 Monitoring Sektor Node")
    st.markdown(f"Menampilkan sampel data otomatis berdasarkan preferensi pengaturan **{jumlah_node}** node aktif di sidebar.")
    
    # Generate data dinamis berdasarkan input slider sidebar
    data_nodes = []
    for i in range(1, 6):
        data_nodes.append({
            "ID Sektor": f"NODE-00{i}",
            "Kapasitas Alokasi": jumlah_node * i * 3,
            "Respon Ping": f"{10 + i}ms",
            "Integritas Data": "100% Secure" if idx := i != 4 else "92% Perlu Cek"
        })
    
    df = pd.DataFrame(data_nodes)
    st.dataframe(df, use_container_width=True, hide_index=True)

with tab2:
    st.markdown("### 🔐 Status Enkripsi Modul Jaringan")
    col_a, col_b = st.columns(2)
    with col_a:
        st.success(f"Status Proteksi Utama: {status_jaringan}")
        st.metric("Alokasi Enkripsi", "AES-256 Mocked")
    with col_b:
        st.info("Sistem saat ini tidak melemparkan data ke API luar, menjaga data simulasi tetap terisolasi di dalam memori web.")

with tab3:
    st.markdown("""
    ### ℹ️ Mengenai Sistem Demo
    Web ini dibuat menggunakan framework **Streamlit** untuk kebutuhan simulasi UI bertema antarmuka keamanan siber.
    Semua parameter di dalamnya murni bersifat kosmetik/contoh interaksi komponen.
    """)

# Footer Aplikasi
st.divider()
st.markdown("""
<div style='text-align:center; color:#444; font-size:12px;'>
🤖 Mr Robot X — LIVE DEMO VERSION<br>
Dibuat menggunakan Framework Python Streamlit
</div>
""", unsafe_allow_html=True)
