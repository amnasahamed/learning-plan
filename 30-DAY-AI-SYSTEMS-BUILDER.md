# ⚡️ 30-Day AI Systems Builder Path

> Transform from automation beginner to AI systems architect in just 30 days

## 📋 Overview

**Time Commitment**: 30 minutes/day or 3-4 hours/week
**Learning Style**: Learn → Apply → Build → Ship
**End Goal**: Build production-ready AI automation systems

## 🎯 What You'll Achieve

By day 30, you'll be able to:
- ✅ Write & debug Function nodes with confidence
- ✅ Build complex multi-step API workflows
- ✅ Create intelligent AI agents with memory & caching
- ✅ Design scalable RAG/CAG architectures
- ✅ Read, adapt, and deploy Python AI scripts
- ✅ Think in systems: orchestration, data flow, error handling

---

## 🛠️ Prerequisites & Setup

### Required (Start Here)
- [ ] Create free n8n cloud account at [n8n.io](https://n8n.io)
- [ ] Set up API keys (at least one):
  - OpenAI API key (with $5 credit) OR
  - Google Gemini API key (free tier)
- [ ] Install VS Code or any code editor
- [ ] Create GitHub account (for saving workflows)

### Recommended Tools
- [ ] [Postman](https://www.postman.com/) - API testing
- [ ] [Replit](https://replit.com/) or [CodeSandbox](https://codesandbox.io/) - Quick JS testing
- [ ] [Python](https://python.org) installed locally (3.9+)
- [ ] ChatGPT/Claude for code explanations

---

## 📚 Core Resources

**JavaScript**
- [JavaScript.info](https://javascript.info) - Chapters 1-6 (fundamentals)
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - Reference

**n8n Specific**
- [n8n Documentation](https://docs.n8n.io)
- [n8n Function Node Guide](https://docs.n8n.io/code-examples/expressions/function-nodes/)
- [n8n Community](https://community.n8n.io)

**AI/APIs**
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Google Gemini API](https://ai.google.dev/docs)

---

## 🗓️ WEEK 1: JavaScript for Automations

### Goal
Master JavaScript fundamentals needed for n8n Function nodes

### What You'll Build This Week
- **Mini-Project**: Data transformer that cleans & formats API responses
- **Deliverable**: Reusable n8n workflow template

### Daily Breakdown

#### Day 1: Variables & Data Types
**Learn** (15 min)
- `const`, `let`, and when to use each
- Strings, numbers, booleans
- Template literals: `` `Hello ${name}` ``

**Practice** (15 min)
```javascript
// In n8n Function node:
const name = "AI Builder";
const dailyGoal = 30;
return [{
  json: {
    message: `${name} - Day ${dailyGoal} mins`
  }
}];
```

**Task**: Create a Function node that takes input data and adds a timestamp

---

#### Day 2: Arrays & Array Methods
**Learn** (15 min)
- Creating arrays: `[1, 2, 3]`
- `.map()`, `.filter()`, `.find()`
- Array destructuring

**Practice** (15 min)
```javascript
// Filter items over a threshold
const items = $input.all();
const filtered = items
  .map(item => item.json)
  .filter(data => data.price > 100);

return filtered.map(item => ({ json: item }));
```

**Task**: Filter a list of todos to only show incomplete items

---

#### Day 3: Objects & JSON
**Learn** (15 min)
- Object syntax: `{ key: value }`
- Accessing properties: `obj.key` vs `obj['key']`
- Nested objects
- `Object.keys()`, `Object.values()`

**Practice** (15 min)
```javascript
// Restructure API response
const input = $json;
return [{
  json: {
    id: input.userId,
    fullName: `${input.firstName} ${input.lastName}`,
    metadata: {
      created: new Date(),
      source: 'n8n-automation'
    }
  }
}];
```

**Task**: Transform a complex nested object into a flat structure

---

#### Day 4: Loops & Iteration
**Learn** (15 min)
- `for` loops
- `forEach()`, `map()` for arrays
- When to use each

**Practice** (15 min)
```javascript
// Process multiple items
const results = [];
const items = $input.all();

for (const item of items) {
  results.push({
    json: {
      processed: true,
      original: item.json,
      timestamp: Date.now()
    }
  });
}

return results;
```

**Task**: Loop through array of URLs and extract domain names

---

#### Day 5: Functions & Return Patterns
**Learn** (15 min)
- Function syntax: `function name() {}`
- Arrow functions: `() => {}`
- The n8n return pattern: `return [{ json: {} }]`

**Practice** (15 min)
```javascript
// Helper function pattern
function cleanData(input) {
  return {
    id: input.id,
    title: input.title.trim(),
    valid: input.title.length > 0
  };
}

const cleaned = $input.all()
  .map(item => cleanData(item.json));

return cleaned.map(item => ({ json: item }));
```

**Task**: Create a reusable data validation function

---

#### Day 6-7: Week 1 Project
**Build**: "Smart Data Transformer"

**Requirements**:
1. Accept JSON input (simulate API response)
2. Validate required fields exist
3. Clean/normalize text (trim, lowercase)
4. Add metadata (timestamp, id)
5. Filter out invalid entries
6. Return formatted output

**Success Criteria**:
- [ ] Handles missing fields gracefully
- [ ] Works with 1 or 100 items
- [ ] Code is commented and readable
- [ ] Output format is consistent

**Bonus**: Add error logging for invalid items

---

### Week 1 Assessment

Test yourself:
- [ ] Can you explain `const` vs `let`?
- [ ] Can you write a `.filter()` from memory?
- [ ] Can you transform this: `{firstName: "John", lastName: "Doe"}` → `{fullName: "John Doe"}`?
- [ ] Do you understand the n8n return pattern?

If you answered yes to 3/4, you're ready for Week 2!

---

## ⚙️ WEEK 2: APIs and Logic Flow

### Goal
Master external API integration and build complex workflows

### What You'll Build This Week
- **Mini-Project**: Weather Alert Bot (API → Logic → Notification)
- **Deliverable**: Multi-node workflow with error handling

### Daily Breakdown

#### Day 8: HTTP Requests Basics
**Learn** (15 min)
- GET vs POST requests
- Headers, query parameters, body
- Authentication: API keys, Bearer tokens

**Practice** (15 min)
- Create HTTP Request node
- Call free API: `https://api.coindesk.com/v1/bpi/currentprice.json`
- Parse response in Function node

**Task**: Fetch cryptocurrency prices and format nicely

---

#### Day 9: Working with n8n Data
**Learn** (15 min)
- `$json` - current item
- `$input.all()` - all items
- `$node["NodeName"].json` - reference other nodes
- Expressions vs Code

**Practice** (15 min)
```javascript
// Combine data from multiple sources
const apiData = $node["HTTP Request"].json;
const userData = $json;

return [{
  json: {
    user: userData.name,
    weatherData: apiData.current,
    combined: true
  }
}];
```

**Task**: Merge data from two different API calls

---

#### Day 10: Conditional Logic & Branching
**Learn** (15 min)
- IF node in n8n
- Switch node for multiple conditions
- JavaScript if/else in Function nodes

**Practice** (15 min)
```javascript
// Route data based on conditions
const data = $json;

if (data.temperature > 30) {
  return [{
    json: {
      alert: "HOT",
      action: "send_warning"
    }
  }];
} else if (data.temperature < 10) {
  return [{
    json: {
      alert: "COLD",
      action: "send_warning"
    }
  }];
}

return [{ json: { alert: "NORMAL" } }];
```

**Task**: Create workflow that routes based on time of day

---

#### Day 11: Error Handling
**Learn** (15 min)
- Try/catch blocks in JavaScript
- n8n Error Workflow
- Retry logic for failed API calls

**Practice** (15 min)
```javascript
try {
  const data = $json;

  // Might fail if field doesn't exist
  const result = data.nested.property.value;

  return [{ json: { result } }];
} catch (error) {
  return [{
    json: {
      error: true,
      message: error.message,
      fallback: "default_value"
    }
  }];
}
```

**Task**: Add error handling to Week 1's transformer

---

#### Day 12: Data Persistence
**Learn** (15 min)
- n8n's Data Store (KV storage)
- When to cache vs re-fetch
- Set/Get patterns

**Practice** (15 min)
- Store API response in Data Store
- Retrieve cached data
- Implement TTL (time-to-live) logic

**Task**: Cache API responses for 5 minutes

---

#### Day 13-14: Week 2 Project
**Build**: "Weather Alert Bot"

**Workflow**:
1. **Trigger**: Schedule (every 3 hours)
2. **HTTP Node**: Fetch weather from [OpenWeatherMap](https://openweathermap.org/api)
3. **Function**: Parse + check thresholds
4. **IF**: Is alert needed?
5. **Telegram/Slack**: Send notification
6. **Data Store**: Log all checks

**Requirements**:
- [ ] Handles API failures (retry or fallback)
- [ ] Only sends alerts when needed (not every check)
- [ ] Stores history of checks
- [ ] Custom message based on weather type

**Bonus**: Add weekly summary of all alerts

---

### Week 2 Assessment

- [ ] Can you make a GET request with headers?
- [ ] Can you access data from a previous node?
- [ ] Can you add error handling to an API call?
- [ ] Do you understand when to cache data?

3/4 = Ready for Week 3!

---

## 🤖 WEEK 3: Smart Agents & AI APIs

### Goal
Build AI-powered agents with memory and context

### What You'll Build This Week
- **Mini-Project**: Context-Aware AI Assistant
- **Deliverable**: RAG-lite system with caching

### Daily Breakdown

#### Day 15: AI API Fundamentals
**Learn** (15 min)
- API structure: messages, roles (system/user/assistant)
- Temperature, max tokens, stop sequences
- Cost optimization basics

**Practice** (15 min)
```javascript
// Build OpenAI request payload
const userMessage = $json.message;

return [{
  json: {
    model: "gpt-3.5-turbo",
    messages: [
      {
        role: "system",
        content: "You are a helpful assistant."
      },
      {
        role: "user",
        content: userMessage
      }
    ],
    temperature: 0.7,
    max_tokens: 150
  }
}];
```

**Task**: Create your first AI API call in n8n

---

#### Day 16: Dynamic Prompts
**Learn** (15 min)
- Template prompts with variables
- Context injection
- Few-shot prompting

**Practice** (15 min)
```javascript
// Build context-aware prompt
const userQuery = $json.query;
const userHistory = $json.previousMessages || [];

const contextPrompt = `
You are a helpful AI assistant.
User's previous topics: ${userHistory.join(", ")}

User asks: ${userQuery}
`;

return [{
  json: {
    messages: [
      { role: "system", content: contextPrompt }
    ]
  }
}];
```

**Task**: Add user preferences to prompt context

---

#### Day 17: Response Processing
**Learn** (15 min)
- Parsing AI API responses
- Extracting specific info (JSON mode)
- Handling streaming vs completion

**Practice** (15 min)
```javascript
// Parse and validate AI response
const aiResponse = $json.choices[0].message.content;

// Extract structured data
const parsed = {
  rawResponse: aiResponse,
  wordCount: aiResponse.split(' ').length,
  hasCode: aiResponse.includes('```'),
  timestamp: new Date().toISOString()
};

return [{ json: parsed }];
```

**Task**: Extract action items from AI response

---

#### Day 18: Memory & Context Management
**Learn** (15 min)
- Conversation history management
- Context window limits
- Token counting basics

**Practice** (15 min)
```javascript
// Manage conversation history
const newMessage = $json.message;
const history = $node["Get History"].json.messages || [];

// Keep last 10 messages only
const updatedHistory = [...history, newMessage].slice(-10);

return [{
  json: {
    messages: updatedHistory,
    contextSize: updatedHistory.length
  }
}];
```

**Task**: Build a conversation that remembers last 5 exchanges

---

#### Day 19: Caching Strategies
**Learn** (15 min)
- When to cache AI responses
- Cache invalidation strategies
- Semantic caching concepts

**Practice** (15 min)
```javascript
// Check cache before AI call
const query = $json.query;
const cacheKey = query.toLowerCase().trim();

// In real workflow: check Data Store first
// If hit: return cached
// If miss: call AI, then cache

return [{
  json: {
    cacheKey,
    needsAICall: true,
    reason: "cache_miss"
  }
}];
```

**Task**: Add caching to reduce API costs by 50%

---

#### Day 20-21: Week 3 Project
**Build**: "Smart Knowledge Assistant"

**System Flow**:
1. **Webhook/Form**: User submits question
2. **Check Cache**: Is similar question cached?
3. **Fetch Context**: Get relevant docs (Google Sheets/Notion)
4. **Build Prompt**: Inject context + question
5. **AI Call**: Get answer from GPT/Gemini
6. **Store Result**: Cache answer
7. **Return**: Send to user

**Requirements**:
- [ ] Retrieves context from external source
- [ ] Caches responses (7-day TTL)
- [ ] Handles rate limits gracefully
- [ ] Tracks usage/cost
- [ ] Returns response <3 seconds (cached) or <10s (new)

**Bonus**: Add feedback loop (thumbs up/down)

---

### Week 3 Assessment

- [ ] Can you build a dynamic AI prompt?
- [ ] Can you parse and validate AI responses?
- [ ] Do you understand context window limits?
- [ ] Can you implement basic caching?

Ready for the final week!

---

## 🧠 WEEK 4: Python & AI System Architecture

### Goal
Understand AI system design and extend with Python

### What You'll Build This Week
- **Capstone Project**: Full RAG/CAG System
- **Deliverable**: Production-ready AI automation

### Daily Breakdown

#### Day 22: Python Basics for AI
**Learn** (15 min)
- Python syntax vs JavaScript
- Virtual environments
- Installing packages: `pip install`

**Practice** (15 min)
```python
# Simple Python function (run locally)
import json

def process_data(items):
    """Clean and filter items"""
    cleaned = [
        {
            "id": item["id"],
            "name": item["name"].strip()
        }
        for item in items
        if item.get("active", False)
    ]
    return cleaned

# Test
data = [{"id": 1, "name": " Test ", "active": True}]
print(json.dumps(process_data(data)))
```

**Task**: Run this Python script locally

---

#### Day 23: Reading AI Code
**Learn** (15 min)
- Common AI libraries: LangChain, OpenAI SDK
- Understanding embeddings
- Vector similarity basics

**Practice** (15 min)
- Find a simple RAG example on GitHub
- Read through the code
- Identify: where data is loaded, embedded, queried

**Resources**:
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)

**Task**: Explain in your own words how RAG works

---

#### Day 24: Python + n8n Integration
**Learn** (15 min)
- n8n Code node (Python mode)
- Calling local Python scripts via HTTP
- Using Python for heavy compute

**Practice** (15 min)
```python
# In n8n Python Code node
import json

items = _input.all()

# Process with Python
results = []
for item in items:
    data = item['json']
    # Do something complex
    results.append({
        'json': {
            'processed': True,
            'original': data
        }
    })

return results
```

**Task**: Use Python Code node for text processing

---

#### Day 25: System Architecture Thinking
**Learn** (30 min - reading day)
- RAG architecture diagrams
- CAG (Context-Augmented Generation)
- MCP (Model Context Protocol)
- When to use what

**Research**:
- Read: "What is RAG?" articles
- Watch: RAG explainer video
- Diagram: Your own AI system design

**Task**: Draw your ideal AI automation system

---

#### Day 26: Embeddings & Vector Search
**Learn** (15 min)
- What are embeddings?
- Vector databases (Pinecone, Weaviate, Chroma)
- Similarity search basics

**Practice** (15 min)
```python
# Conceptual: Generate embedding
from openai import OpenAI

client = OpenAI(api_key="your-key")

text = "What is n8n?"
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
)

embedding = response.data[0].embedding
# embedding is now a list of ~1536 numbers
```

**Task**: Generate embeddings for 5 different queries

---

#### Day 27-30: CAPSTONE PROJECT
**Build**: "Production RAG System"

### System Architecture

```
┌─────────────────────────────────────────────────┐
│                  USER QUERY                      │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
         ┌───────────────┐
         │  Check Cache  │
         └───────┬───────┘
                 │
         ┌───────▼────────┐
         │   Cache Hit?   │
         └───┬────────┬───┘
             │ NO     │ YES
             │        │
             ▼        ▼
    ┌─────────────┐  └──────► Return Cached
    │  Vectorize  │
    │   Query     │
    └──────┬──────┘
           │
           ▼
    ┌─────────────────┐
    │ Similarity      │
    │ Search Docs     │
    │ (Top 3)         │
    └──────┬──────────┘
           │
           ▼
    ┌─────────────────┐
    │ Build Context   │
    │ + User Query    │
    └──────┬──────────┘
           │
           ▼
    ┌─────────────────┐
    │  Call AI API    │
    │  (GPT/Gemini)   │
    └──────┬──────────┘
           │
           ▼
    ┌─────────────────┐
    │  Cache Result   │
    │  Return Answer  │
    └─────────────────┘
```

### Implementation Steps

**Day 27: Setup & Data Preparation**
- [ ] Choose your knowledge base (Google Docs, Notion, or text files)
- [ ] Extract and clean content
- [ ] Split into chunks (max 500 words each)
- [ ] Store in Google Sheets or Airtable

**Day 28: Embeddings & Search**
- [ ] Create embeddings for all chunks (Python script or n8n)
- [ ] Store embeddings + text in vector DB or simple JSON
- [ ] Test similarity search manually

**Day 29: Build n8n Workflow**
- [ ] Webhook trigger (user query)
- [ ] Vectorize query
- [ ] Find top 3 similar chunks
- [ ] Build context prompt
- [ ] Call AI API
- [ ] Return formatted answer

**Day 30: Polish & Deploy**
- [ ] Add caching layer
- [ ] Error handling & fallbacks
- [ ] Usage tracking
- [ ] Rate limiting
- [ ] Deploy and test with real queries

### Success Criteria
- [ ] Answers questions from your knowledge base accurately
- [ ] Responds in <5 seconds for cached, <15s for new
- [ ] Handles 100+ queries without breaking
- [ ] Costs less than $0.05/query
- [ ] Gracefully handles edge cases

### Bonus Features
- [ ] Multi-language support
- [ ] Source attribution (shows which doc was used)
- [ ] Feedback collection
- [ ] A/B test different prompts
- [ ] Admin dashboard for analytics

---

## 🎓 Final Assessment

You're ready to call yourself an AI Systems Builder if you can:

**Technical Skills**
- [ ] Write complex Function nodes without googling basic syntax
- [ ] Debug API workflows in under 10 minutes
- [ ] Design a RAG system from scratch
- [ ] Read and modify Python AI scripts
- [ ] Optimize for cost and latency

**Systems Thinking**
- [ ] Explain when to cache vs compute
- [ ] Know the tradeoffs: speed vs accuracy vs cost
- [ ] Design error handling and retry logic
- [ ] Think in data flows, not just code

**AI Fluency**
- [ ] Understand embeddings, tokens, context windows
- [ ] Write effective prompts (system + few-shot)
- [ ] Know when to use RAG vs fine-tuning vs prompt engineering
- [ ] Estimate API costs before building

---

## 🚀 What's Next?

### Level Up Options

**Option 1: Go Deeper (Specialization)**
- Advanced LangChain patterns
- Build custom vector search
- Multi-agent systems (CrewAI, AutoGen)
- Fine-tuning models

**Option 2: Go Broader (Diversification)**
- Add voice (Whisper API, ElevenLabs)
- Image generation (DALL-E, Midjourney)
- Video automation (D-ID, Synthesia)
- Web scraping + AI analysis

**Option 3: Build Products (Monetization)**
- AI chatbot as a service
- Custom GPT solutions for businesses
- AI workflow marketplace templates
- Consulting/freelancing

### Recommended Projects
1. **AI Email Assistant**: Auto-categorize and draft replies
2. **Content Repurposer**: Blog → Twitter thread → LinkedIn post
3. **Research Agent**: Given a topic, compile a report with sources
4. **Personal CRM**: Track relationships and suggest follow-ups
5. **Code Reviewer**: Automated PR analysis with improvement suggestions

---

## 📞 Community & Support

### When You Get Stuck
1. **Check the docs**: n8n.io/docs (80% of answers)
2. **Search community**: community.n8n.io
3. **AI tutor**: ChatGPT/Claude with your code
4. **Ask specifically**: "Why does my HTTP node return 401?"

### Join Communities
- [n8n Discord](https://discord.gg/n8n)
- [r/n8n on Reddit](https://reddit.com/r/n8n)
- [n8n Community Forum](https://community.n8n.io)

### Share Your Wins
- Post your capstone project
- Help others who are on Day 1
- Write a blog post about your journey
- Build in public on Twitter/LinkedIn

---

## 📊 Progress Tracker

Track your journey:

```
Week 1: JavaScript Foundations
Day 1:  ⬜ Variables & Data Types
Day 2:  ⬜ Arrays & Array Methods
Day 3:  ⬜ Objects & JSON
Day 4:  ⬜ Loops & Iteration
Day 5:  ⬜ Functions & Return Patterns
Day 6-7: ⬜ Week 1 Project Complete

Week 2: APIs & Logic
Day 8:  ⬜ HTTP Requests Basics
Day 9:  ⬜ Working with n8n Data
Day 10: ⬜ Conditional Logic
Day 11: ⬜ Error Handling
Day 12: ⬜ Data Persistence
Day 13-14: ⬜ Week 2 Project Complete

Week 3: AI & Agents
Day 15: ⬜ AI API Fundamentals
Day 16: ⬜ Dynamic Prompts
Day 17: ⬜ Response Processing
Day 18: ⬜ Memory & Context
Day 19: ⬜ Caching Strategies
Day 20-21: ⬜ Week 3 Project Complete

Week 4: Python & Architecture
Day 22: ⬜ Python Basics
Day 23: ⬜ Reading AI Code
Day 24: ⬜ Python + n8n Integration
Day 25: ⬜ System Architecture
Day 26: ⬜ Embeddings & Vectors
Day 27-30: ⬜ CAPSTONE PROJECT COMPLETE

🎉 GRADUATION: ⬜ I'm an AI Systems Builder!
```

---

## 💡 Pro Tips for Success

1. **Don't skip the projects**: Watching tutorials ≠ learning. Build the thing.

2. **Use AI as a tutor**: When stuck, paste your code into ChatGPT and ask "What's wrong here?"

3. **Keep a learning journal**: Screenshot your progress. Future you will thank you.

4. **Join Day 1**: Start on a Monday. Commit publicly. Find an accountability buddy.

5. **One concept per day**: Don't rush. 30 focused minutes > 2 distracted hours.

6. **Break things**: The best way to learn debugging is to debug. Intentionally break your code and fix it.

7. **Teach to learn**: Explain each concept to a friend (or rubber duck).

8. **Save everything**: Export workflows, save code snippets. Build your personal library.

---

## 🎯 Daily Routine Template

**Before you start (5 min)**
- [ ] Review yesterday's work
- [ ] Check today's goal
- [ ] Open all resources/tabs

**Learning (15 min)**
- [ ] Read concept
- [ ] Watch example if available
- [ ] Take notes in your own words

**Practice (15 min)**
- [ ] Type out the example (don't copy-paste)
- [ ] Modify it to test understanding
- [ ] Complete today's task

**After (5 min)**
- [ ] Save/export your work
- [ ] Update progress tracker
- [ ] Note any questions for tomorrow

---

## 🏆 Graduation Badge

When you complete all 30 days + capstone, you've earned:

**🎓 AI SYSTEMS BUILDER - 2025**
- ✅ JavaScript Automation Expert
- ✅ API Integration Specialist
- ✅ AI Agent Architect
- ✅ RAG System Designer
- ✅ Python AI Fluent

Share your achievement and tag the tools that helped you!

---

**Remember**: The goal isn't perfection. It's progress.

You don't need to know everything. You just need to know how to build, debug, and ship.

**Now go build something amazing.** 🚀

---

*Last updated: 2025*
*Created for ambitious builders who want to master AI automation in 30 days*
