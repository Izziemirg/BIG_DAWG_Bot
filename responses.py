from random import choice

# Personalized responses per user
user_responses = {
    "arcvade": [
        "Jose is the Spirit Airlines of COD",
        "Drop Jose!",
        "Watch out Jose is gonna touch you",
        "I do not speak Portuguese man",
        "If Jose keeps playing, imma unleash an AI chatbot",
        "I will only play with Jose senior",
        "Drop Jose, pick up LA",
        "I wish Jose could grapple with reality",
        "Ill pay someone $20 to report Jose to ICE",
        "GMU wants that M.S. back",
        "Little leprechaun",
        "Gonna take a scroll through Jose's old Facebook photos",
        "How are your Farsi lessons going?"
    ],
    "izzie": [
        "Not sure why yall don’t pick up Izzie"
    ],
    "cheggstudy": [
        "You still using Chegg in 2025?",
        "CheggStudy out here doing your homework again?"
    ],
    "easybake8992": [
        "Syracuse wants their M.S. back",
        "Cookin up another L?"
    ],
    "karim.zebdi": [
        "Karim, you dropping hot or hiding?",
        "Zebdi out here acting like he’s got a 5.0 K/D."
    ],
    "noonxo": [
        "You like Egyptians too much for me to trust you",
        "Very Indian of you",
        "FOR PAKISTANNNNN"
    ],
    "zsheisty2498": [
        "You ain't a thug",
        "Undershirt killa",
        "Raw dawgin life huh?",
        "You movin booky"
    ],
    "samie_mirghani": [
        "Samie out here thinking he’s the main character!",
        "Mirghani you ain't shit"
    ]
}

def get_response(user_input: str, username: str) -> str:
    lowered: str = user_input.lower()

    # Default random response
    default_responses = [
        'Do not raise your voice at BIG DAWG!',
        'What are you talking about?',
        'Not sure why yall dont pick up Izzie',
        'SMH',
        'Do your parents know you have a phone with internet access?',
        'How do we kick him from the chat?',
        'What is the country of Italy in the shape of?',
        'Stop playin with BIG DAWG',
        'Ruffff!',
        'Grrgghhhhhh'
    ]

    # Special responses for certain phrases
    special_responses = {
        'hi': "Well you're awfully silent mannnnn",
        'hello': "Hello little man!",
        'how are you': "Feelin Good, player!",
        'bye': "See ya little man",
        'this is annoying': "Jose thinks he is an actual gamer",
        'suck me': "Oh lord, this guy stinks"
    }

    # Check if user_input matches any key phrases
    for key, response in special_responses.items():
        if key in lowered:
            return response

    # Check if there are personalized responses for the user
    if username in user_responses:
        return choice(user_responses[username])

    # If no match, return a random default response
    return choice(default_responses)
