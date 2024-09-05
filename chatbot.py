import subprocess

# Example context about your company or service
context = """
We are a tech company offering a variety of services, including:
1. Web Development (Angular, React, Node.js)
2. Mobile App Development
3. Cloud Solutions
4. AI and Machine Learning
"""

def run_tinyllama(prompt):
    # Combine your context with the user's query
    full_prompt = f"{context}\n\nUser question: {prompt}\nAnswer:"
    try:
        result = subprocess.run(
            ["ollama", "run", "tinyllama", full_prompt],
            capture_output=True,
            text=True,
            encoding='utf-8',
            universal_newlines=True
        )
        return result.stdout
    except Exception as e:
        return f"An error occurred: {e}"

def chat():
    print("Custom TinyLlama Chatbot. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = run_tinyllama(user_input)
        print("Bot:", response.strip())

if __name__ == "__main__":
    chat()
