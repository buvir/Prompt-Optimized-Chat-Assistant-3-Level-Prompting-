import os
from openai import OpenAI

# ----------------------------
# 1️⃣ Load API key safely
# ----------------------------
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Set OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

# ----------------------------
# 2️⃣ Choose prompt type
# ----------------------------
prompt_type = input("Choose prompt (zero_shot / few_shot / chain_of_thought): ").strip().lower()
prompt_file = f"prompts/{prompt_type}.txt"

# Check if prompt file exists
if not os.path.exists(prompt_file):
    print(f"❌ Prompt file not found: {prompt_file}")
    print("Available prompts: zero_shot, few_shot, chain_of_thought")
    exit(1)

# Read prompt
with open(prompt_file, "r", encoding="utf-8") as f:
    prompt_text = f.read()

# ----------------------------
# 3️⃣ Send prompt to ChatGPT API
# ----------------------------
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text}
        ],
        max_tokens=200
    )
    output = response.choices[0].message.content.strip()
    print("\n💡 LLM Output:\n", output)

except Exception as e:
    print(f"❌ Error calling OpenAI API: {e}")
