# AI-CHATBOT-WITH-NLP

COMPANY : CODTECH IT SOLUTIONS

NAME : Nihar Patel

INTERN ID : CT06DF925

DOMAIN : PYTHON PROGRAMMING

DURATION : 6 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

Task Name: AI Chatbot with NLP The AI Chatbot with NLP (Natural Language Processing) is a Python-based conversational assistant designed to interact with users through simple text-based dialogue. Using core concepts of NLP, pattern recognition, and user intent classification, this chatbot can handle greetings, farewells, jokes, name queries, and basic general knowledge questions. The project demonstrates how artificial intelligence can simulate human-like conversation using lightweight tools and logic.

Technologies and Tools Used Python: The main programming language used due to its simplicity and strong support for NLP tasks.

NLTK (Natural Language Toolkit): A powerful Python library used for building NLP applications. In this chatbot, NLTK is used to define and manage dialogue pairs, and to tokenize or clean user input.

Regular Expressions (re): Used to match user queries against known intent patterns.

Random Module: Helps in selecting varied responses randomly from a set of appropriate replies to add human-like unpredictability.

Command Line Interface: The chatbot runs in a terminal or command prompt, where users interact by typing questions or prompts.

How It Works The chatbot uses a rule-based approach. Predefined patterns (such as “hello”, “what is your name”, or “tell me a joke”) are stored and matched against user input using regular expressions. When a match is found, the chatbot replies with a randomly chosen appropriate response from a predefined list.

Before processing, the input is cleaned using a preprocessing function that converts text to lowercase and removes punctuation. This ensures that inputs like “Hi!” and “hi” are treated the same.

The Chat class from NLTK is initialized using a list of (pattern, responses) pairs. Each user input is compared against these patterns using re.match, and if a pattern is detected, a corresponding response is selected and returned. If no match is found, a default fallback message like “I am sorry, I don’t understand” is shown.

The bot runs in a continuous loop until the user types "quit".

Applications Educational Projects: Ideal for students learning the basics of artificial intelligence and NLP.

Customer Support Prototypes: Can be adapted to answer frequently asked questions or guide users.

Interactive Kiosks or Chat Interfaces: Used in scenarios like museum guides, school portals, or mobile apps to answer basic queries.

Personal Assistants: Can be integrated into personal systems to simulate a conversational interface.

Mental Health Check-ins (basic): Can be configured with supportive messages and check-in questions.

Platform & Requirements Platform: Cross-platform – works on Windows, macOS, or Linux.

Environment: Command-line (Terminal or Command Prompt).

Libraries Required:

nltk

re

random

The script is lightweight and can run on low-resource machines without requiring internet access, as it does not rely on third-party APIs.

Conclusion The AI Chatbot with NLP is a simple yet effective demonstration of how human-computer interaction can be simulated using natural language techniques. It introduces core ideas like intent matching, pattern recognition, and response generation. Though basic in design, the chatbot provides a foundation for more complex systems involving machine learning, real-time APIs, or integration with web platforms. Its simplicity and modularity make it ideal for beginners and for academic purposes in AI and NLP courses.

Output
