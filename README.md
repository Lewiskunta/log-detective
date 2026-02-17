# Production Log Detective

A tool that teaches junior developers how to read production logs and not just what went wrong, hence becoming a productivity multiplier by helping them troubleshoot issues faster in the long term

## The Problem

When something breaks in production, senior engineers find the issue in 90 seconds. Junior developers stare at the same logs and see nothing. The gap isn't intelligence  it's methodology.

Most developers paste their logs into an AI tool, get an answer, copy the fix, and move on. That's expensive Googling. Next time the same error hits, they're back to square one.

## How It Works

Instead of just returning an answer, the tool teaches you the mental process behind reading logs. Feed it your logs and a description of what broke. It responds with:

1. **What to look for first** - and why
2. **Step-by-step analysis** - tracing the sequence of events
3. **Root cause** - with a clear explanation
4. **Skill to practice** - so you improve with every incident

After using this consistently, you start finding issues yourself. That's the goal.

## Setup

**Get a free Groq API key**

Go to https://console.groq.com/keys, sign up (no credit card required), and create an API key.

**Install dependencies**
```bash
pip install groq httpx
```

**Add your API key**

Open `log_detective.py` and replace:
```python
api_key = "YOUR_GROQ_API_KEY_HERE"
```

**Run**
```bash
python log_detective.py
```

## Using It Effectively

The trap most developers fall into is using this as a search engine, paste logs, copy answer, move on.

The better approach: try reading the logs yourself first, form a theory, then run the tool and compare your thinking to the AI's analysis. Study the methodology, not just the answer. The patterns compound over time.

## Stack

- Python 3.x
- Groq API (free) - Llama 3.3 70B
- httpx
