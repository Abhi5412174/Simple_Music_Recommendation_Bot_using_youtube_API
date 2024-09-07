# Music Recommendation Bot
# Concept: A bot that recommends songs or playlists based on the user’s mood or preferences.
from submain import authenticate_youtube, get_youtube_recommendation

# Main chatbot
def music_recommendation_bot():
    print("\nWelcome to the YouTube Music Recommendation Bot!")
    print("I can suggest YouTube playlists based on your mood or favorite genre.")
    
    youtube = authenticate_youtube()
    while True:
        user_input = input("Tell me your mood or favorite genre (type 'quit' to exit): ").lower()
        if user_input == 'quit':
            print("Goodbye! Enjoy your music!")
            break
        
        recommendations = get_youtube_recommendation(youtube, user_input)
        # Display recommendations
        if recommendations:
            print(f"\nHere are some YouTube playlists you might enjoy for '{user_input}':\n")
            index = 1
            for playlist in recommendations:
                print(f"{index}. {playlist['name']} - {playlist['url']}")
                index += 1 
            print(f"{index}. {playlist['name']} - {playlist['url']}")
        else:
            print(f"Sorry, I couldn't find any playlists for '{user_input}'. Try another mood or genre!")

if __name__ == "__main__":
    music_recommendation_bot()
