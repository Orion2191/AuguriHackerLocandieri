import streamlit as st
import time
import os
import base64
import streamlit.components.v1 as components

# Configurazione Pagina
st.set_page_config(page_title="BREACH_2025", page_icon="💀", layout="centered")

# --- CSS PER IL LOOK TERMINALE E PIOGGIA ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; overflow: hidden; }
    
    header, footer, #MainMenu {visibility: hidden;}

    .log-text {
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
        line-height: 1.8;
        position: relative;
        z-index: 100;
    }

    .terminal-box {
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 12px !important;
        white-space: pre !important;
        border: 1px solid #00FF41;
        padding: 15px;
        background: rgba(0,0,0,0.9);
        position: relative;
        z-index: 100;
        overflow: hidden;
    }

    /* ANIMAZIONE CYBER-RAIN NATALIZIA */
    .matrix-rain {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    }
    .bit {
        position: absolute;
        top: -30px;
        font-family: monospace;
        font-size: 18px;
        animation: fall linear infinite;
    }
    @keyframes fall {
        to { transform: translateY(110vh); }
    }
    </style>
    """, unsafe_allow_html=True)

def find_file(name):
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.lower() == name.lower():
                return os.path.join(root, f)
    return None

# Funzione per suonare audio in modo TOTALMENTE INVISIBILE
def play_audio_hidden(file_path):
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # Inietta un tag audio HTML5 con autoplay e senza controlli
            audio_html = f"""
                <audio autoplay="true" style="display:none;">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """
            components.html(audio_html, height=0, width=0)

# Genera la pioggia natalizia (CSS puro)
def start_cyber_rain():
    import random
    cols = 40 # Più densa
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
        st.markdown('<p class="log-text">ID: UNKNOWN_DEVICE<br>CONNECTION: DIAL-UP REQUIRED</p>', unsafe_allow_html=True)
        if st.button("ESTABLISH CONNECTION (RUN EXPLOIT)"):
            st.session_state.authorized = True
            st.rerun()
    else:
        # --- FASE 1: SUONO MODEM + LOG (26 SECONDI) ---
        play_audio_hidden(find_file("modem.mp3"))

        log_placeholder = st.empty()
        full_log = ""
        steps = [
            ("> Dialing 01010011...", 2.5),
            ("> Carrier detected...", 1.5),
            ("> Handshake: V.90 Protocol...", 6.0),
            ("> Bypassing IDS/IPS...", 4.5),
            ("> Escalating to root...", 3.5),
            ("> Searching secret_payload...", 3.0),
            ("> Decrypting visual data...", 5.0),
        ] # Totale circa 26 secondi

        for text, delay in steps:
            full_log += text + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
            time.sleep(delay)

        # --- FASE 2: MUSICA ROCK + MATRIX RAIN + IMMAGINE ---
        
        # Audio Rock (sovrascrive il modem essendo un nuovo componente iniettato)
        play_audio_hidden(find_file("musica.mp3"))
        
        # Pioggia Digitale
        start_cyber_rain()

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

        img_path = find_file("foto.png")
        if img_path:
            st.image(img_path, use_container_width=True)
        
        st.markdown('<p class="log-text">root@cybersec:~# _</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
