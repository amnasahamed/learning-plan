#!/usr/bin/env python3
"""
Comprehensive courseData.json Enhancement Script
Enhances Days 8-30 with detailed, rich content matching Days 1-5
"""

import json
import sys

# Enhancement data for all days 8-30
ALL_ENHANCEMENTS = {
    8: {
        "theory": "HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the web. Every API call you make in n8n uses HTTP to send requests and receive responses. Understanding HTTP methods, status codes, headers, and request/response structure is essential for building robust automations.\n\n**HTTP Methods:**\n- **GET**: Retrieve data from a server (read-only, no side effects)\n- **POST**: Create new resources or submit data\n- **PUT/PATCH**: Update existing resources\n- **DELETE**: Remove resources\n\n**Key Concepts:**\n- **Headers**: Metadata about the request (authentication, content type)\n- **Query Parameters**: Data passed in the URL (?key=value)\n- **Request Body**: Data sent with POST/PUT requests (JSON, form data)\n- **Status Codes**: 200 (success), 201 (created), 400 (bad request), 404 (not found), 500 (server error)\n\n**Why This Matters for n8n:**\nThe HTTP Request node is one of the most powerful nodes in n8n. It lets you connect to any API, whether it's a popular service or a custom internal API. Mastering HTTP fundamentals allows you to integrate with virtually any system.",
        "concepts": [
            {
                "name": "GET Requests",
                "explanation": "Retrieve data from an API without modifying anything. GET requests pass data via URL query parameters. They're idempotent, meaning multiple identical requests have the same effect as a single request.",
                "example": "// In n8n HTTP Request node\n// Method: GET\n// URL: https://api.example.com/users\n// Query Parameters: { limit: 10, status: 'active' }\n\n// Then in Function node to process response:\nconst users = $json.data;\nconst activeUsers = users.filter(u => u.status === 'active');\nreturn [{ json: { users: activeUsers, count: activeUsers.length } }];"
            },
            {
                "name": "POST Requests with JSON Body",
                "explanation": "Send data to create new resources. POST requests include data in the request body, typically as JSON. The server responds with the created resource and usually a 201 status code.",
                "example": "// In n8n HTTP Request node\n// Method: POST  \n// URL: https://api.example.com/users\n// Body (JSON):\n{\n  \"name\": \"John Doe\",\n  \"email\": \"john@example.com\"\n}\n\n// Process response:\nconst created = $json;\nreturn [{ json: { success: true, userId: created.id } }];"
            },
            {
                "name": "Request Headers",
                "explanation": "Headers provide metadata about the request. Common headers include Authorization (for API keys/tokens), Content-Type (data format), and Accept (expected response format).",
                "example": "// Common headers in n8n HTTP Request:\nconst headers = {\n  'Authorization': 'Bearer YOUR_TOKEN',\n  'Content-Type': 'application/json',\n  'Accept': 'application/json'\n};"
            },
            {
                "name": "Status Code Handling",
                "explanation": "HTTP status codes indicate the result of your request. 2xx means success, 4xx means client error, 5xx means server error. Always check status codes to handle errors gracefully.",
                "example": "// Check status code:\nconst statusCode = $node['HTTP Request'].json.$statusCode;\n\nif (statusCode >= 200 && statusCode < 300) {\n  return [{ json: { success: true } }];\n} else {\n  return [{ json: { error: true, code: statusCode } }];\n}"
            }
        ],
        "codeExamples": [
            {
                "title": "Parse and Transform API Response",
                "language": "javascript",
                "code": "// After calling JSONPlaceholder API (GET /users)\nconst users = $json;\n\n// Transform to include only essential fields\nconst transformedUsers = users.map(user => ({\n  id: user.id,\n  name: user.name,\n  email: user.email,\n  companyName: user.company.name,\n  domain: user.email.split('@')[1],\n  processedAt: new Date().toISOString()\n}));\n\n// Filter to only .com domains\nconst comUsers = transformedUsers.filter(user => \n  user.domain.endsWith('.com')\n);\n\nreturn comUsers.map(user => ({ json: user }));",
                "explanation": "Common pattern: fetch data from API, extract relevant fields, transform structure, filter based on criteria. This demonstrates how to work with API responses in n8n Function nodes."
            },
            {
                "title": "Build Dynamic API Request Parameters",
                "language": "javascript",
                "code": "// Build URL with query parameters dynamically\nconst filters = $json.filters;\n\nconst queryParams = {};\nif (filters.status) queryParams.status = filters.status;\nif (filters.minPrice) queryParams.min_price = filters.minPrice;\nif (filters.category) queryParams.category = filters.category;\n\n// Add pagination\nqueryParams.page = filters.page || 1;\nqueryParams.limit = filters.limit || 20;\n\nreturn [{ \n  json: { \n    params: queryParams,\n    url: 'https://api.example.com/products'\n  } \n}];",
                "explanation": "Shows how to dynamically build API request parameters based on input data. Use this pattern when you need flexible, configurable API calls."
            },
            {
                "title": "Handle API Errors Gracefully",
                "language": "javascript",
                "code": "// Check if HTTP Request succeeded\nconst response = $json;\nconst httpNode = $node['HTTP Request'].json;\n\nif (!httpNode || httpNode.error) {\n  return [{\n    json: {\n      success: false,\n      error: 'API request failed',\n      details: httpNode.error || 'Unknown error'\n    }\n  }];\n}\n\nconst statusCode = httpNode.$statusCode || 200;\nif (statusCode >= 400) {\n  return [{\n    json: {\n      success: false,\n      statusCode,\n      retryable: statusCode >= 500\n    }\n  }];\n}\n\nreturn [{\n  json: {\n    success: true,\n    data: response\n  }\n}];",
                "explanation": "Production-ready error handling for API calls. Always check for errors and status codes before processing response data."
            }
        ],
        "practice": {
            "title": "Build a GitHub User Lookup",
            "instructions": "Create a workflow that:\n1. Accepts a GitHub username\n2. Calls GitHub API (GET https://api.github.com/users/{username})\n3. Extracts: name, repos, followers, bio\n4. Handles errors if user doesn't exist\n5. Returns formatted data",
            "starterCode": "// After HTTP Request to GitHub API\nconst response = $json;\n\n// Your code here\n\nreturn [{ json: { /* result */ } }];",
            "hints": [
                "GitHub API returns 404 if user not found",
                "Check status code first",
                "Extract: login, name, public_repos, followers",
                "Add 'found' boolean flag",
                "Include timestamp"
            ],
            "solution": "const response = $json;\nconst statusCode = $node['HTTP Request'].json.$statusCode;\n\nif (statusCode === 404) {\n  return [{ json: { found: false, error: 'User not found' } }];\n}\n\nif (statusCode >= 400) {\n  return [{ json: { found: false, error: 'API error' } }];\n}\n\nconst userData = {\n  found: true,\n  username: response.login,\n  name: response.name || 'No name',\n  bio: response.bio || 'No bio',\n  publicRepos: response.public_repos,\n  followers: response.followers,\n  avatarUrl: response.avatar_url,\n  fetchedAt: new Date().toISOString()\n};\n\nreturn [{ json: userData }];"
        },
        "keyTakeaways": [
            "HTTP is the foundation of all API communication",
            "GET retrieves, POST creates, PUT updates, DELETE removes",
            "Always check status codes before processing responses",
            "Headers carry authentication and metadata",
            "Query params go in URL, body data in POST/PUT",
            "Handle errors gracefully to prevent crashes"
        ],
        "resources": [
            {
                "title": "MDN - HTTP Overview",
                "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview",
                "type": "documentation"
            },
            {
                "title": "HTTP Status Codes",
                "url": "https://httpstatuses.com/",
                "type": "reference"
            },
            {
                "title": "n8n HTTP Request Node",
                "url": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/",
                "type": "documentation"
            }
        ]
    }
}

print("Starting enhancement script...")
print(f"Loaded enhancement data for Day 8")
print("This is a partial script - continuing to build full enhancements...")

