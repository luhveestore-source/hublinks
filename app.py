import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="🛍️",
    layout="centered"
)

# 2. ESTILO VISUAL (CORES: ROSA, DOURADO, PRETO, LILÁS)
st.markdown("""
    <style>
    /* Fundo Principal */
    .stApp {
        background-color: #0e0e0e; /* Preto */
        color: white;
    }
    
    /* Centralização Geral */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    /* Título Principal */
    .main-title {
        color: #FF69B4; /* Rosa Choque */
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 2.5rem;
        font-weight: bold;
        margin-top: 10px;
        text-shadow: 2px 2px #9370DB; /* Sombra Lilás */
    }

    /* Texto de Boas-vindas */
    .welcome-text {
        color: #E6E6FA; /* Lilás claro */
        font-size: 1.1rem;
        line-height: 1.5;
        max-width: 500px;
        margin: 0 auto 30px auto;
    }

    /* Cartões de links */
    .link-card {
        background: linear-gradient(145deg, #1a1a1a, #2b1a2b); /* Degradê Preto para Lilás escuro */
        border: 2px solid #d4af37; /* Dourado */
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
        transition: 0.3s;
        box-shadow: 0px 4px 10px rgba(255, 105, 180, 0.2); /* Brilho Rosa */
    }
    
    .link-card:hover {
        border-color: #FF69B4; /* Muda para Rosa no hover */
        transform: scale(1.05);
    }

    .card-title {
        color: #d4af37; /* Dourado */
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .btn-acessar {
        display: inline-block;
        color: #ffffff !important;
        background-color: #FF69B4; /* Rosa */
        text-decoration: none;
        font-weight: bold;
        padding: 8px 20px;
        border-radius: 50px;
        font-size: 0.9rem;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO (LOGO GRANDE E CENTRALIZADO)
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Logo maior e centralizado
col_logo, _ = st.columns([1, 0.01]) # Truque para centralizar
with col_logo:
    try:
        st.image("1000396187.jpeg", width=300) # Aumentei para 300px
    except:
        st.write("✨ [Logo Luhvee Stores] ✨")

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
        <div style="color: #b0b0b0; font-size: 0.85rem;">{descricao}</div>
        <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
    </div>
    """, unsafe_allow_html=True)

# 5. GRADE DE PRODUTOS (2 POR LINHA NO MOBILE FICA ÓTIMO)
c1, c2 = st.columns(2)
with c1:
    render_card("Shopee 🛍️", "Meus achadinhos favoritos.", "https://collshp.com/luhveestores")
    render_card("Internacional 🌎", "Novidades do mundo todo.", "https://luhvee-store.systeme.io/prodentim-special")
with c2:
    render_card("Mercado Livre 🤝", "Produtos com entrega rápida.", "https://www.mercadolivre.com.br/social/axwelloliveira")
    render_card("Realme 📱", "Celulares e tecnologia.", "https://www.realme.com/br/")

st.write("---")

# 6. REDES SOCIAIS (TOM MENOS FORMAL)
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
