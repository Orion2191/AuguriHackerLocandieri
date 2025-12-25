import streamlit as st
import time
import os
import streamlit.components.v1 as components

# Configurazione Pagina
st.set_page_config(page_title="BREACH_TERMINAL_2025", page_icon="💀", layout="centered")

# CSS: Terminale puro + Nascondi Audio Player
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    div[data-testid="stAudio"] { display: none; } /* Nasconde il player */
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
        position: relative;
        z-index: 10;
    }
    .log-text {
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
        line-height: 1.8;
        position: relative;
        z-index: 10;
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

def matrix_rain():
    matrix_js = """
    <canvas id="matrixCanvas" style="position: fixed; top: 0; left: 0; z-index: 1; width: 100vw; height: 100vh; opacity: 0.4;"></canvas>
    <script>
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const chars = "010101XMAS2025HACK";
    const fontSize = 16;
    const columns = canvas.width / fontSize;
    const drops = [];
    for (let i = 0; i < columns; i++) drops[i] = 1;
    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < drops.length; i++) {
            const text = chars.charAt(Math.floor(Math.random() * chars.length));
            ctx.fillStyle = (Math.random() > 0.5) ? '#00FF41' : '#FF0000'; 
            ctx.font = fontSize + 'px monospace';
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(draw, 33);
    </script>
    """
    components.html(matrix_js, height=0)

def main():
    if 'authorized' not in st.session_state:
        st.session_state.authorized = False

    if not st.session_state.authorized:
        st.markdown('<p class="log-text">ID: UNKNOWN_DEVICE<br>CONNECTION: DIAL-UP REQUIRED</p>', unsafe_allow_html=True)
        if st.button("ESTABLISH CONNECTION (RUN EXPLOIT)"):
            st.session_state.authorized = True
            st.rerun()
    else:
        audio_placeholder = st.empty()
        
        # --- PARTENZA MODEM ---
        modem_path = find_file("modem.mp3")
        if modem_path:
            with open(modem_path, "rb") as f:
                audio_placeholder.audio(f.read(), format="audio/mp3", autoplay=True)

        log_placeholder = st.empty()
        full_log = ""

        # --- SEQUENZA LOG SINCRONIZZATA (TOTALE: 26 SECONDI) ---
        steps = [
            ("> Dialing 01010011...", 2.5),             # Selezione numero
            ("> Carrier detected...", 1.5),              # Segnale trovato
            ("> Handshake: V.90 Protocol...", 6.0),      # Il fischio grattato più lungo
            ("> Bypassing IDS/IPS...", 4.0),             # Tentativo intrusione
            ("> Escalating to root...", 3.5),            # Privilegi
            ("> Accessing secret_payload...", 2.5),      # Ricerca file
            ("> Decrypting visual data...", 5.0),        # Decodifica finale
            ("---------------------------------------", 1.0) # Fine audio modem
        ]
        # Totale: 2.5+1.5+6+4+3.5+2.5+5+1 = 26.0 secondi

        for text, delay in steps:
            full_log += text + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
            time.sleep(delay)

        # --- FASE FINALE: MATRIX RAIN + ROCK ---
        matrix_rain()

        rock_path = find_file("musica.mp3")
        if rock_path:
            with open(rock_path, "rb") as f:
                audio_placeholder.audio(f.read(), format="audio/mp3", autoplay=True)

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
