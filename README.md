# Simple AI Based Website Tester

A modular Python project that uses AI (Groq) and Selenium to automatically test websites. Users can provide natural language instructions like:

> "Test login on https://the-internet.herokuapp.com/login with username 'tomsmith' and password 'SuperSecretPassword!'"

The AI converts these instructions into structured test steps, executes them in a headless browser, and explains the results in plain English.

---

## Features

- **Natural Language → JSON Steps**: AI generates test steps automatically.  
- **Automated Browser Actions**: Opens URLs, fills forms, clicks buttons, and checks for text using Selenium.  
- **AI Explanations**: Get human-friendly explanations of why a test passed or failed.   
- **Streamlit UI**: Interactive web interface to run tests and ask follow-up questions.

---
