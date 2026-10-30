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
    try:
        cards = json.load(arquivo)

        if not isinstance(cards, dict) or not cards:
            st.error("O arquivo não contém cards válidos.")
        else:
            st.session_state["dados"] = cards
            st.session_state["carregado"] = True
            st.session_state["pergunta"] = choice(list(cards.keys()))
            st.session_state["mostrar_resposta"] = False

    except (json.JSONDecodeError, UnicodeDecodeError):
        st.error("Não foi possível ler o arquivo. Verifique se é um JSON válido.")


# =========================
# EXIBIR CARD
# =========================

if st.session_state.get("carregado", False):
    dados = st.session_state["dados"]
    pergunta = st.session_state["pergunta"]
    resposta = dados[pergunta]

    st.success("Arquivo carregado")

    st.markdown("## Pergunta")
    st.markdown(f"### {pergunta}")

    if not st.session_state.get("mostrar_resposta", False):
        if st.button("Revelar resposta", use_container_width=True):
            st.session_state["mostrar_resposta"] = True
            st.rerun()
    else:
        st.markdown("## Resposta")
        st.markdown(str(resposta))

    if st.button("Outra Pergunta", use_container_width=True):
        perguntas = list(dados.keys())
        if len(perguntas) > 1:
            perguntas.remove(pergunta)

        st.session_state["pergunta"] = choice(perguntas)
        st.session_state["mostrar_resposta"] = False
        st.rerun()
