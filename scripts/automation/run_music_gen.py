import os
import sys
# scripts/automation/music_generator.py의 상대 경로를 시스템 패스에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from music_generator import TizTineMusicGenerator

# --- API 키는 환경변수(GOOGLE_GENAI_API_KEY)로 설정하여 사용하세요 ---
API_KEY = os.environ.get("GOOGLE_GENAI_API_KEY")

def run_test():
    try:
        # 1. 제너레이터 초기화
        generator = TizTineMusicGenerator(api_key=API_KEY)
        
        # 2. 이미지 경로 설정 (비 오는 날 테마)
        image_path = os.path.join("assets", "images", "characters", "v1.1_headset", "04_rain.png")
        if not os.path.exists(image_path):
            print(f"[!] 에러: 이미지 파일을 찾을 수 없습니다. ({image_path})")
            return

        # 3. 프롬프트 (가이드라인 준수)
        prompt = (
            "Create a nostalgic and cozy lo-fi hip-hop track inspired by this rainy night scene with Tiz-Tine. "
            "Ensure it is 90 BPM, instrumental only with soft Rhodes piano and muffled drums. No vocals."
        )

        # 4. 음악 생성
        output_name = "tiztine_rain_lofi.mp3"
        print(f"[*] Gemini Lyria 3 모델을 사용하여 '{output_name}' 생성을 시도합니다...")
        
        output_path = generator.generate_from_image(image_path, prompt, output_name)
        
        if output_path:
            print(f"\n[성공] 음원 생성이 완료되었습니다: {output_path}")
            print("[알림] 이제 shorts_generator.py를 사용하여 영상을 제작할 수 있습니다.")
        else:
            print("\n[실패] 음원 생성에 실패했습니다. API 할당량이나 모델 접근 권한을 확인하세요.")

    except Exception as e:
        print(f"\n[오류 발생]: {e}")

if __name__ == "__main__":
    run_test()
