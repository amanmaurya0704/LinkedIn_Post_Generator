import os
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

class OpenAILLM:
    def __init__(self):
        load_dotenv()

    def get_openai_llm(self):
        try:
            self.open_api_key=os.getenv("OPENAI_API_KEY")
            llm = ChatOpenAI(api_key =self.open_api_key, model='gpt-4o')

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")
        
        return llm