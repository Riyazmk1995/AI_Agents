from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import streamlit as st
import json
from datetime import datetime
from agent_4 import ManagerAgent
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
manager_agent = ManagerAgent()

@app.post("/process")
async def process(request: Request):
    data = await request.json()
    user_input = data.get("user_input")
    documents = data.get("documents")
    response = manager_agent.process(user_input, documents)
    return JSONResponse(content=response)

def set_page_config():
    st.set_page_config(
        page_title="AI AgentFlow Manager",
        page_icon="🤖",
        layout="wide"
    )

def initialize_session_state():
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False

def add_styles():
    # Base styles
    base_styles = """
        .stApp {
            transition: background-color 0.3s ease;
        }
        .title {
            text-align: center;
            padding: 2rem 0;
            font-size: 2.5rem;
            font-weight: bold;
            transition: color 0.3s ease;
        }
        .welcome-message {
            text-align: center;
            padding: 1rem;
            border-radius: 10px;
            margin: 2rem 0;
            line-height: 1.6;
            transition: background-color 0.3s ease;
        }
        .stButton button {
            border-radius: 8px !important;
            padding: 0.5rem 2rem !important;
            font-weight: bold !important;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            transform: translateY(-2px);
        }
        .history-item {
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }
        .dark-mode-container {
            position: fixed;
            top: 1rem;
            right: 1rem;
            z-index: 1000;
            padding: 0.5rem;
            border-radius: 8px;
        }
        .sidebar-history {
            padding: 1rem;
            margin-top: 2rem;
        }
    """

    # Dark mode specific styles
    dark_mode_styles = """
        .stApp {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        }
        .title {
            color: #ffffff;
        }
        .welcome-message {
            background: rgba(45, 45, 45, 0.7);
            color: #ffffff;
        }
        .history-item {
            background: rgba(45, 45, 45, 0.7);
            color: #ffffff;
        }
    """ if st.session_state.dark_mode else """
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%);
        }
        .title {
            color: #1E3D59;
        }
        .welcome-message {
            background: rgba(255, 255, 255, 0.7);
            color: #1E3D59;
        }
        .history-item {
            background: rgba(255, 255, 255, 0.7);
            color: #1E3D59;
        }
    """

    st.markdown(
        f"""
        <style>
        {base_styles}
        {dark_mode_styles}
        </style>
        """,
        unsafe_allow_html=True
    )

def add_to_history(query, documents, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.history.append({
        "timestamp": timestamp,
        "query": query,
        "documents": documents,
        "response": response
    })

def download_json(data, filename):
    json_str = json.dumps(data, indent=2)
    return json_str

def display_history_sidebar():
    st.sidebar.title("📜 Query History")
    
    if st.session_state.history:
        for idx, item in enumerate(reversed(st.session_state.history)):
            with st.sidebar.expander(f"Query from {item['timestamp']}", expanded=False):
                st.write("**Query:**", item["query"])
                if item["documents"]:
                    st.write("**Documents:**", item["documents"])
                st.write("**Response:**")
                st.json(item["response"])
                
                json_str = download_json(item, f"result_{idx}.json")
                st.download_button(
                    label="Download This Result 📥",
                    data=json_str,
                    file_name=f"result_{idx}.json",
                    mime="application/json"
                )
        
        # Download all history button at the top of sidebar
        json_str = download_json(st.session_state.history, "complete_history.json")
        st.sidebar.download_button(
            label="Download Complete History 📥",
            data=json_str,
            file_name="complete_history.json",
            mime="application/json"
        )
    else:
        st.sidebar.info("No queries yet. Your history will appear here.")

def main():
    set_page_config()
    initialize_session_state()
    add_styles()
    
    # Display history in sidebar
    display_history_sidebar()
    
    # Dark mode toggle in top right
    col_space, col_toggle = st.columns([4, 1])
    with col_toggle:
        dark_mode = st.toggle("🌓 Dark Mode", value=st.session_state.dark_mode)
        if dark_mode != st.session_state.dark_mode:
            st.session_state.dark_mode = dark_mode
            st.rerun()  # Using st.rerun() instead of experimental_rerun
    
    # Title and welcome message
    st.markdown('<div class="title">AI AgentFlow</div>', unsafe_allow_html=True)
    st.markdown(
        '''
        <div class="welcome-message">
            <h2>Welcome to AgentFlow! 👋</h2>
            <p>Your intelligent AI-powered task management system.</p>
            <p>Let our specialized agents handle your tasks with precision and efficiency.</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    # Main input section
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Enter Your Query")
        user_input = st.text_input("", placeholder="Type your query here...")
        
    with col2:
        st.subheader("📄 Document Input")
        documents = st.text_area("", placeholder="Enter any relevant documents here...")
    
    # Process button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        process_button = st.button("Process Request 🚀")
    
    if process_button and user_input:
        with st.spinner('Processing your request...'):
            response = manager_agent.process(user_input, documents)
            add_to_history(user_input, documents, response)
            
        # Display results
        with st.expander("📊 Results", expanded=True):
            st.json(response)
            
            # Download button for current result
            current_result = {
                "query": user_input,
                "documents": documents,
                "response": response,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            json_str = download_json(current_result, "result.json")
            st.download_button(
                label="Download Results 📥",
                data=json_str,
                file_name="result.json",
                mime="application/json"
            )
        
        st.success("Task processed successfully!")

if __name__ == "__main__":
    main()