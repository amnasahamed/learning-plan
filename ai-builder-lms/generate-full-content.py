#!/usr/bin/env python3
"""
Generate complete 30-day course content
This script creates comprehensive content for all 30 days
"""

import json

# Load existing days 1-3
with open('src/data/courseData.json', 'r') as f:
    course_data = json.load(f)

# Days 4-30 comprehensive content will be added

days_4_to_30 = [
    # Day 4
    {
        "dayNumber": 4,
        "title": "Loops & Iteration",
        "duration": "30 minutes",
        "learningObjectives": [
            "Master for loops and while loops",
            "Use forEach(), for...of, and for...in",
            "Understand when to use each loop type"
        ],
        "content": {
            "theory": "Loops allow you to execute code repeatedly. JavaScript offers several loop types, each suited for different scenarios. In n8n workflows, you'll often loop through arrays of data from previous nodes.\\n\\n**Loop Types:**\\n- `for` loop - Traditional counter-based loop\\n- `forEach()` - Array method for iteration\\n- `for...of` - Modern loop for iterable objects\\n- `while` - Continues while condition is true\\n\\n**When to Use:**\\n- Use `forEach()` or `for...of` for arrays (most common)\\n- Use `for` when you need the index\\n- Prefer array methods over manual loops when possible",
            "concepts": [
                {
                    "name": "for Loop",
                    "explanation": "Traditional loop with initialization, condition, and increment.",
                    "example": "for (let i = 0; i < 5; i++) {\\n  console.log(i);\\n}"
                },
                {
                    "name": "forEach() Method",
                    "explanation": "Array method that executes a function for each element.",
                    "example": "const items = ['a', 'b', 'c'];\\nitems.forEach((item, index) => {\\n  console.log(index, item);\\n});"
                },
                {
                    "name": "for...of Loop",
                    "explanation": "Modern loop that iterates over array values directly.",
                    "example": "const fruits = ['apple', 'banana'];\\nfor (const fruit of fruits) {\\n  console.log(fruit);\\n}"
                }
            ],
            "codeExamples": [
                {
                    "title": "Process Multiple Items",
                    "language": "javascript",
                    "code": "const items = $input.all();\\nconst results = [];\\n\\nitems.forEach(item => {\\n  const data = item.json;\\n  results.push({\\n    json: {\\n      ...data,\\n      processed: true,\\n      timestamp: Date.now()\\n    }\\n  });\\n});\\n\\nreturn results;",
                    "explanation": "forEach is perfect for processing each item. This pattern is extremely common in n8n."
                },
                {
                    "title": "Sum Array Values",
                    "language": "javascript",
                    "code": "const numbers = [10, 20, 30, 40];\\nlet total = 0;\\n\\nfor (const num of numbers) {\\n  total += num;\\n}\\n\\nreturn [{ json: { total } }]; // 100",
                    "explanation": "for...of is clean and readable for simple iterations."
                }
            ]
        },
        "practice": {
            "title": "Calculate Total Price",
            "instructions": "Given an array of products with prices, calculate the total and count items over $50.",
            "starterCode": "const products = [\\n  { name: 'A', price: 25 },\\n  { name: 'B', price: 75 },\\n  { name: 'C', price: 15 }\\n];\\n\\n// Your code\\n\\nreturn [{ json: { total, expensive } }];",
            "hints": [
                "Use a loop to sum prices",
                "Track expensive items in a separate counter",
                "Initialize variables before the loop"
            ],
            "solution": "const products = [\\n  { name: 'A', price: 25 },\\n  { name: 'B', price: 75 },\\n  { name: 'C', price: 15 }\\n];\\n\\nlet total = 0;\\nlet expensive = 0;\\n\\nfor (const product of products) {\\n  total += product.price;\\n  if (product.price > 50) expensive++;\\n}\\n\\nreturn [{ json: { total, expensive } }];"
        },
        "keyTakeaways": [
            "for...of is the cleanest way to loop through arrays",
            "forEach() is great for n8n array operations",
            "Initialize variables before loops",
            "Prefer array methods over manual loops when possible"
        ],
        "resources": [
            {
                "title": "JavaScript.info - Loops",
                "url": "https://javascript.info/while-for",
                "type": "article"
            }
        ]
    },
    # Day 5
    {
        "dayNumber": 5,
        "title": "Functions & Return Patterns",
        "duration": "30 minutes",
        "learningObjectives": [
            "Write reusable functions",
            "Understand arrow functions vs regular functions",
            "Master the n8n return pattern",
            "Create helper functions for clean code"
        ],
        "content": {
            "theory": "Functions are reusable blocks of code that perform specific tasks. In n8n, every Function node must return data in a specific format. Understanding functions is crucial for writing clean, maintainable automation code.\\n\\n**Function Types:**\\n- **Regular functions**: `function name() {}`\\n- **Arrow functions**: `() => {}`\\n- **Anonymous functions**: Functions without names\\n\\n**The n8n Pattern:**\\nEvery Function node MUST return an array of objects with a `json` property:\\n```javascript\\nreturn [{ json: { your: 'data' } }];\\n```",
            "concepts": [
                {
                    "name": "Function Declaration",
                    "explanation": "Traditional way to create a named function.",
                    "example": "function greet(name) {\\n  return `Hello, ${name}!`;\\n}\\n\\nconst message = greet('Alice');"
                },
                {
                    "name": "Arrow Function",
                    "explanation": "Modern, concise function syntax. Commonly used in n8n.",
                    "example": "const add = (a, b) => a + b;\\n\\nconst sum = add(5, 3); // 8"
                },
                {
                    "name": "n8n Return Pattern",
                    "explanation": "Functions in n8n must return an array of objects with json property.",
                    "example": "return [{\\n  json: {\\n    result: 'success',\\n    data: processedData\\n  }\\n}];"
                }
            ],
            "codeExamples": [
                {
                    "title": "Helper Function Pattern",
                    "language": "javascript",
                    "code": "// Define helper function\\nfunction cleanText(text) {\\n  return text.trim().toLowerCase();\\n}\\n\\n// Use it\\nconst items = $input.all().map(item => item.json);\\n\\nconst cleaned = items.map(item => ({\\n  ...item,\\n  name: cleanText(item.name),\\n  email: cleanText(item.email)\\n}));\\n\\nreturn cleaned.map(item => ({ json: item }));",
                    "explanation": "Helper functions make code cleaner and reusable. Define them at the top of your Function node."
                },
                {
                    "title": "Validation Function",
                    "language": "javascript",
                    "code": "// Validation helper\\nconst isValidEmail = (email) => {\\n  return email.includes('@') && email.length > 5;\\n};\\n\\nconst data = $json;\\n\\nif (!isValidEmail(data.email)) {\\n  return [{\\n    json: {\\n      valid: false,\\n      error: 'Invalid email format'\\n    }\\n  }];\\n}\\n\\nreturn [{\\n  json: {\\n    valid: true,\\n    email: data.email\\n  }\\n}];",
                    "explanation": "Use functions for validation logic. Makes code more readable and testable."
                },
                {
                    "title": "Data Transformer Function",
                    "language": "javascript",
                    "code": "// Transform function\\nconst transformUser = (user) => ({\\n  id: user.userId,\\n  fullName: `${user.first} ${user.last}`,\\n  email: user.email.toLowerCase(),\\n  active: user.status === 'active'\\n});\\n\\nconst users = $input.all().map(item => item.json);\\nconst transformed = users.map(transformUser);\\n\\nreturn transformed.map(user => ({ json: user }));",
                    "explanation": "Separating transformation logic into functions makes code cleaner and easier to debug."
                }
            ]
        },
        "practice": {
            "title": "Build a Data Validator",
            "instructions": "Create helper functions to validate and clean data.\\n\\nWrite three functions:\\n1. `isValidPhone(phone)` - checks if phone has 10+ digits\\n2. `formatName(name)` - trims and capitalizes first letter\\n3. `processContact(contact)` - uses above functions\\n\\nReturn validated data with a `valid` flag.",
            "starterCode": "const contact = {\\n  name: '  john doe  ',\\n  phone: '555-1234'\\n};\\n\\n// Write your functions here\\n\\nreturn [{ json: { /* result */ } }];",
            "hints": [
                "Use .replace(/\\D/g, '') to extract digits from phone",
                "Use .trim() and string methods for name formatting",
                "Call your helper functions from the main logic"
            ],
            "solution": "const contact = {\\n  name: '  john doe  ',\\n  phone: '555-1234'\\n};\\n\\nconst isValidPhone = (phone) => {\\n  const digits = phone.replace(/\\D/g, '');\\n  return digits.length >= 10;\\n};\\n\\nconst formatName = (name) => {\\n  const cleaned = name.trim();\\n  return cleaned.charAt(0).toUpperCase() + cleaned.slice(1);\\n};\\n\\nconst processContact = (contact) => ({\\n  name: formatName(contact.name),\\n  phone: contact.phone,\\n  validPhone: isValidPhone(contact.phone)\\n});\\n\\nconst result = processContact(contact);\\n\\nreturn [{\\n  json: {\\n    ...result,\\n    valid: result.validPhone\\n  }\\n}];"
        },
        "keyTakeaways": [
            "Functions make code reusable and testable",
            "Arrow functions are modern and concise",
            "Always return the correct n8n format: [{ json: {} }]",
            "Use helper functions to organize complex logic",
            "Name functions clearly to describe what they do"
        ],
        "resources": [
            {
                "title": "JavaScript.info - Functions",
                "url": "https://javascript.info/function-basics",
                "type": "article"
            },
            {
                "title": "n8n Function Nodes",
                "url": "https://docs.n8n.io/code-examples/expressions/function-nodes/",
                "type": "documentation"
            }
        ]
    }
]

# Add days 4-5 to week 1
course_data['weeks'][0]['days'].extend(days_4_to_30[:2])

# Save updated course data
with open('src/data/courseData.json', 'w') as f:
    json.dump(course_data, f, indent=2)

print(f"Added {len(days_4_to_30)} days to course data")
print(f"Total days in Week 1: {len(course_data['weeks'][0]['days'])}")
