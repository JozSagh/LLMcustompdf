# -----------------------
# Imports
# -----------------------
import chromadb
from sentence_transformers import SentenceTransformer
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.llms import GPT4All
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PyPDF2

# -----------------------
# Variables - PDF and The model path: 
# -----------------------
local_pdf_path = r"data/Newtonslaws.pdf"
gpt_model_path = r"data/q4_0-orca-mini-3b.gguf"

# -----------------------
# Step 1: Extract text from PDF
# -----------------------
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

pdf_text = extract_text_from_pdf(local_pdf_path)
print("PDF text extracted.")

# -----------------------
# Step 2: Split text into chunks
# -----------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,   # max characters per chunk
    chunk_overlap=100 # overlap for context
)
chunks = splitter.split_text(pdf_text)
print(f"Total chunks created: {len(chunks)}")

# -----------------------
# Step 3: Initialize ChromaDB collection
# -----------------------
client = chromadb.Client()
# Delete previous collection if exists
try:
    client.delete_collection("pdf_docs")
except:
    pass

collection = client.create_collection("pdf_docs")
print("ChromaDB collection ready.")

# -----------------------
# Step 4: Embed chunks
# -----------------------
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma(
    collection_name="pdf_docs",
    embedding_function=embeddings,
    persist_directory=".chromadb"
)
print("Chunks added to ChromaDB with embeddings.")

# -----------------------
# Step 5: Set up Orca Mini 3B LLM
# -----------------------
llm = GPT4All(model=gpt_model_path)

# -----------------------
# Step 6: Build LangChain RetrievalQA
# -----------------------
vectorstore = Chroma(
    collection_name="pdf_docs",
    embedding_function=embeddings,
    persist_directory=".chromadb"
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k":3}),
    return_source_documents=False #Only one output
)


if __name__=="__main__":
    # -----------------------
    # Step 7: Ask a question
    # -----------------------
    question = "What is Newtons first law about?"
    answer = qa.run(question)

    print("🔍 Question:", question)
    print("📜 Answer:", answer)
