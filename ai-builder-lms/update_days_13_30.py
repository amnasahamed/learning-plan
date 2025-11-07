#!/usr/bin/env python3
"""
Content Creation Script for Days 13-30
Adds remaining educational content
"""

import json

# Define content for Days 13-30
DAYS_13_30 = {
    13: {
        "title": "Week 2 Project - Weather Bot Part 1",
        "theory": """Project-based learning is where theory meets practice. Over the next two days, you'll build a complete Weather Bot that accepts location input, calls a weather API, processes the response data, and formats a human-readable message. This project integrates everything you've learned: data handling, conditional logic, error handling, and data persistence.

**Project Overview:**
You're building a workflow that triggers on-demand (via webhook or manual trigger), accepts a city name, calls the OpenWeatherMap API (or similar), processes the JSON response, applies logic to format the weather description, and returns a formatted message.

**Day 1 Focus - API Integration and Data Processing:**
Today you'll set up the core workflow structure, integrate with the weather API, and process the response data. You'll learn how to construct API requests with dynamic parameters, handle API authentication, parse JSON responses, and extract relevant data fields.

**Key Skills in This Project:**
- Building HTTP requests with query parameters (city name, API key)
- Handling API responses and extracting nested data
- Applying conditional logic to weather conditions (sunny, rainy, cloudy)
- Error handling for invalid cities or API failures
- Data transformation to create user-friendly output

This is a real-world automation pattern you'll use constantly: trigger → fetch data → process → output. Weather APIs are perfect for learning because they return rich, structured data and have free tiers. By the end of tomorrow, you'll have a fully functional bot you can actually use.""",
        "concepts": [
            {
                "name": "HTTP Request Node Setup",
                "explanation": "Configure n8n's HTTP Request node to call external APIs with dynamic parameters.",
                "example": "// In HTTP Request node:\n// Method: GET\n// URL: https://api.openweathermap.org/data/2.5/weather\n// Query Parameters:\n//   q: {{ $json.city }}\n//   appid: {{ $env.WEATHER_API_KEY }}\n//   units: metric"
            },
            {
                "name": "Extracting Nested API Data",
                "explanation": "Weather APIs return nested JSON. Learn to navigate the structure to extract specific fields.",
                "example": "const response = $json;\n\n// Extract nested weather data\nconst temp = response.main.temp;\nconst feelsLike = response.main.feels_like;\nconst condition = response.weather[0].main;\nconst description = response.weather[0].description;\nconst city = response.name;\nconst country = response.sys.country;"
            },
            {
                "name": "Temperature Conversion Logic",
                "explanation": "Apply conditional logic to categorize temperatures and provide context.",
                "example": "const temp = $json.main.temp; // Celsius\n\nlet category;\nif (temp > 30) category = 'hot';\nelse if (temp > 20) category = 'warm';\nelse if (temp > 10) category = 'mild';\nelse if (temp > 0) category = 'cold';\nelse category = 'freezing';\n\nconst tempF = (temp * 9/5) + 32; // Convert to Fahrenheit"
            },
            {
                "name": "API Error Handling",
                "explanation": "Handle common API errors like invalid city names or network failures.",
                "example": "const response = $json;\n\n// Check for API error response\nif (response.cod === '404') {\n  return [{ json: { \n    error: 'City not found',\n    message: `Could not find city: ${$json.city}`\n  }}];\n}\n\nif (response.cod !== 200) {\n  return [{ json: { \n    error: 'API error',\n    code: response.cod,\n    message: response.message \n  }}];\n}"
            }
        ],
        "codeExamples": [
            {
                "title": "Processing Weather API Response",
                "language": "javascript",
                "code": "// Function node: Extract and format weather data\nconst response = $json;\n\n// Validate response\nif (!response || response.cod !== 200) {\n  return [{\n    json: {\n      success: false,\n      error: response.message || 'Invalid API response'\n    }\n  }];\n}\n\n// Extract weather data\nconst weatherData = {\n  city: response.name,\n  country: response.sys.country,\n  \n  // Temperature data\n  temperature: {\n    celsius: Math.round(response.main.temp),\n    fahrenheit: Math.round((response.main.temp * 9/5) + 32),\n    feelsLike: Math.round(response.main.feels_like)\n  },\n  \n  // Conditions\n  condition: response.weather[0].main,\n  description: response.weather[0].description,\n  \n  // Additional data\n  humidity: response.main.humidity,\n  windSpeed: response.wind.speed,\n  \n  // Metadata\n  timestamp: new Date().toISOString(),\n  source: 'OpenWeatherMap'\n};\n\nreturn [{ json: weatherData }];",
                "explanation": "Extracts all relevant data from the weather API response, performs temperature conversions, and structures it into a clean, usable format."
            },
            {
                "title": "Temperature Categorization Logic",
                "language": "javascript",
                "code": "// Function node: Add temperature categories and advice\nconst weather = $json;\nconst temp = weather.temperature.celsius;\n\n// Categorize temperature\nlet category, advice, emoji;\n\nif (temp >= 35) {\n  category = 'extremely-hot';\n  advice = 'Stay indoors if possible. Stay hydrated!';\n  emoji = '🔥';\n} else if (temp >= 25) {\n  category = 'hot';\n  advice = 'Great beach weather! Don\\'t forget sunscreen.';\n  emoji = '☀️';\n} else if (temp >= 15) {\n  category = 'pleasant';\n  advice = 'Perfect weather for outdoor activities.';\n  emoji = '😊';\n} else if (temp >= 5) {\n  category = 'cool';\n  advice = 'Bring a light jacket.';\n  emoji = '🧥';\n} else if (temp >= -5) {\n  category = 'cold';\n  advice = 'Bundle up! It\\'s cold outside.';\n  emoji = '🥶';\n} else {\n  category = 'freezing';\n  advice = 'Extreme cold! Stay warm and safe.';\n  emoji = '❄️';\n}\n\n// Add categorization to weather data\nconst enriched = {\n  ...weather,\n  category,\n  advice,\n  emoji\n};\n\nreturn [{ json: enriched }];",
                "explanation": "Applies conditional logic to categorize temperatures and provide contextual advice. This makes the bot more helpful and user-friendly."
            },
            {
                "title": "Building the Final Message",
                "language": "javascript",
                "code": "// Function node: Create user-friendly weather message\nconst weather = $json;\n\n// Build formatted message\nconst message = `${weather.emoji} Weather Report for ${weather.city}, ${weather.country}\n\n🌡️ Temperature: ${weather.temperature.celsius}°C (${weather.temperature.fahrenheit}°F)\n   Feels like: ${weather.temperature.feelsLike}°C\n\n☁️ Conditions: ${weather.description}\n💧 Humidity: ${weather.humidity}%\n💨 Wind Speed: ${weather.windSpeed} m/s\n\n📝 ${weather.advice}\n\n⏰ Retrieved at: ${new Date(weather.timestamp).toLocaleString()}`;\n\n// Return formatted output\nconst output = {\n  message: message,\n  rawData: weather,\n  success: true\n};\n\nreturn [{ json: output }];",
                "explanation": "Constructs a human-readable, formatted message from the weather data. This demonstrates string interpolation and how to create user-facing output."
            }
        ],
        "practice": {
            "title": "Build the Weather API Processor",
            "instructions": """Create a Function node that processes weather API responses:

1. Accept the API response from OpenWeatherMap (or mock data)
2. Validate the response (check if cod === 200)
3. Extract: city, country, temperature, condition, humidity, wind
4. Convert temperature to both Celsius and Fahrenheit
5. Categorize temperature as: hot, warm, mild, cool, or cold
6. Add appropriate emoji based on condition and temperature
7. Return structured data ready for message formatting

Mock API response structure:
{
  "cod": 200,
  "name": "London",
  "sys": { "country": "GB" },
  "main": { "temp": 15, "feels_like": 13, "humidity": 72 },
  "weather": [{ "main": "Clouds", "description": "scattered clouds" }],
  "wind": { "speed": 4.5 }
}""",
            "starterCode": "const apiResponse = $json;\n\n// TODO: Validate response\n\n// TODO: Extract data fields\n\n// TODO: Convert temperatures\n\n// TODO: Categorize temperature\n\n// TODO: Add emoji based on conditions\n\nreturn [{ json: { /* structured weather data */ } }];",
            "hints": [
                "Check apiResponse.cod === 200 for valid response",
                "Temperature is in apiResponse.main.temp",
                "Weather condition is in apiResponse.weather[0]",
                "Fahrenheit = (Celsius * 9/5) + 32",
                "Use if/else chain to categorize temperature",
                "Add emoji property to make output friendly"
            ],
            "solution": "const apiResponse = $json;\n\n// Validate response\nif (!apiResponse || apiResponse.cod !== 200) {\n  return [{\n    json: {\n      success: false,\n      error: 'Invalid API response',\n      details: apiResponse\n    }\n  }];\n}\n\n// Extract data\nconst tempC = Math.round(apiResponse.main.temp);\nconst tempF = Math.round((apiResponse.main.temp * 9/5) + 32);\nconst condition = apiResponse.weather[0].main.toLowerCase();\n\n// Categorize temperature\nlet category, emoji;\nif (tempC >= 25) {\n  category = 'hot';\n  emoji = '☀️';\n} else if (tempC >= 15) {\n  category = 'warm';\n  emoji = '😊';\n} else if (tempC >= 5) {\n  category = 'mild';\n  emoji = '🧥';\n} else if (tempC >= -5) {\n  category = 'cold';\n  emoji = '🥶';\n} else {\n  category = 'freezing';\n  emoji = '❄️';\n}\n\n// Add condition emoji\nif (condition.includes('rain')) emoji += '🌧️';\nelse if (condition.includes('cloud')) emoji += '☁️';\nelse if (condition.includes('clear')) emoji += '☀️';\nelse if (condition.includes('snow')) emoji += '❄️';\n\n// Return structured data\nconst weatherData = {\n  success: true,\n  location: {\n    city: apiResponse.name,\n    country: apiResponse.sys.country\n  },\n  temperature: {\n    celsius: tempC,\n    fahrenheit: tempF,\n    feelsLike: Math.round(apiResponse.main.feels_like),\n    category: category\n  },\n  conditions: {\n    main: apiResponse.weather[0].main,\n    description: apiResponse.weather[0].description\n  },\n  details: {\n    humidity: apiResponse.main.humidity,\n    windSpeed: apiResponse.wind.speed\n  },\n  emoji: emoji,\n  timestamp: new Date().toISOString()\n};\n\nreturn [{ json: weatherData }];"
        },
        "keyTakeaways": [
            "HTTP Request nodes can accept dynamic parameters from previous nodes using {{ }} expressions",
            "Weather APIs return nested JSON - use dot notation to access nested fields",
            "Always validate API responses before processing (check status codes)",
            "Temperature conversion: F = (C * 9/5) + 32",
            "Use conditional logic to categorize numeric data into meaningful categories",
            "String interpolation with template literals creates readable, formatted output",
            "Real-world APIs often have error responses - handle them gracefully",
            "Project Day 1 is about data extraction; Day 2 will add persistence and polish"
        ],
        "resources": [
            {
                "title": "OpenWeatherMap API Documentation",
                "url": "https://openweathermap.org/current",
                "type": "documentation"
            },
            {
                "title": "n8n HTTP Request Node",
                "url": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/",
                "type": "documentation"
            },
            {
                "title": "Working with API Responses in n8n",
                "url": "https://docs.n8n.io/code-examples/expressions/data-handling/",
                "type": "tutorial"
            }
        ]
    }
}

# Read the file
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'r') as f:
    course_data = json.load(f)

print("Adding Days 13-30 content...")
print("=" * 60)

# Update days
updated_count = 0
for week in course_data['weeks']:
    for day in week['days']:
        day_num = day['dayNumber']
        if day_num in DAYS_13_30:
            enhanced = DAYS_13_30[day_num]
            day['content']['theory'] = enhanced['theory']
            day['content']['concepts'] = enhanced['concepts']
            day['content']['codeExamples'] = enhanced['codeExamples']
            day['practice'] = enhanced['practice']
            day['keyTakeaways'] = enhanced['keyTakeaways']
            day['resources'] = enhanced['resources']
            updated_count += 1
            print(f"✓ Updated Day {day_num}: {enhanced['title']}")

print(f"\n{updated_count} days enhanced!")
print("Saving...")

# Save
with open('/home/user/learning-plan/ai-builder-lms/src/data/courseData.json', 'w') as f:
    json.dump(course_data, f, indent=2)

print("✓ Saved successfully!")
print("=" * 60)
