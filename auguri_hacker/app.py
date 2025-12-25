import streamlit as st
import time
import os
import base64
import streamlit.components.v1 as components

# 1. Configurazione Pagina
st.set_page_config(page_title="BREACHMAS_2025", page_icon="💀", layout="wide")

# 2. CSS Avanzato per Mobile e Rimozione Spazi
st.markdown("""
    <style>
    .stApp { background-color: #000000; overflow-x: hidden; }
    header, footer, #MainMenu {visibility: hidden;}
    
    /* Riduce gli spazi tra i blocchi di Streamlit */
    .block-container { padding-top: 2rem !important; padding-bottom: 0rem !important; }
    div.stVerticalBlock > div { padding: 0px !important; margin: 0px !important; }

    /* LOG: Grandi e nitidi */
    .log-text {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 20px !important; 
        line-height: 1.4 !important;
        margin-bottom: 5px !important;
    }

    /* ASCII BOX: Infrangibile e Responsive */
    .terminal-box {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
        white-space: pre !important;
        border: 1px solid #00FF41;
        padding: 10px;
        background: rgba(0,0,0,0.9);
        display: inline-block;
        /* Dimensione font proporzionale alla larghezza schermo */
        font-size: 1.6vw !important; 
        line-height: 1.1 !important;
        width: 100%;
        overflow: hidden;
    }

    @media screen and (max-width: 600px) {
        .terminal-box { font-size: 2.1vw !important; padding: 5px; }
        .log-text { font-size: 16px !important; }
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

    /* Nasconde player */
    div[data-testid="stAudio"] { position: fixed; bottom: -100px; }
    </style>
    """, unsafe_allow_html=True)

def find_file(name):
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.lower() == name.lower(): return os.path.join(root, f)
    return None

def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def play_audio_hidden(b64_string):
    if b64_string:
        audio_html = f'<audio autoplay="true" style="display:none;"><source src="data:audio/mp3;base64,{b64_string}" type="audio/mp3"></audio>'
        components.html(audio_html, height=0, width=0)

def main():
    if 'auth' not in st.session_state: st.session_state.auth = False

    if not st.session_state.auth:
        st.markdown('<div class="log-text">ID: CACTUS_SERVER<br>STATUS: ENCRYPTED</div>', unsafe_allow_html=True)
        if st.button("RUN EXPLOIT"):
            st.session_state.auth = True
            st.rerun()
    else:
        # --- START: Caricamento simultaneo ---
        audio_placeholder = st.empty()
        # Carichiamo subito il modem
        modem_b64 = get_audio_b64(find_file("modem.mp3"))
        play_audio_hidden(modem_b64)
        
        log_placeholder = st.empty()
        full_log = ""
        
        # Elenco log sincronizzati
        steps = [
            ("> Dialing 01010011...", 2.0),
            ("> Carrier detected...", 1.5),
            ("> Handshake: V.90...", 6.0),
            ("> Bypassing IDS/IPS...", 4.5),
            ("> Escalating to root...", 3.5),
            ("> Decrypting buffer...", 3.0),
        ]

        # Esecuzione log
        for i, (text, delay) in enumerate(steps):
            full_log += text + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
            # A metà dei log, iniziamo a caricare la musica rock in memoria (background)
            if i == 3: 
                rock_b64 = get_audio_b64(find_file("musica.mp3"))
            time.sleep(delay)

        # Ultimo passo senza ritardo perché il file è già pronto
        full_log += "> Executing payload...<br>"
        log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
        time.sleep(1.5)

        # --- AZIONE FINALE ---
        play_audio_hidden(rock_b64)
        
        # Matrix Rain
        cols = 30
        rain_html = '<div class="matrix-rain">'
        for i in range(cols):
            rain_html += f'<div class="bit" style="left:{i*3.3}%; color:{"#00FF41" if i%2==0 else "#FF0000"}; animation-duration:{2+i%3}s; animation-delay:{i%2}s;">{os.urandom(1).hex()[0]}</div>'
        st.markdown(rain_html + '</div>', unsafe_allow_html=True)

        # ASCII ART coordinata
        ascii_art = r"""
 █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ██╗
██╔══██╗██║   ██║██╔════╝ ██║   ██║██╔══██╗██║
███████║██║   ██║██║  ███╗██║   ██║██████╔╝██║
██╔══██║██║   ██║██║   ██║██║   ██║██╔══██╗██║
██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝

██╗      ██████╗  ██████╗  █████╗  ███╗   ██╗██████╗ ██╗███████╗██████╗ ██╗
██║     ██╔═══██╗██╔════╝ ██╔══██╗ ████╗  ██║██╔══██╗██║██╔════╝██╔══██╗██║
██║     ██║   ██║██║      ███████║ ██╔██╗ ██║██║  ██║██║█████╗  ██████╔╝██║
██║     ██║   ██║██║      ██╔══██║ ██║╚██╗██║██║  ██║██║██╔══╝  ██╔══██╗██║
███████╗╚██████╔╝╚██████╗ ██║  ██║ ██║ ╚████║██████╔╝██║███████╗██║  ██║██║
╚══════╝ ╚═════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═══╝╚═════╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝"""
        
        st.markdown(f'<div class="terminal-box">{ascii_art}</div>', unsafe_allow_html=True)
        
        st.success("SUCCESS: Buon Natale, Locandieri!")

        # Immagine senza spazi
        img_path = find_file("foto.png")
        if img_path:
            st.image(img_path, use_container_width=True)
        
        st.markdown('<div class="log-text">root@cactus_server:~# _</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
