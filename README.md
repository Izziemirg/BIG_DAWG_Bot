BIG DAWG Bot 🤖🐶

A Discord bot that responds to messages in a fun and interactive way, targeting specific users when mentioned.

Features:

✅ Responds to specific users when mentioned after "get em"

✅ Selects responses based on the mentioned user’s username

✅ Supports private messages with ? prefix

✅ Tracks a targeted user and responds accordingly

✅ Built with Python and Discord.py

Installation & Setup:

1. Clone the Repository

git clone https://github.com/yourusername/big-dawg-bot.git
cd big-dawg-bot

2. Install Dependencies

Ensure you have Python installed, then install the required packages:
pip install -r requirements.txt

3. Set Up Environment Variables

Create a .env file and add your bot token:
DISCORD_TOKEN=your_bot_token_here

4. Run the Bot

python main.py


Configuration:

The bot listens for "get em" to set a target user. The Target will be whatever username you @ in the message.
It responds only to messages from the target user. It will ignore other user responses until you specify another user to respond to.
Responses are selected randomly from responses.py. You should edit these responses to personalize them.
To send private messages, prefix the message with ?.

Customization:

To add or modify responses, edit responses.py:

user_responses = {
    "username1": ["Response 1", "Response 2"],
    "username2": ["Funny response here"]
}

Troubleshooting:

Bot not responding?

Ensure the bot is online in Discord.
Check that the DISCORD_TOKEN is correctly set.
Verify that Intents.message_content = True is enabled.
ModuleNotFoundError (e.g., dotenv, discord)?

Run: pip install -r requirements.txt


Contributing

Feel free to submit pull requests or report issues! 🎉


