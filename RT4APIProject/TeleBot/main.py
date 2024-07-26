"""Main module for the bot"""
import time

from TeleUtils import receiver, sender


# Initialize the variable globally
n_new_mensaje = 0

def main():
    """Main function"""
    global n_new_mensaje

    print("Getting updates....")
    res = receiver.get_updates()

    # Check if result has enough entries
    results = res.get("result", [])
    print(f"Results: {results}" )
    message = results[-1].get("message", {})
    message_id = message.get("message_id")
    user_id = message.get("from", {}).get("id")
    user_text = message.get("text")

    if n_new_mensaje != message_id:
        n_new_mensaje = message_id
        sender.send_message(user_id, user_text)

if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)