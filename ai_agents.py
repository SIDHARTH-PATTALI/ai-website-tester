import os, json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_test_steps(user_input: str):
    prompt = f"""
    You are a strict JSON generator for website test steps.

    Instruction: "{user_input}"

    Output only a JSON array. Do not include any extra text.
    Example:
    [
      {{"action": "open", "url": "https://example.com/login"}},
      {{"action": "fill", "field": "username", "value": "test"}},
      {{"action": "fill", "field": "password", "value": "1234"}},
      {{"action": "click", "selector": "button[type=submit]"}},
      {{"action": "check", "text": "Welcome"}}
    ]
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    raw_output = response.choices[0].message.content.strip()
    try:
        steps = json.loads(raw_output)
        return json.dumps(steps, indent=2)
    except Exception:
        return json.dumps([
            {"action": "open", "url": "https://the-internet.herokuapp.com/login"},
            {"action": "fill", "field": "username", "value": "tomsmith"},
            {"action": "fill", "field": "password", "value": "SuperSecretPassword!"},
            {"action": "click", "selector": "button[type=submit]"},
            {"action": "check", "text": "You logged into a secure area!"}
        ], indent=2)

def explain_results(results: list, question: str):
    prompt = f"""
    You are an AI assistant that explains website test results in simple English.

    Test Results:
    {results}

    User Question:
    {question}

    Give a clear, beginner-friendly explanation.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
