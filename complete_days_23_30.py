#!/usr/bin/env python3
"""
Complete Days 23-30 with production-ready content matching Days 1-22 quality.
"""

import json

# Read the current courseData.json
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'r') as f:
    course_data = json.load(f)

# Find Week 4 and update Days 23-30
for week in course_data['weeks']:
    if week['weekNumber'] == 4:
        # Clear existing days and add complete content
        week['days'] = [
            {
                "dayNumber": 23,
                "title": "Reading AI Code",
                "duration": "30 minutes",
                "learningObjectives": [
                    "Read and understand LangChain source code",
                    "Trace data flow through AI library functions",
                    "Understand embeddings in code context",
                    "Recognize common AI code patterns"
                ],
                "content": {
                    "theory": """Reading AI library code is a crucial skill for building production AI systems. Unlike writing code from scratch, reading existing AI libraries like LangChain, OpenAI SDK, and Transformers teaches you best practices, common patterns, and how professional AI systems are architected.

**Why Read AI Code?**
- **Learn Patterns**: See how experts structure AI workflows
- **Understand Internals**: Know what's happening under the hood
- **Debug Effectively**: Trace issues through library code
- **Customize Confidently**: Modify libraries when needed

**Key Skills for Reading AI Code:**

**1. Identifying Model Initialization:**
Look for where AI models are created and configured. Common patterns include client initialization (OpenAI, Anthropic), model loading (Transformers), and configuration objects.

**2. Understanding Prompt Templates:**
AI libraries use template systems to inject variables into prompts. LangChain's PromptTemplate, f-strings in Python, and template literals in JavaScript are common approaches.

**3. Tracing Data Flow:**
Follow data from input → processing → model call → output. Look for:
- Input validation and preprocessing
- API call construction
- Response parsing and post-processing
- Error handling

**4. Recognizing Common Patterns:**
- **Chains**: Sequential processing steps (LangChain chains)
- **Agents**: Decision-making loops with tool use
- **Retrievers**: Vector database queries
- **Callbacks**: Logging, streaming, monitoring

**5. Reading Embeddings Code:**
Embeddings convert text to vectors. Look for:
- Tokenization (breaking text into tokens)
- Model calls to embedding endpoints
- Vector normalization
- Batch processing for efficiency

**How to Approach AI Library Code:**

1. **Start with Examples**: Read library examples before source code
2. **Follow One Path**: Trace a single function call from start to finish
3. **Use Debuggers**: Step through code with breakpoints
4. **Read Documentation**: Cross-reference code with docs
5. **Experiment**: Modify and test to understand behavior""",
                    "concepts": [
                        {
                            "name": "Reading OpenAI SDK Code",
                            "explanation": "The OpenAI Python SDK provides clean patterns for API calls. Understanding client initialization, chat completion structure, and response handling.",
                            "example": """# Reading OpenAI SDK code patterns
from openai import OpenAI

# Client initialization - stores API key and defaults
client = OpenAI(api_key="sk-...")

# Chat completion call - notice the clean structure
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are helpful."},
        {"role": "user", "content": "Hello!"}
    ],
    temperature=0.7
)

# Response structure - access nested attributes
message_content = response.choices[0].message.content
tokens_used = response.usage.total_tokens

# Key pattern: response.choices[0].message.content
# Always check response.choices array"""
                        },
                        {
                            "name": "Understanding LangChain Chains",
                            "explanation": "LangChain chains connect multiple steps. Reading chain code reveals how data flows from prompt → model → parser → output.",
                            "example": """# Reading LangChain chain code
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

# 1. Prompt template - notice {variable} syntax
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write 3 facts about {topic}"
)

# 2. LLM initialization
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# 3. Chain combines prompt + model
chain = LLMChain(llm=llm, prompt=prompt)

# 4. Execution - input goes through: prompt → llm → output
result = chain.run(topic="Python")

# Data flow: topic → PromptTemplate.format() → ChatOpenAI.predict() → string result"""
                        },
                        {
                            "name": "Tracing Embedding Generation",
                            "explanation": "Embeddings are generated by calling embedding models. Understanding the flow: text → tokenization → model → vector array.",
                            "example": """# Reading embedding generation code
from openai import OpenAI

client = OpenAI(api_key="sk-...")

def generate_embedding(text, model="text-embedding-ada-002"):
    \"\"\"Generate embedding vector for text.\"\"\"

    # Replace newlines (OpenAI best practice)
    text = text.replace("\\n", " ")

    # Call embedding API - notice .embeddings endpoint
    response = client.embeddings.create(
        input=[text],  # Can batch multiple texts
        model=model
    )

    # Extract vector from response
    # Structure: response.data[0].embedding
    embedding = response.data[0].embedding  # List of 1536 floats

    return embedding

# Usage
vector = generate_embedding("AI is amazing")
print(f"Vector length: {len(vector)}")  # 1536 for ada-002

# Key insight: embeddings are just lists of floats representing semantic meaning"""
                        },
                        {
                            "name": "Recognizing AI Code Patterns",
                            "explanation": "Professional AI code follows common patterns: retry logic, error handling, streaming responses, and token counting.",
                            "example": """# Common AI code patterns to recognize

import time
from openai import OpenAI, RateLimitError

client = OpenAI()

def call_with_retry(messages, max_retries=3):
    \"\"\"Pattern: Retry logic for rate limits.\"\"\"
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            return response
        except RateLimitError:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                time.sleep(wait_time)
            else:
                raise

# Pattern: Streaming responses
def stream_response(messages):
    \"\"\"Pattern: Stream tokens as they arrive.\"\"\"
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True  # Enable streaming
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")

# Pattern: Token counting before API call
import tiktoken

def count_tokens(text, model="gpt-3.5-turbo"):
    \"\"\"Pattern: Count tokens to avoid limits.\"\"\"
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))"""
                        }
                    ],
                    "codeExamples": [
                        {
                            "title": "Reading and Modifying LangChain Source",
                            "language": "python",
                            "code": """# Example: Understanding LangChain's TextSplitter
# This shows how to read library code and create custom versions

from langchain.text_splitter import RecursiveCharacterTextSplitter

# Original LangChain code (simplified version of what you'd see in source)
class CustomTextSplitter:
    \"\"\"Custom splitter based on reading LangChain source.\"\"\"

    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        # Reading the code shows these separators tried in order
        self.separators = ["\\n\\n", "\\n", " ", ""]

    def split_text(self, text):
        \"\"\"Split text recursively using separators.\"\"\"
        chunks = []

        # Try each separator until chunks are small enough
        for separator in self.separators:
            if separator == "":
                # Base case: split into characters
                return self._split_by_size(text)

            # Split by current separator
            splits = text.split(separator)

            for split in splits:
                if len(split) <= self.chunk_size:
                    chunks.append(split)
                else:
                    # Recursively split large chunks
                    sub_chunks = self._split_large_chunk(split, separator)
                    chunks.extend(sub_chunks)

        return chunks

    def _split_by_size(self, text):
        \"\"\"Create chunks of exact size (fallback).\"\"\"
        return [text[i:i+self.chunk_size]
                for i in range(0, len(text), self.chunk_size - self.chunk_overlap)]

    def _split_large_chunk(self, text, separator):
        \"\"\"Handle chunks that are still too large.\"\"\"
        # Continue with next separator in list
        next_sep_idx = self.separators.index(separator) + 1
        if next_sep_idx < len(self.separators):
            next_sep = self.separators[next_sep_idx]
            return text.split(next_sep)
        return [text]

# Usage - now you understand how it works internally
splitter = CustomTextSplitter(chunk_size=500, chunk_overlap=50)
text = "Your long document here..." * 100
chunks = splitter.split_text(text)
print(f"Created {len(chunks)} chunks by reading and understanding the source")""",
                            "explanation": "This example shows how reading LangChain's RecursiveCharacterTextSplitter source code helps you understand the recursive splitting algorithm. You can then create custom versions or debug issues."
                        },
                        {
                            "title": "Debugging OpenAI API Calls by Reading SDK",
                            "language": "python",
                            "code": """# Example: Debug OpenAI calls by understanding SDK internals
import json
from openai import OpenAI

client = OpenAI(api_key="sk-...")

def debug_chat_call(messages, model="gpt-3.5-turbo"):
    \"\"\"
    Debug OpenAI calls by inspecting request/response.
    Reading SDK code shows these are the key components.
    \"\"\"

    print("=== REQUEST DEBUG ===")
    print(f"Model: {model}")
    print(f"Messages: {json.dumps(messages, indent=2)}")

    # Make the call
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7
        )

        print("\\n=== RESPONSE DEBUG ===")
        # Reading SDK source shows response structure
        print(f"Response ID: {response.id}")
        print(f"Model used: {response.model}")
        print(f"Created at: {response.created}")

        # Choices array - SDK always returns array
        choice = response.choices[0]
        print(f"\\nFinish reason: {choice.finish_reason}")
        print(f"Message role: {choice.message.role}")
        print(f"Message content: {choice.message.content}")

        # Usage object - critical for monitoring costs
        print(f"\\nTokens - Prompt: {response.usage.prompt_tokens}")
        print(f"Tokens - Completion: {response.usage.completion_tokens}")
        print(f"Tokens - Total: {response.usage.total_tokens}")

        # Estimate cost (reading docs + code helps you understand pricing)
        cost_per_1k = 0.002  # GPT-3.5-turbo pricing
        estimated_cost = (response.usage.total_tokens / 1000) * cost_per_1k
        print(f"Estimated cost: ${estimated_cost:.6f}")

        return response.choices[0].message.content

    except Exception as e:
        print(f"\\n=== ERROR DEBUG ===")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")

        # Reading SDK code shows common error types
        if "rate_limit" in str(e).lower():
            print("Suggestion: Implement exponential backoff retry")
        elif "invalid_api_key" in str(e).lower():
            print("Suggestion: Check OPENAI_API_KEY environment variable")
        elif "context_length_exceeded" in str(e).lower():
            print("Suggestion: Reduce message length or use longer context model")

        raise

# Test it
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain embeddings in one sentence."}
]

result = debug_chat_call(messages)""",
                            "explanation": "By reading the OpenAI SDK source code, you understand the exact structure of requests and responses. This makes debugging much easier - you know what fields to inspect and common error patterns."
                        },
                        {
                            "title": "Understanding Embeddings in Vector Search Code",
                            "language": "python",
                            "code": """# Example: Read and understand embedding + search code
import numpy as np
from openai import OpenAI

client = OpenAI(api_key="sk-...")

class SimpleVectorStore:
    \"\"\"
    Simple vector store showing how embeddings work.
    Reading this helps understand Pinecone, Weaviate, etc.
    \"\"\"

    def __init__(self):
        self.documents = []  # Store original text
        self.embeddings = []  # Store vectors

    def add_document(self, text):
        \"\"\"Add document by generating and storing embedding.\"\"\"
        # Generate embedding - reading SDK shows this pattern
        embedding = self._generate_embedding(text)

        self.documents.append(text)
        self.embeddings.append(embedding)

        print(f"Added: '{text[:50]}...' (vector length: {len(embedding)})")

    def search(self, query, top_k=3):
        \"\"\"Find similar documents using cosine similarity.\"\"\"
        if not self.embeddings:
            return []

        # Generate query embedding
        query_embedding = self._generate_embedding(query)

        # Calculate similarity with all documents
        similarities = []
        for idx, doc_embedding in enumerate(self.embeddings):
            similarity = self._cosine_similarity(query_embedding, doc_embedding)
            similarities.append((idx, similarity))

        # Sort by similarity (highest first)
        similarities.sort(key=lambda x: x[1], reverse=True)

        # Return top_k results
        results = []
        for idx, score in similarities[:top_k]:
            results.append({
                'text': self.documents[idx],
                'score': score
            })

        return results

    def _generate_embedding(self, text):
        \"\"\"Generate embedding using OpenAI API.\"\"\"
        response = client.embeddings.create(
            input=text.replace("\\n", " "),
            model="text-embedding-ada-002"
        )
        return response.data[0].embedding

    def _cosine_similarity(self, vec1, vec2):
        \"\"\"Calculate cosine similarity between two vectors.\"\"\"
        # Reading vector DB code shows this is the standard formula
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)

        dot_product = np.dot(vec1, vec2)
        magnitude = np.linalg.norm(vec1) * np.linalg.norm(vec2)

        return dot_product / magnitude

# Usage example
vector_store = SimpleVectorStore()

# Add documents
vector_store.add_document("Python is a programming language for AI")
vector_store.add_document("JavaScript is used for web development")
vector_store.add_document("Machine learning uses Python and TensorFlow")

# Search
results = vector_store.search("AI programming languages", top_k=2)

print("\\n=== Search Results ===")
for result in results:
    print(f"Score: {result['score']:.4f}")
    print(f"Text: {result['text']}")
    print()""",
                            "explanation": "This code shows how vector databases work internally. By reading this pattern, you can understand how Pinecone, Weaviate, and other vector DBs use embeddings and cosine similarity for semantic search."
                        },
                        {
                            "title": "n8n Function Node: Call Python AI Script",
                            "language": "javascript",
                            "code": """// n8n Function node: Prepare data for Python AI script
// This shows how to read Python code and integrate it with n8n

const inputText = $json.text || "";

// Reading Python AI scripts shows they expect this JSON structure
const pythonInput = {
  text: inputText,
  operation: "analyze",
  options: {
    model: "gpt-3.5-turbo",
    max_tokens: 500,
    temperature: 0.7
  }
};

// Python scripts read from stdin, so we need to format properly
// Reading examples shows JSON string on single line is expected
const formattedInput = JSON.stringify(pythonInput);

// Return in format for Execute Command node
return [{
  json: {
    command: "python3",
    arguments: ["/path/to/ai_script.py"],
    stdin: formattedInput
  }
}];

// After Execute Command runs Python script, another Function node parses output:
// const pythonOutput = JSON.parse($json.stdout);
// return [{ json: pythonOutput }];""",
                            "explanation": "Reading Python AI scripts helps you understand they expect JSON on stdin and return JSON on stdout. This Function node shows how to prepare data for Python from n8n by studying the code patterns."
                        }
                    ]
                },
                "practice": {
                    "title": "Read and Understand a Real AI Code Snippet",
                    "instructions": """You've been given this LangChain code snippet from a real project. Read it carefully and answer:

1. What does this code do?
2. Trace the data flow: what happens to the user's query?
3. What would you modify to change the chunk size?
4. What happens if no documents are found?

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Setup
embeddings = OpenAIEmbeddings()
vectorstore = Pinecone.from_existing_index("my-index", embeddings)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)

# Use it
result = qa_chain.run("What is RAG?")
```

Write your analysis, then create a simple n8n Function node that prepares a query for a similar Python script.""",
                    "starterCode": """// n8n Function node: Prepare data for RAG query
const userQuery = $json.query || "";

// TODO: Create object with query and configuration
// TODO: Match the structure you observed in the Python code
// TODO: Return formatted for Execute Command node

return [{ json: {} }];""",
                    "hints": [
                        "The code creates embeddings, connects to Pinecone, and uses a QA chain",
                        "Data flow: query → retriever finds docs → stuff them in prompt → LLM answers",
                        "search_kwargs={'k': 3} controls how many chunks are retrieved",
                        "RetrievalQA handles the case when no docs are found (uses LLM without context)",
                        "Your Function node should pass the query and k value to Python"
                    ],
                    "solution": """// n8n Function node: Prepare RAG query for Python
const userQuery = $json.query || "";

// Structure matching what the Python RAG script expects
const ragInput = {
  query: userQuery,
  retrieval_config: {
    top_k: 3,  // How many documents to retrieve
    score_threshold: 0.7  // Minimum similarity score
  },
  llm_config: {
    model: "gpt-3.5-turbo",
    temperature: 0,  // Deterministic for RAG
    max_tokens: 500
  }
};

// Format for Execute Command node
return [{
  json: {
    command: "python3",
    arguments: ["rag_query.py"],
    stdin: JSON.stringify(ragInput)
  }
}];

// Analysis:
// 1. This code sets up a RAG system using Pinecone vector DB
// 2. Data flow: query → embedding → vector search → retrieve 3 docs → combine with query → LLM
// 3. Change search_kwargs={"k": 5} to retrieve 5 chunks instead of 3
// 4. If no docs found, RetrievalQA falls back to LLM answering without context"""
                },
                "keyTakeaways": [
                    "Reading AI library code teaches you professional patterns and best practices",
                    "Always trace data flow: input → processing → API call → output → parsing",
                    "OpenAI SDK pattern: response.choices[0].message.content for chat responses",
                    "LangChain chains connect: PromptTemplate → LLM → OutputParser",
                    "Embeddings are generated via API calls and returned as float arrays (vectors)",
                    "Common patterns to recognize: retry logic, streaming, token counting, error handling",
                    "Vector search uses cosine similarity between query embedding and document embeddings",
                    "Reading code helps you debug issues and customize libraries confidently"
                ],
                "resources": [
                    {
                        "title": "LangChain Source Code (GitHub)",
                        "url": "https://github.com/langchain-ai/langchain",
                        "type": "code"
                    },
                    {
                        "title": "OpenAI Python SDK Source",
                        "url": "https://github.com/openai/openai-python",
                        "type": "code"
                    },
                    {
                        "title": "How to Read Code Effectively",
                        "url": "https://www.freecodecamp.org/news/how-to-read-code/",
                        "type": "article"
                    },
                    {
                        "title": "LangChain Expression Language (LCEL)",
                        "url": "https://python.langchain.com/docs/expression_language/",
                        "type": "documentation"
                    }
                ]
            },
            # Day 24 will go here
            {
                "dayNumber": 24,
                "title": "Python + n8n Integration",
                "duration": "30 minutes",
                "learningObjectives": [
                    "Execute Python scripts from n8n workflows",
                    "Pass data between n8n and Python via JSON",
                    "Handle Python virtual environments",
                    "Build HTTP endpoints for Python AI services"
                ],
                "content": {
                    "theory": """Combining n8n's workflow automation with Python's AI capabilities creates powerful systems. While n8n excels at orchestration, Python provides access to advanced AI libraries like LangChain, Transformers, and specialized ML tools.

**Integration Methods:**

**1. Execute Command Node (Local Scripts):**
- Run Python scripts directly from n8n
- Pass data via stdin/stdout
- Best for: Self-hosted n8n, simple scripts
- Limitation: Doesn't work on n8n Cloud

**2. HTTP Request Node (Python APIs):**
- Call Python FastAPI/Flask endpoints
- Pass data via JSON HTTP requests
- Best for: Production systems, n8n Cloud
- Most scalable and maintainable approach

**3. Webhooks (Python → n8n):**
- Python services trigger n8n workflows
- Useful for: Event-driven architectures
- Example: ML model completes → webhook → n8n notifies users

**Data Exchange Pattern:**

```
n8n → JSON → Python → Process → JSON → n8n
```

**Key Concepts:**

**Virtual Environments:**
Python projects use virtual environments (venv) to isolate dependencies. Essential for avoiding package conflicts when running multiple AI projects.

**JSON Serialization:**
Both n8n and Python use JSON for data exchange. Understanding JSON conversion is critical:
- n8n: JavaScript objects (automatic)
- Python: `json.loads()` (string → dict) and `json.dumps()` (dict → string)

**Error Handling:**
Production integrations need robust error handling:
- Catch Python exceptions
- Return error details to n8n
- Implement retry logic in n8n
- Log errors for debugging

**Environment Variables:**
Store API keys and secrets in environment variables, not code:
- n8n: Built-in credential system
- Python: `os.getenv()` or `python-dotenv`

**Common Integration Patterns:**

1. **Text Processing**: n8n sends text → Python chunks/cleans → returns processed
2. **AI Inference**: n8n provides input → Python calls model → returns prediction
3. **Embedding Generation**: n8n sends documents → Python generates embeddings → returns vectors
4. **RAG Query**: n8n provides question → Python searches vectors + calls LLM → returns answer""",
                    "concepts": [
                        {
                            "name": "Python Script with stdin/stdout",
                            "explanation": "Python scripts can receive JSON from n8n via stdin and return results via stdout. This is the simplest integration for self-hosted n8n.",
                            "example": """# process_text.py - Python script for n8n Execute Command
import json
import sys

def main():
    # Read input from n8n (via stdin)
    input_json = sys.stdin.read()
    input_data = json.loads(input_json)

    # Extract data
    text = input_data.get('text', '')
    operation = input_data.get('operation', 'count_words')

    # Process based on operation
    if operation == 'count_words':
        result = {
            'word_count': len(text.split()),
            'char_count': len(text),
            'line_count': len(text.splitlines())
        }
    elif operation == 'uppercase':
        result = {'text': text.upper()}
    else:
        result = {'error': f'Unknown operation: {operation}'}

    # Return to n8n (via stdout)
    print(json.dumps(result))

if __name__ == '__main__':
    main()

# Usage in n8n Execute Command node:
# Command: python3
# Arguments: /path/to/process_text.py
# stdin: {{ $json }}"""
                        },
                        {
                            "name": "FastAPI Endpoint for AI Services",
                            "explanation": "Create HTTP API endpoints with FastAPI to expose Python AI capabilities to n8n. This works with n8n Cloud and is production-ready.",
                            "example": """# ai_service.py - FastAPI service for n8n
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class ChatRequest(BaseModel):
    message: str
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7

class ChatResponse(BaseModel):
    response: str
    tokens_used: int

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model=request.model,
            messages=[{"role": "user", "content": request.message}],
            temperature=request.temperature
        )

        return ChatResponse(
            response=response.choices[0].message.content,
            tokens_used=response.usage.total_tokens
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run with: uvicorn ai_service:app --host 0.0.0.0 --port 8000
# n8n calls: POST http://your-server:8000/chat
# Body: {"message": "Hello!", "temperature": 0.9}"""
                        },
                        {
                            "name": "n8n HTTP Request to Python",
                            "explanation": "From n8n, call Python HTTP endpoints using the HTTP Request node. This is the most versatile integration method.",
                            "example": """// n8n Function node: Prepare data for Python API
const userMessage = $json.message || "Hello";

// Prepare request for Python FastAPI service
const apiRequest = {
  message: userMessage,
  model: "gpt-3.5-turbo",
  temperature: 0.7,
  max_tokens: 500
};

return [{
  json: apiRequest
}];

// Then use HTTP Request node:
// Method: POST
// URL: http://your-python-service:8000/chat
// Body: {{ $json }}
// Headers: Content-Type: application/json

// Next Function node processes response:
// const aiResponse = $json.response;
// const tokens = $json.tokens_used;
// return [{ json: { answer: aiResponse, cost: tokens * 0.000002 } }];"""
                        },
                        {
                            "name": "Environment Setup and Dependencies",
                            "explanation": "Proper Python environment setup ensures your AI scripts have the right dependencies isolated from other projects.",
                            "example": """# Terminal: Setup Python environment for n8n integration

# 1. Create virtual environment
python3 -m venv ai_env

# 2. Activate environment
# Linux/Mac:
source ai_env/bin/activate
# Windows:
ai_env\\\\Scripts\\\\activate

# 3. Install dependencies
pip install openai langchain fastapi uvicorn python-dotenv

# 4. Create requirements.txt for version control
pip freeze > requirements.txt

# 5. Create .env file for secrets
cat > .env << EOF
OPENAI_API_KEY=sk-your-key-here
PINECONE_API_KEY=your-pinecone-key
EOF

# 6. Run your service
uvicorn ai_service:app --reload

# In your Python code, load environment:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')"""
                        }
                    ],
                    "codeExamples": [
                        {
                            "title": "Complete Python → n8n Integration: Text Chunking Service",
                            "language": "python",
                            "code": """# chunk_service.py - FastAPI service for document chunking
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

app = FastAPI(title="Text Chunking Service")

class ChunkRequest(BaseModel):
    text: str
    chunk_size: int = 1000
    chunk_overlap: int = 200

class ChunkResponse(BaseModel):
    chunks: List[str]
    chunk_count: int
    avg_chunk_length: float

@app.post("/chunk", response_model=ChunkResponse)
async def chunk_text(request: ChunkRequest):
    \"\"\"
    Chunk text using LangChain's splitter.
    Called from n8n HTTP Request node.
    \"\"\"
    try:
        # Initialize splitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=request.chunk_size,
            chunk_overlap=request.chunk_overlap,
            separators=["\\n\\n", "\\n", ". ", " ", ""]
        )

        # Split text
        chunks = splitter.split_text(request.text)

        # Calculate stats
        avg_length = sum(len(c) for c in chunks) / len(chunks) if chunks else 0

        return ChunkResponse(
            chunks=chunks,
            chunk_count=len(chunks),
            avg_chunk_length=round(avg_length, 2)
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chunking failed: {str(e)}")

@app.get("/health")
async def health_check():
    \"\"\"Health check endpoint for monitoring.\"\"\"
    return {"status": "healthy", "service": "chunk_service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Install: pip install fastapi uvicorn langchain
# Run: python chunk_service.py
# Test: curl -X POST http://localhost:8000/chunk -H "Content-Type: application/json" -d '{"text":"Long document..."}'""",
                            "explanation": "Complete FastAPI service that chunks text for n8n. Exposes HTTP endpoint that n8n can call with HTTP Request node. Includes error handling, type validation, and health check."
                        },
                        {
                            "title": "n8n Workflow: Call Python Chunking Service",
                            "language": "javascript",
                            "code": """// n8n Function node 1: Prepare document for chunking
const documentText = $json.content || "";

// Configure chunking parameters
const chunkConfig = {
  text: documentText,
  chunk_size: 1000,
  chunk_overlap: 200
};

return [{ json: chunkConfig }];

// --- HTTP Request Node Configuration ---
// Method: POST
// URL: http://your-python-server:8000/chunk
// Body Content Type: JSON
// Body: {{ $json }}

// --- Function node 2: Process chunked response ---
const chunks = $json.chunks || [];
const chunkCount = $json.chunk_count || 0;

// Create separate item for each chunk (useful for parallel processing)
const items = chunks.map((chunk, index) => ({
  json: {
    chunk_index: index,
    chunk_text: chunk,
    total_chunks: chunkCount,
    chunk_length: chunk.length
  }
}));

return items;

// Now each chunk is a separate item in the workflow
// You can process them in parallel (e.g., generate embeddings)""",
                            "explanation": "Complete n8n workflow showing how to call the Python chunking service. First Function prepares data, HTTP Request calls Python, second Function processes response and splits chunks into separate items for parallel processing."
                        },
                        {
                            "title": "Python Embedding Service with Error Handling",
                            "language": "python",
                            "code": """# embedding_service.py - Production-ready embedding service
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional
from openai import OpenAI, RateLimitError, APIError
import os
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Embedding Service")
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

class EmbedRequest(BaseModel):
    texts: List[str]
    model: str = "text-embedding-ada-002"

class EmbedResponse(BaseModel):
    embeddings: List[List[float]]
    total_tokens: int
    model: str

def generate_embeddings_with_retry(texts: List[str], model: str, max_retries: int = 3):
    \"\"\"Generate embeddings with exponential backoff retry.\"\"\"

    for attempt in range(max_retries):
        try:
            # Clean texts (OpenAI recommendation)
            cleaned_texts = [text.replace("\\n", " ") for text in texts]

            # Call API
            response = client.embeddings.create(
                input=cleaned_texts,
                model=model
            )

            # Extract embeddings
            embeddings = [item.embedding for item in response.data]
            total_tokens = response.usage.total_tokens

            logger.info(f"Generated {len(embeddings)} embeddings using {total_tokens} tokens")

            return embeddings, total_tokens

        except RateLimitError as e:
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt) + 1  # Exponential backoff: 2, 5, 9 seconds
                logger.warning(f"Rate limit hit, retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logger.error("Max retries reached for rate limit")
                raise HTTPException(status_code=429, detail="Rate limit exceeded after retries")

        except APIError as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise HTTPException(status_code=502, detail=f"OpenAI API error: {str(e)}")

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Embedding generation failed: {str(e)}")

@app.post("/embed", response_model=EmbedResponse)
async def create_embeddings(request: EmbedRequest):
    \"\"\"Generate embeddings for a list of texts.\"\"\"

    if not request.texts:
        raise HTTPException(status_code=400, detail="No texts provided")

    if len(request.texts) > 100:
        raise HTTPException(status_code=400, detail="Maximum 100 texts per request")

    embeddings, total_tokens = generate_embeddings_with_retry(
        request.texts,
        request.model
    )

    return EmbedResponse(
        embeddings=embeddings,
        total_tokens=total_tokens,
        model=request.model
    )

@app.get("/health")
async def health():
    return {"status": "healthy"}

# Run: uvicorn embedding_service:app --host 0.0.0.0 --port 8001""",
                            "explanation": "Production-ready embedding service with proper error handling, retry logic, logging, and input validation. Shows professional patterns for Python AI services that integrate with n8n."
                        },
                        {
                            "title": "n8n Function: Batch Process with Python API",
                            "language": "javascript",
                            "code": """// n8n Function node: Batch process items with Python API
// This handles multiple documents and batches them efficiently

const documents = $input.all();  // Get all items from previous node

// Extract texts from all documents
const texts = documents.map(item => item.json.content || item.json.text || "");

// Batch into groups of 20 (OpenAI embedding API limit is ~100)
const batchSize = 20;
const batches = [];

for (let i = 0; i < texts.length; i += batchSize) {
  batches.push(texts.slice(i, i + batchSize));
}

// Prepare API calls for each batch
const apiCalls = batches.map((batch, batchIndex) => ({
  json: {
    texts: batch,
    model: "text-embedding-ada-002",
    batch_index: batchIndex,
    total_batches: batches.length
  }
}));

return apiCalls;

// Next: HTTP Request node calls Python embedding service for each batch
// Then: Function node combines results

// --- Combine results Function node: ---
// const allBatches = $input.all();
// const allEmbeddings = allBatches.flatMap(batch => batch.json.embeddings);
// const totalTokens = allBatches.reduce((sum, batch) => sum + batch.json.total_tokens, 0);
//
// return [{
//   json: {
//     embeddings: allEmbeddings,
//     total_embeddings: allEmbeddings.length,
//     total_tokens: totalTokens,
//     estimated_cost: (totalTokens / 1000) * 0.0001  // ada-002 pricing
//   }
// }];""",
                            "explanation": "Shows how to batch process large numbers of items through Python API from n8n. Handles splitting into batches, making parallel API calls, and combining results. Essential pattern for production AI workflows."
                        }
                    ]
                },
                "practice": {
                    "title": "Build a Python AI Service and Call it from n8n",
                    "instructions": """Create a simple Python FastAPI service and integrate it with n8n:

**Part 1: Python Service (sentiment_service.py)**
Create a FastAPI endpoint that:
1. Accepts a text string
2. Counts positive words ("good", "great", "excellent", "amazing")
3. Counts negative words ("bad", "poor", "terrible", "awful")
4. Returns sentiment score and label (positive/negative/neutral)

**Part 2: n8n Integration**
Create a Function node that:
1. Takes input text from $json.text
2. Prepares it for the Python API
3. Would call POST /analyze endpoint
4. (Simulate the response processing)

Test with: "This is a great and amazing product!" (should be positive)""",
                    "starterCode": """# sentiment_service.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SentimentRequest(BaseModel):
    text: str

# TODO: Create /analyze endpoint
# TODO: Count positive and negative words
# TODO: Calculate sentiment score
# TODO: Return result

# n8n Function node:
// const inputText = $json.text || "";
// TODO: Prepare request object
// TODO: Return formatted for HTTP Request node
// return [{ json: {} }];""",
                    "hints": [
                        "Use text.lower().split() to get words",
                        "Define positive_words = ['good', 'great', 'excellent', 'amazing']",
                        "Score = (positive_count - negative_count)",
                        "Label: score > 0 = 'positive', score < 0 = 'negative', else 'neutral'",
                        "n8n Function should return object with 'text' field"
                    ],
                    "solution": """# sentiment_service.py - Complete solution
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    score: int
    positive_count: int
    negative_count: int

@app.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest):
    text = request.text.lower()
    words = text.split()

    positive_words = ["good", "great", "excellent", "amazing", "wonderful", "fantastic"]
    negative_words = ["bad", "poor", "terrible", "awful", "horrible", "disappointing"]

    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)

    score = pos_count - neg_count

    if score > 0:
        sentiment = "positive"
    elif score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return SentimentResponse(
        sentiment=sentiment,
        score=score,
        positive_count=pos_count,
        negative_count=neg_count
    )

@app.get("/health")
async def health():
    return {"status": "healthy"}

# Run: uvicorn sentiment_service:app --port 8000 --reload

# --- n8n Function Node Solution ---
// Prepare data for Python sentiment API
const inputText = $json.text || "";

const sentimentRequest = {
  text: inputText
};

return [{ json: sentimentRequest }];

// Then HTTP Request node:
// POST http://localhost:8000/analyze
// Body: {{ $json }}

// Process response:
// const result = $json;
// return [{
//   json: {
//     original_text: inputText,
//     sentiment: result.sentiment,
//     score: result.score,
//     details: `Found ${result.positive_count} positive and ${result.negative_count} negative words`
//   }
// }];"""
                },
                "keyTakeaways": [
                    "Python + n8n integration combines workflow automation with advanced AI capabilities",
                    "Two main methods: Execute Command (local) and HTTP Request (production/cloud)",
                    "FastAPI is ideal for creating Python AI services that n8n can call via HTTP",
                    "Always use JSON for data exchange between n8n and Python",
                    "Virtual environments (venv) isolate Python dependencies per project",
                    "Production services need error handling, retry logic, and logging",
                    "Batch processing efficiently handles large numbers of items through Python APIs",
                    "Store API keys in environment variables, never hardcode them"
                ],
                "resources": [
                    {
                        "title": "FastAPI Documentation",
                        "url": "https://fastapi.tiangolo.com/",
                        "type": "documentation"
                    },
                    {
                        "title": "n8n Execute Command Node",
                        "url": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/",
                        "type": "documentation"
                    },
                    {
                        "title": "Python Virtual Environments Guide",
                        "url": "https://docs.python.org/3/tutorial/venv.html",
                        "type": "tutorial"
                    },
                    {
                        "title": "Building APIs with FastAPI (Video)",
                        "url": "https://www.youtube.com/watch?v=0sOvCWFmrtA",
                        "type": "video"
                    }
                ]
            }
        ]
        break

# Save the updated courseData
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'w') as f:
    json.dump(course_data, f, indent=2)

print("Days 23-24 completed! Continuing with Days 25-30...")
