import streamlit as st
import time
import os
import base64
from PIL import Image, ImageDraw, ImageFont
import streamlit.components.v1 as components

# 1. Configurazione Pagina
st.set_page_config(page_title="BREACHMAS_2025", page_icon="💀", layout="wide")

# 2. CSS: Log Grandi e Stile Terminale
st.markdown("""
    <style>
    .stApp { background-color: #000000; overflow-x: hidden; }
    header, footer, #MainMenu {visibility: hidden;}
    
    .block-container { padding-top: 2rem !important; }

    /* LOG: Sempre grandi e leggibili */
    .log-text {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 20px !important; 
        line-height: 1.5 !important;
        text-shadow: 0 0 5px #00FF41;
        margin-bottom: 10px !important;
        display: block;
    }

    /* Nasconde player audio */
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

def matrix_rain_js():
    js_code = """
    <canvas id="matrix" style="position: fixed; top: 0; left: 0; z-index: 0; width: 100vw; height: 100vh; opacity: 0.5;"></canvas>
    <script>
    const canvas = document.getElementById('matrix');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const chars = "010101XMAS";
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
    components.html(js_code, height=0)

def main():
    if 'authorized' not in st.session_state: st.session_state.authorized = False

    if not st.session_state.authorized:
        st.markdown('<div class="log-text">SYSTEM: CACTUS_SERVER<br>DATE: 25-12-2025<br>STATUS: ENCRYPTED</div>', unsafe_allow_html=True)
        if st.button("RUN EXPLOIT"):
            st.session_state.authorized = True
            st.rerun()
    else:
        # 1. MODEM (26s)
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
            ("> Decrypting visual data...", 5.0),
        ]

        for i, (text, delay) in enumerate(steps):
            full_log += text + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
            if i == 4: rock_b64 = get_audio_b64(find_file("musica.mp3"))
            time.sleep(delay)

        # --- AZIONE FINALE ---
        play_audio_hidden(rock_b64)
        matrix_rain_js()

        # LA SCRITTA ASCII (AUGURI LOCANDIERI!)
        # Per evitare che si distrugga, la mettiamo in un blocco preformattato 
        # dentro un DIV che forziamo a non andare mai a capo.
        ascii_art = r"""
 █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ██╗
██╔══██╗██║   ██║██╔════╝ ██║   ██║██╔══██╗██║
███████║██║   ██║██║  ███╗██║   ██║██████╔╝██║
██╔══██║██║   ██║██║   ██║██║   ██║██╔══██╗██║
██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝

██╗      ██████╗  ██████╗  █████╗  ███╗   ██╗██████╗ ██╗███████╗██████╗ ██╗██╗
██║     ██╔═══██╗██╔════╝ ██╔══██╗ ████╗  ██║██╔══██╗██║██╔════╝██╔══██╗██║██║
██║     ██║   ██║██║      ███████║ ██╔██╗ ██║██║  ██║██║█████╗  ██████╔╝██║██║
██║     ██║   ██║██║      ██╔══██║ ██║╚██╗██║██║  ██║██║██╔══╝  ██╔══██╗██║╚═╝
███████╗╚██████╔╝╚██████╗ ██║  ██║ ██║ ╚████║██████╔╝██║███████╗██║  ██║██║██╗
╚══════╝ ╚═════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═══╝╚═════╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝
        """
        
        # Tecnica finale: Usiamo un tag <pre> con font-size calcolato in VW (Viewport Width)
        # 1.3vw assicura che 75 caratteri stiano in larghezza su ogni schermo.
        st.markdown(f"""
            <div style="border: 1px solid #00FF41; padding: 10px; background: rgba(0,0,0,0.9); margin-bottom: 20px;">
                <pre style="color: #00FF41; font-family: 'Courier New', monospace; font-size: 1.3vw; line-height: 1.1; white-space: pre; overflow: visible;">{ascii_art}</pre>
            </div>
            <style>
            @media screen and (max-width: 600px) {{
                pre {{ font-size: 1.6vw !important; }}
            }}
            </style>
            """, unsafe_allow_html=True)
        
        st.success("SUCCESS: Buon Natale, Locandieri!")

        img_path = find_file("foto.png")
        if img_path:
            st.image(img_path, use_container_width=True)
        
        st.markdown('<div class="log-text">root@cactus_server:~# _</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
