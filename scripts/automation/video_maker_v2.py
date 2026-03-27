import os
import sys
from datetime import datetime
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

def create_tiztine_shorts_v2(scene_images, scene_durations, audio_path, output_path):
    """
    여러 장면의 이미지와 오디오를 합성하여 시나리오 기반의 쇼츠 영상을 제작합니다.
    :param scene_images: 장면별 이미지 경로 리스트
    :param scene_durations: 장면별 지속 시간 리스트 (초)
    :param audio_path: 배경 오디오 경로
    :param output_path: 출력 파일 경로
    """
    print(f"🎬 [v2.0] 고품질 영상 제작 시작: {output_path}")
    
    # 1. 오디오 로드
    if not os.path.exists(audio_path):
        print(f"❌ 오류: 오디오를 찾을 수 없습니다: {audio_path}")
        return
    audio = AudioFileClip(audio_path)
    total_duration = audio.duration
    
    # 2. 각 장면 클립 생성 및 연결
    clips = []
    for i, (img_path, duration) in enumerate(zip(scene_images, scene_durations)):
        if not os.path.exists(img_path):
            print(f"⚠️ 경고: 이미지를 찾을 수 없어 건너뜁니다: {img_path}")
            continue
        
        # 마지막 장면의 경우 오디오 길이에 딱 맞게 조정
        if i == len(scene_images) - 1:
            current_total = sum(scene_durations[:-1])
            duration = max(0.1, total_duration - current_total)
            print(f"🕒 마지막 장면 길이 조정: {duration:.2f}초 (총 {total_duration:.2f}초에 맞춤)")

        # 9:16 (1080x1920) 리사이징 및 지속 시간 설정 (v2.x 문법)
        clip = ImageClip(img_path).with_duration(duration).resized(height=1920)
        clips.append(clip)
    
    if not clips:
        print("❌ 오류: 유효한 이미지 클립이 없습니다.")
        return
        
    final_video = concatenate_videoclips(clips, method="compose")
    
    # 오디오 설정
    final_video = final_video.with_audio(audio)
    
    # 3. 렌더링
    print("⏳ 최종 렌더링 중... (fps=30, codec=libx264)")
    final_video.write_videofile(
        output_path, 
        fps=30, 
        codec="libx264", 
        audio_codec="aac"
    )
    
    print(f"✅ 영상 제작 완료: {output_path}")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # 시나리오에 따른 설정 (SCENARIO_01_RAINY.md 기준)
    scenes = [
        os.path.join(BASE_DIR, "assets", "images", "production", "rainy_01.png"), # 00-05s
        os.path.join(BASE_DIR, "assets", "images", "production", "rainy_02.png"), # 05-12s
        os.path.join(BASE_DIR, "assets", "images", "production", "rainy_03.png"), # 12-18s
        os.path.join(BASE_DIR, "assets", "images", "production", "rainy_04.png")  # 18-20s
    ]
    durations = [5, 7, 6, 2] # 총 20초
    
    # 최근 생성된 오디오 파일 경로 (필요시 업데이트)
    AUDIO_FILE = os.path.join(BASE_DIR, "assets", "audio", "tiztine_rainy_lofi_20s_20260327_211416.wav")
    
    OUTPUT_FILE = os.path.join(BASE_DIR, "assets", "video", "tiztine_shorts_v2_rainy.mp4")
    
    create_tiztine_shorts_v2(scenes, durations, AUDIO_FILE, OUTPUT_FILE)
