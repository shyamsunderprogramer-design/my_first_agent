# create virtual environment
python -m venv <env_name>

# activate virtual environment
<env_name>\Scripts\activate

# if incase if you get error "<env_name>\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system." try this
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# install Agent Development Kit (ADK) for Python (must Python 3.10 or later)
pip install google-adk

# create agent
adk create my_agent
# or
python -m agents.create_agent <agent_name>

// reposnse: Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models (fill later)        
Choose model (1, 2): 1
1. Google AI
 Studio: https://aistudio.google.com/apikey

Enter Google API key: <your_api_key>

Agent created in D:\Rep\My_Agents\my_first_agent:
- .env
- __init__.py
- agent.py
//


# if want to use web interface
adk web --port 8000
