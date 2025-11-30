# 🤖 Prompt-Optimized Chat Assistant

A hands-on demonstration of advanced prompt engineering techniques with Large Language Models (LLMs). This project showcases how strategically designed prompts can dramatically improve the quality, reliability, and reasoning capabilities of AI responses.

## 🎯

"I built a prompt engineering demo that compares three prompting techniques - zero-shot, few-shot, and chain-of-thought - showing how strategic prompt design significantly improves LLM output quality and reasoning capabilities."

## 📝 What It Does - Simple Explanation

### Zero-Shot Prompting
**Input**: Just the question without examples
**Output**: Model tries to answer based on its general knowledge


**Built a prompt engineering demo to showcase:**
- **Zero-shot prompting** – Model answers without examples using only instructions
- **Few-shot prompting** – Model learns from in-context examples before answering  
- **Chain-of-thought (CoT) prompting** – Model explains reasoning step-by-step for complex problems

Input:
"Text: 'Weather is okay' → Neutral
Text: 'This is amazing!' → Positive
Text: 'I hate traffic' → Negative
Text: 'Package arrived early' 

**Demonstrated Skills:**
- ✅ **Prompt Design & Engineering** – Crafting effective instructions for LLMs
- ✅ **Context Injection** – Providing relevant examples and constraints
- ✅ **Reasoning Control** – Guiding model thought processes for accurate results
- ✅ **LLM Integration** – Working with local and cloud-based language models
- ✅ **Output Quality Optimization** – Using prompt techniques to improve response quality

## 🚀 Overview

Different prompting strategies yield dramatically different results from LLMs. This project implements and compares three fundamental techniques:

- **Zero-Shot Prompting**: Direct instructions without examples
- **Few-Shot Prompting**: Learning from demonstration examples  
- **Chain-of-Thought Prompting**: Step-by-step reasoning guidance

## 🛠️ Technical Implementation

### Architecture
```

prompt-engineering-demo/
│
├── prompts/ # Prompt templates demonstrating each technique
│ ├── zero_shot.txt # Direct instruction-based prompts
│ ├── few_shot.txt # Example-driven prompts
│ └── chain_of_thought.txt # Step-by-step reasoning prompts
│
├── app.py # Main application with interactive demo
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

Local LLM with Ollama

```
# 1. Install Ollama from https://ollama.ai/

# 2. Pull a model (in separate terminal)
ollama pull llama3.2:1b

# 3. Start Ollama service (keep this running)
ollama serve

# 4. Set up Python environment
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install requests

# 5. Run the application
python app.py
```