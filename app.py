import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="💖",
    layout="centered"
)

# 2. CSS PERSONALIZADO (APENAS ROSA, PRETO E LILÁS)
st.markdown("""
    <style>
    /* Fundo Preto */
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }

    /* Centralização de tudo */
    .stMainBlockContainer {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    /* Título Rosa com sombra Lilás */
    .main-title {
        color: #FF69B4; /* Rosa */
        font-size: 2.2rem;
        font-weight: bold;
        text-shadow: 2px 2px #9370DB; /* Lilás */
        margin: 10px 0;
    }

    /* Cards de Links (Rosa e Lilás) */
    .link-card {
        background: rgba(147, 112, 219, 0.1); /* Fundo Lilás transparente */
        border: 2px solid #FF69B4; /* Borda Rosa */
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        min-height: 180px;
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

    /* Botão Rosa "QUERO VER" */
    .btn-acessar {
        background-color: #FF69B4 !important;
        color: white !important;
        text-decoration: none;
        font-weight: bold;
        padding: 10px 30px;
        border-radius: 50px;
        font-size: 0.9rem;
        margin-top: 15px;
        display: inline-block;
    }

    /* Seção Quem é a Luhvee (Final da página) */
    .about-box {
        background-color: #1a1a1a;
        border: 1px solid #9370DB; /* Borda Lilás */
        border-radius: 15px;
        padding: 25px;
        margin-top: 40px;
        text-align: center;
        line-height: 1.6;
        color: #E6E6FA; /* Lilás claro */
    }

    /* Botões de Redes Sociais do Streamlit (Lilás) */
    div.stButton > button {
        background-color: #9370DB !important;
        color: white !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO (LOGO PEQUENO)
st.image("1000396187.jpeg", width=180) 

st.markdown("<div class='main-title'>✨ Luhvee Stores ✨</div>", unsafe_allow_html=True)
st.markdown("<p style='color: #E6E6FA;'>Bem-vindo ao seu paraíso de compras! 🛍️</p>", unsafe_allow_html=True)

st.write("")

# 4. CARDS DE LINKS PRINCIPAIS (3 COLUNAS)
col1, col2, col3 = st.columns(3)

def render_card(col, titulo, url):
    with col:
        st.markdown(f"""
        <div class="link-card">
            <div style="color: #FF69B4; font-size: 1.3rem; font-weight: bold;">{titulo}</div>
            <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
        </div>
        """, unsafe_allow_html=True)

render_card(col1, "Shopee 🛍️", "https://collshp.com/luhveestores")
render_card(col2, "Mercado Livre 🤝", "https://www.mercadolivre.com.br/social/axwelloliveira")
render_card(col3, "Internacional 🌎", "https://luhvee-store.systeme.io/prodentim-special")

st.write("---")

# 5. REDES SOCIAIS E SUPORTE
st.markdown("<p style='text-align: center; color: #FF69B4;'>Não esquece de nos seguir ❤️</p>", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)
s1.link_button("Insta 📸", "https://instagram.com/luhveestore", use_container_width=True)
s2.link_button("TikTok ♪", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
s3.link_button("Telegram ✈️", "https://t.me/luhveestores", use_container_width=True)
s4.link_button("Grupo VIP 💬", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
# BOTÃO DE SUPORTE (ROSA DESTAQUE)
st.link_button("💖 Fale com a Luh da Luhvee 💖", "https://wa.me/5511948021428", type="primary", use_container_width=True)

# 6. SEÇÃO QUEM É A LUHVEE (NO FINAL DA PÁGINA)
st.markdown(f"""
    <div class="about-box">
        <h3 style="color: #FF69B4; margin-bottom: 15px;">✨ Quem é a LuhVee Stores? ✨</h3>
        <p>A LuhVee Stores não é só uma loja… é uma <b>experiência 💖</b></p>
        <p>Selecionamos produtos que realmente valem a pena, com ofertas que cabem no seu bolso e tendências que estão bombando. 
        Nosso objetivo é te ajudar a comprar melhor, gastar menos e ainda se sentir incrível.</p>
        <p>💬 Aqui tem dica, tem promoção e, acima de tudo, <b>cuidado em cada indicação</b>. 
        Se você ama praticidade e economia, você está no lugar certo!</p>
        <p style="color: #FF69B4; font-weight: bold;">Bem-vindo à LuhVee Stores 💕</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='opacity: 0.3; font-size: 0.7rem;'>Luhvee Stores ✨</p>", unsafe_allow_html=True)
