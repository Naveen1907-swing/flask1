import http.client
import streamlit as st
from googletrans import Translator
import json

translator = Translator()

def get_chatgpt_response(message):
    conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")
    payload = "{\"messages\":[{\"role\":\"user\",\"content\":\"" + message + "\"}],\"web_access\":false}"
    headers = {
        'x-rapidapi-key': "b3f00fe5cemshc7eaab2ade19a85p12e03bjsnc5a15b5ce04b",
        'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
        'Content-Type': "application/json"
    }
    conn.request("POST", "/gpt4", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def translate_text(text, lang):
    result = translator.translate(text, dest=lang)
    return result.text

def main():
    st.title("Chatbot")
    message = st.text_input("You : ")
    if st.button("Send"):
        response = get_chatgpt_response(message)
        response_json = json.loads(response)
        chatgpt_response = response_json["result"]
        st.write("ChatGPT: " + chatgpt_response)

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Telugu"):
                telugu_response = translate_text(chatgpt_response, 'te')
                st.write("Telugu: " + telugu_response)
        with col2:
            if st.button("Tamil"):
                tamil_response = translate_text(chatgpt_response, 'ta')
                st.write("Tamil: " + tamil_response)
        with col3:
            if st.button("Hindi"):
                hindi_response = translate_text(chatgpt_response, 'hi')
                st.write("Hindi: " + hindi_response)

if _name_ == "_main_":
    main()
