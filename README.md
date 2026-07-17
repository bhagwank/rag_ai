# 🚀 Production-Ready RAG AI Backend

A production-style **Retrieval-Augmented Generation (RAG)** application built with **FastAPI**, **LangChain**, **Ollama**, **ChromaDB**, **Redis**, **PostgreSQL**, **Docker**, and **Kubernetes**.

The application allows users to upload PDF documents, generate embeddings, perform semantic search, and receive context-aware answers using a locally hosted **Llama 3.2** model.

---

# 📌 Features

* Upload PDF documents
* Automatic document ingestion and chunking
* Embedding generation using **nomic-embed-text**
* Semantic search using **ChromaDB**
* Context-aware answer generation using **Llama 3.2 (Ollama)**
* REST APIs built with FastAPI
* Interactive Swagger UI
* Redis-based response caching
* PostgreSQL metadata storage
* Docker containerization
* Docker Compose support
* Kubernetes deployment
* GitHub Actions CI/CD
* Structured logging
* Production-ready project architecture

---

# 🏗️ System Architecture

```text
                         User
                           │
                    Swagger UI / REST API
                           │
                        FastAPI
                           │
          ┌────────────────┼────────────────┐
          │                │                │
       Redis         PostgreSQL        ChromaDB
      (Cache)         (Metadata)      (Embeddings)
                           │
                       LangChain
                           │
                        Ollama
                           │
                     Llama 3.2 Model
                           │
                     Generated Answer
```

---

# 🛠️ Technology Stack

| Category            | Technology         |
| ------------------- | ------------------ |
| Language            | Python 3.12        |
| Backend Framework   | FastAPI            |
| LLM Framework       | LangChain          |
| LLM                 | Ollama (Llama 3.2) |
| Embedding Model     | nomic-embed-text   |
| Vector Database     | ChromaDB           |
| Relational Database | PostgreSQL         |
| Cache               | Redis              |
| ORM                 | SQLAlchemy         |
| Containerization    | Docker             |
| Orchestration       | Kubernetes         |
| CI/CD               | GitHub Actions     |

---

# 📂 Project Structure

```text
rag_ai_project_v2/

├── app/
│   ├── api/
│   ├── services/
│   ├── rag/
│   ├── db/
│   ├── cache/
│   ├── core/
│   ├── models/
│   └── main.py
│
├── chroma_db/
├── uploads/
├── documents/
├── logs/
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Prerequisites

* Python 3.12+
* Docker Desktop
* Kubernetes (Docker Desktop or Minikube)
* Ollama
* PostgreSQL
* Redis

---

# 📥 Installation

## Clone Repository

```bash
git clone <repository-url>
cd rag_ai_project_v2
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔧 Environment Variables

Create a `.env` file.

```env
LLM_MODEL=llama3.2:3b
EMBEDDING_MODEL=nomic-embed-text

OLLAMA_BASE_URL=http://localhost:11434

CHROMA_PATH=./chroma_db

UPLOAD_FOLDER=./uploads
DOCUMENT_FOLDER=./documents

REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
CACHE_TTL=3600

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=rag_ai_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=********
```

---

# ▶️ Running the Application

## Local Development

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

## Docker

Build

```bash
docker build -t rag_ai_backend .
```

Run

```bash
docker compose up --build
```

---

# ☸️ Kubernetes Deployment

Apply Kubernetes manifests

```bash
kubectl apply -f k8s/
```

Check Pods

```bash
kubectl get pods
```

Check Services

```bash
kubectl get svc
```

Port Forward

```bash
kubectl port-forward service/rag-api-service 8000:8000
```

---

# 📡 REST APIs

| Method | Endpoint                | Description              |
| ------ | ----------------------- | ------------------------ |
| POST   | `/upload`               | Upload and ingest PDF    |
| POST   | `/ask`                  | Ask questions using RAG  |
| GET    | `/search`               | Search indexed documents |
| GET    | `/documents`            | List uploaded documents  |
| DELETE | `/documents/{filename}` | Delete a document        |
| GET    | `/debug`                | Debug information        |
| GET    | `/health`               | Health check (optional)  |

---

# 🔄 RAG Workflow

```text
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Chunk Documents
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
User Question
      │
      ▼
Redis Cache
      │
 Cache Hit? ── Yes ──► Return Cached Response
      │
      No
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build Prompt
      │
      ▼
Ollama (Llama 3.2)
      │
      ▼
Generate Answer
      │
      ▼
Store Response in Redis
      │
      ▼
Return Response
```

---

# 🗄️ Database Responsibilities

## PostgreSQL

Stores structured application data:

* Document metadata
* Upload status
* Page count
* Chunk count
* Query history (future)
* User information (future)
* Feedback (future)

## ChromaDB

Stores:

* Embeddings
* Chunks
* Vector index
* Semantic search data

## Redis

Stores:

* Cached responses
* Frequently asked questions
* Temporary application cache

---

# 🚀 CI/CD

GitHub Actions pipeline:

```text
Git Push

↓

GitHub Actions

↓

Install Dependencies

↓

Build Docker Image

↓

Run Tests

↓

Push Image

↓

Deploy to Kubernetes
```

---

# 📊 Production Features

* Layered architecture
* Service-based design
* Dependency injection
* Redis caching
* PostgreSQL integration
* Vector database integration
* Docker support
* Kubernetes manifests
* Structured logging
* Health checks
* Production-ready folder structure

---

# 🔮 Future Enhancements

* User authentication (JWT)
* Role-based access control
* Background document ingestion
* Streaming LLM responses
* Multiple LLM support
* Hybrid search
* LangSmith integration
* Prometheus metrics
* Grafana dashboards
* AWS deployment (EKS, RDS, ElastiCache, S3)

---

# 💡 Key Design Decisions

### Why ChromaDB?

ChromaDB is optimized for vector embeddings and semantic similarity search.

### Why PostgreSQL?

PostgreSQL stores structured relational data such as document metadata, upload status, and query history.

### Why Redis?

Redis reduces repeated LLM calls by caching frequently requested responses, improving latency and reducing compute cost.

### Why FastAPI?

FastAPI provides high performance, asynchronous request handling, automatic OpenAPI documentation, and strong type validation.

### Why Kubernetes?

Kubernetes provides container orchestration, horizontal scaling, self-healing, rolling updates, and high availability.

---

# 📈 Future Production Architecture

```text
Users
   │
Load Balancer
   │
FastAPI Pods
   │
Redis
   │
PostgreSQL
   │
ChromaDB
   │
Ollama
```

---

# 🧪 Testing

* API testing using Swagger UI
* Docker Compose deployment
* Kubernetes deployment validation
* PostgreSQL metadata verification
* Redis cache verification
* ChromaDB vector search validation

---

# 👨‍💻 Author

Developed as a production-style AI Backend Engineering project to demonstrate:

* Python Backend Development
* FastAPI
* LangChain
* RAG
* ChromaDB
* Redis
* PostgreSQL
* Docker
* Kubernetes
* CI/CD
* Production AI Architecture
