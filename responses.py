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
        "How are your Farsi lessons going?",
        "BIGGG hot tub guy, huh?"
    ],
    "izzie": [
        "Not sure why yall don’t pick up Izzie"
    ],
    "cheggstudy": [
        "You still using Chegg in 2025?",
        "Ruben Amorim your lord and savior, huh?",
        "Your lego collection is mid at best",
        "The Harry Maguire of gaming"
    ],
    "easybake8992": [
        "Syracuse wants their M.S. back",
        "Cookin up another L?",
        "The Eazybake oven only cookin baby food!",
        "Sneaky athletic",
        "Can we kick him out the chat?",
        "Syd, please take his electronics away",
        "Ipad kid vibes",
        "Jose is your indentured servant",
        "Don't make me drive to Delaware rn",
        "Does Syd make you dress up like pulp fiction?",
        "I heard you peed in a closet",
        "I'm more of an Milwaukee guy than a Dewalt guy....",
        "Best data scientist I have ever met tbh",
        "Who did you steal your snowboard from?",
        "I wish Evan could grapple with reality"
        "White, no tats"
    ],
    "karim.zebdi": [
        "Its MR. ZEBDI to you",
        "Karim why don't you share the old vaccums man?",
        "Khalil is my favorite Zebdi",
        "Venmo request me $0.67 man",
        "Everytime he says something important, his nose grows!",
        "HES HUGE!",
        "Best bladder to have on a roadtrip",
        "VERY Algerian of you man",
        "That is pretty Algerian man",
        "Someone give him the boot",
        "El fado?",
        "Used car salesman vibes",
        "All I know is NASA is cooked if you work for them",
        "The Nicholas Pepe of gaming",
        "Sand monkey vibes"
    ],
    "noonxo": [
        "You like Egyptians too much for me to trust you",
        "Very Indian of you man",
        "FOR PAKISTANNNNN"
    ],
    "zsheisty2498": [
        "You ain't a thug",
        "Undershirt killa",
        "Raw dawgin life huh?",
        "You movin booky",
        "Most productive worker the US government has",
        "Golf ball bully",
        "Athletic af for no reason"
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
