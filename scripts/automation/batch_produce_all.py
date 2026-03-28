import os
import sys
import argparse
from datetime import datetime

# sys path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from music_generator import TizTineMusicGenerator
from video_maker_v2 import create_tiztine_shorts_v2

# API Key
API_KEY = os.environ.get("GOOGLE_GENAI_API_KEY")
if not API_KEY:
    try:
        with open(".env", "r") as f:
            for line in f:
                if line.startswith("GOOGLE_GENAI_API_KEY="):
                    API_KEY = line.split("=")[1].strip()
                    break
    except:
        pass

# 5대 테마 정의 (우천 제외 4종)
THEMES = [
    {
        "id": "01_street",
        "name": "Street",
        "image": "assets/images/characters/v1.1_headset/01_street.png",
        "prompt": "Hip-hop lo-fi beat for a trendy street scene. Heavy bass, scratch sounds, 95 BPM, cool and active vibe. Instrumental only.",
        "caption": "[TIZ-TINE] Street Mood: Let's walk the city beats. 🎧"
    },
    {
        "id": "02_home",
        "name": "Home",
        "image": "assets/images/characters/v1.1_headset/02_home.png",
        "prompt": "Warm and cozy acoustic lo-fi beat. Soft guitar, vinyl crackle, 80 BPM, relaxing home atmosphere. Instrumental only.",
        "caption": "[TIZ-TINE] Home Sweet Home: Cozy vibes only. ✨"
    },
    {
        "id": "03_cafe",
        "name": "Cafe",
        "image": "assets/images/characters/v1.1_headset/03_cafe.png",
        "prompt": "Jazz lo-fi hip-hop for a calm cafe scene. Smooth saxophone, coffee shop ambient noise, 85 BPM, sophisticated vibe. Instrumental only.",
        "caption": "[TIZ-TINE] Cafe Digging: Music and Coffee. ☕"
    },
    {
        "id": "05_library",
        "name": "Library",
        "image": "assets/images/characters/v1.1_headset/05_library.png",
        "prompt": "Study lo-fi beat for a focus session. Minimalist piano, repetitive calming loop, 75 BPM, deep focus library vibe. Instrumental only.",
        "caption": "[TIZ-TINE] Library Focus: Deep dive into the sound. 📚"
    }
]

def produce_theme(theme):
    print(f"\n--- 🚀 Producing Theme: {theme['name']} ---")
    
    # 1. Generate Music
    generator = TizTineMusicGenerator(api_key=API_KEY)
    audio_filename = f"tiztine_bgm_{theme['id']}.mp3"
    audio_path = os.path.join("assets", "audio", audio_filename)
    
    if not os.path.exists(audio_path):
        print(f"[*] Generating music for {theme['name']}...")
        result_audio = generator.generate_from_image(theme['image'], theme['prompt'], audio_filename)
        if not result_audio:
            print(f"[!] FAILED: Music generation failed for {theme['name']}.")
            return
        audio_path = result_audio
    else:
        print(f"[*] Audio already exists at {audio_path}")

    # 2. Create Video
    # For simplicity, we use the single theme image for the entire 20s
    output_video_path = os.path.join("assets", "video", f"tiztine_shorts_{theme['id']}.mp4")
    print(f"[*] Creating video for {theme['name']}...")
    create_tiztine_shorts_v2([theme['image']], [20], audio_path, output_video_path)
    
    # 3. Organize for Upload
    DATE_STR = "2026-03-28"
    prod_dir = rf"d:\Projects\티즈틴(TIZ-TINE)\assets\production\youtube\{DATE_STR}"
    os.makedirs(prod_dir, exist_ok=True)
    
    import shutil
    shutil.copy(output_video_path, os.path.join(prod_dir, f"{theme['id']}_shorts.mp4"))
    
    # Create individual POST_META
    meta_path = os.path.join(prod_dir, f"POST_META_{theme['id']}.md")
    with open(meta_path, "w", encoding="utf-8") as f:
        f.write(f"# 📂 유튜브 업로드 메타데이터 ({theme['name']})\n\n")
        f.write(f"## 1. 제목 (Title)\n[TIZ-TINE] {theme['caption']} #Shorts #로파이 #티즈틴\n\n")
        f.write(f"## 2. 상세 설명 (Description)\n{theme['caption']}\n\n구독과 좋아요는 티즈틴에게 큰 힘이 됩니다! 🐶✨\n\n#TIZTINE #LoFi #Maltese #Animation #Shorts\n\n---\n\n## 3. 태그 (Tags)\n티즈틴, TIZ-TINE, 로파이, LoFi, {theme['name']}, 캐릭터, 애니메이션\n")

    print(f"[+] DONE: Theme {theme['name']} produced and ready for upload at {prod_dir}")

if __name__ == "__main__":
    if not API_KEY:
        print("[!] GOOGLE_GENAI_API_KEY is missing.")
        sys.exit(1)
        
    for theme in THEMES:
        produce_theme(theme)
