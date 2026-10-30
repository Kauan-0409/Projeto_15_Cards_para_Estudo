# Study Cards

Aplicação desenvolvida em **Python** e **Streamlit** para criar,
carregar e estudar cards de perguntas e respostas. O projeto utiliza
inteligência artificial por meio da API da **Groq** para gerar perguntas
e respostas automaticamente a partir de um tema.

## Funcionalidades

-   **Página inicial:** apresenta o funcionamento da aplicação e orienta
    o usuário.
-   **Meus Cards:** permite carregar arquivos `.json` com perguntas e
    respostas e estudar usando cards interativos.
-   **Gerar Cards com IA:** recebe um tema e solicita à IA a criação de
    10 perguntas e respostas didáticas.
-   **Salvar cards:** permite baixar o conjunto gerado em um arquivo
    `.json`, para reutilização na página Meus Cards.

## Tecnologias utilizadas

-   Python
-   Streamlit
-   Groq API
-   `python-dotenv`
-   JSON
-   HTML e CSS

## Estrutura do projeto

``` text
PROJETO_15_GERADOR_CARDS/
│
├── pages/
│   ├── 01_Cards.py
│   └── 02_Gerar_Cards_com_IA.py
│
├── .env
├── card.html
├── gerador.py
├── Inicio.py
├── requirements.txt
└── style.txt
```

### Principais arquivos

  -----------------------------------------------------------------------
  Arquivo                             Responsabilidade
  ----------------------------------- -----------------------------------
  `Inicio.py`                         Página inicial e apresentação da
                                      aplicação.

  `pages/01_Cards.py`                 Carrega arquivos JSON e apresenta
                                      os cards para estudo.

  `pages/02_Gerar_Cards_com_IA.py`    Interface para informar um tema,
                                      gerar perguntas e respostas e
                                      baixar o resultado.

  `gerador.py`                        Classe responsável por se comunicar
                                      com a API da Groq e processar a
                                      resposta da IA.

  `style.txt`                         Estilos CSS utilizados na
                                      apresentação dos cards.

  `card.html`                         Arquivo HTML relacionado ao layout
                                      dos cards.

  `requirements.txt`                  Lista de dependências Python do
                                      projeto.

  `.env`                              Armazena a chave de acesso à API da
                                      Groq.
  -----------------------------------------------------------------------

> **Atenção:** não compartilhe o arquivo `.env` nem publique sua chave
> de API no GitHub. Inclua `.env` no `.gitignore`.

## Como funciona

### 1. Página inicial

A página `Inicio.py` apresenta a proposta do Study Cards e explica as
formas de utilizar a aplicação.

### 2. Gerar cards com IA

Na página **Gerar Cards com IA**:

1.  Informe um tema no campo de texto.
2.  Clique em **Gerar cards**.
3.  A aplicação envia uma instrução para a API da Groq.
4.  O modelo retorna perguntas e respostas em formato JSON.
5.  A aplicação apresenta o conteúdo para conferência.
6.  Utilize **Salvar Arquivo** para baixar os cards em `.json`.

O gerador foi configurado para solicitar 10 pares de pergunta e
resposta. As perguntas devem ter formato semelhante ao de questões de
prova, e as respostas devem ser didáticas.

### 3. Estudar com cards

Na página **Meus Cards**:

1.  Selecione um arquivo `.json`.
2.  Clique em **Carregar**.
3.  Uma pergunta é escolhida aleatoriamente.
4.  Interaja com o card para visualizar a resposta.
5.  Clique em **Outra Pergunta** para selecionar outra questão.

## Formato dos arquivos JSON

Os arquivos de cards utilizam um objeto JSON no qual cada chave é uma
pergunta e seu respectivo valor é a resposta.

Exemplo:

``` json
{
    "O que é uma variável em Python?": "Uma variável é um nome utilizado para armazenar e acessar um valor durante a execução do programa.",
    "Qual é a diferença entre uma lista e uma tupla?": "Uma lista é mutável, enquanto uma tupla não permite alterações após sua criação."
}
```

Você também pode criar seus próprios arquivos seguindo essa estrutura e
carregá-los na aplicação.

## Requisitos

-   Python instalado.
-   Uma chave de API da Groq.
-   Dependências listadas em `requirements.txt`.

## Configuração do ambiente

### 1. Clone o repositório

``` bash
git clone URL_DO_REPOSITORIO
cd PROJETO_15_GERADOR_CARDS
```

Substitua `URL_DO_REPOSITORIO` pelo endereço do repositório Git.

### 2. Crie e ative um ambiente virtual

**Windows (PowerShell):**

``` powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

``` bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` ainda não contenha todas as
bibliotecas utilizadas, instale:

``` bash
pip install streamlit groq python-dotenv
```

### 4. Configure a chave da Groq

Crie um arquivo `.env` na raiz do projeto e adicione:

``` env
GROQ_API_KEY=sua_chave_de_api
```

Obtenha sua chave na plataforma da Groq: https://console.groq.com/keys

Não coloque aspas em torno da chave, a menos que sua configuração exija
isso.

## Como executar

Na raiz do projeto, com o ambiente virtual ativado, execute:

``` bash
streamlit run Inicio.py
```

O Streamlit iniciará a aplicação e exibirá o endereço local no terminal.
Normalmente, a aplicação poderá ser acessada em:

``` text
http://localhost:8501
```

## Modelo de inteligência artificial

A aplicação instancia o gerador com o identificador de modelo:

``` python
Gerador("openai/gpt-oss-120b")
```

Esse identificador é enviado à API da Groq por meio do método
`chat.completions.create()`. A disponibilidade dos modelos pode mudar;
consulte a documentação da Groq caso seja necessário trocar o modelo.

## Observações importantes

-   As respostas são geradas por inteligência artificial e podem conter
    erros. Revise o material antes de utilizá-lo como referência de
    estudo.
-   A geração de cards depende de conexão com a internet e de uma chave
    válida da Groq.
-   Os cards são armazenados localmente pelo usuário em arquivos JSON. O
    projeto apresentado não implementa banco de dados ou sincronização
    entre dispositivos.
-   O arquivo `.env` deve permanecer privado.
-   O nome do arquivo JSON pode ser escolhido no momento do download.

## Possíveis melhorias

-   Permitir gerar cards a partir de um texto ou arquivo enviado pelo
    usuário.
-   Adicionar edição das perguntas e respostas antes do download.
-   Evitar a repetição da pergunta atual ao selecionar outra
    aleatoriamente.
-   Adicionar categorias, níveis de dificuldade e tags.
-   Registrar o histórico de estudo e o desempenho do usuário.
-   Implementar um sistema de revisão espaçada.
-   Armazenar os cards em um banco de dados para acesso em diferentes
    dispositivos.
-   Validar a estrutura do JSON e tratar respostas inválidas da API com
    mensagens específicas.

## Licença

Defina aqui a licença de distribuição do projeto, caso ele seja
publicado ou compartilhado.
