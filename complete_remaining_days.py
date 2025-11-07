#!/usr/bin/env python3
"""
Complete Days 25-30 with production-ready content.
"""

import json

# Read the current courseData.json
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'r') as f:
    course_data = json.load(f)

# Define complete content for Days 25-30
days_25_30 = [
    # DAY 25 content is created separately due to size
]

# Find Week 4 and append Days 25-30
for week in course_data['weeks']:
    if week['weekNumber'] == 4:
        # Days 23-24 are already there, now append 25-30

        # DAY 25: System Architecture Thinking
        week['days'].append({
            "dayNumber": 25,
            "title": "System Architecture Thinking",
            "duration": "30 minutes",
            "learningObjectives": [
                "Design scalable RAG system architectures",
                "Understand separation of concerns in AI systems",
                "Plan for error handling and monitoring",
                "Make informed technology stack decisions"
            ],
            "content": {
                "theory": """Building production AI systems requires architectural thinking beyond individual workflows. You need to design systems that are scalable, maintainable, and resilient.

**Core Architectural Principles:**

**1. Separation of Concerns:**
Break your AI system into distinct layers:
- **API Layer**: Handles requests/responses, validation, authentication
- **Processing Layer**: Business logic, data transformation
- **AI Layer**: Model calls, embeddings, vector search
- **Storage Layer**: Databases, vector stores, caching
- **Monitoring Layer**: Logging, metrics, alerts

**2. Scalability Considerations:**

**Caching Strategy:**
- Cache expensive operations (embeddings, model calls)
- Use Redis or similar for distributed caching
- Implement TTL (time-to-live) based on data freshness needs

**Rate Limiting:**
- Protect your APIs from overload
- Queue requests during traffic spikes
- Implement backoff strategies for external APIs

**Async Processing:**
- Use queues (RabbitMQ, Redis Queue) for long-running tasks
- Return job IDs immediately, process asynchronously
- Webhook callbacks when processing completes

**3. RAG (Retrieval-Augmented Generation) Architecture:**

```
User Query → Embedding → Vector Search → Retrieved Docs → Prompt Engineering → LLM → Response
     ↓                                                              ↓
 Validation                                                    Post-processing
```

**Components:**
- **Document Ingestion Pipeline**: Upload → Chunk → Embed → Store
- **Query Pipeline**: Question → Embed → Search → Rank → Retrieve
- **Generation Pipeline**: Context + Query → Prompt → LLM → Answer
- **Feedback Loop**: User ratings → Improve retrieval/prompts

**4. CAG (Cognitive Augmented Generation) Patterns:**

CAG extends RAG with reasoning and tool use:
- **Agent Loop**: Think → Act → Observe → Repeat
- **Tool Integration**: Web search, calculators, databases
- **Chain of Thought**: Break complex queries into steps
- **Self-Reflection**: Evaluate answers, retry if needed

**5. Error Handling Architecture:**

**Graceful Degradation:**
- If vector search fails → use keyword search fallback
- If primary LLM fails → try backup model
- If no docs found → answer from LLM's knowledge only

**Circuit Breakers:**
- Stop calling failing services after N failures
- Automatically recover when service is healthy
- Prevent cascade failures

**6. Monitoring and Observability:**

**Key Metrics:**
- Latency (p50, p95, p99)
- Error rates by type
- Token usage and costs
- Cache hit rates
- User satisfaction scores

**Logging Strategy:**
- Structure logs as JSON for parsing
- Log: request_id, user_id, operation, duration, status
- Correlation IDs to trace requests across services

**7. Technology Stack Decisions:**

**For RAG Systems:**

| Component | Options | Best For |
|-----------|---------|----------|
| Vector DB | Pinecone, Weaviate, Qdrant | Choose based on scale, hosting preference |
| Embeddings | OpenAI, Cohere, open-source | Cost vs. performance tradeoff |
| LLM | GPT-4, Claude, Llama | Quality needs, budget, data privacy |
| Orchestration | n8n, LangChain, Custom | Complexity, team skills |
| Caching | Redis, Memcached | Distributed vs. local |

**Decision Framework:**
1. **Start Simple**: Use managed services (Pinecone, OpenAI)
2. **Measure**: Add monitoring before scaling
3. **Optimize**: Identify bottlenecks with data
4. **Scale**: Upgrade components as needed

**8. Data Flow Design:**

Good architecture clearly defines data flow:

```
Ingestion Flow:
Raw Docs → Validate → Clean → Chunk → Embed → Vector DB
                ↓                              ↓
           Error Queue                    Metadata Store

Query Flow:
Question → Validate → Embed → Vector Search → Rank → Top K Docs
                                                           ↓
                                                   Prompt Template
                                                           ↓
                                                       LLM Call
                                                           ↓
                                                   Post-process → Response
```

Each arrow represents a clear interface with defined inputs/outputs.""",
                "concepts": [
                    {
                        "name": "Layered Architecture for AI Systems",
                        "explanation": "Organize AI systems into layers with clear responsibilities. Each layer has defined inputs, outputs, and dependencies.",
                        "example": """# Python: Layered RAG architecture example

# Layer 1: API Layer (FastAPI)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str
    max_results: int = 3

class QueryResponse(BaseModel):
    answer: str
    sources: list
    confidence: float

@app.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    try:
        # Layer 2: Processing Layer - validate and prepare
        validated_query = processing_layer.validate_query(request.question)

        # Layer 3: AI Layer - retrieve and generate
        result = ai_layer.process_query(validated_query, request.max_results)

        # Layer 4: Monitoring Layer - log metrics
        monitoring_layer.log_query(request.question, result)

        return result
    except Exception as e:
        # Centralized error handling
        monitoring_layer.log_error(e)
        raise HTTPException(status_code=500, detail=str(e))

# Layer 2: Processing Layer
class ProcessingLayer:
    def validate_query(self, question: str) -> str:
        if len(question) < 3:
            raise ValueError("Question too short")
        if len(question) > 500:
            raise ValueError("Question too long")
        return question.strip()

# Layer 3: AI Layer
class AILayer:
    def __init__(self, vector_store, llm):
        self.vector_store = vector_store
        self.llm = llm

    def process_query(self, question: str, max_results: int):
        # Get relevant documents
        docs = self.vector_store.search(question, k=max_results)

        # Generate answer
        answer = self.llm.generate(question, docs)

        return answer

# Clear separation: API → Processing → AI → Storage"""
                    },
                    {
                        "name": "Caching Strategy for AI Operations",
                        "explanation": "Cache expensive operations (embeddings, LLM calls) to reduce costs and improve latency. Use cache keys based on operation inputs.",
                        "example": """# Python: Implement caching for embeddings and LLM calls
import hashlib
import json
import redis

# Initialize Redis cache
cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

def get_cache_key(operation: str, data: dict) -> str:
    \"\"\"Generate consistent cache key from operation and data.\"\"\"
    # Sort dict for consistent hashing
    sorted_data = json.dumps(data, sort_keys=True)
    hash_value = hashlib.md5(sorted_data.encode()).hexdigest()
    return f"{operation}:{hash_value}"

def cached_embedding(text: str, model: str = "text-embedding-ada-002"):
    \"\"\"Get embedding with caching.\"\"\"

    # Check cache first
    cache_key = get_cache_key("embedding", {"text": text, "model": model})
    cached_result = cache.get(cache_key)

    if cached_result:
        print(f"Cache HIT for embedding")
        return json.loads(cached_result)

    print(f"Cache MISS - calling OpenAI")

    # Generate embedding
    from openai import OpenAI
    client = OpenAI()
    response = client.embeddings.create(input=text, model=model)
    embedding = response.data[0].embedding

    # Cache for 24 hours (86400 seconds)
    cache.setex(cache_key, 86400, json.dumps(embedding))

    return embedding

def cached_llm_call(messages: list, model: str = "gpt-3.5-turbo", temperature: float = 0):
    \"\"\"Cache LLM calls (only for temperature=0 for deterministic results).\"\"\"

    if temperature > 0:
        # Don't cache non-deterministic calls
        return call_llm(messages, model, temperature)

    cache_key = get_cache_key("llm", {"messages": messages, "model": model})
    cached_result = cache.get(cache_key)

    if cached_result:
        print(f"Cache HIT - saved API call!")
        return json.loads(cached_result)

    print(f"Cache MISS - calling LLM")
    result = call_llm(messages, model, temperature)

    # Cache for 1 hour
    cache.setex(cache_key, 3600, json.dumps(result))

    return result

# Cache strategy saves money and improves performance!"""
                    },
                    {
                        "name": "Error Handling and Graceful Degradation",
                        "explanation": "Design systems to handle failures gracefully. Implement fallbacks, circuit breakers, and retry logic with exponential backoff.",
                        "example": """# Python: Comprehensive error handling for RAG system
import time
from enum import Enum
from typing import Optional

class SearchStrategy(Enum):
    VECTOR = "vector"
    KEYWORD = "keyword"
    HYBRID = "hybrid"

class RAGSystemWithFallbacks:
    def __init__(self, vector_db, keyword_db, primary_llm, fallback_llm):
        self.vector_db = vector_db
        self.keyword_db = keyword_db
        self.primary_llm = primary_llm
        self.fallback_llm = fallback_llm
        self.circuit_breaker_failures = 0
        self.circuit_breaker_threshold = 5

    def query(self, question: str) -> dict:
        \"\"\"Query with multi-level fallbacks.\"\"\"

        # Try retrieval with fallbacks
        docs = self._retrieve_with_fallback(question)

        # Try generation with fallbacks
        answer = self._generate_with_fallback(question, docs)

        return {
            "answer": answer,
            "sources": docs,
            "strategy_used": self.strategy_used
        }

    def _retrieve_with_fallback(self, question: str) -> list:
        \"\"\"Try vector search, fall back to keyword search.\"\"\"

        try:
            # Primary: Vector search
            docs = self.vector_db.search(question, k=3)
            self.strategy_used = SearchStrategy.VECTOR
            return docs

        except Exception as e:
            print(f"Vector search failed: {e}, trying keyword search")

            try:
                # Fallback: Keyword search
                docs = self.keyword_db.search(question, k=3)
                self.strategy_used = SearchStrategy.KEYWORD
                return docs

            except Exception as e2:
                print(f"All search methods failed: {e2}")
                # Return empty list - LLM will answer without context
                self.strategy_used = None
                return []

    def _generate_with_fallback(self, question: str, docs: list) -> str:
        \"\"\"Try primary LLM, fall back to secondary.\"\"\"

        # Check circuit breaker
        if self.circuit_breaker_failures >= self.circuit_breaker_threshold:
            print("Circuit breaker open - using fallback LLM directly")
            return self._call_llm(self.fallback_llm, question, docs)

        try:
            # Primary LLM
            answer = self._call_llm(self.primary_llm, question, docs)

            # Reset circuit breaker on success
            self.circuit_breaker_failures = 0

            return answer

        except Exception as e:
            print(f"Primary LLM failed: {e}")

            # Increment circuit breaker
            self.circuit_breaker_failures += 1

            try:
                # Fallback LLM
                answer = self._call_llm(self.fallback_llm, question, docs)
                return answer

            except Exception as e2:
                # Last resort: return error message
                return f"I apologize, but I'm unable to process your question right now. Please try again later."

    def _call_llm(self, llm, question: str, docs: list, max_retries: int = 3) -> str:
        \"\"\"Call LLM with exponential backoff retry.\"\"\"

        for attempt in range(max_retries):
            try:
                return llm.generate(question, docs)
            except RateLimitError:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + 1
                    print(f"Rate limit - waiting {wait_time}s")
                    time.sleep(wait_time)
                else:
                    raise

# This architecture ensures users always get a response!"""
                    },
                    {
                        "name": "System Monitoring and Observability",
                        "explanation": "Implement comprehensive monitoring to understand system health, performance, and costs. Use structured logging and metrics.",
                        "example": """# Python: Monitoring layer for RAG system
import time
import json
import logging
from datetime import datetime
from typing import Any, Dict
from functools import wraps

# Configure structured logging
logger = logging.getLogger("rag_system")
handler = logging.StreamHandler()
formatter = logging.Formatter(json.dumps({
    "timestamp": "%(asctime)s",
    "level": "%(levelname)s",
    "message": "%(message)s"
}))
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class RAGMetrics:
    \"\"\"Track system metrics.\"\"\"

    def __init__(self):
        self.queries_total = 0
        self.queries_failed = 0
        self.total_latency = 0
        self.total_tokens = 0
        self.total_cost = 0

    def record_query(self, latency: float, tokens: int, success: bool):
        self.queries_total += 1
        self.total_latency += latency
        self.total_tokens += tokens
        self.total_cost += (tokens / 1000) * 0.002  # Estimate

        if not success:
            self.queries_failed += 1

    def get_stats(self) -> dict:
        return {
            "total_queries": self.queries_total,
            "failed_queries": self.queries_failed,
            "success_rate": 1 - (self.queries_failed / max(self.queries_total, 1)),
            "avg_latency_ms": self.total_latency / max(self.queries_total, 1) * 1000,
            "total_tokens": self.total_tokens,
            "total_cost_usd": self.total_cost
        }

metrics = RAGMetrics()

def monitor_operation(operation_name: str):
    \"\"\"Decorator to monitor any operation.\"\"\"
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            request_id = f"{operation_name}_{int(time.time() * 1000)}"

            logger.info({
                "event": "operation_started",
                "operation": operation_name,
                "request_id": request_id
            })

            try:
                result = func(*args, **kwargs)

                duration = time.time() - start_time

                logger.info({
                    "event": "operation_completed",
                    "operation": operation_name,
                    "request_id": request_id,
                    "duration_ms": duration * 1000,
                    "success": True
                })

                metrics.record_query(duration,
                                   getattr(result, 'tokens', 0),
                                   True)

                return result

            except Exception as e:
                duration = time.time() - start_time

                logger.error({
                    "event": "operation_failed",
                    "operation": operation_name,
                    "request_id": request_id,
                    "duration_ms": duration * 1000,
                    "error": str(e),
                    "error_type": type(e).__name__
                })

                metrics.record_query(duration, 0, False)

                raise

        return wrapper
    return decorator

# Usage
@monitor_operation("vector_search")
def search_vectors(query: str, k: int = 3):
    # Your search logic
    pass

@monitor_operation("llm_generation")
def generate_answer(question: str, context: list):
    # Your generation logic
    pass

# Get metrics anytime
print(json.dumps(metrics.get_stats(), indent=2))"""
                    }
                ],
                "codeExamples": [
                    {
                        "title": "Complete RAG System Architecture (ASCII Diagram + Code Structure)",
                        "language": "python",
                        "code": """# Complete RAG System Architecture
# This shows how all components fit together

\"\"\"
RAG SYSTEM ARCHITECTURE
=======================

┌─────────────────────────────────────────────────────────────┐
│                         API GATEWAY                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Rate Limiting│  │ Auth/API Keys│  │ Request      │      │
│  │              │→ │              │→ │ Validation   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                    PROCESSING LAYER                          │
│                                                               │
│  ┌───────────────────────────────────────────────────┐      │
│  │  INGESTION PIPELINE          QUERY PIPELINE       │      │
│  │                                                     │      │
│  │  Upload → Clean → Chunk     Query → Validate      │      │
│  │     ↓       ↓       ↓           ↓                  │      │
│  │  Validate  OCR   Split       Embed                 │      │
│  └───────────────────────────────────────────────────┘      │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                      AI LAYER                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Embedding   │  │ Vector Search│  │  LLM         │      │
│  │  Service     │→ │  Service     │→ │  Service     │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                    STORAGE LAYER                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Vector DB    │  │  Cache       │  │  Metadata    │      │
│  │ (Pinecone)   │  │  (Redis)     │  │  (Postgres)  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                   MONITORING LAYER                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Logging     │  │  Metrics     │  │  Alerting    │      │
│  │  (JSON logs) │  │  (Prometheus)│  │  (PagerDuty) │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
\"\"\"

# Code structure matching this architecture

# === API GATEWAY LAYER ===
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security.api_key import APIKeyHeader

app = FastAPI(title="RAG System API")

API_KEY_HEADER = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Depends(API_KEY_HEADER)):
    if api_key not in valid_api_keys:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key

@app.post("/query")
async def query_endpoint(
    request: QueryRequest,
    api_key: str = Depends(verify_api_key)
):
    # API Gateway validates, then passes to Processing Layer
    return await processing_layer.handle_query(request)

# === PROCESSING LAYER ===
class ProcessingLayer:
    def __init__(self, ai_layer, storage_layer):
        self.ai_layer = ai_layer
        self.storage_layer = storage_layer

    async def handle_query(self, request: QueryRequest):
        # Validate
        validated = self._validate_query(request.question)

        # Check cache first
        cached = await self.storage_layer.cache.get(validated)
        if cached:
            return cached

        # Pass to AI layer
        result = await self.ai_layer.process_query(validated)

        # Cache result
        await self.storage_layer.cache.set(validated, result)

        return result

# === AI LAYER ===
class AILayer:
    def __init__(self, embedding_service, vector_service, llm_service):
        self.embedding_service = embedding_service
        self.vector_service = vector_service
        self.llm_service = llm_service

    async def process_query(self, question: str):
        # 1. Embed query
        query_embedding = await self.embedding_service.embed(question)

        # 2. Search vectors
        docs = await self.vector_service.search(query_embedding, k=3)

        # 3. Generate answer with LLM
        answer = await self.llm_service.generate(question, docs)

        return answer

# === STORAGE LAYER ===
class StorageLayer:
    def __init__(self):
        self.vector_db = PineconeClient()
        self.cache = RedisCache()
        self.metadata_db = PostgresDB()

# === MONITORING LAYER ===
import logging

class MonitoringLayer:
    def __init__(self):
        self.logger = logging.getLogger("rag_system")
        self.metrics = PrometheusMetrics()

    def log_query(self, query, result, duration):
        self.logger.info({
            "event": "query_completed",
            "query": query,
            "duration_ms": duration * 1000,
            "success": True
        })
        self.metrics.record_query_latency(duration)

# This architecture ensures:
# - Separation of concerns (each layer has one job)
# - Scalability (layers can scale independently)
# - Maintainability (clear interfaces between layers)
# - Observability (monitoring at every layer)""",
                        "explanation": "Complete RAG system architecture showing how all components connect. ASCII diagram visualizes the layers, and code shows how to structure each layer with clear responsibilities."
                    },
                    {
                        "title": "n8n Workflow: Architected RAG System",
                        "language": "javascript",
                        "code": """// n8n Function node: RAG system following architectural principles
// This shows how to structure a complex workflow with separation of concerns

// === LAYER 1: Validation & Preparation ===
function validateAndPrepare() {
  const query = $json.query || "";

  // Validation
  if (query.length < 3) {
    throw new Error("Query too short");
  }

  if (query.length > 500) {
    throw new Error("Query too long - max 500 characters");
  }

  // Prepare with metadata
  return {
    query: query.trim(),
    timestamp: new Date().toISOString(),
    request_id: `req_${Date.now()}`,
    config: {
      top_k: 3,
      score_threshold: 0.7,
      temperature: 0
    }
  };
}

// === LAYER 2: Cache Check ===
// (Would connect to Redis via HTTP Request node)
function prepareCacheCheck(data) {
  const cacheKey = `query:${hashString(data.query)}`;

  return {
    json: {
      operation: "GET",
      key: cacheKey,
      original_data: data
    }
  };
}

// === LAYER 3: Orchestration Logic ===
function orchestrateRAGQuery(data) {
  // This Function node decides the workflow path

  const cacheResult = $node["Cache Check"].json;

  if (cacheResult.hit) {
    // Cache hit - return immediately
    return [{
      json: {
        answer: cacheResult.value,
        source: "cache",
        latency_ms: 50
      }
    }];
  }

  // Cache miss - continue to vector search
  return [{
    json: {
      query: data.query,
      embedding_needed: true,
      proceed_to_search: true
    }
  }];
}

// === LAYER 4: Error Handling & Fallback ===
function handleSearchError() {
  const error = $json.error;

  if (error.includes("vector_db_timeout")) {
    // Fallback to keyword search
    return [{
      json: {
        fallback_strategy: "keyword_search",
        query: $json.original_query
      }
    }];
  }

  if (error.includes("rate_limit")) {
    // Queue for retry
    return [{
      json: {
        action: "queue_for_retry",
        retry_after: 60,
        query: $json.original_query
      }
    }];
  }

  // Unknown error - return graceful message
  return [{
    json: {
      answer: "I apologize, I'm experiencing technical difficulties. Please try again.",
      error_logged: true
    }
  }];
}

// === LAYER 5: Monitoring & Logging ===
function logMetrics() {
  const startTime = $node["Start"].json.timestamp;
  const endTime = new Date().toISOString();
  const duration = new Date(endTime) - new Date(startTime);

  return [{
    json: {
      event: "query_completed",
      request_id: $node["Start"].json.request_id,
      duration_ms: duration,
      tokens_used: $json.tokens || 0,
      cache_hit: $json.source === "cache",
      success: !$json.error,
      timestamp: endTime
    }
  }];
}

// === Helper Functions ===
function hashString(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash;
  }
  return hash.toString(36);
}

// === Main Execution ===
// Each function would be in a separate Function node
// Connected with IF nodes for flow control
// Try/catch nodes for error handling
// HTTP Request nodes for external services

const validated = validateAndPrepare();
return [{ json: validated }];

// Workflow structure:
// 1. Webhook (entry point)
// 2. Function: validateAndPrepare
// 3. HTTP Request: Check Redis cache
// 4. IF: Cache hit?
//    YES → Return cached result
//    NO → Continue to step 5
// 5. HTTP Request: Generate embedding
// 6. HTTP Request: Vector search (with error handling)
// 7. IF: Search successful?
//    YES → Step 8
//    NO → Function: handleSearchError (fallback)
// 8. HTTP Request: Call LLM with context
// 9. Function: Format response
// 10. HTTP Request: Store in cache
// 11. Function: logMetrics
// 12. Respond to webhook

// This architecture ensures:
// - Clear separation of concerns
// - Error handling at each step
// - Graceful fallbacks
// - Comprehensive monitoring
// - Cacheable results""",
                        "explanation": "Shows how to architect a RAG system in n8n following software engineering principles. Each function has a single responsibility, error handling is comprehensive, and monitoring is built-in. This is production-ready architecture."
                    }
                ],
            },
            "practice": {
                "title": "Design a RAG System Architecture",
                "instructions": """You're building a RAG system for customer support documentation. Design the architecture:

**Requirements:**
- Handle 1000 queries/day
- Response time < 3 seconds
- Documents update weekly
- Need to track costs

**Your Task:**
1. Draw (or describe) the system architecture with layers
2. Identify caching strategy (what to cache, for how long?)
3. Describe error handling (what could fail? What are fallbacks?)
4. Define key metrics to monitor

**Bonus:** Write a Function node that implements circuit breaker logic.""",
                "starterCode": """// Architecture Design:
// TODO: List all system components
// TODO: Define data flow
// TODO: Identify failure points

// Function node: Circuit Breaker Implementation
const operation = $json.operation;

// TODO: Track failures
// TODO: Open circuit after N failures
// TODO: Auto-close circuit after timeout

return [{ json: { allowed: true } }];""",
                "hints": [
                    "Components: API Gateway, Query Processor, Vector DB, LLM, Cache, Monitor",
                    "Cache embeddings (24h), cache query results (1h), cache LLM responses (for temp=0 only)",
                    "Failures: Vector DB timeout → keyword search, LLM rate limit → queue, Both fail → offline message",
                    "Metrics: queries/min, p95 latency, error rate, cost/query, cache hit rate",
                    "Circuit breaker: Track last N results, open if >50% fail, close after 60s"
                ],
                "solution": """// === ARCHITECTURE DESIGN ===

\"\"\"
Customer Support RAG System Architecture
=========================================

LAYER 1: API Gateway
├─ Rate limiter (1000/day = ~1/min per user)
├─ Authentication (API keys)
└─ Input validation

LAYER 2: Processing Layer
├─ Query validation & cleaning
├─ Query classification (technical/billing/general)
└─ Cache checker (Redis)

LAYER 3: AI Layer
├─ Embedding Service (OpenAI)
├─ Vector Search (Pinecone)
└─ LLM Service (GPT-3.5-turbo)

LAYER 4: Storage
├─ Vector DB: Pinecone (1000 docs, 1536 dims)
├─ Cache: Redis (1GB, 24h TTL for embeddings, 1h for queries)
└─ Analytics DB: PostgreSQL (query logs, metrics)

LAYER 5: Monitoring
├─ Logging: Structured JSON logs
├─ Metrics: Latency, error rate, cost/query, cache hit rate
└─ Alerts: Error rate >5%, latency >3s, cost >$10/day
\"\"\"

// CACHING STRATEGY
const CACHE_STRATEGY = {
  document_embeddings: {
    ttl: 604800,  // 7 days (docs update weekly)
    key_pattern: "embed:doc:{doc_id}"
  },
  query_embeddings: {
    ttl: 86400,  // 24 hours
    key_pattern: "embed:query:{hash}"
  },
  query_results: {
    ttl: 3600,  // 1 hour
    key_pattern: "result:{query_hash}",
    condition: "temperature === 0"  // Only cache deterministic
  }
};

// ERROR HANDLING & FALLBACKS
const ERROR_HANDLING = {
  vector_db_failure: {
    fallback: "keyword_search",
    action: "Log error, use PostgreSQL full-text search"
  },
  llm_rate_limit: {
    fallback: "queue_request",
    action: "Add to Redis queue, retry after 60s"
  },
  both_failed: {
    fallback: "offline_message",
    action: "Return: 'Our AI is temporarily unavailable. Email support@company.com'"
  }
};

// KEY METRICS
const METRICS_TO_TRACK = {
  performance: ["p50_latency_ms", "p95_latency_ms", "p99_latency_ms"],
  reliability: ["queries_total", "queries_failed", "error_rate_percent"],
  costs: ["tokens_per_query_avg", "cost_per_query_usd", "daily_cost_usd"],
  efficiency: ["cache_hit_rate_percent", "avg_tokens_retrieved"]
};

// === CIRCUIT BREAKER IMPLEMENTATION ===
// Function node: Circuit Breaker for LLM calls

const WINDOW_SIZE = 10;  // Track last 10 attempts
const FAILURE_THRESHOLD = 0.5;  // Open if 50% fail
const TIMEOUT_MS = 60000;  // Close after 60 seconds

// Get circuit breaker state from previous node or initialize
let circuitState = $node["CircuitBreakerState"]?.json || {
  state: "CLOSED",  // CLOSED, OPEN, HALF_OPEN
  failures: [],
  lastOpened: null
};

function updateCircuitBreaker(success) {
  const now = Date.now();

  // Add result to window
  circuitState.failures.push({
    success: success,
    timestamp: now
  });

  // Keep only last WINDOW_SIZE attempts
  if (circuitState.failures.length > WINDOW_SIZE) {
    circuitState.failures.shift();
  }

  // Calculate failure rate
  const recentFailures = circuitState.failures.filter(f => !f.success).length;
  const failureRate = recentFailures / circuitState.failures.length;

  // State machine logic
  if (circuitState.state === "CLOSED") {
    if (failureRate >= FAILURE_THRESHOLD) {
      circuitState.state = "OPEN";
      circuitState.lastOpened = now;
      console.log("Circuit breaker OPENED - too many failures");
    }
  } else if (circuitState.state === "OPEN") {
    if (now - circuitState.lastOpened > TIMEOUT_MS) {
      circuitState.state = "HALF_OPEN";
      console.log("Circuit breaker HALF_OPEN - attempting recovery");
    }
  } else if (circuitState.state === "HALF_OPEN") {
    if (success) {
      circuitState.state = "CLOSED";
      circuitState.failures = [];
      console.log("Circuit breaker CLOSED - service recovered");
    } else {
      circuitState.state = "OPEN";
      circuitState.lastOpened = now;
      console.log("Circuit breaker OPEN again - recovery failed");
    }
  }

  return circuitState;
}

// Check if we should allow this request
const allowed = circuitState.state !== "OPEN";

return [{
  json: {
    allowed: allowed,
    circuit_state: circuitState.state,
    failure_rate: circuitState.failures.length > 0
      ? circuitState.failures.filter(f => !f.success).length / circuitState.failures.length
      : 0,
    use_fallback: !allowed,
    circuit_breaker_state: circuitState  // Pass to next node
  }
}];

// Usage in workflow:
// 1. Before LLM call → Check circuit breaker
// 2. If allowed === false → Use fallback service
// 3. After LLM call → Update circuit breaker with success/failure
// 4. Circuit auto-recovers after 60s"""
            },
            "keyTakeaways": [
                "System architecture requires thinking beyond individual workflows - design for scale and resilience",
                "Separate concerns into layers: API, Processing, AI, Storage, Monitoring",
                "Implement caching for expensive operations (embeddings, LLM calls) to reduce costs and latency",
                "Always have fallback strategies - vector search fails → keyword search, primary LLM fails → backup LLM",
                "Circuit breakers prevent cascade failures by stopping calls to failing services",
                "Monitor key metrics: latency (p95, p99), error rates, costs, cache hit rates",
                "RAG architecture: Ingest (chunk→embed→store) + Query (embed→search→generate)",
                "Make technology decisions based on your scale: start simple with managed services, optimize when you have data"
            ],
            "resources": [
                {
                    "title": "System Design Primer",
                    "url": "https://github.com/donnemartin/system-design-primer",
                    "type": "guide"
                },
                {
                    "title": "AWS Well-Architected Framework",
                    "url": "https://aws.amazon.com/architecture/well-architected/",
                    "type": "documentation"
                },
                {
                    "title": "RAG System Architecture Patterns",
                    "url": "https://www.pinecone.io/learn/retrieval-augmented-generation/",
                    "type": "article"
                },
                {
                    "title": "Circuit Breaker Pattern",
                    "url": "https://martinfowler.com/bliki/CircuitBreaker.html",
                    "type": "article"
                }
            ]
        })

        break

# Save the updated data
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'w') as f:
    json.dump(course_data, f, indent=2)

print("Day 25 completed successfully!")
print("Now adding Days 26-30...")
