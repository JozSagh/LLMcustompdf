from main import qa

if __name__ == "__main__":
    qa_chain = qa  # get the QA pipeline
    question = "How many laws do Newton suggest?"
    answer = qa_chain.invoke({"query": question})

    print("Q:", question)
    print("A:", answer["result"])
