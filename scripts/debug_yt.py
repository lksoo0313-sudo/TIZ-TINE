import os
import os.path
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/youtube'] 
TOKEN_FILE = r'd:\Projects\.agent\agent-luna\.agent\token_full.json'

def debug_channel_info():
    if not os.path.exists(TOKEN_FILE):
        print("Token file missing.")
        return
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

    try:
        print("[*] 채널 정보를 조회 중입니다...")
        channels_response = youtube.channels().list(
            part="snippet,brandingSettings",
            mine=True
        ).execute()

        if not channels_response['items']:
            print("No channel found.")
            return

        channel = channels_response['items'][0]
        print(f"Channel ID: {channel['id']}")
        print(f"Current Snippet: {json.dumps(channel.get('snippet', {}), indent=2, ensure_ascii=False)}")
        print(f"Current BrandingSettings: {json.dumps(channel.get('brandingSettings', {}), indent=2, ensure_ascii=False)}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_channel_info()
