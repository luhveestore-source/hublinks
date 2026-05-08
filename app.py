import streamlit as st

# Configuração da página
st.set_page_config(page_title="Luhvee Stores | Hub", page_icon="🛍️")

# Estilo Personalizado (Cores: Preto, Rosa, Lilás e Dourado)
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        color: #FFFFFF;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #FF69B4; /* Rosa */
        color: white;
        border: 2px solid #D4AF37; /* Dourado */
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #9370DB; /* Lilás */
        border: 2px solid #FFFFFF;
    }
    h1, h2, h3 {
        color: #D4AF37 !important; /* Dourado */
        text-align: center;
    }
    .motivos-box {
        background-color: #1A1A1A;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #9370DB;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho
st.title("Luhvee Stores")
st.subheader("Curadoria & Estilo por Luana Avelino")

# 1. Os 3 Motivos para escolher a Luhvee (Organizado e Clean)
with st.container():
    st.markdown('<div class="motivos-box">', unsafe_allow_html=True)
    st.markdown("### ✨ Por que a Luhvee Stores?")
    st.write("💎 **Curadoria Especialista:** Selecionamos a dedo os melhores achadinhos da Shopee, Shein e Mercado Livre. O ouro chega até você.")
    st.write("🚚 **Logística Sem Fronteiras:** Entrega rápida e segura para absolutamente qualquer lugar do Brasil.")
    st.write("💰 **Estilo que Cabe no Bolso:** Tendência das passarelas com a economia que você ama.")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. Botões de Links (Ajustados com seus links atuais)
st.markdown("### 🔗 Nossos Canais")

if st.button("👠 Catálogo de Calçados (Shopintegra)"):
    st.write("Redirecionando... https://www.shopintegra.com.br/catalogo/luhvee-stores-shoes")

if st.button("🛍️ Vitrine Shopee (Achadinhos)"):
    st.write("Redirecionando... https://collshp.com/luhveestores?view=storefront")

if st.button("📢 Grupo VIP de Ofertas (WhatsApp)"):
    st.write("Redirecionando... https://chat.whatsapp.com/IBneTrHJemMLla4wzU8Wbj")

if st.button("📸 Siga no Instagram @luhveestore"):
    st.write("Redirecionando... https://instagram.com/luhveestore")

# Rodapé com a mensagem formulada
st.markdown("---")
st.markdown("""
**Oi! Que bom ter você aqui!** 🛍️  
Nosso trabalho é garimpar o melhor em estilo e economia para você.  
*Entregamos em todo o Brasil com o cuidado que você merece.* **Bjs da Luh ❤️🖤✨**
""")
