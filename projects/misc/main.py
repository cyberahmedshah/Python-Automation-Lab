# def feb_no(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return feb_no(n-1)+feb_no(n-2)

# n=int(input("Enter the number: "))
# print(feb_no(n))


# s={5,10,15}
# e={10, 20, 30}
# # print(s.union(e))
# # print(e.union(s))
# # print(s.intersection(e))
# # print(type(s))

# print(s.issuperset(e))
# print(s.isdisjoint(e))

# d={
#     111: "Ahmed",
#     112: "Hamza",
#     113: "Ali",
#     114: "Hassan"
# }


# d.pop(114)
# print(d)


#print(d[int(input("Enter the id: "))])

# print(d.keys())
# print(d.values())


# for key in d.keys():
#     print(d[key])


# dic={
#     int(input("Enter the id: ")): input("Enter the name: "),

# }


# for i in range(11):
  
#  if i==5:
#         continue
#  print(i)   
# else:
#     print("Loop tested")


# x=int(input("Enter the number: "))
# if x%2==0:
#     print("Even")
# else:
#     print("Odd")


# for i in range(1,11):
#     if i%2==0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")



# for i in range(11):
#     if i==7:
#      continue
#     print(i)
# else:
#     print("working")



# for i in range(1, 6):
#     print(f"iteration no {i} in for loop")
# else:
#     print("end of loop")
# print("out of loop")


# try:
#  a=int(input("Enter the number: "))
#  for i in range(1, 11):
#   print(f"{a} x {i} = {(a)*i}")
# except:
#   print("Invalid input")

# # print("program working")



# a=int(input("Enter the number: "))
# for i in range(1,11):
#     if type(a) is int:
#         print(f"{a} x {i} = {a*i}")
#     elif type(a) is str:
#         print ("invalid input")



# def test(a, n):
#     try:
#      return a*n
#     finally:
#         print("Done")



# a= int(input("Number one: "))
# b= int(input("Number two: "))
# print(test(a, b))



# a=input("Enter the number(1-9): " ).lower()

# if a=="quit":
#     print("Program Exited")
#     exit()
# b=int(a)
# if b<1 or b>9:
#     raise ValueError
# if b>=1 and b<=9:
#     print("Program Working")



# a=[{"Questions":"Who created linux?", "OPtions":"a.me" "b.he" "c.they d.us", "answers":"a"}]
# answer=str(input("Enter the option: ")).strip().lower()
# if answer== a[{"answers"[1]}]:
#     print("correct")
# else:
#     print("wrong")



# id=[2, 43, 14, 99, 81]
# for v, i in enumerate(id):
#     print(f"{v}."

"""
Basic AI Chatbot Backend — Python
Uses the Anthropic Claude API to power a simple conversational chatbot.

Install dependency first:
    pip install anthropic

Set your API key:
    export ANTHROPIC_API_KEY="your-api-key-here"
    (Get a free key at: https://console.anthropic.com)
"""

import os
from anthropic import Anthropic

# ── 1. Setup ──────────────────────────────────────────────────────────────────

# The Anthropic client automatically reads ANTHROPIC_API_KEY from the environment
client = Anthropic()

# Conversation history — this is how the AI "remembers" the chat.
# Each message is a dict: {"role": "user" or "assistant", "content": "..."}
conversation_history = []

# System prompt — gives the AI its personality and rules
SYSTEM_PROMPT = """
You are a helpful, friendly, and concise assistant.
Answer the user's questions clearly and honestly.
If you don't know something, say so.
"""

# ── 2. Core function ──────────────────────────────────────────────────────────

def chat(user_message: str) -> str:
    """
    Send a user message to Claude and get a reply.

    How it works:
    1. Append the user's message to the conversation history
    2. Send the full history to the Claude API
    3. Get Claude's reply, append it to history, and return it

    The history is what gives the bot "memory" — without it, every
    message would be treated as a brand new conversation.
    """

    # Step 1 — Add the user's message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Step 2 — Call the Claude API with the full conversation so far
    response = client.messages.create(
        model="claude-sonnet-4-20250514",   # The Claude model to use
        max_tokens=1024,                     # Max length of the reply
        system=SYSTEM_PROMPT,                # Bot personality / instructions
        messages=conversation_history        # Full chat history for context
    )

    # Step 3 — Extract the reply text from the response
    assistant_reply = response.content[0].text

    # Step 4 — Save the bot's reply to history so future turns remember it
    conversation_history.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return assistant_reply


# ── 3. Helper: clear memory ───────────────────────────────────────────────────

def reset_conversation():
    """Wipe the conversation history to start fresh."""
    conversation_history.clear()
    print("🔄 Conversation reset.\n")


# ── 4. Main loop (run this file directly to chat in the terminal) ─────────────

def main():
    print("=" * 50)
    print("  Simple AI Chatbot  (type 'quit' to exit)")
    print("  Type 'reset' to start a new conversation")
    print("=" * 50)
    print()

    while True:
        # Get input from the user
        user_input = input("You: ").strip()

        # Skip empty input
        if not user_input:
            continue

        # Exit command
        if user_input.lower() in ("quit", "exit", "bye"):
            print("Bot: Goodbye! 👋")
            break

        # Reset command
        if user_input.lower() == "reset":
            reset_conversation()
            continue

        # Send the message and print the reply
        try:
            reply = chat(user_input)
            print(f"\nBot: {reply}\n")

        except Exception as e:
            print(f"\n⚠️  Error: {e}\n")


if __name__ == "__main__":
    main()