# 🚀 Python ADK (Agent Development Kit)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/Google-Gemini-green?logo=google" />
  <img src="https://img.shields.io/badge/ADK-CLI-orange" />
</p>

<p align="center">
  <img width="800" src="https://capsule-render.vercel.app/api?type=rect&color=0:333,100:0d6efd&height=120&section=header&text=Build%20AI%20Agents%20with%20Gemini&fontColor=ffffff&fontSize=40" />
</p>

A **modern, visually rich, GitHub‑ready README** to help you set up and use the **Python ADK** for building **Gemini-powered AI agents**.

---

## 🌟 Features

* ⚡ **Quickstart-friendly**
* 🎨 **Visual diagrams & icons**
* 🤖 **Agent creation made simple**
* 🌐 **Optional Web UI**
* 📦 **Clean folder structure overview**

---

## 📌 Table of Contents

* [Prerequisites](#-prerequisites)
* [Create Virtual Environment](#-1-create--activate-virtual-environment)
* [Install ADK](#-2-install-adk)
* [Create Your First Agent](#-3-create-your-first-agent)
* [Run Your Agent](#-5-run-your-agent)
* [Web UI](#-6-optional-use-the-web-ui)
* [Project Structure](#-7-visual-project-overview)
* [Troubleshooting](#-troubleshooting)
* [Learn More](#-learn-more)

---

## 🎯 Prerequisites

<p align="center">

| Requirement       | Version               |
| ----------------- | --------------------- |
| 🐍 Python         | **3.10+**             |
| 🌐 Internet       | Required              |
| 🔑 Google API Key | From Google AI Studio |

👉 **Get API Key:** [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

</p>

---

## 📁 1. Create & Activate Virtual Environment

### 🔨 Create environment

```bash
python -m venv <env_name>
```

### ⚡ Activate (Windows PowerShell)

```bash
<env_name>/Scripts/activate
```

### ⚠️ PowerShell Execution Policy Error?

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

Then activate again.

---

## 📦 2. Install ADK

```bash
pip install google-adk
```

---

## 🤖 3. Create Your First Agent

### Option A — ADK CLI

```bash
adk create <agent_name>
```

```bash
adk create my_agent
```

### Option B — Python

```bash
python -m agents.create_agent <agent_name>
```

## 🧭 4. Agent Creation Flow

```
Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models
Choose model (1, 2): 1

Enter Google API key: <your_api_key>
```
🎉 **Your Agent Is Ready!**

---

## 🧠 5. Run Your Agent

```python
adk run <agent_name>
```
🎉 **Your Agent Is Ready!**

## 🌐 6. (Optional) Use the Web UI

```bash
adk web --port 8000
```

Open browser:

### 👉 [http://localhost:8000](http://localhost:8000)

---

## 📚 7. Visual Project Overview

```
📦 my_agent
│
├── 🧠 agent.py        → Your agent logic
├── 🔐 .env             → Contains GOOGLE_API_KEY
└── 📄 __init__.py      → Package marker
```

---

## ❓ Troubleshooting

| Issue                           | Fix                                                        |
| ------------------------------- | ---------------------------------------------------------- |
| 🔴 Script blocked in PowerShell | Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force |
| 🔴 API key not found            | Ensure .env contains GOOGLE_API_KEY=your_key               |
| 🔴 Module not found             | Activate virtual environment                               |
| 🔴 Cannot install google-adk    | pip install --upgrade pip                                  |

---

## 📘 Learn More

📖 Full docs & examples:
👉 [https://google.github.io/adk-docs/#learn-more](https://google.github.io/adk-docs/#learn-more)

---

<p align="center">
  <img width="600" src="https://capsule-render.vercel.app/api?type=soft&color=0d6efd&text=Happy%20Building!&fontColor=fff&height=120" />
</p>
