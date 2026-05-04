import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="💖",
    layout="centered"
)

# 2. CSS PERSONALIZADO (ROSA, PRETO E LILÁS)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }
    .stMainBlockContainer {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .main-title {
        color: #FF69B4; 
        font-size: 2.2rem;
        font-weight: bold;
        text-shadow: 2px 2px #9370DB; 
        margin: 10px 0;
    }
    .link-card {
        background: rgba(147, 112, 219, 0.1); 
        border: 2px solid #FF69B4; 
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        min-height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .link-card:hover {
        border-color: #9370DB;
        transform: scale(1.02);
    }
    .btn-acessar {
        background-color: #FF69B4 !important;
        color: white !important;
        text-decoration: none;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 50px;
        font-size: 0.8rem;
        margin-top: 15px;
        display: inline-block;
    }
    .about-box {
        background-color: #1a1a1a;
        border: 1px solid #9370DB; 
        border-radius: 15px;
        padding: 25px;
        margin-top: 40px;
        text-align: center;
        line-height: 1.6;
        color: #E6E6FA; 
    }
    div.stButton > button {
        background-color: #9370DB !important;
        color: white !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO
st.image("1000396187.jpeg", width=180) 
st.markdown("<div class='main-title'>✨ Luhvee Stores ✨</div>", unsafe_allow_html=True)
st.markdown("<p style='color: #E6E6FA;'>Seu paraíso de compras atualizado! 🛍️</p>", unsafe_allow_html=True)

# Função auxiliar para criar os cards
def render_card(col, titulo, url):
    with col:
        st.markdown(f"""
        <div class="link-card">
            <div style="color: #FF69B4; font-size: 1.1rem; font-weight: bold;">{titulo}</div>
            <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
        </div>
        """, unsafe_allow_html=True)

# 4. CARDS DE LINKS (LINHA 1: 3 COLUNAS)
col1, col2, col3 = st.columns(3)
render_card(col1, "Shopee 🛍️", "https://collshp.com/luhveestores")
render_card(col2, "Mercado Livre 🤝", "https://www.mercadolivre.com.br/social/axwelloliveira")
render_card(col3, "Shein ✨", "https://onelink.shein.com/5/5ohy42r5xmbb")

# 4.1 CARDS DE LINKS (LINHA 2: 2 COLUNAS) - AQUI ESTÁ A CORREÇÃO
st.write("") 
col4, col5 = st.columns(2)
render_card(col4, "Loja Virtual LuhVee Stores ❤️", "https://luhveestores.com")
render_card(col5, "Internacional 🌎", "https://luhvee-store.systeme.io/prodentim-special")

st.write("---")

# 5. REDES SOCIAIS E SUPORTE
st.markdown("<p style='text-align: center; color: #FF69B4;'>Não esquece de nos seguir ❤️</p>", unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
s1.link_button("Insta 📸", "https://instagram.com/luhveestore", use_container_width=True)
s2.link_button("TikTok ♪", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
s3.link_button("Telegram ✈️", "https://t.me/luhveestores", use_container_width=True)
s4.link_button("Grupo VIP 💬", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
st.link_button("💖 Fale com a Luh da Luhvee 💖", "https://wa.me/5511948021428", type="primary", use_container_width=True)

# 6. SEÇÃO SOBRE
st.markdown(f"""
    <div class="about-box">
        <h3 style="color: #FF69B4; margin-bottom: 15px;">✨ Quem é a LuhVee Stores? ✨</h3>
        <p>A LuhVee Stores não é só uma loja… é uma <b>experiência 💖</b></p>
        <p>Selecionamos produtos que realmente valem a pena, com ofertas que cabem no seu bolso.</p>
        <p style="color: #FF69B4; font-weight: bold;">Bem-vindo à LuhVee Stores 💕</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='opacity: 0.3; font-size: 0.7rem;'>Luhvee Stores ✨</p>", unsafe_allow_html=True)
