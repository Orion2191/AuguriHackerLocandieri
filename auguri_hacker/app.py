import streamlit as st
import time
import os
import base64
import streamlit.components.v1 as components

# Configurazione Pagina
st.set_page_config(page_title="BREACH_2025", page_icon="💀", layout="centered")

# --- CSS DEFINITIVO: LOOK TERMINALE E AUTO-SCALING ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; overflow-x: hidden; }
    header, footer, #MainMenu {visibility: hidden;}

    .log-text {
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
        line-height: 1.8;
        position: relative;
        z-index: 100;
    }

    /* BOX ASCII: Stesso stile ma RESPONSIVO */
    .terminal-box {
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace !important;
        white-space: pre !important;
        border: 1px solid #00FF41;
        padding: 15px;
        background: rgba(0,0,0,0.9);
        position: relative;
        z-index: 100;
        
        /* Font dinamico che si stringe su mobile senza rompersi */
        font-size: 1.1vw !important; 
        line-height: 1.1 !important;
        letter-spacing: -0.02em;
        width: 100%;
        text-align: center;
        display: inline-block;
    }

    /* Aggiustamento specifico per smartphone */
    @media screen and (max-width: 600px) {
        .terminal-box {
            font-size: 1.3vw !important; /* Leggermente più grande per distinguere i tratti */
            padding: 8px;
            letter-spacing: -0.05em;
        }
        .log-text { font-size: 13px; }
    }

    /* Matrix Rain Natalizia */
    .matrix-rain {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: 1;
    }
    .bit {
        position: absolute; top: -30px;
        font-family: monospace; font-size: 18px;
        animation: fall linear infinite;
    }
    @keyframes fall { to { transform: translateY(110vh); } }
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
    cols = 40
    html_bits = '<div class="matrix-rain">'
    for i in range(cols):
        left = i * 2.5
        duration = random.uniform(2, 6)
        delay = random.uniform(0, 4)
        color = "#00FF41" if i % 2 == 0 else "#FF0000"
        char = random.choice(["0", "1", "X", "M", "A", "S"])
        html_bits += f'<div class="bit" style="left:{left}%; color:{color}; animation-duration:{duration}s; animation-delay:{delay}s;">{char}</div>'
    html_bits += '</div>'
    st.markdown(html_bits, unsafe_allow_html=True)

def main():
    if 'authorized' not in st.session_state:
        st.session_state.authorized = False

    if not st.session_state.authorized:
        st.markdown('<p class="log-text">ID: CACTUS_SERVER<br>SECURITY: CRITICAL<br>STATUS: ENCRYPTED</p>', unsafe_allow_html=True)
        if st.button("RUN EXPLOIT"):
            st.session_state.authorized = True
            st.rerun()
    else:
        # 1. Modem Audio (26 secondi di sincronizzazione)
        modem_b64 = get_audio_b64(find_file("modem.mp3"))
        play_audio_hidden(modem_b64)

        log_placeholder = st.empty()
        full_log = ""
        
        steps = [
            ("> Dialing 01010011...", 2.5),
            ("> Carrier detected...", 1.5),
            ("> Handshake: V.90 Protocol...", 6.0),
            ("> Bypassing IDS/IPS...", 4.5),
            ("> Escalating to root...", 3.5),
            ("> Accessing secret_payload...", 3.0),
            ("> Decrypting visual data...", 2.0),
        ]

        for text, delay in steps:
            full_log += text + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
            time.sleep(delay)

        # Buffer calcolato per la musica rock
        full_log += "> Executing payload...<br>"
        log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
        rock_b64 = get_audio_b64(find_file("musica.mp3"))
        time.sleep(3.0) 

        # --- FASE FINALE (ROCK + RAIN + ASCII) ---
        play_audio_hidden(rock_b64)
        start_cyber_rain()

        # ASCII ART: AUGURI + LOCANDIERI! (Stesso stile coordinato)
        # Ottimizzata per essere leggibile anche se rimpicciolita
        ascii_art = r"""
 █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ██╗
██╔══██╗██║   ██║██╔════╝ ██║   ██║██╔══██╗██║
███████║██║   ██║██║  ███╗██║   ██║██████╔╝██║
██╔══██║██║   ██║██║   ██║██║   ██║██╔══██╗██║
██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝

██╗     ██████╗  ██████╗ █████╗ ███╗   ██╗██████╗ ██╗███████╗██████╗ ██╗██╗
██║    ██╔═══██╗██╔════╝██╔══██╗████╗  ██║██╔══██╗██║██╔════╝██╔══██╗██║██║
██║    ██║   ██║██║     ███████║██╔██╗ ██║██║  ██║██║█████╗  ██████╔╝██║██║
██║    ██║   ██║██║     ██╔══██║██║╚██╗██║██║  ██║██║██╔══╝  ██╔══██╗██║╚═╝
███████╗╚██████╔╝╚██████╗██║  ██║██║ ╚████║██████╔╝██║███████╗██║  ██║██║██╗
╚══════╝ ╚═════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝
        """
        
        st.markdown(f'<div class="terminal-box">{ascii_art}</div>', unsafe_allow_html=True)
        
        st.success("SUCCESS: Buon Natale, Locandieri!")

        img_path = find_file("foto.png")
        if img_path:
            st.image(img_path, use_container_width=True)
        
        st.markdown('<p class="log-text">root@cactus_server:~# _</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

