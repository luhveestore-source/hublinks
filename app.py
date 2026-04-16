import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="🛍️",
    layout="wide" # Layout wide ajuda a distribuir melhor os elementos
)

# 2. CSS PARA PROPORÇÃO E CENTRALIZAÇÃO TOTAL
st.markdown("""
    <style>
    /* Fundo e Texto Base */
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }

    /* Forçar centralização de tudo */
    .stMainBlockContainer {
        max-width: 900px;
        margin: auto;
    }

    /* Centralização de Imagens do Streamlit */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    /* Estilo do Título ✨ Luhvee Stores ✨ */
    .main-title {
        color: #FF69B4; /* Rosa */
        font-size: 2.8rem;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px #9370DB; /* Sombra Lilás */
        margin-bottom: 10px;
    }

    /* Texto de Boas-vindas centralizado */
    .welcome-text {
        color: #E6E6FA;
        text-align: center;
        font-size: 1.1rem;
        line-height: 1.6;
        margin-bottom: 40px;
    }

    /* Cartões Proporcionais */
    .link-card {
        background: linear-gradient(145deg, #1a1a1a, #2b1a2b);
        border: 2px solid #d4af37; /* Dourado */
        border-radius: 20px;
        padding: 30px 20px;
        text-align: center;
        min-height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        margin: 10px 0;
    }

    .card-title {
        color: #d4af37;
        font-size: 1.5rem;
        font-weight: bold;
    }

    /* Botão Rosa "QUERO VER" - Estilo Capturar.JPG */
    .btn-acessar {
        background-color: #FF69B4 !important;
        color: white !important;
        text-decoration: none;
        font-weight: bold;
        padding: 12px 0;
        width: 85%;
        border-radius: 50px;
        font-size: 1rem;
        display: block;
        transition: 0.3s;
        box-shadow: 0px 4px 10px rgba(255, 105, 180, 0.3);
    }
    
    .btn-acessar:hover {
        transform: scale(1.05);
        background-color: #ff85c2 !important;
    }

    /* Centralização das Colunas de Redes Sociais */
    div[data-testid="stHorizontalBlock"] {
        align-items: center;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO CENTRALIZADO
# Logo com tamanho proporcional (300px é o ideal para não ocupar a tela toda)
try:
    st.image("1000396187.jpeg", width=300)
except:
    st.markdown("<h2 style='text-align: center;'>Luhvee Stores</h2>", unsafe_allow_html=True)

st.markdown("<div class='main-title'>✨ Luhvee Stores ✨</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='welcome-text'>
        <b>Bem-vindo ao seu paraíso de compras!</b><br>
        Encontre tudo o que você precisa em um único lugar.<br>
        Desde produtos incríveis até conteúdos exclusivos, a Luhvee Stores reúne as melhores oportunidades para você! 🛒🎁
    </div>
    """, unsafe_allow_html=True)

# 4. CARDS DE LINKS EM COLUNAS
col1, col2, col3 = st.columns(3)

def render_card(col, titulo, descricao, url):
    with col:
        st.markdown(f"""
        <div class="link-card">
            <div>
                <div class="card-title">{titulo}</div>
                <div style="color: #b0b0b0; font-size: 0.9rem; margin-top: 10px;">{descricao}</div>
            </div>
            <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
        </div>
        """, unsafe_allow_html=True)

render_card(col1, "Shopee 🛍️", "Meus achadinhos favoritos.", "https://collshp.com/luhveestores")
render_card(col2, "Mercado Livre 🤝", "Produtos com entrega rápida.", "https://www.mercadolivre.com.br/social/axwelloliveira")
render_card(col3, "Internacional 🌎", "Novidades e conteúdos globais.", "https://luhvee-store.systeme.io/prodentim-special")

st.markdown("<br><hr style='border: 0.1px solid #333;'><br>", unsafe_allow_html=True)

# 5. REDES SOCIAIS E SUPORTE
st.markdown("<h3 style='text-align: center; color: #9370DB; font-size: 1.2rem;'>Não esquece de nos seguir, fique por dentro das melhores promoções ❤️</h3>", unsafe_allow_html=True)

# Botões de Redes Sociais
social_col1, social_col2, social_col3, social_col4 = st.columns(4)
social_col1.link_button("Insta 📸", "https://instagram.com/luhveestore", use_container_width=True)
social_col2.link_button("TikTok ♪", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
social_col3.link_button("Telegram ✈️", "https://t.me/luhveestores", use_container_width=True)
social_col4.link_button("Grupo VIP 💬", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
# Botão de Suporte Principal
st.link_button("💖 Fale com a Luh da Luhvee 💖", "https://wa.me/5511948021428", type="primary", use_container_width=True)

st.markdown("<br><p style='text-align: center; opacity: 0.5; font-size: 0.8rem;'>Feito com amor por Luhvee Stores ✨</p>", unsafe_allow_html=True)
