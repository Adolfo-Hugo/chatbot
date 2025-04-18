import streamlit as st
import requests
import json
api_key = st.secrets["API_KEY"] 

st.set_page_config(page_title="Chatbot Interativo", layout="centered")

st.title("HugoB0t")


api_key = f'{api_key}'  


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


prompt = st.chat_input("Digite sua mensagem:")
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>© 2025 Adolfo Hugo Silva | Todos os direitos reservados</p>", unsafe_allow_html=True)

if prompt:
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )


    if response.status_code == 200:
        resposta_json = response.json()
        conteudo_resposta = resposta_json['choices'][0]['message']['content']
        st.session_state.messages.append({"role": "assistant", "content": conteudo_resposta})
        with st.chat_message("assistant"):
            st.markdown(conteudo_resposta)
    else:
        st.error(f"Erro na requisição: {response.status_code}")
        st.error(response.text)

