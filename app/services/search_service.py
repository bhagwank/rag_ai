from app.db.chroma import get_vector_store


def similarity_search(question):

    vector_store = get_vector_store()

    docs = vector_store.similarity_search_with_score(

        question,

        k=5

    )

    results=[]

    for doc,score in docs:

        results.append({

            "score":score,

            "metadata":doc.metadata,

            "content":doc.page_content

        })

    return results