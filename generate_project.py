import openai
import os
import datetime

# Set up OpenAI client (new SDK)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 1: Generate project idea
idea_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an AI that creates small, interesting beginner-level Python projects."},
        {"role": "user", "content": "Give me a unique and creative Python project idea with a one-line description."}
    ]
)

idea_response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Use gpt-3.5 instead of gpt-4
    messages=[
        {"role": "system", "content": "You are an AI that creates small, interesting beginner-level Python projects."},
        {"role": "user", "content": "Give me a unique and creative Python project idea with a one-line description."}
    ]
)

# Step 2: Create folder
today = datetime.datetime.now().strftime("%Y-%m-%d")
folder = f"{today}-{project_title}"
os.makedirs(folder, exist_ok=True)

# Step 3: Create README.md
with open(f"{folder}/README.md", "w") as f:
    f.write(f"# {project_title.replace('-', ' ').title()}\n\n{description}")

# Step 4: Generate starter code
code_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Write starter Python code for this project: {description}"}
    ]
)

code = code_response.choices[0].message.content.strip()

with open(f"{folder}/main.py", "w") as f:
    f.write(code)
