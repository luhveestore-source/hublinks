import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="🛍️",
    layout="centered"
)

# 2. ESTILO VISUAL (ROSA, DOURADO, PRETO, LILÁS)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }
    
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .main-title {
        color: #FF69B4; /* Rosa */
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        margin-top: 10px;
        text-shadow: 2px 2px #9370DB; /* Lilás */
    }

    .welcome-text {
        color: #E6E6FA; /* Lilás claro */
        font-size: 1.1rem;
        line-height: 1.5;
        margin-bottom: 30px;
    }

    .link-card {
        background: linear-gradient(145deg, #1a1a1a, #2b1a2b);
        border: 2px solid #d4af37; /* Dourado */
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
        transition: 0.3s;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .link-card:hover {
        border-color: #FF69B4;
        transform: scale(1.05);
    }

    .card-title {
        color: #d4af37;
        font-size: 1.3rem;
        font-weight: bold;
    }

    .btn-acessar {
        display: inline-block;
        color: #ffffff !important;
        background-color: #FF69B4;
        text-decoration: none;
        font-weight: bold;
        padding: 10px 25px;
        border-radius: 50px;
        font-size: 0.9rem;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO (LOGO E BOAS-VINDAS)
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

try:
    # Logo Centralizado e Maior
    st.image("1000396187.jpeg", width=350) 
except:
    st.write("✨ **Luhvee Stores** ✨")

st.markdown("<h1 class='main-title'>✨ Luhvee Stores ✨</h1>", unsafe_allow_html=True)

st.markdown("""
    <div class='welcome-text'>
        <b>Bem-vindo ao seu paraíso de compras!</b><br>
        Encontre tudo o que você precisa em um único lugar.<br>
        Desde produtos incríveis até conteúdos exclusivos, a Luhvee Stores reúne as melhores oportunidades para você! 🛒🎁
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 4. FUNÇÃO PARA CARDS
def render_card(titulo, descricao, url):
    st.markdown(f"""
    <div class="link-card">
        <div class="card-title">{titulo}</div>
        <div style="color: #b0b0b0; font-size: 0.85rem; margin-top: 5px;">{descricao}</div>
        <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
    </div>
    """, unsafe_allow_html=True)

# 5. GRADE DE PRODUTOS (3 COLUNAS ALINHADAS)
col1, col2, col3 = st.columns(3)

with col1:
    render_card("Shopee 🛍️", "Meus achadinhos favoritos com os melhores preços.", "https://collshp.com/luhveestores")

with col2:
    render_card("Mercado Livre 🤝", "Produtos selecionados com entrega super rápida.", "https://www.mercadolivre.com.br/social/axwelloliveira")

with col3:
    render_card("Internacional 🌎", "Oportunidades e conteúdos exclusivos globais.", "https://luhvee-store.systeme.io/prodentim-special")

st.write("---")

# 6. REDES SOCIAIS E SUPORTE
st.markdown("<h3 style='text-align: center; color: #9370DB;'>Não esquece de nos seguir, fique por dentro das melhores promoções ❤️</h3>", unsafe_allow_html=True)

social_col1, social_col2, social_col3, social_col4 = st.columns(4)
social_col1.link_button("Insta 📸", "https://instagram.com/luhveestore", use_container_width=True)
social_col2.link_button("TikTok ♪", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
social_col3.link_button("Telegram ✈️", "https://t.me/luhveestores", use_container_width=True)
social_col4.link_button("Grupo VIP 💬", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
# BOTÃO DE SUPORTE PERSONALIZADO
st.link_button("💖 Fale com a Luh da Luhvee 💖", "https://wa.me/5511948021428", type="primary", use_container_width=True)

st.markdown("<br><p style='text-align: center; opacity: 0.5;'>Feito com amor por Luhvee Stores ✨</p>", unsafe_allow_html=True)
