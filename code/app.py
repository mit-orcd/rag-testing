from flask import Flask, request, render_template, jsonify, redirect, url_for
# from dotenv import load_dotenv, set_key
import os
from unstructured.staging.base import elements_from_json
from unstructured.chunking.title import chunk_by_title
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import utils as chromautils
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from huggingface_hub import login
from langchain.chains import RetrievalQA
import huggingface_hub

app = Flask(__name__)

retriever = None
llm_model = None
langchain = None

access_token = "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"
huggingface_hub.login(token=access_token)

LLM_MODEL_NAME = "gpt2" # "meta-llama/Meta-Llama-3.1-8B-Instruct"
EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"
PATH_RELEVANT_DOCS = "../vectorstore/" # path to the documentation we want

def initialize_components():
    """ Initialize the retriever and LLM components based on the current settings. """
    global retriever, llm_model, langchain
    global LLM_MODEL_NAME, EMBEDDING_MODEL_NAME, PATH_RELEVANT_DOCS
    # vector_db_path = get_vector_db_path(EMBEDDING_MODEL_NAME)

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectorstore = Chroma(persist_directory=PATH_RELEVANT_DOCS, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    llm_model = HuggingFacePipeline.from_model_id( # simple way
    model_id=LLM_MODEL_NAME, # meta-llama/Meta-Llama-3.1-8B-Instruct# gated model, you must get access first to use it. I'll also have options to use non-gated models
    task="text-generation",
    device = "cuda" if torch.cuda.is_available() else "cpu",
    pipeline_kwargs={"max_new_tokens": 350,}
    )

    prompt_template = """
    <|start_header_id|>user<|end_header_id|>
    You are an assistant for answering questions using provided context.
    You are given the extracted parts of a long document and a question. Provide a conversational answer.
    If you don't know the answer, just say "I do not know." Don't make up an answer.  
    Question: {question}
    Context: {context}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template,
    )

    langchain = RetrievalQA.from_chain_type(llm_model, retriever=retriever, chain_type_kwargs={"prompt": prompt})

initialize_components()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', 
                           llm_model_name=LLM_MODEL_NAME,
                           embedding_model_name=EMBEDDING_MODEL_NAME,
                           num_relevant_docs=PATH_RELEVANT_DOCS,
                           )

@app.route('/update_settings', methods=['POST'])
def update_settings():
    global LLM_MODEL_NAME, EMBEDDING_MODEL_NAME, PATH_RELEVANT_DOCS
    LLM_MODEL_NAME = request.form['llm_model_name']
    EMBEDDING_MODEL_NAME = request.form['embedding_model_name']
    PATH_RELEVANT_DOCS = int(request.form['num_relevant_docs'])
    
    # Reinitialize the components (llm and retriever objects)
    initialize_components()
    print(f"Updating model name: {LLM_MODEL_NAME} | embedding model: {EMBEDDING_MODEL_NAME} | documentation {PATH_RELEVANT_DOCS}")
    return redirect(url_for('admin'))

@app.route('/query', methods=['POST'])
def query():
    question = request.json['query_text']
    response = langchain.invoke(question)
    response_text = response["result"].split("\n\n")[1]  # extract the response text, excluding the context
    return jsonify({'response': response_text})

if __name__ == "__main__":
    app.run(debug=True, port=8080)


