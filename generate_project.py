import openai
import os
import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are an AI that creates small, interesting beginner-level Python projects."},
    {"role": "user", "content": "Give me a unique and creative Python project idea with a one-line description."}
  ]
)

idea = response.choices[0].message['content']
project_title = idea.split(":")[0].strip().replace(" ", "-").lower()
description = idea.split(":", 1)[1].strip()

today = datetime.datetime.now().strftime("%Y-%m-%d")
folder = f"{today}-{project_title}"
os.makedirs(folder, exist_ok=True)

with open(f"{folder}/README.md", "w") as f:
    f.write(
        f"# {project_title.replace('-', ' ').title()}\n\n{description}"
    )

code_response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": f"Write starter Python code for this project: {description}"}
  ]
)
code = code_response.choices[0].message['content']

with open(f"{folder}/main.py", "w") as f:
    f.write(code)
