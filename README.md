Agent Development Kit (ADK) — Python Setup & Usage Guide

This guide explains how to create and run AI agents using the Google Agent Development Kit (ADK) in Python.
It includes environment setup, agent creation, configuration steps, and how to launch the optional web interface.

📌 Requirements

Python 3.10+

Pip

PowerShell (Windows) or Bash (Linux/Mac)

Google API Key from Google AI Studio
👉 https://aistudio.google.com/apikey

🚀 1. Create a Virtual Environment

Run the following command:

python -m venv <env_name>

🚀 2. Activate the Virtual Environment
Windows (PowerShell)
<env_name>\Scripts\activate

⚠️ If you get this error:
<env_name>\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.


Fix it using:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force


Then activate again.

🚀 3. Install the Agent Development Kit (ADK)
pip install google-adk

🚀 4. Create a New Agent

You can create an agent using the ADK CLI or using Python directly.

Option A — Using ADK CLI
adk create my_agent

📟 5. Setup During Agent Creation

You'll be prompted:

Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models (fill later)
Choose model (1, 2): 1

1. Google AI Studio: https://aistudio.google.com/apikey

Enter Google API key: <your_api_key>


After completion, your agent folder will be created:

Agent created in D:\Rep\My_Agents\my_first_agent:
- .env
- __init__.py
- agent.py

📁 6. Project Structure Explained
my_agent/
│
├── agent.py        # Main agent logic
├── .env            # Stores your API key & environment variables
├── __init__.py     # Marks folder as a Python package

.env Example:
GOOGLE_API_KEY=your_api_key_here

🧠 7. Running Your Agent

After creation, you can run or extend your agent by editing agent.py.

Typical usage inside your project:

from my_agent.agent import agent

response = agent.run("Hello!")
print(response)


Or run scripts you create inside the environment.

🌐 8. (Optional) Launch the Web Interface

To use the built-in ADK web UI:

adk web --port 8000


Then open in the browser:

http://localhost:8000

❓ Troubleshooting
⚠️ PowerShell script execution disabled

Run:

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

⚠️ Pip cannot find google-adk

Make sure your virtual environment is activated.

⚠️ API Key errors

Ensure .env contains:

GOOGLE_API_KEY=your_key

📌 Additional Notes

ADK supports tools, memory, custom actions, and multi-agent workflows.

You may add additional agents inside the same project.

Use agent.run() to interact programmatically.


📚 Learn More

For additional documentation, examples, and advanced usage guides, visit the official ADK docs:
👉 https://google.github.io/adk-docs/#learn-more