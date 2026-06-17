# HoYoLab Auto Check-In

Um script em Python automatizado, leve e direto para realizar o check-in diário nos jogos da HoYoverse (Genshin Impact, Honkai: Star Rail e Zenless Zone Zero) diretamente pelo terminal.

---

## ✨ Funcionalidades

* **Suporte Multi-Jogo:** Executa o check-in de forma sequencial para Genshin Impact, Honkai: Star Rail e Zenless Zone Zero.
* **Segurança de Credenciais:** Utiliza variáveis de ambiente (`.env`) para garantir que seus tokens sensíveis não fiquem expostos no código.
* **Logs Claros no Terminal:** Exibe mensagens detalhadas indicando sucesso, se o check-in já foi realizado ou se ocorreu algum erro de API.

---

## 🚀 Pré-requisitos

Antes de rodar o script, você precisará ter instalado:

* Python 3.x
* Gerenciador de pacotes `pip`

---

## 📦 Instalação e Configuração

1. **Clone o repositório:**

   ```bash
   git clone [https://github.com/MOBSAD/HoyoCheck.git](https://github.com/MOBSAD/HoyoCheck.git)
   ```

   ```bash
   cd HoyoCheck
   ```

2. **Instale as dependências:**

  Recomendo que gere um ambiente virtual com python3 -m venv
   ```bash
   
   python3 -m venv ../HoyoCheck/
   source bin/activate
   pip install -r requirements.txt
   ```

3. **Configure as Variáveis de Ambiente:**

   Crie um arquivo chamado `.env` na raiz do projeto e adicione os seus cookies obtidos no site do HoYoLab:
   
   ```env
   LTOKEN_V2="seu_ltoken_v2_aqui"
   LTUID_V2="seu_ltuid_v2_aqui"
   ```

---

## 🔑 Como Obter seus Cookies (`ltoken_v2` e `ltuid_v2`)

   1. Acesse o site do [HoYoLab](https://www.hoyolab.com/) e faça login na sua conta.
   2. Abra o painel de **Ferramentas do Desenvolvedor** do seu navegador (pressione `F12` ou `Ctrl + Shift + I`).
   3. Navegue até a aba **Application** (Aplicativo) ou **Storage** (Armazenamento) e clique na seção **Cookies**.
   4. Selecione a URL do HoYoLab e busque pelas chaves `ltoken_v2` e `ltuid_v2` na tabela.
   5. Copie os respectivos valores e cole-os no seu arquivo `.env`.

---

## 🛠️ Como Executar

   Com tudo configurado, basta rodar o comando abaixo no seu terminal para executar o check-in:

   ```bash
   python main.py
   ```

---

### Exemplo esperado de Saída no Terminal:

   ```text
   [ CHECK-IN AUTOMATICO HOYOLAB INICIADO ]

   [ INFO ] - [Genshin Impact]: Check-in realizado com sucesso!
   [ INFO ] - [Honkai: Star Rail]: Você já realizou o check-in de hoje.
   [ INFO ] - [Zenless Zone Zero]: Check-in realizado com sucesso!
   ```

---

Esse Readme.md tal como o .gitignore foram criados com auxílio de inteligência artificial, as informações foram revisadas e testadas antes durante e após o envio do conteúdo. 18/06/2026
