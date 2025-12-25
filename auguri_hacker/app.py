import streamlit as st
import time
import os

# Configurazione Pagina
st.set_page_config(page_title="System Breach", page_icon="💀")

# CSS per il look Terminale - Forza il font e impedisce l'andata a capo automatica
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .terminal-box {
        background-color: #000000;
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 12px !important;
        white-space: pre !important;
        overflow-x: auto !important;
        line-height: 1.2 !important;
        border: 1px solid #00FF41;
        padding: 15px;
        margin-bottom: 20px;
    }
    .log-text {
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Funzione per trovare il file anche se il nome è scritto male (es. FOTO.PNG)
    def find_image(target_name):
        for root, dirs, files in os.walk("."):
            for f in files:
                if f.lower() == target_name.lower():
                    return os.path.join(root, f)
        return None

    if 'run' not in st.session_state:
        st.session_state.run = False

    if not st.session_state.run:
        st.markdown('<p style="color:#00FF41; font-family:monospace;">[SYSTEM OVERRIDE READY]</p>', unsafe_allow_html=True)
        if st.button("RUN DECRYPT_AUGURI.SH"):
            st.session_state.run = True
            st.rerun()
    else:
        # LOG DI CARICAMENTO
        log_placeholder = st.empty()
        log_content = ""
        for msg in ["> Injecting SQLi...", "> Bypassing Auth...", "> Downloading foto.png...", "> Finalizing..."]:
            log_content += msg + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{log_content}</div>', unsafe_allow_html=True)
            time.sleep(0.5)

        # SCRITTA ASCII - CORRETTA E PROTETTA
        # Ho usato il tag <pre> dentro una div con classe terminal-box
        ascii_art = r"""
 █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ██╗
██╔══██╗██║   ██║██╔════╝ ██║   ██║██╔══██╗██║
███████║██║   ██║██║  ███╗██║   ██║██████╔╝██║
██╔══██║██║   ██║██║   ██║██║   ██║██╔══██╗██║
██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝
        """
        st.markdown(f'<div class="terminal-box">{ascii_art}</div>', unsafe_allow_html=True)
        
        st.success("ACCESS GRANTED: Buon Natale, Hacker!")

        # CARICAMENTO IMMAGINE (Cerca foto.png)
        img_path = find_image("foto.png")
        
        if img_path:
            st.image(img_path, caption="DECRYPTED_MEDIA_01", use_container_width=True)
            st.balloons()
        else:
            st.error("ERRORE: Non trovo 'foto.png' su GitHub!")
            st.write("File presenti nel server:", os.listdir('.'))

        st.markdown('<p style="color:#00FF41; font-family:monospace;">root@cybersec:~# _</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
