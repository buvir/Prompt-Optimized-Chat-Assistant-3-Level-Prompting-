import requests
import json

# ----------------------------
# Configuration - OLLAMA (Local)
# ----------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"  # Change to your installed model

# ----------------------------
# Function to load prompts
# ----------------------------
def load_prompt(prompt_type):
    """Loads the content of a prompt file."""
    prompt_file = f"prompts/{prompt_type}.txt"
    try:
        with open(prompt_file, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: Prompt file '{prompt_file}' not found.")
        return None

# ----------------------------
# Function to get LLM response from Ollama
# ----------------------------
def get_llm_response(prompt_content):
    """Sends the prompt to local Ollama API and returns the response."""
    payload = {
        "model": MODEL,
        "prompt": prompt_content,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "top_p": 0.9
        }
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['response'].strip()
    except requests.exceptions.ConnectionError:
        return "❌ Error: Cannot connect to Ollama. Make sure it's running!\nRun: 'ollama serve' in your terminal."
    except Exception as e:
        return f"❌ Error calling Ollama API: {str(e)}"

# ----------------------------
# Main Demo Loop
# ----------------------------
def main():
    print("\n" + "="=50)
    print("🤖 Prompt-Optimized Chat Assistant (Local Ollama)")
    print("="=50)
    print("Using LOCAL LLM - 100% FREE and private!")
    print(f"Model: {MODEL}")

    while True:
        print("\nAvailable Prompting Techniques:")
        print("1. Zero-Shot Prompting")
        print("2. Few-Shot Prompting")
        print("3. Chain-of-Thought (CoT) Prompting")
        print("4. Exit")

        choice = input("\nSelect a technique (1-4): ").strip()

        prompt_map = {
            "1": "zero_shot",
            "2": "few_shot",
            "3": "chain_of_thought"
        }

        if choice == "4":
            print("👋 Thanks for using the assistant! Goodbye.")
            break
        elif choice in prompt_map:
            prompt_type = prompt_map[choice]
            print(f"\n--- Loading {prompt_type.replace('_', ' ').title()} ---")

            prompt_content = load_prompt(prompt_type)
            if prompt_content is None:
                continue

            if input("Show the prompt being sent? (y/n): ").lower() == 'y':
                print(f"\n📄 Prompt:\n{prompt_content}\n{'-'*40}")

            print("\n🤔 Thinking...")
            response = get_llm_response(prompt_content)

            print(f"\n✅ Assistant's Response:\n{response}")

        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()