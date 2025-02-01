import streamlit as st
import dseek

st.title("Deep Seek Web Application - Demo")
st.write("This is a simple app that demonstrates how to use the ChatCompletionsClient to interact with the deployed DeepSeek-R1 model")

query = st.text_area("Enter your query here:")

full_response = ""

if st.button("Submit"):
    with st.spinner("Fetching response..."):
        response_container = st.empty()
        for update in dseek.get_response(query):
            if update.choices:
                if update.choices and update.choices[0].delta.content:
                    full_response += update.choices[0].delta.content
                    response_container.markdown(full_response) #update incrementally

        dseek.client.close()