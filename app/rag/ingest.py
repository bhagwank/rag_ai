from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.embeddings import get_embedding_model
from app.core.config import settings

from langchain_chroma import Chroma
import os


BATCH_SIZE = 100


def ingest_pdf(pdf_path):

    print("=" * 60)
    print(f"Loading {pdf_path}")
    print("=" * 60)

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print(f"Pages Loaded : {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    print(f"Chunks Created : {len(chunks)}")

    filename = os.path.basename(pdf_path)

    for index, chunk in enumerate(chunks):

        chunk.metadata["source"] = filename
        chunk.metadata["chunk_id"] = index

    embeddings = get_embedding_model()

    vector_store = Chroma(
        persist_directory=settings.CHROMA_PATH,
        embedding_function=embeddings
    )

    total_batches = (len(chunks) + BATCH_SIZE - 1) // BATCH_SIZE

    print(f"Total batches : {total_batches}")

    for batch_number, start in enumerate(range(0, len(chunks), BATCH_SIZE), start=1):

        end = start + BATCH_SIZE
        batch = chunks[start:end]

        print(f"\nProcessing Batch {batch_number}/{total_batches}")

        vector_store.add_documents(batch)

        print(f"Indexed {len(batch)} chunks")

    print("\nIndexing Completed Successfully!")