import os
from moviepy import ImageClip, AudioFileClip
from datetime import datetime

# 설정
BASE_DIR = r"d:\Projects\티즈틴(TIZ-TINE)"
AUDIO_PATH = os.path.join(BASE_DIR, "production_log", "2026-03-30", "Where_The_Tide_Meets_Sky.mp3")
IMAGE_PATH = os.path.join(BASE_DIR, "assets", "images", "characters", "v1.1_headset", "03_cafe.png")
OUTPUT_DIR = os.path.join(BASE_DIR, "production_log", "2026-03-30")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "tiztine_shorts_20260330_v3_cafe.mp4")

def produce_short():
    print(f"[*] 렌더링 시작: {AUDIO_PATH}")
    
    # 오디오 로드
    audio = AudioFileClip(AUDIO_PATH)
    duration = audio.duration
    
    # 이미지 클립 (MoviePy 2.0+ 문법)
    # 9:16 비율 (1080x1920)로 리사이징
    clip = ImageClip(IMAGE_PATH).with_duration(duration).resized(height=1920)
    
    # 최종 영상 설정
    video = clip.with_audio(audio)
    
    # 렌더링
    print(f"[*] 동영상 렌더링 중... (총 {duration:.2f}초)")
    video.write_videofile(
        OUTPUT_FILE, 
        fps=24, 
        codec="libx264", 
        audio_codec="aac"
    )
    print(f"[+] 제작 완료: {OUTPUT_FILE}")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    produce_short()
