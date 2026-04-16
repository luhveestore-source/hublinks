import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="🛍️",
    layout="centered"
)

# 2. CSS PARA DESIGN E CENTRALIZAÇÃO
st.markdown("""
    <style>
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }

    /* Centralização Absoluta */
    .stMainBlockContainer {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }

    /* Título Principal */
    .main-title {
        color: #FF69B4;
        font-size: 2.2rem;
        font-weight: bold;
        text-shadow: 2px 2px #9370DB;
        margin: 10px 0;
    }

    /* Seção "Quem é a Luhvee" */
    .about-section {
        background: rgba(147, 112, 219, 0.1); /* Fundo lilás bem suave */
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid #FF69B4;
        text-align: center;
        line-height: 1.6;
    }

    /* Cards de Links */
    .link-card {
        background: linear-gradient(145deg, #1a1a1a, #2b1a2b);
        border: 2px solid #d4af37;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        min-height: 200px;
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
        padding: 10px 25px;
        border-radius: 50px;
        font-size: 0.9rem;
        display: block;
        margin-top: 15px;
    }

    /* Estilo para a lista de benefícios no "Quem é" */
    .about-list {
        list-style: none;
        padding: 0;
        margin: 15px 0;
        text-align: left;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO (LOGO DIMINUÍDO)
st.image("1000396187.jpeg", width=200) # Tamanho reduzido para 200px

st.markdown("<div class='main-title'>✨ Luhvee Stores ✨</div>", unsafe_allow_html=True)

st.markdown("""
    <div style='color: #E6E6FA; font-size: 1.1rem; margin-bottom: 20px;'>
        <b>Bem-vindo ao seu paraíso de compras!</b>
    </div>
    """, unsafe_allow_html=True)

# 4. SEÇÃO QUEM É A LUHVEE (NOVO)
st.markdown(f"""
    <div class="about-section">
        <h2 style="color: #FF69B4;">✨ Quem é a LuhVee Stores? ✨</h2>
        <p>A LuhVee Stores não é só uma loja… <b>é uma experiência 💖</b></p>
        <p>Aqui, a gente vive de descobrir os melhores achadinhos da internet e transformar isso em praticidade, economia e estilo pra você.</p>
        <div style="text-align: center;">
            <ul class="about-list">
                <li>🛍️ Selecionamos produtos que realmente valem a pena</li>
                <li>💸 Ofertas que cabem no seu bolso</li>
                <li>🔥 Tendências que estão bombando</li>
                <li>💡 Dicas inteligentes pra facilitar sua vida</li>
            </ul>
        </div>
        <p>Tudo isso com um único objetivo:<br>
        <b>👉 te ajudar a comprar melhor, gastar menos e ainda se sentir incrível com suas escolhas.</b></p>
        <p>A LuhVee é sobre conexão. É sobre entender o que você quer antes mesmo de você procurar.</p>
        <p>💬 Aqui tem dica, tem promoção, tem novidade…<br>
        Mas acima de tudo, tem cuidado em cada indicação.</p>
        <p>🚀 Se você ama praticidade, economia e achadinhos incríveis… você está no lugar certo.</p>
        <h3 style="color: #FF69B4;">Bem-vindo à LuhVee Stores 💕</h3>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# 5. CARDS DE LINKS
col1, col2, col3 = st.columns(3)

def render_link(col, titulo, url):
    with col:
        st.markdown(f"""
        <div class="link-card">
            <div style="color: #d4af37; font-size: 1.3rem; font-weight: bold;">{titulo}</div>
            <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
        </div>
        """, unsafe_allow_html=True)

render_link(col1, "Shopee 🛍️", "https://collshp.com/luhveestores")
render_link(col2, "Mercado Livre 🤝", "https://www.mercadolivre.com.br/social/axwelloliveira")
render_link(col3, "Internacional 🌎", "https://luhvee-store.systeme.io/prodentim-special")

st.write("---")

# 6. POR QUE COMPRAR? (RESUMO)
st.markdown("<h3 style='text-align: center; color: #d4af37;'>Por que comprar conosco?</h3>", unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1:
    st.markdown('<div style="text-align:center;">✨<br><b>Melhor Seleção</b></div>', unsafe_allow_html=True)
with b2:
    st.markdown('<div style="text-align:center;">🛡️<br><b>Segurança</b></div>', unsafe_allow_html=True)
with b3:
    st.markdown('<div style="text-align:center;">💰<br><b>Melhores Preços</b></div>', unsafe_allow_html=True)

st.write("---")

# 7. REDES E SUPORTE
st.markdown("<p style='text-align: center; color: #9370DB;'>Não esquece de nos seguir ❤️</p>", unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
s1.link_button("Insta", "https://instagram.com/luhveestore", use_container_width=True)
s2.link_button("TikTok", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
s3.link_button("Telegram", "https://t.me/luhveestores", use_container_width=True)
s4.link_button("Grupo VIP", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
st.link_button("💖 Fale com a Luh da Luhvee 💖", "https://wa.me/5511948021428", type="primary", use_container_width=True)