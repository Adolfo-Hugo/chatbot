# HugoChatB0t - Chatbot Interativo

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

HugoChatB0t é um chatbot interativo desenvolvido com Streamlit que utiliza a API do OpenRouter para gerar respostas inteligentes às mensagens dos usuários.

## Funcionalidades

- Interface limpa e intuitiva
- Histórico de conversa persistente durante a sessão
- Integração com o modelo deepseek/deepseek-r1:free via OpenRouter API
- Design responsivo e centralizado

## Pré-requisitos

- Python 3.7+
- Conta no [OpenRouter](https://openrouter.ai/) para obter uma API key

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/hugochatbot.git
cd hugochatbot
```

2. Crie e ative um ambiente virtual (opcional mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

1. Renomeie o arquivo `.env.example` para `.env` e adicione sua API key do OpenRouter:
```
API_KEY=sua_chave_aqui
```

2. Alternativamente, você pode configurar as secrets diretamente no Streamlit se estiver hospedando lá.

## Uso

Execute o aplicativo com:
```bash
streamlit run app.py
```

O aplicativo será aberto automaticamente no seu navegador padrão.

## Estrutura do Projeto

```
hugochatbot/
├── app.py            # Código principal do aplicativo
├── requirements.txt  # Dependências do projeto
├── .env.example      # Modelo de arquivo de configuração
└── README.md         # Este arquivo
```

## Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) - Framework para criação de aplicativos web com Python
- [OpenRouter API](https://openrouter.ai/) - Plataforma para acessar diversos modelos de LLM
- [Requests](https://docs.python-requests.org/) - Biblioteca para fazer requisições HTTP

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autor

Adolfo Hugo Silva - © 2025 Todos os direitos reservados

---

**Nota**: Este projeto é apenas para fins educacionais e demonstrativos. Certifique-se de seguir os Termos de Serviço do OpenRouter ao utilizá-lo.
