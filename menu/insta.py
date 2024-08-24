from instabot import Bot

def post_to_instagram(username, password, photo_path, caption):
    try:
        # Initialize the bot
        bot = Bot()

        # Login to Instagram
        bot.login(username=username, password=password)

        # Post the picture
        bot.upload_photo(photo_path, caption=caption)

        # Logout from Instagram
        bot.logout()

        print("Post uploaded successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Login credentials
USERNAME = 'pytho_n12357'
PASSWORD = 'test_user12@'

# Path to the picture you want to post
photo_path = '/root/python/photo.jpg'

# Caption for the post
caption = 'Hello '

# Call the function to post to Instagram
post_to_instagram(USERNAME, PASSWORD, photo_path, caption)
