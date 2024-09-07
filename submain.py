from googleapiclient.discovery import build

# YouTube API configuration
API_KEY = 'Your_youtube_API_key_here'  # Replace with your actual YouTube API key
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Function to authenticate and initialize the YouTube API client
def authenticate_youtube():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    return youtube

# Function to get YouTube playlist recommendations based on mood/genre
def get_youtube_recommendation(youtube, mood_or_genre):
    request = youtube.search().list(
        q = mood_or_genre + ' playlist',
        part = 'snippet',
        type = 'playlist',
        maxResults = 5 # this gives you total 5 suggestions but you can iincrease or decrease this
    )
    response = request.execute()

    playlists = []
    for item in response['items']:
        playlist_title = item['snippet']['title']
        playlist_url = f"https://www.youtube.com/playlist?list={item['id']['playlistId']}"
        playlists.append({
            'name': playlist_title,
            'url': playlist_url
        })

    return playlists