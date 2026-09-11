import streamlit as st
import os
import base64

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Album Kenangan", page_icon="🌸", layout="wide")

# 2. Fungsi Encode Gambar Lokal ke Base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Ambil string base64 dari background
bg_image_path = "background/bg.jpeg"
bg_base64 = get_base64_image(bg_image_path)

# 3. Inisialisasi State Halaman
if 'page' not in st.session_state:
    st.session_state.page = 1

def go_to_album():
    st.session_state.page = 2

def go_to_home():
    st.session_state.page = 1

# 4. CSS Custom dengan Background Base64 & Efek RGB pada Judul
custom_css = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Poppins:wght@400;600;700&display=swap');

/* Set Background Gambar */
.stApp {{
    background-image: url("data:image/jpeg;base64,{bg_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Overlay Transparan */
[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0) !important;
}}

/* --- STYLING HALAMAN 1 (WELCOME PAGE) --- */
.welcome-container {{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 55vh;
    text-align: center;
}}

/* Keyframes untuk Animasi Floating (Naik-Turun) */
@keyframes float {{
    0% {{ transform: translateY(0px); }}
    50% {{ transform: translateY(-12px); }}
    100% {{ transform: translateY(0px); }}
}}

/* Keyframes untuk Animasi Warna RGB Bergerak */
@keyframes rgb-shift {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}

.animated-title {{
    font-family: 'Caveat', cursive;
    font-size: 68px;
    font-weight: 800;
    
    /* Gradasi Warna RGB Gradien */
    background: linear-gradient(270deg, #ff0055, #7a00ff, #00e5ff, #ff0055);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    
    /* Gabungan Animasi Naik-Turun & Warna Bergerak */
    animation: float 3.5s ease-in-out infinite, rgb-shift 6s ease infinite;
    
    /* Shadow Gelap Tebal agar Teks Sangat Kontras & Jelas Dibaca */
    filter: drop-shadow(3px 3px 5px rgba(0, 0, 0, 0.7));
    margin-bottom: 10px;
}}

.animated-subtitle {{
    font-family: 'Poppins', sans-serif;
    font-size: 20px;
    color: #ffffff;
    font-weight: 600;
    background: rgba(0, 0, 0, 0.4);
    padding: 10px 24px;
    border-radius: 20px;
    backdrop-filter: blur(8px);
    display: inline-block;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

/* Styling Tombol Masuk Custom */
div.stButton > button {{
    background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%) !important;
    color: #4a2e35 !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
    font-size: 18px !important;
    border-radius: 30px !important;
    padding: 12px 35px !important;
    border: 2px solid #ffffff !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
    transition: all 0.3s ease !important;
    display: block;
    margin: 0 auto;
}}

div.stButton > button:hover {{
    transform: scale(1.08) !important;
    box-shadow: 0 6px 20px rgba(166, 193, 238, 0.6) !important;
}}

/* --- STYLING HALAMAN 2 (GALERI ALBUM) --- */

/* Styling Warna Judul & Subheader Halaman 2 Biar Jelas Dibaca */
h1, h3, [data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h3 {{
    color: #4a2e35 !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700 !important;
    text-shadow: 1px 1px 3px rgba(255, 255, 255, 0.9);
}}

/* Efek Hover Zoom & Shadow pada Gambar */
[data-testid="stImage"] img {{
    border-radius: 15px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 3px solid #ffffff;
    box-shadow: 0 8px 15px rgba(0,0,0,0.1);
}}

[data-testid="stImage"] img:hover {{
    transform: scale(1.04);
    box-shadow: 0 12px 25px rgba(166, 193, 238, 0.5);
}}

/* Styling Caption / Deskripsi Foto */
[data-testid="stCaptionContainer"] {{
    color: #332227 !important;
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(6px);
    padding: 10px;
    border-radius: 10px;
    font-size: 0.95rem !important;
    text-align: center;
    margin-top: 8px;
}}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# HALAMAN 1: LANDING / WELCOME SLIDE
# ---------------------------------------------------------
if st.session_state.page == 1:
    st.markdown("""
        <div class="welcome-container">
            <h1 class="animated-title">✨ Welcome to Album Kenangan ✨</h1>
            <p class="animated-subtitle">Simpan & kenang setiap detik momen berharga bersama.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("🚀 Klik untuk Masuk", on_click=go_to_album, use_container_width=True)

# ---------------------------------------------------------
# HALAMAN 2: ALBUM KENANGAN & MUSIK
# ---------------------------------------------------------
elif st.session_state.page == 2:
    col_title, col_btn = st.columns([5, 1])
    with col_title:
        st.title("📖 Galeri Album Kenangan")
    with col_btn:
        st.button("⬅️ Kembali", on_click=go_to_home)

    # 1. Pemutar Musik MP3 Lokal (Hidden + Autoplay)
    audio_path = "music/lagu.mp3"  # <-- Ganti nama_file_kamu.mp3 sesuai nama file kamu
    
    if os.path.exists(audio_path):
        audio_base64 = get_base64_image(audio_path) # Pakai fungsi base64 yang sudah ada
        st.markdown(f"""
            <audio autoplay loop style="display:none;">
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
        """, unsafe_allow_html=True)

    st.divider()

    # 2. Galeri Foto & Deskripsi
    st.subheader("📸 Koleksi Momen")

    photo_data = [
        {
            "file": "foto1.jpeg",
            "title": "Momen #1",
            "desc": "Foto kebersamaan waktu mpls."
        },
        {
            "file": "foto2.jpeg",
            "title": "Momen #2",
            "desc": "Foto bareng setelah pemilihan ketua osis."
        },
        {
            "file": "foto3.jpeg",
            "title": "Momen #3",
            "desc": "memperingati hari guru."
        },
        {
            "file": "foto4.jpeg",
            "title": "Momen #4",
            "desc": "foto bersama teman-teman ketika menjadi petugas upacara."
        },
        {
            "file": "foto5.jpeg",
            "title": "Momen #5",
            "desc": "foto memeriahkan perayaan kemerdekaan."
        },
    ]

    photo_dir = "photo"
    if os.path.exists(photo_dir):
        for i in range(0, len(photo_data), 3):
            cols = st.columns(3)
            batch = photo_data[i:i+3]
            
            for j, item in enumerate(batch):
                photo_path = os.path.join(photo_dir, item["file"])
                if os.path.exists(photo_path):
                    with cols[j]:
                        st.image(photo_path, use_container_width=True)
                        st.caption(f"**{item['title']}**\n\n{item['desc']}")
    else:
        st.warning("Folder 'photo/' tidak ditemukan.")