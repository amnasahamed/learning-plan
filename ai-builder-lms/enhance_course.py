import json

# Read the original course data
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'r') as f:
    course_data = json.load(f)

# Enhancement data for Days 8-30
enhancements = {
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
                "example": "// In n8n HTTP Request node\n// Method: POST\n// URL: https://api.example.com/users\n// Body (JSON):\n{\n  \"name\": \"John Doe\",\n  \"email\": \"john@example.com\",\n  \"role\": \"user\"\n}\n\n// Process response:\nconst createdUser = $json;\nreturn [{ json: { success: true, userId: createdUser.id, message: 'User created' } }];"
            },
            {
                "name": "Request Headers",
                "explanation": "Headers provide metadata about the request. Common headers include Authorization (for API keys/tokens), Content-Type (data format), and Accept (expected response format).",
                "example": "// Common headers in n8n HTTP Request:\nconst headers = {\n  'Authorization': 'Bearer YOUR_API_TOKEN',\n  'Content-Type': 'application/json',\n  'Accept': 'application/json',\n  'User-Agent': 'n8n-automation'\n};"
            },
            {
                "name": "Status Code Handling",
                "explanation": "HTTP status codes indicate the result of your request. 2xx means success, 4xx means client error (bad request), 5xx means server error. Always check status codes to handle errors gracefully.",
                "example": "// In Function node after HTTP Request:\nconst response = $json;\nconst statusCode = $node['HTTP Request'].json.$statusCode;\n\nif (statusCode >= 200 && statusCode < 300) {\n  return [{ json: { success: true, data: response } }];\n} else if (statusCode >= 400 && statusCode < 500) {\n  return [{ json: { error: 'Client error', code: statusCode, message: response.error } }];\n} else {\n  return [{ json: { error: 'Server error', code: statusCode } }];\n}"
            }
        ],
        "codeExamples": [
            {
                "title": "Parse and Transform API Response",
                "language": "javascript",
                "code": "// After calling JSONPlaceholder API (GET /users)\nconst users = $json; // Array of user objects\n\n// Transform to include only essential fields\nconst transformedUsers = users.map(user => ({\n  id: user.id,\n  name: user.name,\n  email: user.email,\n  companyName: user.company.name,\n  // Add computed field\n  domain: user.email.split('@')[1],\n  // Add metadata\n  processedAt: new Date().toISOString()\n}));\n\n// Filter to only .com domains\nconst comUsers = transformedUsers.filter(user => \n  user.domain.endsWith('.com')\n);\n\nreturn comUsers.map(user => ({ json: user }));",
                "explanation": "Common pattern: fetch data from API, extract relevant fields, transform structure, filter based on criteria. This demonstrates how to work with API responses in n8n Function nodes."
            },
            {
                "title": "Build Dynamic API Request Parameters",
                "language": "javascript",
                "code": "// Build URL with query parameters dynamically\nconst filters = $json.filters; // From previous node\n\n// Construct query parameters object\nconst queryParams = {};\n\nif (filters.status) {\n  queryParams.status = filters.status;\n}\n\nif (filters.minPrice) {\n  queryParams.min_price = filters.minPrice;\n}\n\nif (filters.category) {\n  queryParams.category = filters.category;\n}\n\n// Add pagination\nqueryParams.page = filters.page || 1;\nqueryParams.limit = filters.limit || 20;\n\n// Return formatted for HTTP Request node\nreturn [{ \n  json: { \n    params: queryParams,\n    url: 'https://api.example.com/products',\n    // For logging\n    queryString: new URLSearchParams(queryParams).toString()\n  } \n}];",
                "explanation": "Shows how to dynamically build API request parameters based on input data. Use this pattern when you need flexible, configurable API calls."
            },
            {
                "title": "Handle API Errors Gracefully",
                "language": "javascript",
                "code": "// Check if HTTP Request node succeeded\nconst response = $json;\nconst httpNode = $node['HTTP Request'].json;\n\n// Check for errors\nif (!httpNode || httpNode.error) {\n  return [{\n    json: {\n      success: false,\n      error: 'API request failed',\n      details: httpNode.error || 'Unknown error',\n      timestamp: new Date().toISOString()\n    }\n  }];\n}\n\n// Check status code\nconst statusCode = httpNode.$statusCode || 200;\n\nif (statusCode >= 400) {\n  return [{\n    json: {\n      success: false,\n      statusCode: statusCode,\n      error: response.message || 'Request failed',\n      retryable: statusCode >= 500 // Server errors are retryable\n    }\n  }];\n}\n\n// Success case\nreturn [{\n  json: {\n    success: true,\n    data: response,\n    processedAt: new Date().toISOString()\n  }\n}];",
                "explanation": "Production-ready error handling for API calls. Always check for errors and status codes before processing response data. This prevents workflow crashes."
            }
        ],
        "practice": {
            "title": "Build a GitHub User Lookup",
            "instructions": "Create a workflow that:\n1. Accepts a GitHub username as input\n2. Calls the GitHub API (GET https://api.github.com/users/{username})\n3. Extracts: name, public repos count, followers, bio\n4. Handles errors if user doesn't exist\n5. Returns formatted user data\n\nTest with usernames: 'octocat', 'torvalds', 'nonexistentuser123'",
            "starterCode": "// After HTTP Request node to https://api.github.com/users/octocat\nconst response = $json;\n\n// Your transformation code here\n// Handle success and error cases\n\nreturn [{ json: { /* your result */ } }];",
            "hints": [
                "GitHub API returns 404 if user doesn't exist - handle this case",
                "Extract fields: login, name, public_repos, followers, bio, avatar_url",
                "Add a 'found' boolean to indicate success/failure",
                "Use optional chaining (?.) for fields that might be null",
                "Add timestamp to track when data was fetched"
            ],
            "solution": "// After HTTP Request node\nconst response = $json;\nconst statusCode = $node['HTTP Request'].json.$statusCode;\n\n// Handle 404 - user not found\nif (statusCode === 404) {\n  return [{\n    json: {\n      found: false,\n      error: 'User not found',\n      username: $node['HTTP Request'].parameter.url.split('/').pop()\n    }\n  }];\n}\n\n// Handle other errors\nif (statusCode >= 400) {\n  return [{\n    json: {\n      found: false,\n      error: 'API error',\n      statusCode: statusCode\n    }\n  }];\n}\n\n// Success - transform data\nconst userData = {\n  found: true,\n  username: response.login,\n  name: response.name || 'No name provided',\n  bio: response.bio || 'No bio',\n  publicRepos: response.public_repos,\n  followers: response.followers,\n  following: response.following,\n  avatarUrl: response.avatar_url,\n  profileUrl: response.html_url,\n  // Computed fields\n  isActive: response.public_repos > 0,\n  popularity: response.followers + response.public_repos,\n  // Metadata\n  fetchedAt: new Date().toISOString()\n};\n\nreturn [{ json: userData }];"
        },
        "keyTakeaways": [
            "HTTP is the foundation of all API communication",
            "GET retrieves data, POST creates data, PUT/PATCH updates, DELETE removes",
            "Always check status codes (2xx success, 4xx client error, 5xx server error)",
            "Headers carry authentication and metadata",
            "Query parameters pass data in the URL, body data in POST/PUT",
            "Handle errors gracefully to prevent workflow crashes"
        ],
        "resources": [
            {
                "title": "MDN - HTTP Overview",
                "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview",
                "type": "documentation"
            },
            {
                "title": "HTTP Status Codes Reference",
                "url": "https://httpstatuses.com/",
                "type": "reference"
            },
            {
                "title": "n8n HTTP Request Node Docs",
                "url": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/",
                "type": "documentation"
            }
        ]
    }
}

print("Enhancement script loaded. Processing Day 8...")
print(json.dumps(enhancements[8], indent=2))
