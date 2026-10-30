import streamlit as st
from gerador import Gerador
import json
from random import choice


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

        st.session_state["dados"] = resultado


    except Exception as e:
        st.session_state["dados"] = None
        st.warning(f'Erro: {e}')


# ============================================================
# EXIBIR Perguntas
# ============================================================

try:
    if st.session_state["dados"]:
        st.markdown("""
        ## ✅ Seus cards estão prontos!

        Confira as perguntas e respostas abaixo antes de estudar. Como foram geradas por IA, vale verificar se estão corretas.

        Quando estiver satisfeito, baixe o arquivo e carregue-o na página **📚 Cards** para começar a estudar.
        """)
        # st.write(st.session_state["dados"])
        for i,kv in enumerate(st.session_state["dados"].items()):
            st.markdown(f"# Pergunta {i+1}")
            st.markdown(f"### {kv[0]}")
            st.markdown(f'- Resposta: {kv[1]}')
            st.markdown('---')


        # ========================================================
        # DOWNLOAD
        # ========================================================

        with st.popover("Salvar Arquivo"):

            nome_arquivo = st.text_input(
                "Nome do Arquivo"
            ).replace(' ', '_')
            st.write(f'{nome_arquivo}.json')
            st.download_button(
                label="Download",

                data=json.dumps(
                    st.session_state["dados"],
                    indent=4,
                    ensure_ascii=False
                ),

                file_name=f"{nome_arquivo}.json",

                mime="application/json",

                icon=":material/download:",

                width=600
            )
except:
    pass