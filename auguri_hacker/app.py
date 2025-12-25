import streamlit as st
import time

# Configurazione Pagina
st.set_page_config(page_title="System Breach - Greetings", page_icon="💀")

# CSS per il look Terminale
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .terminal { color: #00FF41; font-family: 'Courier New', monospace; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

def main():
    if 'run' not in st.session_state:
        st.session_state.run = False

    if not st.session_state.run:
        st.markdown('<p class="terminal">READY TO DECRYPT AD-2025_PAYLOAD?</p>', unsafe_allow_html=True)
        if st.button("RUN EXPLOIT"):
            st.session_state.run = True
            st.rerun()
    else:
        # Sequenza Terminale
        placeholder = st.empty()
        log_text = ""
        logs = [
            "> Initializing connection...",
            "> Bypassing firewall...",
            "> Escalating privileges to root...",
            "> Accessing /home/user/secret_greetings...",
            "> Decrypting visual data...",
            "---------------------------------------"
        ]
        
        for log in logs:
            log_text += log + "\n\n"
            placeholder.markdown(f'<pre class="terminal">{log_text}</pre>', unsafe_allow_html=True)
            time.sleep(0.7)

        # Scritta ASCII corretta
        st.markdown("""<pre class="terminal">
 █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗██████╗ ██╗
██╔══██╗██║   ██║██╔════╝ ██║   ██║██╔══██╗██║
███████║██║   ██║██║  ███╗██║   ██║██████╔╝██║
██╔══██║██║   ██║██║   ██║██║   ██║██╔══██╗██║
██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝</pre>""", unsafe_allow_html=True)

        st.success("Target compromised. Message displayed below:")
        
        # --- CARICAMENTO IMMAGINE ---
        # Sostituisci 'foto.jpg' con il nome esatto del tuo file (es. 'regalo.png')
        st.image("foto.jpg", caption="[DECRYPTED_IMAGE_V1.0]", use_container_width=True)
        
        st.balloons()
        st.markdown('<p class="terminal">ubuntu@cybersec:~$ _</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()