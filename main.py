from typing import Final, Optional
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)

target_user: Optional[str] = None  # Stores the current target username
target_display_name: Optional[str] = None  # Stores the current target display name


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str, target_user: str) -> None:
    if not user_message:
        print('(Big Dawg is asleep)')
        return

    is_private = user_message.startswith("?")
    if is_private:
        user_message = user_message[1:]

    try:
        # Respond based on the target user
        response: str = get_response(user_message, target_user)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    global target_user, target_display_name

    if message.author == client.user:
        return

    username: str = str(message.author)  # Unique Discord username (e.g., "User#1234")
    display_name: str = message.author.display_name  # Server nickname (display name)
    user_message: str = message.content.strip()
    channel: str = str(message.channel)

    # If bot is mentioned and "get em" is in the message, set the target user and their display name
    if client.user.mentioned_in(message) and " get em " in user_message.lower():
        mentioned_user = message.mentions[1] if message.mentions else None  # Get the first mentioned user

        if mentioned_user:
            target_user = str(mentioned_user)  # Set target_user to the mentioned user's username
            target_display_name = mentioned_user.display_name  # Set target_display_name to mentioned user's display name
            await message.channel.send(f"I'm on yo ass {target_display_name}")
        return

    # Kill switch: If bot is mentioned and "stand down" is in the message, deactivate targeting
    if client.user.mentioned_in(message) and " chill out" in user_message.lower():
        if target_user:
            await message.channel.send(f"Alright, I’ll leave {target_display_name} alone.")
            target_user = None
            target_display_name = None
        else:
            await message.channel.send("I'm not targeting anyone right now.")
        return

    print(f'[{message.channel}] {target_user} ({target_display_name}): "{message.content}"')

    # Only respond to the target user (checking both username and display name)
    if username == target_user or display_name == target_display_name:
        await send_message(message, user_message, target_user)  # Pass the correct target_user


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(TOKEN)


if __name__ == '__main__':
    main()
