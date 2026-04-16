import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="🛍️",
    layout="centered" # Mantém o conteúdo focado no meio
)

# 2. CSS DEFINITIVO (CENTRALIZAÇÃO TOTAL)
st.markdown("""
    <style>
    /* Reset de fundo */
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }

    /* Forçar centralização de todos os blocos do Streamlit */
    .stMainBlockContainer {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    /* Logo Centralizado */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    /* Título ✨ Luhvee Stores ✨ */
    .main-title {
        color: #FF69B4;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px #9370DB;
        width: 100%;
        margin: 10px 0;
    }

    /* Texto de Boas-vindas */
    .welcome-text {
        color: #E6E6FA;
        text-align: center;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 30px;
    }

    /* Cards de Links (Proporção Capturar.JPG) */
    .link-card {
        background: linear-gradient(145deg, #1a1a1a, #2b1a2b);
        border: 2px solid #d4af37;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px;
    }

    .btn-acessar {
        background-color: #FF69B4 !important;
        color: white !important;
        text-decoration: none;
        font-weight: bold;
        padding: 10px 0;
        width: 100%;
        border-radius: 50px;
        font-size: 0.9rem;
        text-align: center;
        display: block;
    }

    /* Cards de Benefícios */
    .benefit-card {
        background-color: #151515;
        border: 1px solid #333;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Ajuste de colunas no telemóvel */
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 calc(33.333% - 1rem) !important;
        min-width: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO
try:
    # Aumentei um pouco para 350px para dar destaque
    st.image("1000396187.jpeg", width=350)
except:
    st.markdown("## 🛍️ LUHVEE STORES")

st.markdown("<div class='main-title'>✨ Luhvee Stores ✨</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='welcome-text'>
        <b>Bem-vindo ao seu paraíso de compras!</b><br>
        Encontre tudo o que você precisa em um único lugar.<br>
        Desde produtos incríveis até conteúdos exclusivos, a Luhvee Stores reúne as melhores oportunidades para você! 🛒🎁
    </div>
    """, unsafe_allow_html=True)

# 4. CARDS DE PRODUTOS (3 COLUNAS)
c1, c2, c3 = st.columns(3)

def render_card(col, titulo, desc, url):
    with col:
        st.markdown(f"""
        <div class="link-card">
            <div>
                <div style="color: #d4af37; font-size: 1.2rem; font-weight: bold;">{titulo}</div>
                <div style="color: #b0b0b0; font-size: 0.8rem; margin-top: 5px;">{desc}</div>
            </div>
            <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
        </div>
        """, unsafe_allow_html=True)

render_card(c1, "Shopee 🛍️", "Achadinhos favoritos.", "https://collshp.com/luhveestores")
render_card(c2, "Mercado Livre 🤝", "Entrega rápida.", "https://www.mercadolivre.com.br/social/axwelloliveira")
render_card(c3, "Internacional 🌎", "Novidades globais.", "https://luhvee-store.systeme.io/prodentim-special")

st.write("---")

# 5. POR QUE COMPRAR CONOSCO?
st.markdown("<h3 style='text-align: center; color: #d4af37;'>Por que comprar através da Luhvee Stores?</h3>", unsafe_allow_html=True)

b1, b2, b3 = st.columns(3)
with b1:
    st.markdown('<div class="benefit-card">✨<br><b>Melhor Seleção</b><br><small>Produtos de qualidade</small></div>', unsafe_allow_html=True)
with b2:
    st.markdown('<div class="benefit-card">🛡️<br><b>Segurança</b><br><small>Plataformas verificadas</small></div>', unsafe_allow_html=True)
with b3:
    st.markdown('<div class="benefit-card">💰<br><b>Melhores Preços</b><br><small>Ofertas e promoções</small></div>', unsafe_allow_html=True)

st.write("---")

# 6. REDES SOCIAIS E SUPORTE
st.markdown("<p style='text-align: center; color: #9370DB;'>Não esquece de nos seguir, fique por dentro das melhores promoções ❤️</p>", unsafe_allow_html=True)

# Botões de Redes
s1, s2, s3, s4 = st.columns(4)
s1.link_button("Insta 📸", "https://instagram.com/luhveestore", use_container_width=True)
s2.link_button("TikTok ♪", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
s3.link_button("Telegram ✈️", "https://t.me/luhveestores", use_container_width=True)
s4.link_button("Grupo VIP 💬", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
st.link_button("💖 Fale com a Luh da Luhvee 💖", "https://wa.me/5511948021428", type="primary", use_container_width=True)
