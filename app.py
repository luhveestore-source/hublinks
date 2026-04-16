import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Luhvee Stores | Central de Links",
    page_icon="✨",
    layout="centered"
)

# 2. ESTILO VISUAL (CSS)
st.markdown("""
    <style>
    /* Fundo do aplicativo */
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }
    
    /* Cartões de links principais */
    .link-card {
        background-color: #1a1a1a;
        border: 1px solid #d4af37; /* Dourado */
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        text-align: center;
        transition: 0.4s;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .link-card:hover {
        border-color: #ffffff;
        transform: scale(1.02);
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.3);
    }

    .card-title {
        color: #ffffff;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .card-text {
        color: #b0b0b0;
        font-size: 0.9rem;
        margin-bottom: 20px;
    }

    /* Botão de Acesso dentro do Card */
    .btn-acessar {
        display: inline-block;
        color: #000000 !important;
        background-color: #d4af37;
        text-decoration: none;
        font-weight: bold;
        padding: 8px 20px;
        border-radius: 8px;
        font-size: 0.9rem;
        transition: 0.3s;
    }
    
    .btn-acessar:hover {
        background-color: #ffffff;
    }

    /* Ajuste para o texto central */
    .welcome-text {
        text-align: center;
        color: #a0a0a0;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO (LOGO E BOAS-VINDAS)
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

# Tenta carregar o seu logo. Se o arquivo não estiver na pasta, ele ignora.
try:
    st.image("1000396187.jpeg", width=180)
except:
    st.warning("⚠️ Arquivo de imagem '1000396187.jpeg' não encontrado. Certifique-se de que ele está na mesma pasta do código.")

st.markdown("<h1>✨ Luhvee Stores ✨</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class="welcome-text">
        <b>Bem-vindo ao seu paraíso de compras!</b><br>
        Encontre tudo o que você precisa em um único lugar.<br>
        Desde produtos incríveis até conteúdos exclusivos, a Luhvee Stores reúne as melhores oportunidades para você! 🛒🎁
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 4. FUNÇÃO PARA GERAR OS CARDS
def render_card(titulo, descricao, url):
    st.markdown(f"""
    <div class="link-card">
        <div class="card-title">{titulo}</div>
        <div class="card-text">{descricao}</div>
        <a href="{url}" target="_blank" class="btn-acessar">ACESSAR AGORA ↗</a>
    </div>
    """, unsafe_allow_html=True)

# 5. GRADE DE LINKS (GRID 3 COLUNAS)
col1, col2, col3 = st.columns(3)

with col1:
    render_card("Shopee", "As melhores ofertas e achadinhos selecionados.", "https://collshp.com/luhveestores")

with col2:
    render_card("Mercado Livre", "Visite nossa loja oficial e produtos premium.", "https://www.mercadolivre.com.br/social/axwelloliveira")

with col3:
    render_card("Internacional", "Conteúdos e produtos para o mercado global.", "https://luhvee-store.systeme.io/prodentim-special")

st.divider()

# 6. CONECTE-SE CONOSCO (REDES SOCIAIS)
st.markdown("<h3 style='text-align: center;'>Conecte-se Conosco</h3>", unsafe_allow_html=True)

# Organizando em botões largos para fácil clique no celular
c1, c2 = st.columns(2)
with c1:
    st.link_button("📸 Instagram Oficial", "https://instagram.com/luhveestore", use_container_width=True)
    st.link_button("✈️ Canal Telegram", "https://t.me/luhveestores", use_container_width=True)

with c2:
    st.link_button("📱 TikTok", "https://www.tiktok.com/@luhvee.stores", use_container_width=True)
    st.link_button("👥 Grupo VIP WhatsApp", "https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj", use_container_width=True)

st.write("")
st.link_button("📞 Suporte Direto (Falar com Consultor)", "https://wa.me/5511948021428", type="primary", use_container_width=True)

# 7. RODAPÉ
st.markdown("<br><p style='text-align: center; color: #555;'>© 2024 Luhvee Stores - Todos os direitos reservados.</p>", unsafe_allow_html=True)
