from app.db.chroma import get_vector_store


def list_documents():

    vector_store = get_vector_store()

    data = vector_store._collection.get()

    docs={}

    for meta in data["metadatas"]:

        docs[meta["document"]]=1

    return{

        "documents":list(docs.keys())

    }