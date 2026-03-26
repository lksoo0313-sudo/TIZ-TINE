import os
from datetime import datetime
from moviepy.editor import ImageClip, AudioFileClip, TextClip, CompositeVideoClip

class TizTineShortsGenerator:
    """
    TIZ-TINE 전용 쇼츠 영상 생성기 (v2.0)
    - 이미지와 오디오를 합쳐 고화질 세로형 쇼츠(9:16, 1080x1920) 영상을 생성합니다.
    - 자막(Caption) 및 워터마크(Logo) 오버레이 기능을 포함합니다.
    """
    def __init__(self, output_dir="outputs/shorts"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

    def generate_short(self, image_path, audio_path, caption=None, logo_path=None, output_name=None):
        """
        쇼츠 영상 생성 메인 함수
        :param image_path: 배경 이미지 경로 (9:16 권장)
        :param audio_path: 배경 음악 경로 (.mp3, .wav 등)
        :param caption: 화면 하단에 표시할 자막 (옵션)
        :param logo_path: 화면 상단에 표시할 로고/워터마크 경로 (옵션)
        :param output_name: 출력 파일명 (None이면 자동 생성)
        """
        print(f"[*] 영상 제작 시작: {image_path} + {audio_path}")
        
        # 1. 오디오 클립 로드 및 길이 확인
        if not os.path.exists(audio_path):
            print(f"[!] 에러: 오디오 파일을 찾을 수 없습니다. ({audio_path})")
            return None
        
        audio = AudioFileClip(audio_path)
        duration = audio.duration
        
        # 2. 배경 이미지 클립 생성 (쇼츠 규격 1080x1920 강제 리사이징)
        if not os.path.exists(image_path):
            print(f"[!] 에러: 이미지 파일을 찾을 수 없습니다. ({image_path})")
            return None
            
        bg_clip = ImageClip(image_path).set_duration(duration)
        
        # 쇼츠 비율(9:16) 맞추기 - 높이 1920 기준 리사이즈 후 중앙 배치
        bg_clip = bg_clip.resize(height=1920)
        final_video_width = 1080
        final_video_height = 1920
        
        clips = [bg_clip.set_position("center")]
        
        # 3. 자막 추가 (옵션)
        if caption:
            # 주의: 시스템에 폰트가 설치되어 있어야 합니다. (기본: Arial 또는 NanumGothic)
            try:
                txt_clip = TextClip(
                    caption, 
                    fontsize=60, 
                    color='white', 
                    font='Arial-Bold', # 또는 'NanumGothic-ExtraBold'
                    method='caption',
                    size=(final_video_width * 0.8, None),
                    stroke_color='black',
                    stroke_width=2
                ).set_start(0).set_duration(duration).set_position(('center', 1500))
                clips.append(txt_clip)
            except Exception as e:
                print(f"[!] 자막 생성 중 오류 발생 (폰트 문제 등): {e}")

        # 4. 로고/워터마크 추가 (옵션)
        if logo_path and os.path.exists(logo_path):
            logo_clip = ImageClip(logo_path).set_duration(duration).resize(width=200).set_position((800, 100)).set_opacity(0.8)
            clips.append(logo_clip)
        
        # 5. 최종 합성
        video = CompositeVideoClip(clips, size=(final_video_width, final_video_height))
        video = video.set_audio(audio)
        
        # 6. 파일 저장
        if not output_name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_name = f"tiztine_short_{timestamp}.mp4"
            
        output_path = os.path.join(self.output_dir, output_name)
        
        print(f"[*] 동영상 렌더링 중... (저장 경로: {output_path})")
        video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
        
        print(f"[+] 제작 완료: {output_path}")
        return output_path

if __name__ == "__main__":
    # 사용 예시 (추후 실제 파일 경로로 실행하세요)
    # generator = TizTineShortsGenerator()
    # generator.generate_short("assets/images/characters/v1.1_headset/01_street.png", "assets/audio/test_lofi.mp3", caption="City Pop Vibes with TIZ-TINE")
    print("[!] 쇼츠 제작 엔진(v2.0)이 로드되었습니다. 실제 에셋이 준비되면 실행 가능합니다.")
