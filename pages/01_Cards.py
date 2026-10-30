import streamlit as st
import json
from random import choice


st.markdown("""
# 📚 Meus Cards

Carregue um arquivo de cards que você já tem e comece a estudar.

**Formato aceito:** arquivo `.json`

> 💡 Ainda não tem um arquivo? Crie seus cards em **✨ Gerar Cards com IA** ou **📄 Gerar Cards com Arquivo**. Os cards gerados podem ser salvos e carregados aqui depois.

""")


arquivo = st.file_uploader("Carregue seu arquivo", type=".json")




# =========================
# CARREGAR ARQUIVO
# =========================

if arquivo is not None and st.button("Carregar"):

    cards = json.load(arquivo)

    st.session_state["dados"] = cards
    st.session_state["carregado"] = True

    # Escolhe a primeira pergunta
    st.session_state["pergunta"] = choice(list(cards.keys()))


# =========================
# EXIBIR CARD
# =========================

if st.session_state.get("carregado", False):

    dados = st.session_state["dados"]
    pergunta = st.session_state["pergunta"]
    resposta = dados[pergunta]

    st.success("Arquivo carregado")

    with open("style.txt", "r", encoding="utf-8") as f:
        estilo = f.read()

    st.markdown(estilo, unsafe_allow_html=True)

    st.html(f"""
    <div class="card">
        <div class="upper-part">
            <div class="upper-part-face">{pergunta}</div>
            <div class="upper-part-back">
                {resposta}
            </div>
        </div>

        <div class="lower-part">
            <div class="lower-part-face">Pergunta</div>
            <div class="lower-part-back">Resposta</div>
        </div>
    </div>
    """)

    if st.button('Outra Pergunta'):
        st.session_state["pergunta"] = choice(list(st.session_state["dados"].keys()))
        st.rerun()
