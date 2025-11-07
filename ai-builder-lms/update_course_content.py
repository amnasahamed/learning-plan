#!/usr/bin/env python3
"""
Content Creation Script for Days 9-30
Replaces generic template content with real, educational material
"""

import json

# Define real educational content for each day
ENHANCED_CONTENT = {
    9: {
        "title": "Working with n8n Data",
        "theory": """n8n workflows process data through a chain of nodes, and understanding how to access and manipulate this data is fundamental to building effective automations. Unlike traditional programming where you explicitly pass variables, n8n uses special variables and methods to access data from the current node or previous nodes in your workflow.

**Core Data Access Methods:**

**$json** - The most commonly used variable, it represents the JSON data from the current item being processed. When a previous node sends data to your Function node, $json contains that data object. For example, if an HTTP Request node fetches user data, $json might be `{ "name": "John", "email": "john@example.com" }`.

**$input.all()** - Returns an array of ALL items passed to the current node. In n8n, nodes can process multiple items at once. Each item in the array has the structure `{ json: {...}, binary: {...} }`. This is essential when you need to aggregate, compare, or process multiple items together rather than one at a time.

**$node['NodeName'].json** - Allows you to reference data from any specific node in your workflow, not just the immediate predecessor. This is powerful for merging data from different branches or accessing data from earlier in the workflow. The node name must match exactly (including spaces and capitalization).

Understanding n8n's item structure `[{ json: {...} }]` is critical. Every Function node must return data in this format. The outer array can contain multiple items, and each item is an object with at least a `json` property containing your data.""",
        "concepts": [
            {
                "name": "$json - Current Item Data",
                "explanation": "Accesses the JSON data of the current item being processed. This is your primary way to read input data in a Function node.",
                "example": "// Access properties from current item\nconst email = $json.email;\nconst name = $json.name;\nconst userId = $json.id;\n\nconsole.log(`Processing user: ${name}`);"
            },
            {
                "name": "$input.all() - All Items Array",
                "explanation": "Returns an array containing all items passed to this node. Each item has the structure { json: {...}, binary: {...} }. Use this for batch operations or when you need to see all items at once.",
                "example": "// Get all items and extract emails\nconst allItems = $input.all();\nconst emailList = allItems.map(item => item.json.email);\n\n// Count total items\nconst totalCount = allItems.length;\nconsole.log(`Processing ${totalCount} items`);"
            },
            {
                "name": "$node['NodeName'].json - Reference Specific Nodes",
                "explanation": "Access data from any named node in your workflow. Useful for merging data from different sources or branches.",
                "example": "// Get data from different nodes\nconst apiData = $node['HTTP Request'].json;\nconst userData = $node['Get User'].json;\n\n// Merge data from multiple sources\nconst merged = {\n  ...apiData,\n  user: userData\n};"
            },
            {
                "name": "n8n Item Structure",
                "explanation": "All n8n nodes work with items in the format [{ json: {...}, binary: {...} }]. Your Function nodes must return this structure.",
                "example": "// Correct n8n return format\nconst result = {\n  processedData: 'value',\n  timestamp: new Date().toISOString()\n};\n\n// Must wrap in array with json property\nreturn [{ json: result }];"
            }
        ],
        "codeExamples": [
            {
                "title": "Processing Current Item with $json",
                "language": "javascript",
                "code": "// Function node: Enrich user data\nconst currentUser = $json;\n\n// Access nested properties\nconst email = currentUser.email;\nconst firstName = currentUser.profile?.firstName || 'Unknown';\n\n// Add computed fields\nconst enriched = {\n  ...currentUser,\n  emailDomain: email.split('@')[1],\n  processedAt: new Date().toISOString(),\n  userId: currentUser.id || Date.now(),\n  displayName: `${firstName} (${email})`\n};\n\n// Return in n8n format\nreturn [{ json: enriched }];",
                "explanation": "This example shows how to use $json to access the current item's data, extract nested properties safely with optional chaining, and add computed fields."
            },
            {
                "title": "Batch Processing with $input.all()",
                "language": "javascript",
                "code": "// Function node: Calculate statistics from all items\nconst allItems = $input.all();\n\n// Extract all values\nconst prices = allItems.map(item => item.json.price || 0);\nconst total = prices.reduce((sum, price) => sum + price, 0);\nconst average = total / prices.length;\nconst max = Math.max(...prices);\nconst min = Math.min(...prices);\n\n// Create summary object\nconst summary = {\n  itemCount: allItems.length,\n  totalValue: total,\n  averagePrice: average,\n  maxPrice: max,\n  minPrice: min,\n  items: allItems.map(item => item.json)\n};\n\n// Return single item with summary\nreturn [{ json: summary }];",
                "explanation": "Demonstrates using $input.all() to access all items at once, performing calculations across the entire dataset, and returning aggregated results."
            },
            {
                "title": "Merging Data from Multiple Nodes",
                "language": "javascript",
                "code": "// Function node: Merge data from different workflow branches\n// Assumes you have nodes named 'API Call' and 'Database Query'\n\n// Get current item\nconst currentItem = $json;\n\n// Reference other nodes by name\nconst apiResponse = $node['API Call'].json;\nconst dbRecord = $node['Database Query'].json;\n\n// Merge all data sources\nconst combined = {\n  // Current item data\n  requestId: currentItem.id,\n  \n  // API data\n  apiStatus: apiResponse.status,\n  apiData: apiResponse.data,\n  \n  // Database data\n  existingRecord: dbRecord.found,\n  recordData: dbRecord.record,\n  \n  // Metadata\n  mergedAt: new Date().toISOString(),\n  sources: ['current', 'api', 'database']\n};\n\nreturn [{ json: combined }];",
                "explanation": "Shows how to use $node['NodeName'].json to reference data from specific nodes in your workflow, enabling complex data merging from multiple sources."
            }
        ],
        "practice": {
            "title": "Build a Data Merger Workflow",
            "instructions": """Create a Function node that:

1. Takes the current item's customer ID ($json.customerId)
2. References order data from a node called 'Get Orders'
3. References product data from a node called 'Get Products'
4. Merges all data into a complete customer profile
5. Adds a computed field for total order value
6. Returns the merged data in proper n8n format

Your output should include:
- Customer info from current item
- List of orders from 'Get Orders' node
- Product details from 'Get Products' node
- Calculated total spent
- Timestamp""",
            "starterCode": "// Get current customer data\nconst customer = $json;\n\n// TODO: Get orders from 'Get Orders' node\n\n// TODO: Get products from 'Get Products' node\n\n// TODO: Calculate total spent\n\n// TODO: Merge all data\n\n// TODO: Return in n8n format\nreturn [{ json: { /* your result */ } }];",
            "hints": [
                "Use $json to get current item data",
                "Use $node['Get Orders'].json to reference the orders node",
                "Use $node['Get Products'].json to reference the products node",
                "The spread operator (...) is useful for merging objects",
                "Remember to return [{ json: {...} }] format"
            ],
            "solution": "// Get current customer data\nconst customer = $json;\n\n// Reference other nodes\nconst orders = $node['Get Orders'].json;\nconst products = $node['Get Products'].json;\n\n// Calculate total spent\nconst totalSpent = orders.orderList?.reduce((sum, order) => {\n  return sum + (order.amount || 0);\n}, 0) || 0;\n\n// Merge all data\nconst customerProfile = {\n  // Customer info\n  customerId: customer.customerId,\n  customerName: customer.name,\n  customerEmail: customer.email,\n  \n  // Orders\n  orders: orders.orderList || [],\n  orderCount: orders.orderList?.length || 0,\n  \n  // Products\n  products: products.productList || [],\n  \n  // Calculated fields\n  totalSpent: totalSpent,\n  averageOrderValue: orders.orderList?.length > 0 \n    ? totalSpent / orders.orderList.length \n    : 0,\n  \n  // Metadata\n  mergedAt: new Date().toISOString(),\n  dataSources: ['customer', 'orders', 'products']\n};\n\n// Return in n8n format\nreturn [{ json: customerProfile }];"
        },
        "keyTakeaways": [
            "$json gives you the current item's data - use this most of the time",
            "$input.all() returns ALL items as an array - use for batch processing or aggregations",
            "$node['NodeName'].json lets you reference any node in your workflow by its exact name",
            "Every Function node must return [{ json: {...} }] format - an array of items",
            "You can return multiple items by adding more objects to the array: [{ json: item1 }, { json: item2 }]",
            "Use optional chaining (?.) to safely access nested properties that might not exist",
            "These data access patterns are fundamental to every n8n workflow you build"
        ],
        "resources": [
            {
                "title": "n8n Data Handling Documentation",
                "url": "https://docs.n8n.io/code-examples/expressions/data-handling/",
                "type": "documentation"
            },
            {
                "title": "n8n Function Node Reference",
                "url": "https://docs.n8n.io/code-examples/methods/",
                "type": "documentation"
            },
            {
                "title": "Working with Items in n8n",
                "url": "https://docs.n8n.io/workflows/items/",
                "type": "tutorial"
            }
        ]
    },

    10: {
        "title": "Conditional Logic & Branching",
        "theory": """Conditional logic is the foundation of intelligent workflows that make decisions based on data. In n8n, you have two powerful approaches: the visual IF/Switch nodes for simple conditions, and JavaScript conditional statements for complex logic within Function nodes.

**JavaScript Conditional Statements:**

**if/else** - The most fundamental control structure. It evaluates a condition and executes different code blocks based on whether the condition is true or false. You can chain multiple conditions using `else if` to handle various scenarios.

**Ternary Operator** - A compact way to write simple if/else logic in a single line: `condition ? valueIfTrue : valueIfFalse`. This is perfect for assigning values conditionally or simple inline decisions.

**Switch Statements** - When you need to compare a single value against multiple possible cases, switch statements are more readable than multiple if/else chains. They're ideal for status codes, categories, or action types.

**n8n IF Node** - A visual node that routes data down different paths based on conditions. It's perfect for workflow branching where you want different nodes to execute based on data properties. For example, sending high-priority orders to one path and normal orders to another.

**n8n Switch Node** - Like the IF node but handles multiple conditions more elegantly. It can route data to different paths (like a routing table) based on matching conditions, with a default fallback path.

The key to effective conditional logic is choosing the right tool: use n8n nodes for workflow routing (visual branching), and use JavaScript conditions for data transformation within a single node.""",
        "concepts": [
            {
                "name": "if/else Statements",
                "explanation": "The fundamental conditional structure in JavaScript. Evaluates a condition and executes different code blocks based on the result.",
                "example": "const item = $json;\n\nif (item.status === 'urgent') {\n  item.priority = 'high';\n  item.notifyImmediately = true;\n} else if (item.status === 'normal') {\n  item.priority = 'medium';\n  item.notifyImmediately = false;\n} else {\n  item.priority = 'low';\n  item.notifyImmediately = false;\n}"
            },
            {
                "name": "Ternary Operator",
                "explanation": "A concise way to write simple if/else logic in one line. Format: condition ? valueIfTrue : valueIfFalse",
                "example": "const item = $json;\n\n// Simple ternary\nconst badge = item.isPremium ? 'PREMIUM' : 'STANDARD';\n\n// Nested ternary (use sparingly)\nconst discount = item.isPremium ? 0.20 : item.isLoyal ? 0.10 : 0;"
            },
            {
                "name": "Switch Statements",
                "explanation": "Efficiently handles multiple possible values for a single variable. More readable than long if/else chains for categorization.",
                "example": "const item = $json;\nlet department;\n\nswitch(item.category) {\n  case 'electronics':\n    department = 'tech';\n    break;\n  case 'clothing':\n    department = 'fashion';\n    break;\n  case 'food':\n    department = 'grocery';\n    break;\n  default:\n    department = 'general';\n}"
            },
            {
                "name": "n8n IF Node Usage",
                "explanation": "Visual branching in n8n workflows. The IF node evaluates conditions and routes data to 'true' or 'false' output paths.",
                "example": "// In the IF node, set condition:\n// Expression: {{ $json.amount > 1000 }}\n//\n// This routes:\n// - Orders over $1000 → 'true' path → VIP processing\n// - Orders under $1000 → 'false' path → Standard processing"
            }
        ],
        "codeExamples": [
            {
                "title": "Multi-Condition Order Routing",
                "language": "javascript",
                "code": "// Function node: Categorize and route orders\nconst order = $json;\n\n// Complex conditional logic\nlet category, priority, processingTime;\n\nif (order.amount > 5000 && order.customer.type === 'enterprise') {\n  category = 'vip';\n  priority = 1;\n  processingTime = '2-hours';\n  order.assignedTeam = 'enterprise';\n  order.requiresApproval = true;\n  \n} else if (order.amount > 1000 || order.isUrgent) {\n  category = 'priority';\n  priority = 2;\n  processingTime = '24-hours';\n  order.assignedTeam = 'priority';\n  order.requiresApproval = order.amount > 2500;\n  \n} else if (order.customer.isReturning) {\n  category = 'loyal';\n  priority = 3;\n  processingTime = '48-hours';\n  order.assignedTeam = 'standard';\n  order.requiresApproval = false;\n  \n} else {\n  category = 'standard';\n  priority = 4;\n  processingTime = '72-hours';\n  order.assignedTeam = 'standard';\n  order.requiresApproval = false;\n}\n\n// Add categorization to order\norder.category = category;\norder.priority = priority;\norder.estimatedProcessingTime = processingTime;\norder.categorizedAt = new Date().toISOString();\n\nreturn [{ json: order }];",
                "explanation": "Demonstrates complex multi-condition logic that categorizes orders based on amount, customer type, and urgency. Each branch sets different properties for downstream processing."
            },
            {
                "title": "Switch Statement for Status Mapping",
                "language": "javascript",
                "code": "// Function node: Map API status codes to user-friendly messages\nconst response = $json;\n\nlet userMessage, shouldRetry, severity;\n\n// Switch statement handles multiple discrete values elegantly\nswitch(response.statusCode) {\n  case 200:\n  case 201:\n    userMessage = 'Success! Your request was processed.';\n    shouldRetry = false;\n    severity = 'info';\n    break;\n    \n  case 400:\n    userMessage = 'Invalid request. Please check your input.';\n    shouldRetry = false;\n    severity = 'error';\n    break;\n    \n  case 401:\n  case 403:\n    userMessage = 'Authentication failed. Please log in again.';\n    shouldRetry = false;\n    severity = 'warning';\n    break;\n    \n  case 429:\n    userMessage = 'Too many requests. Please try again later.';\n    shouldRetry = true;\n    severity = 'warning';\n    break;\n    \n  case 500:\n  case 502:\n  case 503:\n    userMessage = 'Server error. We\\'ll retry automatically.';\n    shouldRetry = true;\n    severity = 'error';\n    break;\n    \n  default:\n    userMessage = `Unexpected response: ${response.statusCode}`;\n    shouldRetry = true;\n    severity = 'warning';\n}\n\nreturn [{\n  json: {\n    ...response,\n    userMessage,\n    shouldRetry,\n    severity,\n    processedAt: new Date().toISOString()\n  }\n}];",
                "explanation": "Shows how switch statements cleanly handle multiple status codes, including grouping similar cases together and providing a default fallback."
            },
            {
                "title": "Ternary Operators for Compact Logic",
                "language": "javascript",
                "code": "// Function node: Quick data enrichment with ternary operators\nconst user = $json;\n\n// Multiple ternary assignments\nconst enrichedUser = {\n  ...user,\n  \n  // Simple ternaries for flags\n  badge: user.isPremium ? '⭐ PREMIUM' : 'Standard',\n  canPost: user.emailVerified ? true : false,\n  maxUploadSize: user.isPremium ? 100 : 10, // MB\n  \n  // Ternary with calculations\n  discount: user.isPremium ? 0.20 : (user.orderCount > 10 ? 0.10 : 0),\n  \n  // Nested ternary for multi-tier logic\n  tier: user.totalSpent > 10000 ? 'platinum' : \n        user.totalSpent > 5000 ? 'gold' :\n        user.totalSpent > 1000 ? 'silver' : 'bronze',\n  \n  // Ternary for null coalescing\n  displayName: user.name ? user.name : user.email.split('@')[0],\n  \n  // Status computation\n  accountStatus: user.isActive && user.emailVerified ? 'active' : 'pending'\n};\n\nreturn [{ json: enrichedUser }];",
                "explanation": "Demonstrates various uses of ternary operators for compact conditional logic, including simple flags, calculations, and even nested ternaries (though these should be used sparingly for readability)."
            }
        ],
        "practice": {
            "title": "Build a Smart Email Classifier",
            "instructions": """Create a Function node that classifies incoming emails based on multiple criteria:

1. Check if email is from VIP sender (sender domain ends with 'vip.com')
2. Check if subject contains urgent keywords: 'URGENT', 'ASAP', 'CRITICAL'
3. Check if email has attachments
4. Based on these conditions, assign:
   - category: 'vip-urgent', 'vip-normal', 'urgent', 'with-attachment', or 'normal'
   - priority: 1-5 (1 is highest)
   - shouldNotify: boolean
   - responseTime: '1-hour', '4-hours', '24-hours'

Use if/else statements for the main logic and ternary operators for simple assignments.

Input format: { sender: '...', subject: '...', hasAttachments: boolean }""",
            "starterCode": "// Email classification logic\nconst email = $json;\n\n// TODO: Check conditions\nconst isVIP = // check if sender ends with 'vip.com'\nconst isUrgent = // check if subject contains urgent keywords\nconst hasAttachments = email.hasAttachments;\n\n// TODO: Classify with if/else\nlet category, priority, responseTime;\n\nif (/* VIP and urgent */) {\n  // Set values\n} else if (/* VIP */) {\n  // Set values\n} else if (/* Urgent */) {\n  // Set values\n}\n// Add more conditions...\n\n// TODO: Return classified email\nreturn [{ json: { /* result */ } }];",
            "hints": [
                "Use .endsWith('vip.com') to check sender domain",
                "Use .toUpperCase().includes('URGENT') for keyword checking",
                "VIP + Urgent should have highest priority",
                "Use ternary operator for shouldNotify based on priority",
                "Remember to include original email data in output"
            ],
            "solution": "// Email classification logic\nconst email = $json;\n\n// Check conditions\nconst isVIP = email.sender.endsWith('vip.com');\nconst subjectUpper = email.subject.toUpperCase();\nconst isUrgent = subjectUpper.includes('URGENT') || \n                 subjectUpper.includes('ASAP') || \n                 subjectUpper.includes('CRITICAL');\nconst hasAttachments = email.hasAttachments;\n\n// Classify with if/else\nlet category, priority, responseTime;\n\nif (isVIP && isUrgent) {\n  category = 'vip-urgent';\n  priority = 1;\n  responseTime = '1-hour';\n  \n} else if (isVIP) {\n  category = 'vip-normal';\n  priority = 2;\n  responseTime = '4-hours';\n  \n} else if (isUrgent) {\n  category = 'urgent';\n  priority = 2;\n  responseTime = '4-hours';\n  \n} else if (hasAttachments) {\n  category = 'with-attachment';\n  priority = 3;\n  responseTime = '24-hours';\n  \n} else {\n  category = 'normal';\n  priority = 4;\n  responseTime = '24-hours';\n}\n\n// Use ternary for notification flag\nconst shouldNotify = priority <= 2 ? true : false;\n\n// Return classified email\nconst classified = {\n  ...email,\n  category,\n  priority,\n  shouldNotify,\n  responseTime,\n  classifiedAt: new Date().toISOString(),\n  flags: {\n    isVIP,\n    isUrgent,\n    hasAttachments\n  }\n};\n\nreturn [{ json: classified }];"
        },
        "keyTakeaways": [
            "Use if/else for complex conditions and multi-statement code blocks",
            "Ternary operators are great for simple conditions and inline assignments",
            "Switch statements excel when comparing one value against multiple possibilities",
            "n8n IF nodes are perfect for visually branching your workflow into different paths",
            "Always include an else or default case to handle unexpected values",
            "Conditions can use && (AND), || (OR), and ! (NOT) to combine logic",
            "Choose the right tool: visual nodes for workflow routing, JavaScript for data transformation"
        ],
        "resources": [
            {
                "title": "MDN - if...else",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else",
                "type": "documentation"
            },
            {
                "title": "MDN - switch statement",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch",
                "type": "documentation"
            },
            {
                "title": "n8n IF Node Documentation",
                "url": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/",
                "type": "documentation"
            },
            {
                "title": "n8n Switch Node Documentation",
                "url": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch/",
                "type": "documentation"
            }
        ]
    },

    11: {
        "title": "Error Handling",
        "theory": """Robust error handling is what separates fragile scripts from production-ready workflows. In n8n automations, errors can occur for many reasons: API timeouts, invalid data, network failures, or unexpected responses. Without proper error handling, a single failed item can crash your entire workflow.

**try/catch Blocks:**
The fundamental JavaScript error handling mechanism. Code in the `try` block executes normally. If an error occurs, execution immediately jumps to the `catch` block where you can handle the error gracefully, log it, or return a safe fallback value.

**n8n Error Trigger Node:**
A special node that listens for workflow errors and executes an alternative path. This is perfect for sending notifications when workflows fail, logging errors to a database, or implementing retry logic at the workflow level.

**Graceful Degradation:**
The practice of designing workflows that continue to function (perhaps with reduced capability) even when parts fail. For example, if an enrichment API fails, return the data without enrichment rather than failing completely.

**Retry Patterns:**
Strategies for automatically retrying failed operations. Simple retry (try again immediately), exponential backoff (wait longer between each retry), or conditional retry (only retry specific error types). Many n8n nodes have built-in retry settings.

**Error Object Structure:**
JavaScript errors have `message`, `name`, and `stack` properties. Understanding these helps you log meaningful error information and implement intelligent error handling that responds differently to different error types.

Always validate input data before processing, use try/catch around risky operations, provide meaningful error messages, and ensure your workflows never completely crash due to a single bad item.""",
        "concepts": [
            {
                "name": "try/catch Error Handling",
                "explanation": "Wraps risky code in a try block and catches any errors that occur, preventing workflow crashes.",
                "example": "try {\n  const result = JSON.parse($json.data);\n  return [{ json: { success: true, result } }];\n} catch (error) {\n  return [{ json: { \n    success: false, \n    error: error.message,\n    input: $json.data \n  }}];\n}"
            },
            {
                "name": "Error Trigger Node",
                "explanation": "n8n node that executes when a workflow encounters an error. Use it to send alerts, log errors, or implement fallback logic.",
                "example": "// In Error Trigger node, you can access:\n// $json.error.message - Error message\n// $json.error.stack - Stack trace\n// $execution.id - Which execution failed\n// \n// Use this to send notifications or log to database"
            },
            {
                "name": "Graceful Degradation",
                "explanation": "Design workflows to continue functioning even when non-critical operations fail.",
                "example": "try {\n  // Try to enrich data with external API\n  const enriched = await callEnrichmentAPI($json);\n  $json.enrichment = enriched;\n} catch (error) {\n  // If enrichment fails, continue without it\n  $json.enrichment = null;\n  $json.enrichmentError = error.message;\n}\nreturn [{ json: $json }];"
            },
            {
                "name": "Validation Before Processing",
                "explanation": "Check data validity before performing operations to prevent errors.",
                "example": "const item = $json;\n\n// Validate required fields\nif (!item.email || !item.name) {\n  return [{ json: { \n    error: 'Missing required fields',\n    received: item \n  }}];\n}\n\n// Validate email format\nif (!item.email.includes('@')) {\n  return [{ json: { \n    error: 'Invalid email format',\n    email: item.email \n  }}];\n}\n\n// Safe to process\nreturn [{ json: { success: true, item } }];"
            }
        ],
        "codeExamples": [
            {
                "title": "Comprehensive Error Handling Pattern",
                "language": "javascript",
                "code": "// Function node: Process API responses with full error handling\nconst item = $json;\n\n// Step 1: Validate input\nif (!item || !item.apiResponse) {\n  return [{\n    json: {\n      success: false,\n      error: 'Missing API response data',\n      errorType: 'VALIDATION_ERROR',\n      timestamp: new Date().toISOString()\n    }\n  }];\n}\n\n// Step 2: Try to process with error handling\ntry {\n  // Parse response (might fail if invalid JSON)\n  const data = typeof item.apiResponse === 'string' \n    ? JSON.parse(item.apiResponse)\n    : item.apiResponse;\n  \n  // Validate response structure\n  if (!data.results || !Array.isArray(data.results)) {\n    throw new Error('Invalid response structure: missing results array');\n  }\n  \n  // Process data\n  const processed = data.results.map(result => ({\n    id: result.id || `generated-${Date.now()}`,\n    value: result.value || 0,\n    processedAt: new Date().toISOString()\n  }));\n  \n  // Success\n  return [{\n    json: {\n      success: true,\n      data: processed,\n      count: processed.length,\n      timestamp: new Date().toISOString()\n    }\n  }];\n  \n} catch (error) {\n  // Step 3: Handle errors gracefully\n  return [{\n    json: {\n      success: false,\n      error: error.message,\n      errorType: error.name,\n      errorStack: error.stack,\n      originalData: item,\n      timestamp: new Date().toISOString()\n    }\n  }];\n}",
                "explanation": "Complete error handling pattern with validation, try/catch, and detailed error reporting. This pattern prevents workflow crashes and provides useful debugging information."
            },
            {
                "title": "Batch Processing with Error Tracking",
                "language": "javascript",
                "code": "// Function node: Process multiple items and track errors\nconst items = $input.all();\n\nconst successful = [];\nconst failed = [];\n\nitems.forEach((item, index) => {\n  try {\n    // Validate item\n    if (!item.json.email) {\n      throw new Error('Missing email field');\n    }\n    \n    // Process item\n    const processed = {\n      ...item.json,\n      emailDomain: item.json.email.split('@')[1],\n      processed: true,\n      processedAt: new Date().toISOString()\n    };\n    \n    successful.push({ json: processed });\n    \n  } catch (error) {\n    // Track failed item with error details\n    failed.push({\n      index: index,\n      item: item.json,\n      error: error.message,\n      timestamp: new Date().toISOString()\n    });\n  }\n});\n\n// Return results summary\nif (successful.length === 0) {\n  // All items failed\n  return [{\n    json: {\n      success: false,\n      message: 'All items failed processing',\n      totalItems: items.length,\n      failed: failed\n    }\n  }];\n}\n\n// Return successful items + error summary\nreturn [\n  ...successful,\n  {\n    json: {\n      _summary: {\n        success: true,\n        successCount: successful.length,\n        failureCount: failed.length,\n        totalCount: items.length,\n        errors: failed\n      }\n    }\n  }\n];",
                "explanation": "Demonstrates processing multiple items while tracking errors. Instead of failing on the first error, this processes all items and returns successful ones plus an error summary."
            },
            {
                "title": "Retry Logic with Exponential Backoff",
                "language": "javascript",
                "code": "// Function node: Implement retry logic for API calls\nconst item = $json;\nconst maxRetries = 3;\nconst baseDelay = 1000; // 1 second\n\nasync function fetchWithRetry(url, retryCount = 0) {\n  try {\n    // Simulate API call (replace with actual fetch/axios call)\n    const response = await $http.get(url);\n    return { success: true, data: response.data };\n    \n  } catch (error) {\n    // Check if we should retry\n    if (retryCount < maxRetries) {\n      // Calculate delay with exponential backoff\n      const delay = baseDelay * Math.pow(2, retryCount);\n      \n      // Log retry attempt\n      console.log(`Retry ${retryCount + 1}/${maxRetries} after ${delay}ms`);\n      \n      // Wait before retrying\n      await new Promise(resolve => setTimeout(resolve, delay));\n      \n      // Recursive retry\n      return fetchWithRetry(url, retryCount + 1);\n    }\n    \n    // Max retries exceeded\n    throw new Error(`Failed after ${maxRetries} retries: ${error.message}`);\n  }\n}\n\n// Use the retry function\ntry {\n  const result = await fetchWithRetry(item.apiUrl);\n  return [{ json: result }];\n  \n} catch (error) {\n  return [{\n    json: {\n      success: false,\n      error: error.message,\n      url: item.apiUrl,\n      retriesAttempted: maxRetries,\n      timestamp: new Date().toISOString()\n    }\n  }];\n}",
                "explanation": "Advanced pattern showing retry logic with exponential backoff. This automatically retries failed API calls with increasing delays, perfect for handling temporary network issues or rate limits."
            }
        ],
        "practice": {
            "title": "Build a Resilient Data Processor",
            "instructions": """Create a Function node that safely processes user data with comprehensive error handling:

1. Validate input has required fields: name, email, age
2. Validate email format (must contain @ and .)
3. Validate age is a number between 0 and 150
4. Try to parse a JSON field called 'metadata' (use try/catch)
5. If ANY validation fails or parsing fails, return an error object (don't crash)
6. If all succeeds, return enriched user data

Your function should NEVER throw an uncaught error. All failures should return graceful error responses.

Test with:
- Valid data
- Missing fields
- Invalid email
- Invalid age
- Malformed JSON in metadata""",
            "starterCode": "const user = $json;\n\n// TODO: Validate required fields\n\n// TODO: Validate email format\n\n// TODO: Validate age range\n\n// TODO: Try to parse metadata with try/catch\n\n// TODO: Return success or error response\nreturn [{ json: { /* your result */ } }];",
            "hints": [
                "Check if fields exist with: if (!user.name)",
                "Check email format with: .includes('@') && .includes('.')",
                "Validate age with: typeof age === 'number' && age >= 0 && age <= 150",
                "Use try/catch around JSON.parse()",
                "Always return [{ json: {...} }] format, never throw errors",
                "Include the validation error details in error responses"
            ],
            "solution": "const user = $json;\n\n// Validation function\nfunction validateUser(user) {\n  const errors = [];\n  \n  // Check required fields\n  if (!user.name) errors.push('Missing required field: name');\n  if (!user.email) errors.push('Missing required field: email');\n  if (user.age === undefined) errors.push('Missing required field: age');\n  \n  // Validate email format\n  if (user.email && (!user.email.includes('@') || !user.email.includes('.'))) {\n    errors.push('Invalid email format');\n  }\n  \n  // Validate age\n  if (user.age !== undefined) {\n    if (typeof user.age !== 'number') {\n      errors.push('Age must be a number');\n    } else if (user.age < 0 || user.age > 150) {\n      errors.push('Age must be between 0 and 150');\n    }\n  }\n  \n  return errors;\n}\n\n// Validate\nconst validationErrors = validateUser(user);\nif (validationErrors.length > 0) {\n  return [{\n    json: {\n      success: false,\n      errorType: 'VALIDATION_ERROR',\n      errors: validationErrors,\n      receivedData: user,\n      timestamp: new Date().toISOString()\n    }\n  }];\n}\n\n// Try to parse metadata\nlet metadata = null;\nlet metadataError = null;\n\nif (user.metadata) {\n  try {\n    metadata = typeof user.metadata === 'string'\n      ? JSON.parse(user.metadata)\n      : user.metadata;\n  } catch (error) {\n    metadataError = error.message;\n    // Continue processing - metadata is optional\n  }\n}\n\n// Success - return enriched data\nconst enriched = {\n  ...user,\n  metadata: metadata,\n  metadataError: metadataError,\n  emailDomain: user.email.split('@')[1],\n  ageGroup: user.age < 18 ? 'minor' : user.age < 65 ? 'adult' : 'senior',\n  processedAt: new Date().toISOString(),\n  validation: {\n    passed: true,\n    checkedFields: ['name', 'email', 'age', 'metadata']\n  }\n};\n\nreturn [{ json: { success: true, data: enriched } }];"
        },
        "keyTakeaways": [
            "Always wrap risky operations in try/catch blocks to prevent workflow crashes",
            "Validate input data BEFORE processing to catch errors early",
            "Return error objects instead of throwing errors - workflows should never crash",
            "Include detailed error information (message, type, timestamp) for debugging",
            "Use n8n's Error Trigger node to handle workflow-level failures",
            "Implement graceful degradation - continue processing even when non-critical operations fail",
            "For batch processing, track errors per item rather than failing the entire batch",
            "Consider retry patterns for temporary failures (network issues, rate limits)"
        ],
        "resources": [
            {
                "title": "MDN - try...catch",
                "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch",
                "type": "documentation"
            },
            {
                "title": "n8n Error Trigger Node",
                "url": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger/",
                "type": "documentation"
            },
            {
                "title": "n8n Error Handling Guide",
                "url": "https://docs.n8n.io/workflows/error-handling/",
                "type": "tutorial"
            }
        ]
    },

    12: {
        "title": "Data Persistence",
        "theory": """Workflows often need to remember information between executions - tracking which emails have been processed, storing user preferences, maintaining counters, or caching API responses. Data persistence is how we store and retrieve data that survives beyond a single workflow execution.

**n8n Storage Options:**

**Set/Get nodes** - n8n's built-in key-value storage. Perfect for simple data persistence needs like flags, counters, or small configuration objects. Data persists across workflow executions and is scoped to your n8n instance.

**External Databases** - For larger datasets or complex queries, connect to PostgreSQL, MySQL, MongoDB, or other databases using n8n's database nodes. This is necessary when you need structured data, relationships, or need to share data with other applications.

**File Storage** - Use n8n's Write/Read Binary Files nodes to store data in files on disk. Good for logs, exports, or when you need human-readable storage.

**Redis/Cache Services** - For high-performance caching with TTL (time-to-live), Redis is excellent. Many n8n workflows use Redis to cache API responses and reduce external API calls.

**Workflow Static Data** - For configuration that doesn't change often, you can store small amounts of data directly in workflow settings or use Code nodes with const objects.

**When to Use What:**
- Simple flags/counters: Set/Get nodes
- Structured data, queries: External database
- Caching with expiry: Redis
- Large binary data: File storage
- Configuration: Workflow static data

Common patterns include: tracking processed items (to avoid duplicates), implementing rate limiting (counting API calls), caching expensive operations, and maintaining workflow state across executions.""",
        "concepts": [
            {
                "name": "n8n Set/Get Nodes",
                "explanation": "Built-in key-value storage for simple data persistence. Set node stores data, Get node retrieves it.",
                "example": "// In Set node:\n// Key: 'processedEmails'\n// Value: {{ $json.emailList }}\n//\n// In Get node:\n// Key: 'processedEmails'\n// Returns the stored value"
            },
            {
                "name": "Checking if Data Exists",
                "explanation": "Before using stored data, check if it exists to avoid errors on first run.",
                "example": "// Function node: Safe retrieval\nconst stored = $input.first().json;\n\nif (!stored || !stored.processedIds) {\n  // First run - initialize\n  return [{ json: { processedIds: [] } }];\n}\n\n// Data exists - use it\nreturn [{ json: stored }];"
            },
            {
                "name": "Appending to Stored Arrays",
                "explanation": "Common pattern: retrieve array, add new items, store back.",
                "example": "// Get existing array from storage\nconst stored = $node['Get Data'].json.items || [];\n\n// Add new item\nconst newItem = $json;\nstored.push(newItem);\n\n// Return to save with Set node\nreturn [{ json: { items: stored } }];"
            },
            {
                "name": "Deduplication Pattern",
                "explanation": "Use stored data to track what's been processed and avoid duplicates.",
                "example": "// Get processed IDs\nconst processed = $node['Get'].json.processedIds || [];\n\n// Get new items\nconst newItems = $input.all();\n\n// Filter out already processed\nconst toProcess = newItems.filter(item => {\n  return !processed.includes(item.json.id);\n});\n\n// Return items that haven't been processed\nreturn toProcess;"
            }
        ],
        "codeExamples": [
            {
                "title": "Email Deduplication System",
                "language": "javascript",
                "code": "// Function node: Track and prevent duplicate email processing\n// Assumes 'Get Processed' node retrieves stored data\n// and 'Set Processed' node will save it back\n\n// Get previously processed email IDs from storage\nconst storedData = $node['Get Processed'].json;\nconst processedIds = storedData.processedIds || [];\n\n// Get current incoming emails\nconst incomingEmails = $input.all().map(item => item.json);\n\n// Filter out emails we've already processed\nconst newEmails = incomingEmails.filter(email => {\n  return !processedIds.includes(email.id);\n});\n\n// If no new emails, return empty\nif (newEmails.length === 0) {\n  return [{\n    json: {\n      message: 'No new emails to process',\n      totalReceived: incomingEmails.length,\n      alreadyProcessed: incomingEmails.length\n    }\n  }];\n}\n\n// Add new email IDs to processed list\nconst newIds = newEmails.map(email => email.id);\nconst updatedProcessedIds = [...processedIds, ...newIds];\n\n// Keep only last 1000 IDs to prevent unlimited growth\nconst trimmedIds = updatedProcessedIds.slice(-1000);\n\n// Return:\n// 1. New emails to process (as separate items)\n// 2. Updated storage data\nreturn [\n  ...newEmails.map(email => ({ json: email })),\n  {\n    json: {\n      _storage: true,\n      processedIds: trimmedIds,\n      lastUpdated: new Date().toISOString(),\n      totalTracked: trimmedIds.length\n    }\n  }\n];",
                "explanation": "Complete deduplication system that tracks processed email IDs, filters out duplicates, and updates storage. Includes logic to trim old IDs to prevent unlimited growth."
            },
            {
                "title": "Rate Limiting with Counter",
                "language": "javascript",
                "code": "// Function node: Implement hourly API rate limiting\n// Tracks API calls per hour and enforces limits\n\n// Get counter from storage\nconst stored = $node['Get Counter'].json;\nconst now = new Date();\nconst currentHour = now.getHours();\nconst currentDate = now.toISOString().split('T')[0];\n\n// Initialize or reset counter if new hour\nlet counter = stored.counter || {};\nconst counterKey = `${currentDate}-${currentHour}`;\n\nif (!counter[counterKey]) {\n  // New hour - reset counter\n  counter = { [counterKey]: 0 };\n  \n  // Clean up old hours (keep only current)\n  // This prevents counter object from growing indefinitely\n}\n\n// Check rate limit\nconst maxCallsPerHour = 100;\nconst currentCalls = counter[counterKey];\n\nif (currentCalls >= maxCallsPerHour) {\n  return [{\n    json: {\n      success: false,\n      error: 'Rate limit exceeded',\n      limit: maxCallsPerHour,\n      currentCalls: currentCalls,\n      resetTime: `${currentHour + 1}:00`,\n      timestamp: now.toISOString()\n    }\n  }];\n}\n\n// Increment counter\ncounter[counterKey]++;\n\n// Return: allow request + updated counter\nreturn [\n  {\n    json: {\n      allowed: true,\n      remaining: maxCallsPerHour - counter[counterKey],\n      resetTime: `${currentHour + 1}:00`,\n      requestData: $json\n    }\n  },\n  {\n    json: {\n      _storage: true,\n      counter: counter,\n      lastUpdated: now.toISOString()\n    }\n  }\n];",
                "explanation": "Implements hourly rate limiting by maintaining a counter in storage. Tracks API calls per hour, enforces limits, and automatically resets each hour."
            },
            {
                "title": "Simple Cache Implementation",
                "language": "javascript",
                "code": "// Function node: Cache API responses with TTL\nconst request = $json;\nconst cacheKey = request.url;\nconst cacheDuration = 5 * 60 * 1000; // 5 minutes in milliseconds\n\n// Get cache from storage\nconst stored = $node['Get Cache'].json;\nconst cache = stored.cache || {};\n\n// Check if cached data exists and is still valid\nif (cache[cacheKey]) {\n  const cached = cache[cacheKey];\n  const age = Date.now() - cached.timestamp;\n  \n  if (age < cacheDuration) {\n    // Cache hit - return cached data\n    return [{\n      json: {\n        data: cached.data,\n        cacheHit: true,\n        cachedAt: new Date(cached.timestamp).toISOString(),\n        expiresIn: Math.round((cacheDuration - age) / 1000) + ' seconds'\n      }\n    }];\n  }\n}\n\n// Cache miss - need to fetch fresh data\n// This would trigger the next node to make the API call\nreturn [{\n  json: {\n    cacheHit: false,\n    needsFetch: true,\n    cacheKey: cacheKey,\n    url: request.url\n  }\n}];\n\n// After API call, another Function node would store the response:\n// cache[cacheKey] = {\n//   data: apiResponse,\n//   timestamp: Date.now()\n// };",
                "explanation": "Basic cache implementation that stores API responses with timestamps, checks cache validity based on TTL (time-to-live), and returns cached data when available."
            }
        ],
        "practice": {
            "title": "Build a Workflow State Tracker",
            "instructions": """Create a system that tracks which users have been onboarded:

1. Retrieve stored list of onboarded user IDs (from a Get node called 'Get Onboarded')
2. Handle the case where no data exists yet (first run)
3. Check if current user ($json.userId) has already been onboarded
4. If already onboarded, return a message saying so
5. If new user, add their ID to the list
6. Return:
   - Status (new or existing)
   - User data
   - Updated storage object (to save with Set node)

The storage object should include:
- Array of onboarded user IDs
- Count of total onboarded users
- Last updated timestamp""",
            "starterCode": "// Get current user\nconst user = $json;\n\n// TODO: Get stored data from 'Get Onboarded' node\n// Handle case where it doesn't exist yet\n\n// TODO: Check if user.userId is in the stored list\n\n// TODO: If existing, return appropriate message\n\n// TODO: If new, add to list and return updated storage\n\nreturn [{ json: { /* your result */ } }];",
            "hints": [
                "Use $node['Get Onboarded'].json to get stored data",
                "Initialize empty array if stored data doesn't exist: || []",
                "Use .includes(userId) to check if ID is in array",
                "Use spread operator to add new ID: [...oldArray, newId]",
                "Mark storage objects with _storage: true for easy identification"
            ],
            "solution": "// Get current user\nconst user = $json;\nconst userId = user.userId;\n\n// Get stored data (handle first run)\nconst stored = $node['Get Onboarded'].json || {};\nconst onboardedIds = stored.onboardedIds || [];\n\n// Check if user already onboarded\nif (onboardedIds.includes(userId)) {\n  return [{\n    json: {\n      status: 'existing',\n      message: `User ${userId} was already onboarded`,\n      onboardedAt: stored.lastUpdated,\n      userData: user\n    }\n  }];\n}\n\n// New user - add to list\nconst updatedIds = [...onboardedIds, userId];\n\n// Return user data + updated storage\nreturn [\n  {\n    json: {\n      status: 'new',\n      message: `User ${userId} successfully onboarded`,\n      totalOnboarded: updatedIds.length,\n      userData: user\n    }\n  },\n  {\n    json: {\n      _storage: true,\n      onboardedIds: updatedIds,\n      totalUsers: updatedIds.length,\n      lastUpdated: new Date().toISOString(),\n      lastUserId: userId\n    }\n  }\n];"
        },
        "keyTakeaways": [
            "Use n8n Set/Get nodes for simple key-value storage that persists between workflow executions",
            "Always handle the case where stored data doesn't exist yet (first run)",
            "Common pattern: Get → Process → Set for updating stored data",
            "Use deduplication to avoid processing the same items multiple times",
            "Trim stored arrays periodically to prevent unlimited growth",
            "For structured data or complex queries, use external databases instead",
            "Add timestamps to stored data for debugging and cache invalidation",
            "Mark storage objects clearly (e.g., _storage: true) to distinguish from regular data"
        ],
        "resources": [
            {
                "title": "n8n Set Node Documentation",
                "url": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/",
                "type": "documentation"
            },
            {
                "title": "n8n Database Integrations",
                "url": "https://docs.n8n.io/integrations/builtin/app-nodes/?categories=database",
                "type": "documentation"
            },
            {
                "title": "n8n Redis Node",
                "url": "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.redis/",
                "type": "documentation"
            }
        ]
    }
}

# Read original file
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'r') as f:
    course_data = json.load(f)

print("Starting content enhancement for Days 9-12...")
print("=" * 60)

# Update days 9-10 (we'll do more in batches)
updated_count = 0
for week in course_data['weeks']:
    for day in week['days']:
        day_num = day['dayNumber']
        if day_num in ENHANCED_CONTENT:
            enhanced = ENHANCED_CONTENT[day_num]
            day['content']['theory'] = enhanced['theory']
            day['content']['concepts'] = enhanced['concepts']
            day['content']['codeExamples'] = enhanced['codeExamples']
            day['practice'] = enhanced['practice']
            day['keyTakeaways'] = enhanced['keyTakeaways']
            day['resources'] = enhanced['resources']
            updated_count += 1
            print(f"✓ Updated Day {day_num}: {enhanced['title']}")

print(f"\n{updated_count} days enhanced successfully!")
print("\nSaving to file...")

# Save updated file
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'w') as f:
    json.dump(course_data, f, indent=2)

print("✓ File saved successfully!")
print("=" * 60)
