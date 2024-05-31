import streamlit as st

st.set_page_config("my App")

st.balloons()

st.chat_message(name="ai")



st.code('''
        print(data)
        
        ''',language='python')
prompt = st.chat_input('Say something:computer')
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
st.header('hi ram :smile:')
st.header('hi ram :question:')