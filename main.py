import streamlit as st
from PIL import Image
from openai import OpenAI


# <--------------------------------------- Streamlit Page ---------------------------------------------------->


# Set page configuration
st.set_page_config(
    page_title='SQLGenie',
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define the sidebar content and inputs
html_temp = """
<div style="background-color:#2F396F;padding:0.7px">
<h3 style="color:white;text-align:center;" >SQLGenie: Your Magical Database Query Assistant</h3>
</div><br>"""

st.markdown(html_temp, unsafe_allow_html=True)

st.sidebar.image('https://i.imgur.com/3XqSI3B.png', width=180)
st.sidebar.markdown("---")

# Sidebar with text options for user input
with st.sidebar:
    db_string = st.text_input("DB Connection String")
    model_names = ["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo", "gpt-4"]
    selected_model = st.selectbox("Select Model", model_names)
    api_key = st.text_input("API Key", type="password")

    # Store values in session state
    st.session_state.db_string = db_string
    st.session_state.selected_model = selected_model
    st.session_state.api_key = api_key  # Corrected

st.sidebar.markdown("---")

# Overview text
overview_text = """
SQLGenie, an AI-driven chatbot, seamlessly interacts with your SQL databases, providing instant answers and insightful plots. It simplifies complex database interactions, offering clear insights and answering general questions about databases and data management practices. SQLGenie transforms data exploration into an engaging experience, making it indispensable for database enthusiasts and professionals. 

Businesses benefit from SQLGenie's ability to streamline data analysis, enhance decision-making processes, and improve overall data management efficiency.
"""

# Display the overview text
st.markdown(overview_text)

# Display the SQLGenie image
image_path = 'sql_genie.jpg'  # Replace with the path to your image file


_left, mid, _right = st.columns(3)
with mid:
    try:
        image = Image.open(image_path)
        st.image(image, caption='SQLGenie', use_column_width=False, width=400)
    except Exception as e:
        st.error(f"Error loading image: {e}")


# <----------------------------------------------------------------------------------------------------------->


client = OpenAI(api_key=st.session_state.api_key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []


# # Create buttons with st.button
# with stylable_container(
#     "green",
#     css_styles="""
#     button1 {
#         background-color: #00FF00;
#         color: black;
#     }""",
# ):
#     button1_clicked = st.sidebar.button("Button 1", key="button1")

# Add a button to the sidebar to start the chat
if st.sidebar.button("Start Chat", key="start"):
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)

    if not st.session_state.api_key:
        st.warning('API key is missing. Please set the OpenAI API key', icon="⚠️")

    else:

        st.session_state.messages = []  # Reset messages
        st.session_state.messages.append({"role": "assistant", "content": "Hello! How can I assist you today?"})


# Add a button to the sidebar to reset the chat
if st.sidebar.button("Reset Chat"):
    st.session_state.messages = []



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Only display the chat input when the user has started the chat
if st.session_state.messages:
    if prompt := st.chat_input("Ask your question!!!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

