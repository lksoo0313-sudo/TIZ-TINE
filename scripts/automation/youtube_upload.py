import os
import os.path
import json
import re
import argparse
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

# 🔧 필수 설정
SCOPES = ['https://www.googleapis.com/auth/youtube'] 
TOKEN_FILE = r'd:\Projects\.agent\agent-luna\.agent\token_full.json'

def parse_metadata(meta_path):
    with open(meta_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 더 유연한 정규식으로 수정
    title_match = re.search(r'## 1\. 제목 \(Title\)\s*\n(.*?)\n', content)
    desc_match = re.search(r'## 2\. 상세 설명 \(Description\)\s*\n(.*?)\n\n---', content, re.DOTALL)
    tags_match = re.search(r'## 3\. 태그 \(Tags\)\s*\n(.*?)\n', content)
    
    title = title_match.group(1).strip() if title_match else "TIZ-TINE: Official LOFI & Music"
    description = desc_match.group(1).strip() if desc_match else "Welcome to TIZ-TINE Official Channel!"
    tags = [tag.strip() for tag in tags_match.group(1).split(',')] if tags_match else ["TIZ-TINE", "Lo-fi"]
    
    return title, description, tags

def upload_video(video_path, meta_path):
    if not os.path.exists(TOKEN_FILE):
        print("[!] 토큰 파일이 없습니다.")
        return

    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

    title, description, tags = parse_metadata(meta_path)
    
    print(f"[*] 업로드 시작: {title}")
    
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': '10' 
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False
        }
    }

    insert_request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=MediaFileUpload(video_path, chunksize=-1, resumable=True)
    )

    print(f"[*] 데이터 전송 중: {video_path}")
    response = None
    while response is None:
        status, response = insert_request.next_chunk()
        if status:
            print(f"[*] 전송 진행률: {int(status.progress() * 100)}%")

    print(f"[+] 업로드 완료! ID: {response['id']}")
    print(f"URL: https://youtu.be/{response['id']}")
    return response['id']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Automated Upload")
    parser.add_argument("--date", help="Upload date folder", default="2026-03-28")
    parser.add_argument("--video", help="Video filename", default="tiztine_shorts_01_rainy.mp4")
    parser.add_argument("--meta", help="Metadata filename", default="POST_META.md")
    args = parser.parse_args()

    BASE_DIR = rf"d:\Projects\티즈틴(TIZ-TINE)\assets\production\youtube\{args.date}"
    VIDEO_FILE = os.path.join(BASE_DIR, args.video)
    META_FILE = os.path.join(BASE_DIR, args.meta)

    if os.path.exists(VIDEO_FILE) and os.path.exists(META_FILE):
        upload_video(VIDEO_FILE, META_FILE)
    else:
        print(f"[!] 업로드할 파일을 찾을 수 없습니다: {VIDEO_FILE}")
