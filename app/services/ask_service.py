from app.rag.retriever import get_retriever
from app.rag.chain import generate_answer

def ask_question(question: str):

    retriever = get_retriever()

    docs = retriever.invoke(question)
    
    for i, doc in enumerate(docs, start=1):
        print(f"\nChunk {i}")
        print(doc.page_content)
        print("-" * 50)
    print("\n===== Retrieved Documents =====")

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    response = generate_answer(
        context=context,
        question=question
    )

    return {
        "question": question,
        "answer": response,
        "chunks": len(docs),
        "sources": [
            doc.metadata
            for doc in docs
        ]
    }