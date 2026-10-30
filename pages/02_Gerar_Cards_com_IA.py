import streamlit as st
from gerador import Gerador
import json


# ============================================================
# CONFIGURAÇÕES INICIAIS
# ============================================================

st.set_page_config(
    page_title="Gerador de Cards",
    page_icon="🧠"
)

gerador = Gerador("openai/gpt-oss-120b")


# ============================================================
# INTERFACE
# ============================================================

st.markdown("""
# ✨ Gerar Cards com IA

Digite um tema e a IA cria cards de perguntas e respostas para você estudar.

**Exemplos de temas:**
- Revolução Francesa
- Fundamentos de Python
- Anatomia do coração
- Verbos irregulares em inglês

> 💡 **Dica:** quanto mais específico o tema, melhores os cards. Em vez de "História", tente "Causas da Primeira Guerra Mundial".

> ℹ️ Os cards são gerados por IA. Vale conferir as respostas, principalmente em assuntos importantes.
""")

tema = st.text_input("Digite o tema escolhido")


# ============================================================
# GERAR CARDS
# ============================================================

if st.button("Gerar cards") and tema:
    try:
        resultado = gerador.gerar_perguntas(tema)

        if not isinstance(resultado, dict) or not resultado:
            st.session_state["dados"] = None
            st.warning("A IA não retornou cards válidos. Tente outro tema.")
        else:
            st.session_state["dados"] = resultado

            # Esconde novamente as respostas dos cards recém-gerados
            for chave in list(st.session_state.keys()):
                if chave.startswith("resposta_visivel_"):
                    del st.session_state[chave]

    except Exception as e:
        st.session_state["dados"] = None
        st.warning(f"Erro: {e}")


# ============================================================
# EXIBIR PERGUNTAS E REVELAR RESPOSTAS
# ============================================================

dados = st.session_state.get("dados")

if dados:
    st.markdown("""
    ## ✅ Seus cards estão prontos!

    As perguntas aparecem primeiro. Clique em **Revelar resposta** quando quiser conferir cada uma.

    Quando estiver satisfeito, baixe o arquivo e carregue-o na página **📚 Cards** para estudar.
    """)

    for i, (pergunta, resposta) in enumerate(dados.items()):
        st.markdown(f"### Pergunta {i + 1}")
        st.markdown(f"**{pergunta}**")

        chave_resposta = f"resposta_visivel_{i}"

        if not st.session_state.get(chave_resposta, False):
            if st.button("Revelar resposta", key=f"botao_revelar_{i}"):
                st.session_state[chave_resposta] = True
                st.rerun()
        else:
            st.markdown("**Resposta:**")
            st.write(resposta)

        st.markdown("---")


    # ========================================================
    # DOWNLOAD
    # ========================================================

    with st.popover("Salvar Arquivo"):
        nome_arquivo = st.text_input("Nome do Arquivo").replace(" ", "_")

        st.write(f"{nome_arquivo or 'cards'}.json")

        st.download_button(
            label="Download",
            data=json.dumps(
                dados,
                indent=4,
                ensure_ascii=False
            ),
            file_name=f"{nome_arquivo or 'cards'}.json",
            mime="application/json",
            icon=":material/download:",
            width=600
        )