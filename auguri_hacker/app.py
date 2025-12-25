import streamlit as st
import time
import os
import base64
import streamlit.components.v1 as components

# 1. FORZA IL LAYOUT LARGO (Risolve il taglio su Desktop)
st.set_page_config(page_title="BREACHMAS 2025", page_icon="💀", layout="wide")

# --- CSS AGGRESSIVO ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    header, footer, #MainMenu {visibility: hidden;}

    /* LOG INIZIALI: Grandi e nitidi */
    .log-text {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 22px !important; 
        font-weight: bold;
        line-height: 1.6;
        text-shadow: 0 0 5px #00FF41;
        margin-bottom: 10px;
    }

    /* CONTENITORE PER ASCII RESPONSIVO */
    .ascii-container {
        width: 100%;
        max-width: 900px;
        margin: 0 auto;
        border: 1px solid #00FF41;
        padding: 10px;
        background: black;
    }

    /* Matrix Rain */
    .matrix-rain {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: 1;
    }
    .bit {
        position: absolute; top: -30px;
        font-family: monospace; font-size: 20px;
        animation: fall linear infinite;
    }
    @keyframes fall { to { transform: translateY(110vh); } }

    /* Nasconde il player audio ma lo tiene attivo */
    div[data-testid="stAudio"] {
        position: fixed;
        bottom: -100px;
    }
    </style>
    """, unsafe_allow_html=True)

def find_file(name):
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.lower() == name.lower():
                return os.path.join(root, f)
    return None

def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def play_audio_hidden(b64_string):
    if b64_string:
        audio_html = f"""
            <audio autoplay="true" style="display:none;">
                <source src="data:audio/mp3;base64,{b64_string}" type="audio/mp3">
            </audio>
        """
        components.html(audio_html, height=0, width=0)

def start_cyber_rain():
    import random
    cols = 30
    html_bits = '<div class="matrix-rain">'
    for i in range(cols):
        left = i * 3.3
        duration = random.uniform(2, 5)
        delay = random.uniform(0, 3)
        color = "#00FF41" if i % 2 == 0 else "#FF0000"
        char = random.choice(["0", "1", "X", "M", "A", "S"])
        html_bits += f'<div class="bit" style="left:{left}%; color:{color}; animation-duration:{duration}s; animation-delay:{delay}s;">{char}</div>'
    html_bits += '</div>'
    st.markdown(html_bits, unsafe_allow_html=True)

def main():
    if 'authorized' not in st.session_state:
        st.session_state.authorized = False

    if not st.session_state.authorized:
        st.markdown('<div class="log-text">ID: CACTUS_SERVER<br>STATUS: ENCRYPTED</div>', unsafe_allow_html=True)
        if st.button("RUN EXPLOIT"):
            st.session_state.authorized = True
            st.rerun()
    else:
        # 1. Modem Audio (26s)
        modem_b64 = get_audio_b64(find_file("modem.mp3"))
        play_audio_hidden(modem_b64)

        log_placeholder = st.empty()
        full_log = ""
        
        steps = [
            ("> Dialing 01010011...", 2.5),
            ("> Carrier detected...", 1.5),
            ("> Handshake: V.90...", 6.0),
            ("> Bypassing IDS/IPS...", 4.5),
            ("> Escalating to root...", 4.0),
            ("> Accessing payload...", 3.0),
            ("> Decrypting buffer...", 2.5),
        ]

        for text, delay in steps:
            full_log += text + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
            time.sleep(delay)

        # Buffer per musica rock
        full_log += "> Executing Payload.bin...<br>"
        log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
        rock_b64 = get_audio_b64(find_file("musica.mp3"))
        time.sleep(2.0) 

        # --- FASE FINALE ---
        play_audio_hidden(rock_b64)
        start_cyber_rain()

        # ASCII ART IN SVG (Garantisce che non si rompa MAI)
        # Ho ridotto leggermente gli spazi tra le lettere per farla stare ovunque
        ascii_svg = r"""
        <svg viewBox="0 0 600 180" xmlns="http://www.w3.org/2000/svg">
            <style> .t { font: bold 12px monospace; fill: #00FF41; } </style>
            <text x="50%" y="20" class="t" text-anchor="middle"> █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ██╗</text>
            <text x="50%" y="35" class="t" text-anchor="middle">██╔══██╗██║   ██║██╔════╝ ██║   ██║██╔══██╗██║</text>
            <text x="50%" y="50" class="t" text-anchor="middle">███████║██║   ██║██║  ███╗██║   ██║██████╔╝██║</text>
            <text x="50%" y="65" class="t" text-anchor="middle">██╔══██║██║   ██║██║   ██║██║   ██║██╔══██╗██║</text>
            <text x="50%" y="80" class="t" text-anchor="middle">██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║</text>
            <text x="50%" y="95" class="t" text-anchor="middle">╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝</text>
            <text x="50%" y="120" class="t" text-anchor="middle">██╗    ██████╗  ██████╗ █████╗ ███╗  ██╗██████╗ ██╗███████╗██████╗ ██╗</text>
            <text x="50%" y="135" class="t" text-anchor="middle">██║    ██╔═══██╗██╔════╝██╔══██╗████╗ ██║██╔══██╗██║██╔════╝██╔══██╗██║</text>
            <text x="50%" y="150" class="t" text-anchor="middle">██║    ██║   ██║██║     ███████║██╔██╗██║██║  ██║██║█████╗  ██████╔╝██║</text>
            <text x="50%" y="165" class="t" text-anchor="middle">██████╗╚██████╔╝╚██████╗██║  ██║██║ ╚████║██████╔╝██║███████╗██║  ██║██║</text>
            <text x="50%" y="180" class="t" text-anchor="middle">╚═════╝ ╚═════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝</text>
        </svg>
        """
        st.markdown(f'<div class="ascii-container">{ascii_svg}</div>', unsafe_allow_html=True)
        
        st.success("SUCCESS: Buon Natale, Locandieri!")

        img_path = find_file("foto.png")
        if img_path:
            st.image(img_path, use_container_width=True)
        
        st.markdown('<div class="log-text">root@cactus_server:~# _</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
