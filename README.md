# 🚀 Local LLM for Interacting with Your Custom Documents

A local Large Language Model (LLM) project that lets you **search and interact with your own documents**.  

### Features
* 🔍 **Document Search Engine** – quickly find relevant information in your documents  
* 🤝 **LLM-powered QA** – ask questions and get answers based on your content  

### How it works
Using a PDF (e.g., Newton’s Laws from Wikipedia), the process is:

1. **Read the document** – load your PDF into the system  
2. **Text extraction & chunking** – split the document into manageable chunks  
3. **Add to ChromaDB** – store the chunks for efficient retrieval  
4. **Run LLM via LangChain** – query the chunks using a local LLM  
5. **Answer custom questions** – receive precise answers based on your document content  

### Example QA 
LLM Answering from the custom PDF about the Newton's laws:
<br><img src="chatllm.png" alt="ChatLLM" width="400"/>
