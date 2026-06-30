# Project Name: SaikatMate Bot
# A simple rule-based chatbot using a dictionary knowledge base

# Ask for user's name
user_name = input("Welcome to SaikatMate Bot!\nPlease enter your name: ").strip()

bot_name = "SaikatMate"

print(f"\n{bot_name}: Hello {user_name}! Nice to meet you.")
print(f"{bot_name}: Type 'help' to see what I can talk about.\n")

# Knowledge base with intents
knowledge_base = {
    "hello": f"Hello {user_name}! Hope you're having a great day.",
    "hi": f"Hi {user_name}! Nice to see you.",
    "how are you": f"I'm doing great, {user_name}! Thanks for asking.",
    "who are you": f"I am {bot_name}, your simple rule-based chatbot.",
    "my name": f"Your name is {user_name}. Nice name!",
    "thank you": f"You're welcome, {user_name}!",
    "thanks": f"Glad I could help, {user_name}.",
    "help": "I can talk about: hello, hi, how are you, who are you, my name, thank you, thanks, motivation, joke, study, coding, favorite language, goal, good job, and help.",
    "motivation": f"Keep learning, {user_name}. Small progress every day leads to big success.",
    "joke": "A programmer went to the kitchen and noticed the coffee machine was broken. They immediately started debugging the water filter, completely forgetting they just needed to plug it in.",
    "study": f"Study a little every day, {user_name}. Consistency beats intensity.",
    "coding": f"Practice regularly, {user_name}. The best way to learn coding is by building projects.",
    "favorite language": "My favorite language is Python because it is simple and powerful.",
    "goal": f"Set a clear goal, {user_name}, and work on it one step at a time.",
    "good job": f"Thank you, {user_name}! I appreciate your kind words."
}

# Exit commands
exit_commands = ["exit", "stop", "bye", "quit"]

# Continuous chatbot loop
while True:

    # Take user input and sanitize it
    user_input = input(f"\n{user_name}: ").strip().lower()

    # Check for exit commands
    if user_input in exit_commands:
        print(
            f"{bot_name}: Goodbye {user_name}! "
            "Thanks for chatting with me. "
            "Keep learning and have a wonderful day!"
        )
        break

    # Get response from dictionary using .get()
    response = knowledge_base.get(
        user_input,
        f"That's an interesting topic, {user_name}! "
        "I don't know much about it yet. "
        "Type 'help' to see the topics I can discuss."
    )

    print(f"{bot_name}: {response}")