# 🌦️ Weather-Ready: AI Outfit Recommender

**Weather-Ready** is an intelligent Agentic AI web application that solves the "what should I wear today?" dilemma. By analyzing real-time meteorological data, the AI agent suggests a curated outfit—from head to toe—tailored specifically to your local climate and current conditions.

---

## ✨ Key Features

* 🌍 **Real-Time Intelligence:** Fetches live weather data (Temperature, Humidity, Conditions) via OpenWeather API.
* 👔 **Full Outfit Lookbook:** Generates a complete recommendation including **Top**, **Bottom**, and **Footwear**.
* 🔍 **Smart City Search:** Integrated city autocomplete for a seamless user experience.
* 🧠 **Agentic Architecture:** A dedicated Python-based logic layer for intelligent decision-making.
* 📱 **Responsive Design:** A sleek, modern UI optimized for both desktop and mobile devices.

---

## 🧠 System Architecture

The project utilizes a multi-tier microservice architecture to ensure a clean separation of concerns:

1.  **Frontend (UI):** A responsive interface that collects user input and displays recommendations.
2.  **Node.js Bridge (Middleware):** Handles city suggestions (Geo API) and acts as the secure communication layer between the UI and the AI.
3.  **Python AI Agent (Backend):** The core engine that processes weather data and executes the decision-making logic to select outfits.



---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 (Custom Properties & Flexbox), JavaScript (ES6+) |
| **Middleware** | Node.js, Express.js |
| **AI Agent** | Python 3.x, Flask |
| **APIs** | OpenWeather Current Weather & Geocoding APIs |

---

## 📁 Project Structure

```
AI_Specialist/
│
├── python_agent/      # AI Logic & Weather Engine
│   ├── api.py         # Flask Entry Point
│   ├── weather_api.py # Weather Data Fetching
│   ├── agent_logic.py # Outfit Decision Logic
│   └── memory.py      # Session management
│
├── node_bridge/       # Communication Layer
│   ├── server.js      # Express Server
│   └── package.json   # Node Dependencies
│
├── frontend/          # User Interface
│   ├── index.html     # Main Layout
│   ├── style.css      # Custom Styling
│   └── script.js      # Frontend Logic & API calls
│
└── README.md

```

## ▶️ Installation & Setup

### 1. Start the Python AI Agent

cd python_agent
python api.pyRuns at: http://localhost:5000


### 2. Start the Node.js Bridge

cd node_bridge
npm install
node server.js
 Runs at: http://localhost:3000

### 3. Launch the Application
Open frontend/index.html using a local server (like VS Code Live Server) to start using the app!

## 🧪 Sample Output
City: Bangalore

Condition: 26°C, Clear

Recommended Outfit:

👕 Top: Casual T-shirt

👖 Bottom: Lightweight Cotton Pants

👟 Footwear: Comfortable Sneakers

## 👤 Author
Ajaykumar AI & Full-Stack Development Enthusiast

## 📜 License
This project is intended for educational purposes only.


**Would you like me to generate a `requirements.txt` file for your Python environment to make the setup even easier?**