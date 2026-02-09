# 🌦️ Weather-Based Outfit Recommendation Agent

A smart **Agentic AI web application** that recommends a **complete outfit** based on real-time weather conditions for a selected city.  
The system combines a **Python-based AI agent** with a **modern, responsive web interface**.

---

## ✨ Key Features

- 🌍 Real-time weather data using OpenWeather API  
- 👔 Full outfit recommendation:
  - Top  
  - Bottom  
  - Footwear  
- 🔍 City autocomplete while typing  
- 🧠 Python-based decision-making agent  
- 🌐 Web interface using HTML, CSS, and JavaScript  
- 🔗 Node.js middleware connecting frontend and Python agent  
- 📱 Fully responsive (desktop & mobile friendly)

---

## 🧠 System Architecture

Browser (HTML / CSS / JavaScript)
↓
Node.js Server (Express)
↓
Python AI Agent (Flask)
↓
OpenWeather APIs


- **Frontend**: Collects user input and displays results  
- **Node.js**: Acts as a bridge and handles city autocomplete  
- **Python Agent**: Fetches weather data and generates outfit recommendations  

---

## 🛠️ Technology Stack

### Frontend
- HTML  
- CSS (Responsive Design)  
- JavaScript  

### Backend
- Python  
- Flask  
- Node.js  
- Express.js  

### APIs
- OpenWeather Weather API  
- OpenWeather Geo API (city suggestions)

---

## 📁 Project Structure

AI_Specialist/
│
├── python_agent/
│ ├── api.py
│ ├── weather_api.py
│ ├── agent_logic.py
│ ├── memory.py
│
├── node_bridge/
│ ├── server.js
│ ├── package.json
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│
└── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Start the Python Agent
```bash
cd python_agent
python api.py
Runs at: http://localhost:5000

2️⃣ Start the Node.js Server
cd node_bridge
npm install
node server.js
Runs at: http://localhost:3000

3️⃣ Open the Frontend
Open frontend/index.html using:

VS Code Live Server (recommended), or

Any local HTTP server

🧪 Sample Output
City: Bangalore
Temperature: 26°C
Condition: Clear

Recommended Outfit:
Top: T-shirt
Bottom: Cotton Pants
Footwear: Sneakers

👤 Author

Ajaykumar
AI & Full-Stack Development Enthusiast


📜 License

This project is intended for educational purposes only.


---

If you want, I can next:
- Shorten this README for **resume**
- Convert it into a **project report**
- Prepare **viva questions & answers**
- Add **screenshots section**

Just tell me 👍