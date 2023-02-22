import curses
import time
import openai

# Set up OpenAI API credentials
openai.api_key = "OPEN_API"

def main(stdscr):
    # Clear the screen
    stdscr.clear()

    # Define the colors
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Prompt color
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Response color

    # Print the welcome message
    stdscr.addstr("Welcome to ChatGPT's Dumb Version! Press Ctrl+C to exit.\n\n", curses.color_pair(1))

    # Start a conversation with ChatGPT
    conversation_history = ""
    while True:
        # Get user input
        stdscr.addstr("You: ", curses.color_pair(1))
        curses.echo()
        user_input = stdscr.getstr().decode(encoding="utf-8")
        curses.noecho()

        # Stop the conversation if the user enters "exit"
        if user_input == "exit":
            break

        # Generate a response from ChatGPT
        response = openai.Completion.create(
            engine="davinci",
            prompt=conversation_history + user_input,
            temperature=0.7,
            max_tokens=50,
            stop=None,
        )

        # Get the generated text and add it to the conversation history
        generated_text = response.choices[0].text.strip()
        conversation_history += user_input + generated_text

        # Print the generated text
        stdscr.addstr("ChatGPT: ", curses.color_pair(1))
        stdscr.addstr(generated_text + "\n", curses.color_pair(2))
        stdscr.refresh()
        time.sleep(0.5)  # Wait for a short time to simulate ChatGPT "thinking"

# Initialize curses and run the main function
curses.wrapper(main)
