import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="🛍️",
    layout="centered"
)

# 2. CSS AVANÇADO PARA CENTRALIZAÇÃO TOTAL E CORES
st.markdown("""
    <style>
    /* Forçar fundo preto em tudo */
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }

    /* Container para centralizar tudo que for HTML */
    .center-all {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }

    /* Título com cores Rosa e Lilás */
    .main-title {
        color: #FF69B4; /* Rosa */
        font-size: 3rem !important;
        font-weight: bold;
        margin-top: 20px;
        text-shadow: 3px 3px #9370DB; /* Lilás */
        font-family: 'Arial', sans-serif;
    }

    /* Texto de boas-vindas centralizado */
    .welcome-text {
        color: #E6E6FA; /* Lilás claro */
        font-size: 1.2rem;
        line-height: 1.6;
        max-width: 600px;
        margin: 20px auto;
        text-align: center;
    }

    /* Estilo dos Cards de Links */
    .link-card {
        background: linear-gradient(145deg, #1a1a1a, #2b1a2b);
        border: 2px solid #d4af37; /* Dourado */
        border-radius: 20px;
        padding: 25px;
        margin: 10px;
        text-align: center;
        transition: 0.3s;
        display: flex;
        flex-direction: column;
        align-items: center;
        box-shadow: 0px 4px 15px rgba(255, 105, 180, 0.1);
    }
    
    .link-card:hover {
        border-color: #FF69B4;
        transform: scale(1.03);
    }

    /* Título dentro do card */
    .card-title {
        color: #d4af37;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Botão "QUERO VER" */
    .btn-acessar {
        display: inline-block;
        color: #ffffff !important;
        background-color: #FF69B4;
        text-decoration: none;
        font-weight: bold;
        padding: 12px 30px;
        border-radius: 50px;
        font-size: 1rem;
        margin-top: 15px;
        border: none;
    }

    /* Ajuste para as imagens do Streamlit ficarem centralizadas */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    
    /* Remover margens extras das colunas */
    [data-testid="column"] {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTEÚDO CENTRALIZADO
st.markdown("<div class='center-all'>", unsafe_allow_html=True)

# Exibição do Logo (Aumentado para 400px para ser o destaque)
try:
    st.image("1000396187.jpeg", width=400)
except:
    st.write("✨ **LUHVEE STORES** ✨")

# Título e Textos
st.markdown("<h1 class='main-title'>✨ Luhvee Stores ✨</h1>", unsafe_allow_html=True)

st.markdown("""
    <div class='welcome-text'>
        <b>Bem-vindo ao seu paraíso de compras!</b><br>
        Encontre tudo o que você precisa em um único lugar.<br>
        Desde produtos incríveis até conteúdos exclusivos, a Luhvee Stores reúne as melhores oportunidades para você! 🛒🎁
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# 4. CARDS DE LINKS (Organizados em colunas centralizadas)
# Usamos colunas, mas o CSS acima garante que o conteúdo dentro delas centralize
col1, col2, col3 = st.columns(3)

def render_card(col, titulo, descricao, url):
    with col:
        st.markdown(f"""
        <div class="link-card">
            <div class="card-title">{titulo}</div>
            <div style="color: #b0b0b0; font-size: 0.9rem;">{descricao}</div>
            <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
        </div>
        """, unsafe_allow_html=True)

render_card(col1, "Shopee 🛍️", "Achadinhos favoritos.", "https://collshp.com/luhveestores")
render_card(col2, "Mercado Livre 🤝", "Entrega rápida.", "https://www.mercadolivre.com.br/social/axwelloliveira")
render_card(col3, "Internacional 🌎", "Novidades globais.", "https://luhvee-store.systeme.io/prodentim-special")

st.markdown("<br><hr style='border: 0.5px solid #333;'><br>", unsafe_allow_html=True)

# 5. RODAPÉ E REDES SOCIAIS
st.markdown("<h3 style='text-align: center; color: #9370DB;'>Não esquece de nos seguir, fique por dentro das melhores promoções ❤️</h3>", unsafe_allow_html=True)

# Redes sociais em botões
c1, c2, c3, c4 = st.columns(4)
c1.link_button("Insta 📸", "https://instagram.com/luhveestore", use_container_width=True)
c2.link_button("TikTok ♪", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
c3.link_button("Telegram ✈️", "https://t.me/luhveestores", use_container_width=True)
c4.link_button("Grupo VIP 💬", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
# SUPORTE DESTAQUE
st.link_button("💖 Fale com a Luh da Luhvee 💖", "https://wa.me/5511948021428", type="primary", use_container_width=True)

st.markdown("<p style='text-align: center; opacity: 0.5; margin-top: 50px;'>Feito com amor por Luhvee Stores ✨</p>", unsafe_allow_html=True)
