import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_tools_agent
from langchain.agents import AgentExecutor
from langchain import hub

# Load API keys from environment variables
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    st.error("Please set your OPENAI_API_KEY in a .env file!")
    st.stop()

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# Pull prompt from LangChain hub
prompt = hub.pull("hwchase17/openai-functions-agent")

# Streamlit Page Configuration
st.set_page_config(
    page_title="Interactive Search Tools with Chat History",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a tool",
    [
        "Search Wikipedia",
        "Search ArXiv Papers",
    ],
)

# Define tools
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

arxiv_api_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv_tool = ArxivQueryRun(api_wrapper=arxiv_api_wrapper)

tools = [wiki_tool, arxiv_tool]

# Create Agent
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = {
        "Search Wikipedia": [],
        "Search ArXiv Papers": [],
    }

# Pages
if page == "Search Wikipedia":
    st.header("Search Wikipedia")
    query = st.text_input("Enter your query for Wikipedia:")
    if st.button("Search Wikipedia"):
        if query.strip():
            result = agent_executor.invoke({"input": f"Search Wikipedia for {query}"})
            st.session_state["chat_history"][page].append(("user", query))
            st.session_state["chat_history"][page].append(("bot", result['output']))
            st.success(f"Result: {result['output']}")
        else:
            st.warning("Please enter a valid query!")

    # Display chat history
    st.write("### Chat History:")
    for role, message in st.session_state["chat_history"][page]:
        if role == "user":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Assistant:** {message}")

elif page == "Search ArXiv Papers":
    st.header("Search ArXiv Papers")
    query = st.text_input("Enter your query for ArXiv:")
    if st.button("Search ArXiv"):
        if query.strip():
            result = agent_executor.invoke({"input": f"Search ArXiv for {query}"})
            st.session_state["chat_history"][page].append(("user", query))
            st.session_state["chat_history"][page].append(("bot", result['output']))
            st.success(f"Result: {result['output']}")
        else:
            st.warning("Please enter a valid query!")

    # Display chat history
    st.write("### Chat History:")
    for role, message in st.session_state["chat_history"][page]:
        if role == "user":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Assistant:** {message}")