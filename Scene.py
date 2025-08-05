import google.generativeai as genai
import pyttsx3
import streamlit as st

model = genai.GenerativeModel(
    model_name = "gemini-2.5-flash",
    system_instruction="You are a AI personal assistant  and your name is Tope. you play a role like JARVIS to your user. Speak british accent to your user"
    
)

GOOGLE_API_KEY="AIzaSyDg1nZnWp92quI54uWngzu5tjjp07-QYLc"

st.set_page_config(
    page_title="SceneBot",   # Sets the tab title
    page_icon="SceneBot.png",                                 # Emoji or path to image
    layout="centered",                              # Optional: can be "wide" or "centered"
    initial_sidebar_state="auto"                    # Optional
)

genai.configure(api_key=GOOGLE_API_KEY)



if "messages" not in st.session_state:
    st.session_state.messages = []  



user_input = st.text_input("You:", key="input")



engine = pyttsx3.init()

if "response" not in st.session_state:
    st.session_state.response = ""



if st.button("Send") and user_input.strip():
 response = model.generate_content(user_input)
 st.session_state.response = response.text
 st.session_state.messages.append({"role": "user", "text": user_input})
 st.session_state.messages.append({"role": "ai", "text": response.text})


 st.write("Tope:", st.session_state.response)


 engine.say(response.text)
 engine.runAndWait()





elif st.session_state.response:
    st.write("Tope:", st.session_state.response)


st.markdown("FULL CONVERSATION")
for msg in st.session_state.messages:
    role = "You" if msg["role"] == "user" else "Tope"
    st.write(f"**{role}:** {msg['text']}")
