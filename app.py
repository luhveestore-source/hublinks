import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="🛍️",
    layout="wide"
)

# 2. CSS COMPLETO (FOCO EM CENTRALIZAÇÃO E DESIGN)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }

    /* Centralização Absoluta do Logo e Títulos */
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }

    /* Título ✨ Luhvee Stores ✨ */
    .main-title {
        color: #FF69B4;
        font-size: 2.8rem;
        font-weight: bold;
        text-shadow: 2px 2px #9370DB;
        margin-top: 10px;
    }

    /* Texto de Boas-vindas */
    .welcome-text {
        color: #E6E6FA;
        font-size: 1.1rem;
        margin-bottom: 30px;
        max-width: 700px;
    }

    /* Cards de Links (Shopee, etc) */
    .link-card {
        background: linear-gradient(145deg, #1a1a1a, #2b1a2b);
        border: 2px solid #d4af37;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }

    .btn-acessar {
        background-color: #FF69B4 !important;
        color: white !important;
        text-decoration: none;
        font-weight: bold;
        padding: 10px 20px;
        width: 90%;
        border-radius: 50px;
        display: block;
    }

    /* Cards de Benefícios (Por que comprar...) */
    .benefit-card {
        background-color: #151515;
        border: 1px solid #333;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        height: 100%;
    }

    .benefit-icon {
        font-size: 2rem;
        margin-bottom: 10px;
    }

    /* Forçar Centralização da Imagem do Streamlit */
    [data-testid="stImage"] > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO CENTRALIZADO
st.markdown("<div class='center-container'>", unsafe_allow_html=True)

# Logo
try:
    st.image("1000396187.jpeg", width=300)
except:
    st.markdown("## ✨ LUHVEE STORES ✨")

st.markdown("<div class='main-title'>✨ Luhvee Stores ✨</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='welcome-text'>
        <b>Bem-vindo ao seu paraíso de compras!</b><br>
        Encontre tudo o que você precisa em um único lugar.<br>
        Desde produtos incríveis até conteúdos exclusivos, a Luhvee Stores reúne as melhores oportunidades para você! 🛒🎁
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 4. CARDS DE LINKS PRINCIPAIS
col1, col2, col3 = st.columns(3)

def render_link(col, titulo, desc, url):
    with col:
        st.markdown(f"""
        <div class="link-card">
            <div>
                <div style="color: #d4af37; font-size: 1.4rem; font-weight: bold;">{titulo}</div>
                <div style="color: #b0b0b0; font-size: 0.9rem; margin-top: 10px;">{desc}</div>
            </div>
            <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
        </div>
        """, unsafe_allow_html=True)

render_link(col1, "Shopee 🛍️", "Achadinhos favoritos.", "https://collshp.com/luhveestores")
render_link(col2, "Mercado Livre 🤝", "Entrega rápida.", "https://www.mercadolivre.com.br/social/axwelloliveira")
render_link(col3, "Internacional 🌎", "Novidades globais.", "https://luhvee-store.systeme.io/prodentim-special")

st.write("<br>", unsafe_allow_html=True)

# 5. NOVA SEÇÃO: POR QUE COMPRAR CONOSCO?
st.markdown("<h2 style='text-align: center; color: #d4af37;'>Por que comprar através da Luhvee Stores?</h2>", unsafe_allow_html=True)

b_col1, b_col2, b_col3 = st.columns(3)

with b_col1:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">✨</div>
        <div style="font-weight: bold; color: #FF69B4;">Melhor Seleção</div>
        <div style="font-size: 0.85rem; color: #b0b0b0;">Acesso a produtos de qualidade das melhores plataformas</div>
    </div>
    """, unsafe_allow_html=True)

with b_col2:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">🛡️</div>
        <div style="font-weight: bold; color: #FF69B4;">Segurança</div>
        <div style="font-size: 0.85rem; color: #b0b0b0;">Compre com confiança em plataformas verificadas</div>
    </div>
    """, unsafe_allow_html=True)

with b_col3:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">💰</div>
        <div style="font-weight: bold; color: #FF69B4;">Melhores Preços</div>
        <div style="font-size: 0.85rem; color: #b0b0b0;">Encontre as melhores ofertas e promoções</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><hr style='border: 0.1px solid #333;'><br>", unsafe_allow_html=True)

# 6. RODAPÉ E REDES SOCIAIS
st.markdown("<h3 style='text-align: center; color: #9370DB; font-size: 1.2rem;'>Não esquece de nos seguir, fique por dentro das melhores promoções ❤️</h3>", unsafe_allow_html=True)

# Botões de Redes Sociais
s_col1, s_col2, s_col3, s_col4 = st.columns(4)
s_col1.link_button("Insta 📸", "https://instagram.com/luhveestore", use_container_width=True)
s_col2.link_button("TikTok ♪", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
s_col3.link_button("Telegram ✈️", "https://t.me/luhveestores", use_container_width=True)
s_col4.link_button("Grupo VIP 💬", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
st.link_button("💖 Fale com a Luh da Luhvee 💖", "https://wa.me/5511948021428", type="primary", use_container_width=True)
