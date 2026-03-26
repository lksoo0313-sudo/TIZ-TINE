import os
from moviepy import ImageClip, AudioFileClip
from datetime import datetime

class TizTineShortsGenerator:
    """
    TIZ-TINE 전용 쇼츠 영상 생성기
    - 이미지와 오디오를 합쳐 고화질 세로형 쇼츠(9:16) 영상을 생성합니다.
    """
    def __init__(self, output_dir="outputs/shorts"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_short(self, image_path, audio_path, duration=15, output_name=None):
        """
        쇼츠 영상 생성 메인 함수
        :param image_path: 배경 이미지 경로
        :param audio_path: 배경 음악 경로
        :param duration: 영상 길이 (초)
        :param output_name: 출력 파일명 (None이면 자동 생성)
        """
        print(f"[*] 영상 생성 시작: {image_path} + {audio_path}")
        
        # 1. 오디오 클립 불러오기
        audio = AudioFileClip(audio_path)
        if audio.duration < duration:
            duration = audio.duration  # 이미지 길이를 오디오 길이에 맞춤
            
        # 2. 이미지 클립 생성 (쇼츠 규격 1080x1920 고려)
        clip = ImageClip(image_path).with_duration(duration)
        
        # 3. 오디오 입히기
        clip = clip.with_audio(audio.with_duration(duration))
        
        # 4. 파일 저장
        if not output_name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_name = f"tiz_tine_short_{timestamp}.mp4"
            
        output_path = os.path.join(self.output_dir, output_name)
        
        print(f"[*] 동영상 렌더링 중... (저장 경로: {output_path})")
        
        # 렌더링 옵션 (초당 프레임 수 24 설정)
        clip.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
        
        print(f"[+] 생성 완료: {output_path}")
        return output_path

if __name__ == "__main__":
    # 테스트 실행 (파일이 있을 경우)
    generator = TizTineShortsGenerator()
    
    # 예시 경로 (실제 파일 경로에 맞게 수정 필요)
    # image = "assets/images/sample.jpg"
    # audio = "assets/audio/sample.mp3"
    # generator.generate_short(image, audio)
    
    print("[!] 기획 단계: 실제 이미지와 오디오 에셋이 준비되면 위 주석을 풀고 실행할 수 있습니다.")
