from random import choice

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    # Default random response
    default_responses = [
        'Do not raise your voice at BIG DAWG!',
        'What are you talking about?',
        'Little leprechaun',
        'Drop Jose!',
        'Not sure why yall dont pick up Izzie',
        'SMH',
        'How are your Farsi lessons going?',
        'GMU wants that M.S. back',
        'I will only play with Jose senior',
        'Do your parents know you have a phone with internet access?',
        'How do we kick him from the chat?',
        'What is the country of Italy in the shape of?',
        'Watch out Jose is gonna touch you',
        'Drop Jose, pick up LA',
        'I do not speak Portuguese man',
        'Jose is the Spirit Airlines of COD',
        'If Jose keep playing, imma unleash an AI chatbot',
        'I wish Jose could grapple with reality',
        'Stop playin with BIG DAWG',
        'Ill pay someone $20 to report Jose to ICE',
        'Ruffff!'
    ]

    # Special responses for certain phrases
    special_responses = {
        'hi': 'Well you\'re awfully silent mannnnn',
        'hello': 'Hello little man!',
        'how are you': 'Feelin Good, player!',
        'bye': 'See ya little man',
        'this is annoying': 'Jose thinks he is an actual gamer',
        'suck me': 'Oh lord, this guys stinks'

    }

    # Check if user_input matches any key phrases
    for key, response in special_responses.items():
        if key in lowered:
            return response

    # If no match, return a random default response
    return choice(default_responses)
