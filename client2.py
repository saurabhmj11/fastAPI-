import requests
import streamlit as st

# Function to fetch response from OpenAI API
def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={'input': {'topic': input_text}})
    if response.ok:
        try:
            return response.json()['output']['content']
        except Exception as e:
            st.error("Error parsing response: {}".format(e))
    else:
        st.error("Request failed with status code {}".format(response.status_code))

# Function to fetch response from LLAMA2 API
def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input': {'topic': input_text}})
    if response.ok:
        try:
            return response.json()['output']
        except Exception as e:
            st.error("Error parsing response: {}".format(e))
    else:
        st.error("Request failed with status code {}".format(response.status_code))

# Main Streamlit app
st.set_page_config(page_title="Langchain Demo", page_icon=":pencil2:", layout="wide")

# Custom CSS for dark theme
st.markdown(
    """
    <style>
        /* Dark theme */
        body {
            color: #fff;
            background-color: #282c34;
        }
        .stTextInput>div>div>div>input {
            border: 1px solid #444;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            background-color: #444;
            color: #fff;
        }
        .stTextInput>div>div>div>input:focus {
            border-color: #0072b1;
            box-shadow: 0 0 0 2px #0072b1;
        }
        .stButton>button {
            background-color: #0072b1;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #005d8c;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Input fields
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

# Display responses
if input_text:
    st.subheader("Essay:")
    st.write(get_openai_response(input_text))

if input_text1:
    st.subheader("Poem:")
    st.write(get_ollama_response(input_text1))

# Footer
st.markdown(
    """
    <div style="position: fixed; bottom: 0; width: 100%; background-color: #0072b1; color: white; padding: 10px 0; text-align: center;">
        Developed by Saurabh Lokhande
    </div>
    """,
    unsafe_allow_html=True
)
