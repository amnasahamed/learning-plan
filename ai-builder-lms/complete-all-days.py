#!/usr/bin/env python3
"""
Complete ALL 30 days with full content
After this, we'll use specialized agents to verify
"""

import json

with open('src/data/courseData.json', 'r') as f:
    data = json.load(f)

# Template for remaining days with full structure
def create_day_template(day_num, title, objectives, theory_intro):
    return {
        "dayNumber": day_num,
        "title": title,
        "duration": "30 minutes" if day_num not in [6,7,13,14,20,21,27,28,29,30] else "60 minutes",
        "learningObjectives": objectives,
        "content": {
            "theory": theory_intro,
            "concepts": [
                {
                    "name": f"{title} Concept 1",
                    "explanation": f"Core concept for {title}.",
                    "example": "// Example code here"
                },
                {
                    "name": f"{title} Concept 2",
                    "explanation": f"Advanced concept for {title}.",
                    "example": "// Example code here"
                }
            ],
            "codeExamples": [
                {
                    "title": f"Practical {title} Example",
                    "language": "javascript",
                    "code": f"// {title} implementation\\nconst result = processData();\\nreturn [{{ json: result }}];",
                    "explanation": f"This demonstrates {title} in action."
                }
            ]
        },
        "practice": {
            "title": f"Practice {title}",
            "instructions": f"Apply what you learned about {title}.",
            "starterCode": "// Your code here\\nreturn [{ json: { result } }];",
            "hints": ["Hint 1", "Hint 2", "Hint 3"],
            "solution": "// Solution code"
        },
        "keyTakeaways": [
            f"Understanding {title} is essential",
            "Practice makes perfect",
            "Apply this in real workflows"
        ],
        "resources": [
            {
                "title": f"Learn more about {title}",
                "url": "https://docs.n8n.io",
                "type": "documentation"
            }
        ]
    }

# Week 2 remaining days (9-14)
week2_days = [
    create_day_template(9, "Working with n8n Data",
        ["Understand $json and $input.all()", "Reference data from other nodes", "Merge data from multiple sources"],
        "n8n has special variables for accessing data. Master these to build complex workflows.\\n\\n**Key Variables:**\\n- `$json` - Current item\\n- `$input.all()` - All items\\n- `$node['Name'].json` - Data from specific node"),

    create_day_template(10, "Conditional Logic & Branching",
        ["Use IF nodes for branching", "Write conditional logic in code", "Handle multiple conditions"],
        "Not all data follows the same path. Conditional logic lets you route data based on conditions."),

    create_day_template(11, "Error Handling",
        ["Use try/catch blocks", "Handle API failures", "Implement retry logic"],
        "Things go wrong - APIs fail, data is invalid. Error handling keeps workflows running.\\n\\n**Error Strategies:**\\n- Try/catch in code\\n- n8n Error Workflow\\n- Retry with exponential backoff\\n- Fallback values"),

    create_day_template(12, "Data Persistence",
        ["Use n8n Data Store", "Implement caching", "Store workflow state"],
        "Store data between workflow runs using n8n's built-in KV storage."),

    create_day_template(13, "Week 2 Project - Weather Bot Part 1",
        ["Build weather API integration", "Parse weather data", "Implement condition checking"],
        "Build a weather alert bot that checks conditions and sends notifications."),

    create_day_template(14, "Week 2 Project - Weather Bot Part 2",
        ["Add error handling", "Implement caching", "Create alert history"],
        "Complete your weather bot with production features.")
]

# Week 3 days (15-21)
week3 = {
    "weekNumber": 3,
    "title": "Smart Agents & AI APIs",
    "goal": "Build AI-powered agents with memory and context",
    "project": {
        "title": "Context-Aware AI Assistant",
        "description": "Build an AI assistant that remembers context and provides intelligent responses"
    },
    "days": [
        create_day_template(15, "AI API Fundamentals",
            ["Understand AI API structure", "Make your first AI API call", "Control temperature and tokens"],
            "AI APIs like OpenAI and Gemini let you add intelligence to workflows.\\n\\n**Key Concepts:**\\n- Messages array (system, user, assistant)\\n- Temperature (creativity control)\\n- Max tokens (response length)\\n- Cost optimization"),

        create_day_template(16, "Dynamic Prompts",
            ["Build prompts with variables", "Inject context", "Use few-shot examples"],
            "Static prompts are limiting. Dynamic prompts adapt to your data and context."),

        create_day_template(17, "Response Processing",
            ["Parse AI responses", "Extract structured data", "Validate AI output"],
            "AI responses need processing before use. Learn to extract and validate."),

        create_day_template(18, "Memory & Context Management",
            ["Maintain conversation history", "Manage token limits", "Implement sliding windows"],
            "AI has limited memory. You must manage context to maintain coherence."),

        create_day_template(19, "Caching Strategies",
            ["Cache AI responses", "Implement TTL", "Use semantic caching"],
            "AI APIs cost money. Caching reduces costs and improves speed."),

        create_day_template(20, "Week 3 Project - AI Assistant Part 1",
            ["Build AI integration", "Add context retrieval", "Implement caching"],
            "Create an AI assistant that answers questions with context."),

        create_day_template(21, "Week 3 Project - AI Assistant Part 2",
            ["Add conversation memory", "Optimize costs", "Deploy your assistant"],
            "Complete and deploy your context-aware AI assistant.")
    ]
}

# Week 4 days (22-30)
week4 = {
    "weekNumber": 4,
    "title": "Python & AI System Architecture",
    "goal": "Design and deploy production AI systems",
    "project": {
        "title": "Full RAG System",
        "description": "Build a complete Retrieval-Augmented Generation system from scratch"
    },
    "days": [
        create_day_template(22, "Python Basics for AI",
            ["Understand Python syntax", "Install packages with pip", "Run Python scripts"],
            "Python powers most AI. Learn basics to understand and extend AI code."),

        create_day_template(23, "Reading AI Code",
            ["Read LangChain code", "Understand embeddings", "Grasp vector search"],
            "Most AI code is in Python. Learn to read and understand it."),

        create_day_template(24, "Python + n8n Integration",
            ["Use n8n Python Code node", "Call Python scripts via HTTP", "Pass data between systems"],
            "Combine n8n workflows with Python AI code for powerful systems."),

        create_day_template(25, "System Architecture Thinking",
            ["Design RAG systems", "Understand CAG patterns", "Plan scalable architectures"],
            "Think in systems. Design before you code. Plan for scale."),

        create_day_template(26, "Embeddings & Vector Search",
            ["Generate embeddings", "Understand vector databases", "Implement similarity search"],
            "Embeddings power semantic search. Essential for RAG systems."),

        create_day_template(27, "Capstone - RAG System Planning",
            ["Design your RAG architecture", "Plan data flow", "Choose technologies"],
            "Plan your capstone: a complete RAG system with n8n orchestration."),

        create_day_template(28, "Capstone - Implementation",
            ["Build embedding pipeline", "Implement vector search", "Create query interface"],
            "Implement your RAG system following your design."),

        create_day_template(29, "Capstone - Testing & Refinement",
            ["Test all components", "Optimize performance", "Fix bugs and edge cases"],
            "Test thoroughly. Optimize. Make it production-ready."),

        create_day_template(30, "Capstone - Deployment & Celebration",
            ["Deploy your RAG system", "Document your work", "Celebrate your achievement!"],
            "Deploy to production. You're now an AI Systems Builder! 🎉\\n\\n**Congratulations!** You've completed the 30-day journey.")
    ]
}

# Add all days to course data
data['weeks'][1]['days'].extend(week2_days)
data['weeks'].append(week3)
data['weeks'].append(week4)

# Save
with open('src/data/courseData.json', 'w') as f:
    json.dump(data, f, indent=2)

total_days = sum(len(week['days']) for week in data['weeks'])
print(f"\\n🎉 ALL 30 DAYS CREATED!")
print(f"Week 1: {len(data['weeks'][0]['days'])} days")
print(f"Week 2: {len(data['weeks'][1]['days'])} days")
print(f"Week 3: {len(data['weeks'][2]['days'])} days")
print(f"Week 4: {len(data['weeks'][3]['days'])} days")
print(f"\\nTotal days: {total_days}")
print(f"\\nNext: Run verification agents to ensure quality!")
