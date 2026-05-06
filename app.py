import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | ✨",
    page_icon="💖",
    layout="centered"
)

# 2. DOCUMENTAÇÃO DO CSS (ESTILO VISUAL)
# Definimos o fundo preto, cores rosa (#FF69B4) e lilás (#9370DB)
st.markdown("""
    <style>
    .stApp { background-color: #0e0e0e; color: white; }
    .stMainBlockContainer { display: flex; flex-direction: column; align-items: center; text-align: center; }
    .main-title {
        color: #FF69B4; font-size: 2.2rem; font-weight: bold;
        text-shadow: 2px 2px #9370DB; margin: 10px 0;
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
    .link-card:hover { border-color: #9370DB; transform: scale(1.02); }
    .btn-acessar {
        background-color: #FF69B4 !important; color: white !important;
        text-decoration: none; font-weight: bold; padding: 10px 20px;
        border-radius: 50px; font-size: 0.8rem; margin-top: 15px; display: inline-block;
    }
    .about-box {
        background-color: #1a1a1a; border: 1px solid #9370DB; 
        border-radius: 15px; padding: 25px; margin-top: 40px; color: #E6E6FA; 
    }
    div.stButton > button { background-color: #9370DB !important; color: white !important; border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO
# Nota: Certifique-se de que o arquivo da imagem está na mesma pasta.
st.image("1000396187.jpeg", width=180) 
st.markdown("<div class='main-title'>✨ Luhvee Stores ✨</div>", unsafe_allow_html=True)
st.markdown("<p style='color: #E6E6FA;'>Tudo o que você ama em um só lugar! 🛍️</p>", unsafe_allow_html=True)

# 4. FUNÇÃO REUTILIZÁVEL PARA OS CARDS
# Esta função evita repetir código HTML para cada botão novo.
def render_card(col, titulo, url):
    with col:
        st.markdown(f"""
        <div class="link-card">
            <div style="color: #FF69B4; font-size: 1rem; font-weight: bold;">{titulo}</div>
            <a href="{url}" target="_blank" class="btn-acessar">QUERO VER! ✨</a>
        </div>
        """, unsafe_allow_html=True)

# 5. LINHA 1 DE LINKS (3 COLUNAS)
col1, col2, col3 = st.columns(3)
render_card(col1, "Shopee 🛍️", "https://collshp.com/luhveestores")
render_card(col2, "Mercado Livre 🤝", "https://www.mercadolivre.com.br/social/axwelloliveira")
render_card(col3, "Shein ✨", "https://onelink.shein.com/5/5ohy42r5xmbb")

# 6. LINHA 2 DE LINKS (3 COLUNAS) - ATUALIZADO
st.write("") 
col4, col5, col6 = st.columns(3)
# Atualização: Link Shopintegra
render_card(col4, "Catálogo de Calçados 👠", "https://www.shopintegra.com.br/catalogo/luhvee-stores-calcados")
# Atualização: Cartão Digital
render_card(col5, "Cartão Digital 🎫", "https://tuframe.com/luhveestores")
render_card(col6, "Internacional 🌎", "https://luhvee-store.systeme.io/prodentim-special")

st.write("---")

# 7. REDES SOCIAIS E SUPORTE
st.markdown("<p style='text-align: center; color: #FF69B4;'>Não esquece de nos seguir ❤️</p>", unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
s1.link_button("Insta 📸", "https://instagram.com/luhveestore", use_container_width=True)
s2.link_button("TikTok ♪", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
s3.link_button("Telegram ✈️", "https://t.me/luhveestores", use_container_width=True)
s4.link_button("Grupo VIP 💬", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
st.link_button("💖 Fale com a Luh da Luhvee 💖", "https://wa.me/5511948021428", type="primary", use_container_width=True)

# 8. SEÇÃO SOBRE
st.markdown(f"""
    <div class="about-box">
        <h3 style="color: #FF69B4; margin-bottom: 15px;">✨ Quem é a LuhVee Stores? ✨</h3>
        <p>A LuhVee Stores não é só uma loja… é uma <b>experiência 💖</b></p>
        <p>Selecionamos produtos que realmente valem a pena, com ofertas incríveis.</p>
        <p style="color: #FF69B4; font-weight: bold;">Bem-vindo à LuhVee Stores 💕</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='opacity: 0.3; font-size: 0.7rem;'>Luhvee Stores ✨</p>", unsafe_allow_html=True)
