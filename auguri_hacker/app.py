import streamlit as st
import time
import os

# Configurazione Pagina
st.set_page_config(page_title="BREACH_TERMINAL_2025", page_icon="💀", layout="centered")

# CSS: Terminale puro e stile hacker
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .terminal-box {
        background-color: #000000;
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 13px !important;
        white-space: pre !important;
        overflow-x: auto !important;
        line-height: 1.2 !important;
        border: 1px solid #00FF41;
        padding: 20px;
    }
    .log-text {
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
        line-height: 1.8;
    }
    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def find_file(name):
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.lower() == name.lower():
                return os.path.join(root, f)
    return None

def main():
    if 'authorized' not in st.session_state:
        st.session_state.authorized = False

    if not st.session_state.authorized:
        st.markdown('<p class="log-text">ID: UNKNOWN_DEVICE<br>CONNECTION: DIAL-UP REQUIRED</p>', unsafe_allow_html=True)
        if st.button("ESTABLISH CONNECTION (RUN EXPLOIT)"):
            st.session_state.authorized = True
            st.rerun()
    else:
        # --- FASE 1: CONNESSIONE MODEM 56K ---
        audio_placeholder = st.empty()
        log_placeholder = st.empty()
        
        # Carica e fai partire il suono del modem
        modem_path = find_file("modem.mp3")
        if modem_path:
            with open(modem_path, "rb") as f:
                audio_placeholder.audio(f.read(), format="audio/mp3", autoplay=True)

        full_log = ""
        steps = [
            ("> Dialing 01010011...", 1.5),
            ("> Carrier detected...", 1.0),
            ("> Handshake in progress...", 2.0),
            ("> Protocol: V.90 (56 Kbps)...", 1.5),
            ("> Bypassing firewall...", 2.0),
            ("> Escalating privileges...", 1.5),
            ("> Accessing /root/secret_payload...", 1.5),
            ("> Decrypting visual data...", 2.0),
            ("---------------------------------------", 0.5)
        ]

        for text, delay in steps:
            full_log += text + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
            time.sleep(delay)

        # --- FASE 2: VIOLAZIONE RIUSCITA (ROCK + NEVE + IMMAGINE) ---
        
        # Fermiamo il modem (sovrascrivendo il placeholder) e facciamo partire la musica rock
        rock_path = find_file("musica.mp3")
        if rock_path:
            with open(rock_path, "rb") as f:
                audio_placeholder.audio(f.read(), format="audio/mp3", autoplay=True)

        st.snow() # Cade la neve

        # ASCII ART
        ascii_art = r"""
 █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ██╗
██╔══██╗██║   ██║██╔════╝ ██║   ██║██╔══██╗██║
███████║██║   ██║██║  ███╗██║   ██║██████╔╝██║
██╔══██║██║   ██║██║   ██║██║   ██║██╔══██╗██║
██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝
        """
        st.markdown(f'<div class="terminal-box">{ascii_art}</div>', unsafe_allow_html=True)
        
        st.success("BREACH SUCCESSFUL: Happy Hacking & Merry Christmas!")

        # Visualizza l'immagine finale
        img_path = find_file("foto.png")
        if img_path:
            st.image(img_path, use_container_width=True)
        
        st.markdown('<p class="log-text">root@cybersec:~# _</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
