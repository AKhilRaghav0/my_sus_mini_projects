import openai
import argparse

# Set up OpenAI API credentials
openai.api_key = "OPEN_AI"

# Define CLI arguments
parser = argparse.ArgumentParser(description='Chat with ChatGPT')
parser.add_argument('--prompt', '-p', required=True, help='The starting prompt for the conversation')
parser.add_argument('--temperature', '-t', type=float, default=0.7, help='The temperature to use for the generation')
parser.add_argument('--max_tokens', '-m', type=int, default=50, help='The maximum number of tokens to generate')
parser.add_argument('--stop_sequence', '-s', type=str, default=None, help='The stop sequence to use for generation')
parser.add_argument('--model', '-n', type=str, default='davinci', help='The OpenAI GPT model to use for generation')

# Parse the arguments
args = parser.parse_args()

# Start a conversation with ChatGPT
print("Starting conversation with ChatGPT...")
conversation_history = ""
while True:
    # Get user input
    user_input = input("You: ")
    
    # Stop the conversation if the user enters "exit"
    if user_input == "exit":
        break
    
    # Generate a response from ChatGPT
    response = openai.Completion.create(
        engine=args.model,
        prompt=args.prompt + conversation_history + user_input,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        stop=args.stop_sequence,
    )
    
    # Get the generated text and add it to the conversation history
    generated_text = response.choices[0].text.strip()
    conversation_history += user_input + generated_text
    
    # Print the generated text
    print("ChatGPT:", generated_text)

