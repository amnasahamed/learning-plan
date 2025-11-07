// Due to JSON file size, generating complete content programmatically
// This will be converted to JSON

const week1Days = require('./courseData.json').weeks[0].days;

const generateDay4 = () => ({
  dayNumber: 4,
  title: "Loops & Iteration",
  duration: "30 minutes",
  learningObjectives: [
    "Master for loops and while loops",
    "Use forEach(), for...of, and for...in",
    "Understand when to use each loop type",
    "Avoid common loop pitfalls"
  ],
  content: {
    theory: "Loops allow you to execute code repeatedly. JavaScript offers several loop types, each suited for different scenarios. In n8n workflows, you'll often loop through arrays of data from previous nodes.\n\n**Loop Types:**\n- `for` loop - Traditional counter-based loop\n- `while` loop - Continues while condition is true\n- `forEach()` - Array method for iteration\n- `for...of` - Modern loop for iterable objects\n- `for...in` - Loop through object properties\n\n**When to Use Each:**\n- Use `forEach()` or `for...of` for arrays (most common in n8n)\n- Use `for` when you need the index or complex control\n- Use `while` when you don't know iterations in advance\n- Avoid `for...in` for arrays (use for objects only)",
    concepts: [
      {
        name: "for Loop",
        explanation: "Traditional loop with initialization, condition, and increment.",
        example: "for (let i = 0; i < 5; i++) {\n  console.log(i); // Prints 0, 1, 2, 3, 4\n}"
      },
      {
        name: "forEach() Method",
        explanation: "Array method that executes a function for each element.",
        example: "const names = ['Alice', 'Bob', 'Charlie'];\nnames.forEach((name, index) => {\n  console.log(`${index}: ${name}`);\n});"
      },
      {
        name: "for...of Loop",
        explanation: "Modern loop that iterates over array values directly.",
        example: "const fruits = ['apple', 'banana', 'orange'];\nfor (const fruit of fruits) {\n  console.log(fruit);\n}"
      },
      {
        name: "while Loop",
        explanation: "Continues looping while condition remains true.",
        example: "let count = 0;\nwhile (count < 3) {\n  console.log(count);\n  count++;\n}"
      }
    ],
    codeExamples: [
      {
        title: "Process Multiple Items with forEach",
        language: "javascript",
        code: "// Get all items from previous node\nconst items = $input.all();\nconst results = [];\n\nitems.forEach(item => {\n  const data = item.json;\n  \n  // Process each item\n  const processed = {\n    ...data,\n    processed: true,\n    timestamp: new Date().toISOString()\n  };\n  \n  results.push({ json: processed });\n});\n\nreturn results;",
        explanation: "forEach is perfect for processing each item in an array. This pattern is extremely common in n8n workflows."
      },
      {
        title: "Extract URLs from Array",
        language: "javascript",
        code: "// Input: array of webpage objects\nconst pages = $input.all().map(item => item.json);\nconst domains = [];\n\nfor (const page of pages) {\n  try {\n    const url = new URL(page.url);\n    domains.push(url.hostname);\n  } catch (error) {\n    // Skip invalid URLs\n    continue;\n  }\n}\n\nreturn [{ json: { domains, count: domains.length } }];",
        explanation: "for...of is clean and readable. The try/catch ensures we skip invalid URLs without breaking the loop."
      },
      {
        title: "Build Array with for Loop",
        language: "javascript",
        code: "// Create numbered items\nconst count = 10;\nconst items = [];\n\nfor (let i = 1; i <= count; i++) {\n  items.push({\n    id: i,\n    name: `Item ${i}`,\n    created: new Date().toISOString()\n  });\n}\n\nreturn items.map(item => ({ json: item }));",
        explanation: "Traditional for loop is useful when you need the index or counter value."
      }
    ]
  },
  practice: {
    title: "Sum Prices and Find Expensive Items",
    instructions: "You have an array of products. Each product has:\n- name (string)\n- price (number)\n- category (string)\n\nCreate a workflow that:\n1. Calculates the total of all prices\n2. Finds all products over $50\n3. Returns the total, expensive items, and count",
    starterCode: "const products = [\n  { name: 'Widget', price: 25, category: 'tools' },\n  { name: 'Gadget', price: 75, category: 'electronics' },\n  { name: 'Doohickey', price: 15, category: 'tools' },\n  { name: 'Gizmo', price: 100, category: 'electronics' }\n];\n\n// Your code here\n\nreturn [{ json: { /* result */ } }];",
    hints: [
      "Use a loop to sum all prices",
      "Use filter() or a loop to find expensive items",
      "Keep track of both total and filtered items"
    ],
    solution: "const products = [\n  { name: 'Widget', price: 25, category: 'tools' },\n  { name: 'Gadget', price: 75, category: 'electronics' },\n  { name: 'Doohickey', price: 15, category: 'tools' },\n  { name: 'Gizmo', price: 100, category: 'electronics' }\n];\n\nlet total = 0;\nconst expensiveItems = [];\n\nfor (const product of products) {\n  total += product.price;\n  \n  if (product.price > 50) {\n    expensiveItems.push(product);\n  }\n}\n\nreturn [{\n  json: {\n    total,\n    expensiveItems,\n    expensiveCount: expensiveItems.length\n  }\n}];"
  },
  keyTakeaways: [
    "for...of is the cleanest way to loop through arrays",
    "forEach() is great for array operations in n8n",
    "Always initialize variables before a loop",
    "Use break to exit a loop early, continue to skip an iteration",
    "Prefer array methods (.map, .filter) over manual loops when possible"
  ],
  resources: [
    {
      title: "JavaScript.info - Loops",
      url: "https://javascript.info/while-for",
      type: "article"
    },
    {
      title: "MDN - Loops and Iteration",
      url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration",
      type: "documentation"
    }
  ]
});

module.exports = { generateDay4 };
