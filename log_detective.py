import os
import httpx
from groq import Groq

def log_detective(logs, issue_description, api_key):
    """
    AI-powered log reading tutor
    Teaches junior devs HOW to read production logs
    """
    client = Groq(
        api_key=api_key,
        http_client=httpx.Client(verify=False)
    )
    
    prompt = f"""I'm a junior developer learning to read production logs.

Something broke in production: {issue_description}

Here are the logs (I don't know what I'm looking at):
{logs}

Act as my mentor. Don't just tell me what's wrong - teach me YOUR methodology:

1. FIRST LOOK: What do you look at FIRST in any log file? (And why?)
2. ANALYSIS STEPS: Walk through your mental process step-by-step as you read these logs
3. ROOT CAUSE: What actually broke?
4. SKILL TO PRACTICE: What's the ONE pattern I should remember for next time?

Teach me to think like a senior engineer reading logs."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.7
    )
    
    return response.choices[0].message.content

# Example: Real production scenario
def demo():
    production_logs = """
2026-02-15 14:23:01 INFO [AuthService] Starting user authentication request
2026-02-15 14:23:01 DEBUG [DatabasePool] Attempting connection to db.prod.internal:5432
2026-02-15 14:23:01 INFO [RequestHandler] Processing login from IP 192.168.1.1
2026-02-15 14:23:02 ERROR [DatabasePool] Connection timeout to db.prod.internal:5432 (timeout=1000ms)
2026-02-15 14:23:02 INFO [DatabasePool] Retrying connection (attempt 1/3)
2026-02-15 14:23:04 ERROR [DatabasePool] Connection timeout to db.prod.internal:5432 (timeout=1000ms)
2026-02-15 14:23:04 WARNING [DatabasePool] Max connection retries exceeded
2026-02-15 14:23:04 ERROR [AuthService] Failed to authenticate user_id=12847 - database unavailable
2026-02-15 14:23:04 INFO [RequestHandler] Returning 503 Service Unavailable to client
"""
    
    issue = "Users can't log in - getting 503 errors"
    
    api_key = "API KEY HERE"
    
    print("=" * 60)
    print("PRODUCTION LOG DETECTIVE - AI Learning Tool")
    print("=" * 60)
    print("\nTHE PROBLEM:")
    print(f"   {issue}\n")
    print("THE LOGS (what you see in production):")
    print(production_logs)
    print("\nAI MENTOR TEACHING YOU TO READ THESE LOGS:\n")
    print("-" * 60)
    
    teaching_response = log_detective(production_logs, issue, api_key)
    print(teaching_response)
    print("\n" + "=" * 60)

if __name__ == "__main__":
    demo()