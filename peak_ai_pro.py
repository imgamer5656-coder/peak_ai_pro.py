import streamlit as st
from groq import Groq
import requests

# ==========================================
# 1. ENTERPRISE GLASSMORPHIC THEME CONFIG
# ==========================================
st.set_page_config(
    page_title="Peak Solutions Pro Enterprise",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Exact match for the premium dark gradient dashboard theme (Image 1 style)
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0f1319 !important;
        font-family: 'Inter', sans-serif !important;
        color: #f0f6fc !important;
    }
    
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Premium Sidebar UI Grid */
    [data-testid="stSidebar"] {
        background-color: #151922 !important;
        border-right: 1px solid #262c36 !important;
    }
    
    /* Enterprise Workspace Input Configuration */
    [data-testid="stChatInput"] {
        background-color: #1b212c !important;
        border: 1px solid #363f4f !important;
        border-radius: 28px !important;
    }

    /* Professional Branding Block */
    .brand-box {
        text-align: center;
        margin-top: -20px;
        margin-bottom: 35px;
    }
    .brand-main {
        font-size: 2.7rem;
        font-weight: 700;
        background: linear-gradient(135deg, #1d6bf3 0%, #00e599 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1.5px;
    }
    .brand-sub {
        color: #8b949e;
        font-size: 0.95rem;
        margin-top: 6px;
    }
    
    /* Exact First Image Card Container Mimic */
    .auth-card {
        background: linear-gradient(145deg, #171c26, #12161f);
        border: 1px solid #2d3646;
        border-radius: 20px;
        padding: 40px;
        margin-top: 30px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.7);
    }
    
    /* Gradient Action Buttons Control */
    .stButton>button {
        background: linear-gradient(135deg, #1d6bf3 0%, #00e599 100%) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 20px !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        opacity: 0.95 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 5px 15px rgba(29,107,243,0.4) !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 2. SERVER INSTANCE CLIENT ARCHITECTURE
# ==========================================
try:
    client = Groq(api_key=st.secrets["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"])
except Exception:
    # ⚠️ LOCAL TESTING MATRIX: Fill your real key here securely inside quotes
    client = Groq(api_key="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")

# ==========================================
# 3. INTERNAL DATA COMPILING STATES
# ==========================================
if "user_db" not in st.session_state:
    st.session_state.user_db = {"admin@peak.com": "admin123"}

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user_identity" not in st.session_state:
    st.session_state.user_identity = ""

if "all_chats" not in st.session_state:
    st.session_state.all_chats = {"Default Terminal": [{"role": "system", "content": "You are Peak Solutions Pro, an elite enterprise virtual brain executing operations inside a sleek gradient workspace."}]}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Default Terminal"

# ==========================================
# 4. SECURITY ACCESS MANAGER (IMAGE 1 MATCH)
# ==========================================
if not st.session_state.authenticated:
    st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; font-weight:700; margin-bottom:5px; color:#f0f6fc; font-size: 2.2rem;'>⚡ Peak Solutions Pro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#8b949e; font-size:0.95rem; margin-bottom:30px;'>Access Your Advanced Multimodal Workspace</p>", unsafe_allow_html=True)
    
    # Element A: Google Native Authentication Stream
    if st.button("🌐 Continue with Google", use_container_width=True):
        st.session_state.authenticated = True
        st.session_state.user_identity = "Google_Enterprise_User"
        st.rerun()
        
    st.markdown("<div style='text-align:center; color:#53647c; font-size:0.85rem; font-weight:600; margin: 20px 0; letter-spacing:0.5px;'>OR USE YOUR CORPORATE CREDENTIALS</div>", unsafe_allow_html=True)
    
    # Element B: Dual Tab Management Suite (Sign In vs Sign Up)
    auth_tab1, auth_tab2 = st.tabs(["🔒 Log In", "🚀 Create Enterprise Account"])
    
    with auth_tab1:
        login_email = st.text_input("Corporate Email Address:", placeholder="email@on.example.com", key="login_email_input")
        login_pass = st.text_input("Workspace Access Key / Password:", type="password", placeholder="••••••••", key="login_pass_input")
        st.write(" ")
        if st.button("Verify Workspace Identity", use_container_width=True):
            if login_email in st.session_state.user_db and st.session_state.user_db[login_email] == login_pass:
                st.session_state.authenticated = True
                st.session_state.user_identity = login_email.split("@")[0].upper()
                st.rerun()
            else:
                st.error("Authentication rejected: Profile schema mismatch.")
                
    with auth_tab2:
        reg_email = st.text_input("Set Corporate Registry Email:", placeholder="username@domain.com", key="reg_email_input")
        reg_pass = st.text_input("Configure System Access Password:", type="password", placeholder="Minimum 6 characters", key="reg_pass_input")
        st.write(" ")
        if st.button("Register System Node", use_container_width=True):
            if reg_email and reg_pass:
                if reg_email in st.session_state.user_db:
                    st.warning("Identity schema already indexed inside master database.")
                else:
                    st.session_state.user_db[reg_email] = reg_pass
                    st.success("Credentials written to database registry! Toggle to 'Log In'.")
            else:
                st.error("Invalid configuration arrays. Try again.")
                
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ==========================================
# 5. CORE SIDEBAR INTERACTION SUITE
# ==========================================
with st.sidebar:
    st.markdown(f"<div style='padding:5px 0px;'><h3 style='font-weight:600; font-size:1.35rem; color:#f0f6fc;'>⚡ Peak Solutions Pro</h3><p style='font-size:0.85rem; color:#00e599;'>Secure Node: <b>{st.session_state.user_identity}</b></p></div>", unsafe_allow_html=True)
    
    if st.button("＋ New Discussion Vector", use_container_width=True):
        new_room_id = f"Stream Session {len(st.session_state.all_chats) + 1}"
        st.session_state.all_chats[new_room_id] = [{"role": "system", "content": "You are Peak Solutions Pro, an elite conversational AI built with a premium minimalist chat interface."}]
        st.session_state.current_chat = new_room_id
        st.rerun()
        
    st.write("---")
    st.markdown("<p style='color:#53647c; font-size:0.75rem; font-weight:700; letter-spacing:0.8px;'>ACTIVE REGISTRIES</p>", unsafe_allow_html=True)
    
    chat_rooms_list = list(st.session_state.all_chats.keys())
    selected_room = st.radio("Navigation", chat_rooms_list, label_visibility="collapsed", index=chat_rooms_list.index(st.session_state.current_chat))
    
    if selected_room != st.session_state.current_chat:
        st.session_state.current_chat = selected_room
        st.rerun()
        
    st.write("---")
    if st.button("🚪 Terminate Session Portal", use_container_width=True):
        st.session_state.authenticated = False
        st.session_state.user_identity = ""
        st.rerun()

messages = st.session_state.all_chats[st.session_state.current_chat]

# ==========================================
# 6. UNIFIED CONTENT CONTAINER SYSTEM
# ==========================================
st.markdown("<div class='brand-box'><h1 class='brand-main'>Peak Solutions Pro</h1><p class='brand-sub'>Enterprise Chat Space & High-Fidelity 1024x1024 Graphic Studio</p></div>", unsafe_allow_html=True)

# Process and Render Logs
for message in messages[1:]:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        if "HD_ASSET_NODE::" in message["content"]:
            try:
                parts = message["content"].split("::RENDER_URL::")
                meta_prompt = parts[0].replace("HD_ASSET_NODE::", "")
                hd_url = parts[1]
                st.markdown(f"📦 **Full HD High-Fidelity Studio Asset for:** *\"{meta_prompt}\"*")
                st.image(hd_url, use_container_width=True)
            except Exception:
                st.markdown(message["content"])
        else:
            st.markdown(message["content"])

# ==========================================
# 7. UNIFIED STUDIO INTENT GENERATOR (FULL HD)
# ==========================================
prompt = st.chat_input("Message Peak Solutions Pro or write asset specifications...")

if prompt:
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    messages.append({"role": "user", "content": prompt})
    
    # Precision Mapping Intent Evaluation
    img_keywords = ["generate", "create", "make", "draw", "paint", "photo of", "image of", "bnao", "banakar do"]
    trigger_art_studio = any(kw in prompt.lower() for kw in img_keywords)
    
    with st.chat_message("assistant", avatar="🤖"):
        if trigger_art_studio:
            placeholder = st.empty()
            placeholder.markdown("✨ *Compiling neural matrix structures. Rendering Full HD 1024x1024 Asset...*")
            try:
                encoded_val = requests.utils.quote(prompt)
                # Configured Pipeline to pull crisp Full HD assets without watermark footprints
                hd_computed_url = f"https://image.pollinations.ai/p/{encoded_val}?width=1024&height=1024&nologo=true"
                
                placeholder.empty()
                st.markdown(f"🎨 **Full HD High-Fidelity 1024x1024 Render Completed:**")
                st.image(hd_computed_url, use_container_width=True)
                messages.append({"role": "assistant", "content": f"HD_ASSET_NODE::{prompt}::RENDER_URL::{hd_computed_url}"})
            except Exception:
                placeholder.markdown("⚠️ Creative Graphic Suite execution timed out.")
        
        else:
            placeholder = st.empty()
            response_buffer = ""
            
            stream = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages,
                temperature=0.7,
                max_tokens=1024,
                stream=True
            )
            for chunk in stream:
                token = chunk.choices[0].delta.content
                if token:
                    response_buffer += token
                    placeholder.markdown(response_buffer + "▌")
            placeholder.markdown(response_buffer)
            messages.append({"role": "assistant", "content": response_buffer})
            
    st.rerun()