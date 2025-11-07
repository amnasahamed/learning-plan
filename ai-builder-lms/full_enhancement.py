#!/usr/bin/env python3
import json

# Read the original course data
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'r') as f:
    course_data = json.load(f)

# Comprehensive enhancement data for Days 8-30
enhancements = {
    8: {  # Day 8 already included in previous file - HTTP Requests Basics
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
    },
    9: {  # Working with n8n Data
        "theory": "n8n has special variables and patterns for accessing data within workflows. Understanding these is crucial for building complex automations. Unlike standalone JavaScript, n8n provides context-aware variables that give you access to data from previous nodes, current items, and workflow execution context.\n\n**Key n8n Variables:**\n- **$json**: The JSON data of the current item being processed\n- **$input.all()**: Returns all items from the previous node as an array\n- **$input.first()**: Returns only the first item\n- **$node['NodeName'].json**: Access data from a specific node\n- **$items()**: Access all items (similar to $input.all())\n- **$itemIndex**: The index of the current item (useful in loops)\n\n**Data Flow Patterns:**\nData in n8n flows through nodes as an array of items. Each item has a `json` property containing the actual data. When you need to transform data, you typically: 1) Get all items, 2) Extract the json property, 3) Transform, 4) Return in n8n format.\n\n**Why This Matters:**\nMastering n8n's data access patterns lets you merge data from multiple sources, create complex transformations, and build sophisticated workflows that reference earlier steps.",
        "concepts": [
            {
                "name": "$json - Current Item",
                "explanation": "Accesses the JSON data of the current item. When a node receives multiple items, it processes them one by one, and $json refers to the current one being processed.",
                "example": "// Single item processing\nconst item = $json;\nconst userName = item.name;\nconst userEmail = item.email;\n\n// Transform current item\nreturn [{\n  json: {\n    fullName: userName,\n    contact: userEmail,\n    processed: true\n  }\n}];"
            },
            {
                "name": "$input.all() - All Items",
                "explanation": "Returns all items from the previous node as an array. Each item is an object with properties like 'json', 'binary', and 'pairedItem'. Use this when you need to process multiple items together.",
                "example": "// Get all items\nconst items = $input.all();\n\n// Extract json from each\nconst allData = items.map(item => item.json);\n\n// Calculate aggregate\nconst total = allData.reduce((sum, item) => sum + item.price, 0);\n\nreturn [{ json: { total, itemCount: items.length } }];"
            },
            {
                "name": "$node['NodeName'].json - Reference Specific Node",
                "explanation": "Access data from a specific node by name, even if it's not the immediately previous node. This is powerful for merging data from different branches of your workflow.",
                "example": "// Get data from multiple nodes\nconst userData = $node['Get User'].json;\nconst orderData = $node['Get Orders'].json;\nconst settingsData = $node['Get Settings'].json;\n\n// Merge all data\nconst combined = {\n  user: {\n    id: userData.id,\n    name: userData.name\n  },\n  orders: orderData,\n  settings: settingsData,\n  mergedAt: new Date().toISOString()\n};\n\nreturn [{ json: combined }];"
            },
            {
                "name": "$itemIndex - Current Index",
                "explanation": "The zero-based index of the current item being processed. Useful for adding sequence numbers or batch processing.",
                "example": "// Add sequence number to each item\nconst item = $json;\n\nreturn [{\n  json: {\n    sequenceNumber: $itemIndex + 1, // 1-based numbering\n    ...item,\n    isFirst: $itemIndex === 0,\n    processedAt: new Date().toISOString()\n  }\n}];"
            }
        ],
        "codeExamples": [
            {
                "title": "Merge Data from Multiple Nodes",
                "language": "javascript",
                "code": "// Scenario: You have user data from one API and their orders from another\n// Now you want to combine them\n\n// Get data from named nodes\nconst user = $node['Get User API'].json;\nconst orders = $node['Get Orders API'].json; // Assume this is an array\n\n// Calculate order statistics\nconst totalOrders = orders.length;\nconst totalSpent = orders.reduce((sum, order) => sum + order.amount, 0);\nconst avgOrderValue = totalOrders > 0 ? totalSpent / totalOrders : 0;\n\n// Create enriched user profile\nconst enrichedProfile = {\n  userId: user.id,\n  name: user.name,\n  email: user.email,\n  orderStats: {\n    totalOrders,\n    totalSpent,\n    avgOrderValue: avgOrderValue.toFixed(2),\n    lastOrderDate: orders.length > 0 ? orders[0].date : null\n  },\n  // Add customer tier based on spending\n  customerTier: totalSpent > 1000 ? 'gold' : totalSpent > 500 ? 'silver' : 'bronze',\n  enrichedAt: new Date().toISOString()\n};\n\nreturn [{ json: enrichedProfile }];",
                "explanation": "Shows how to merge data from multiple API calls using node references. This pattern is essential for enriching data from multiple sources."
            },
            {
                "title": "Process All Items with Aggregation",
                "language": "javascript",
                "code": "// Get all items from previous node (e.g., list of transactions)\nconst items = $input.all().map(item => item.json);\n\n// Group by category\nconst categories = {};\n\nitems.forEach(item => {\n  const category = item.category || 'uncategorized';\n  \n  if (!categories[category]) {\n    categories[category] = {\n      count: 0,\n      total: 0,\n      items: []\n    };\n  }\n  \n  categories[category].count++;\n  categories[category].total += item.amount;\n  categories[category].items.push(item.id);\n});\n\n// Convert to array and add averages\nconst summary = Object.keys(categories).map(category => ({\n  category,\n  count: categories[category].count,\n  total: categories[category].total,\n  average: categories[category].total / categories[category].count,\n  itemIds: categories[category].items\n}));\n\n// Sort by total descending\nsummary.sort((a, b) => b.total - a.total);\n\nreturn [{\n  json: {\n    summary,\n    totalItems: items.length,\n    totalAmount: items.reduce((sum, item) => sum + item.amount, 0),\n    categoriesCount: summary.length\n  }\n}];",
                "explanation": "Demonstrates aggregating data from multiple items. This is useful for creating reports, calculating totals, or grouping related data."
            },
            {
                "title": "Split and Transform Multiple Items",
                "language": "javascript",
                "code": "// Get all input items\nconst items = $input.all().map(item => item.json);\n\n// Transform each item and split into valid/invalid\nconst results = items.map((item, index) => {\n  // Validation\n  const isValid = item.email && \n                  item.email.includes('@') && \n                  item.name && \n                  item.name.length > 0;\n  \n  if (isValid) {\n    return {\n      valid: true,\n      data: {\n        id: item.id || Date.now() + index,\n        name: item.name.trim(),\n        email: item.email.toLowerCase().trim(),\n        processedAt: new Date().toISOString()\n      }\n    };\n  } else {\n    return {\n      valid: false,\n      originalData: item,\n      errors: [\n        !item.email ? 'Missing email' : null,\n        item.email && !item.email.includes('@') ? 'Invalid email format' : null,\n        !item.name ? 'Missing name' : null\n      ].filter(Boolean)\n    };\n  }\n});\n\n// Separate valid and invalid\nconst validItems = results.filter(r => r.valid).map(r => r.data);\nconst invalidItems = results.filter(r => !r.valid);\n\n// Return summary with both arrays\nreturn [{\n  json: {\n    validItems,\n    invalidItems,\n    stats: {\n      total: items.length,\n      valid: validItems.length,\n      invalid: invalidItems.length,\n      successRate: `${((validItems.length / items.length) * 100).toFixed(1)}%`\n    }\n  }\n}];",
                "explanation": "Shows how to process multiple items, validate them, and split into categories. Essential pattern for data quality workflows."
            }
        ],
        "practice": {
            "title": "Build a Multi-Source Data Merger",
            "instructions": "You have data from three nodes:\n- 'User Data': { id: 1, name: 'Alice', email: 'alice@example.com' }\n- 'User Posts': [{ id: 101, title: 'Post 1', likes: 50 }, { id: 102, title: 'Post 2', likes: 30 }]\n- 'User Settings': { theme: 'dark', notifications: true }\n\nCreate a function that:\n1. Merges all three data sources\n2. Calculates total likes across all posts\n3. Determines if user is 'active' (has posts)\n4. Creates a unified user profile\n5. Returns formatted output",
            "starterCode": "// Access data from named nodes\nconst user = $node['User Data'].json;\nconst posts = $node['User Posts'].json;\nconst settings = $node['User Settings'].json;\n\n// Your merging logic here\n\nreturn [{ json: { /* unified profile */ } }];",
            "hints": [
                "Use $node['NodeName'].json to access each data source",
                "Use .reduce() to sum up likes from all posts",
                "Create a nested object structure for the profile",
                "Add computed fields like 'isActive' and 'totalLikes'",
                "Include a timestamp for when the merge occurred"
            ],
            "solution": "// Access data from named nodes\nconst user = $node['User Data'].json;\nconst posts = $node['User Posts'].json; // Array of posts\nconst settings = $node['User Settings'].json;\n\n// Calculate post statistics\nconst totalLikes = posts.reduce((sum, post) => sum + post.likes, 0);\nconst postCount = posts.length;\nconst avgLikes = postCount > 0 ? totalLikes / postCount : 0;\n\n// Determine activity level\nconst isActive = postCount > 0;\nconst activityLevel = postCount > 10 ? 'high' : postCount > 5 ? 'medium' : postCount > 0 ? 'low' : 'inactive';\n\n// Create unified profile\nconst unifiedProfile = {\n  user: {\n    id: user.id,\n    name: user.name,\n    email: user.email\n  },\n  content: {\n    postCount,\n    totalLikes,\n    avgLikes: avgLikes.toFixed(1),\n    posts: posts.map(p => ({\n      id: p.id,\n      title: p.title,\n      likes: p.likes\n    }))\n  },\n  settings: {\n    theme: settings.theme,\n    notifications: settings.notifications\n  },\n  analytics: {\n    isActive,\n    activityLevel,\n    engagement: totalLikes > 100 ? 'high' : totalLikes > 50 ? 'medium' : 'low'\n  },\n  meta: {\n    mergedAt: new Date().toISOString(),\n    source: 'multi-node-merger'\n  }\n};\n\nreturn [{ json: unifiedProfile }];"
        },
        "keyTakeaways": [
            "$json accesses current item, $input.all() gets all items",
            "Use $node['NodeName'].json to reference specific nodes",
            "$itemIndex provides the current item's position",
            "Always return data in n8n format: [{ json: {} }]",
            "Extract .json property when processing multiple items with .map(item => item.json)",
            "Merging multi-source data is a powerful pattern for enrichment"
        ],
        "resources": [
            {
                "title": "n8n Data Structure Documentation",
                "url": "https://docs.n8n.io/data/data-structure/",
                "type": "documentation"
            },
            {
                "title": "n8n Expressions Guide",
                "url": "https://docs.n8n.io/code-examples/expressions/",
                "type": "documentation"
            },
            {
                "title": "n8n Function Node Examples",
                "url": "https://docs.n8n.io/code-examples/expressions/function-nodes/",
                "type": "tutorial"
            }
        ]
    }
}

# Apply enhancements to course data
def enhance_day(day, enhancement):
    if 'theory' in enhancement:
        day['content']['theory'] = enhancement['theory']
    if 'concepts' in enhancement:
        day['content']['concepts'] = enhancement['concepts']
    if 'codeExamples' in enhancement:
        day['content']['codeExamples'] = enhancement['codeExamples']
    if 'practice' in enhancement:
        day['practice'] = enhancement['practice']
    if 'keyTakeaways' in enhancement:
        day['keyTakeaways'] = enhancement['keyTakeaways']
    if 'resources' in enhancement:
        day['resources'] = enhancement['resources']
    return day

# Find and enhance days
for week in course_data['weeks']:
    for day in week['days']:
        day_num = day['dayNumber']
        if day_num in enhancements:
            print(f"Enhancing Day {day_num}: {day['title']}")
            enhance_day(day, enhancements[day_num])

print(f"\nEnhanced {len(enhancements)} days so far.")
print("Days enhanced:", sorted(enhancements.keys()))
