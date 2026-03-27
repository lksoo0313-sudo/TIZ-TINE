import os
from moviepy import ImageClip, AudioFileClip

def create_tiztine_shorts(image_path, audio_path, output_path):
    """
    TIZ-TINE 쇼츠 영상을 제작합니다.
    이미지와 오디오를 합성하여 지정된 경로에 MP4 파일을 생성합니다.
    """
    print(f"🎬 영상 제작 시작: {output_path}")
    
    # 기본 경로 확인
    if not os.path.exists(image_path):
        print(f"❌ 오류: 이미지를 찾을 수 없습니다: {image_path}")
        return
    if not os.path.exists(audio_path):
        print(f"❌ 오류: 오디오를 찾을 수 없습니다: {audio_path}")
        return

    # 오디오 클립 로드
    audio = AudioFileClip(audio_path)
    audio_duration = audio.duration
    print(f"🎵 오디오 길이: {audio_duration:.2f}초")

    # 이미지 클립 생성 (오디오 길이에 맞춤)
    clip = ImageClip(image_path).with_duration(audio_duration)
    
    # 오디오 설정
    clip = clip.with_audio(audio)
    
    # 화질 및 프레임 속도 설정 (Shorts 권장 30fps)
    print("⏳ 렌더링 중... 잠시만 기다려 주세요.")
    clip.write_videofile(
        output_path, 
        fps=30, 
        codec="libx264", 
        audio_codec="aac"
    )
    
    print(f"✅ 영상 제작 완료: {output_path}")

if __name__ == "__main__":
    # 경로 설정
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    IMAGE_FILE = os.path.join(BASE_DIR, "assets", "images", "characters", "v1.1_headset", "04_rain.png")
    AUDIO_FILE = os.path.join(BASE_DIR, "assets", "audio", "tiztine_rainy_lofi_20s_20260327_203307.wav")
    
    OUTPUT_DIR = os.path.join(BASE_DIR, "assets", "video")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    OUTPUT_FILE = os.path.join(OUTPUT_DIR, "tiztine_shorts_01_rainy.mp4")

    # 실행
    create_tiztine_shorts(IMAGE_FILE, AUDIO_FILE, OUTPUT_FILE)
