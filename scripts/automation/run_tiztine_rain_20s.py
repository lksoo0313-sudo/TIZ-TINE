import os
import sys
from music_generator import TizTineMusicGenerator

def main():
    # .env 파일에서 API 키를 로드하기 위한 간단한 로직 (또는 로컬 환경 변수 사용)
    api_key = os.environ.get("GOOGLE_GENAI_API_KEY")
    if not api_key:
        # .env 파일을 수동으로 읽어옴
        try:
            with open(".env", "r") as f:
                for line in f:
                    if line.startswith("GOOGLE_GENAI_API_KEY="):
                        api_key = line.split("=")[1].strip()
                        break
        except FileNotFoundError:
            pass

    if not api_key:
        print("[!] 에러: API 키를 찾을 수 없습니다.")
        return

    # 배경 이미지 경로 (우천 테마)
    image_path = "assets/images/characters/v1.1_headset/04_rain.png"
    
    # 프롬프트 구성 (가이드 기반)
    prompt = (
        "Create a 20-second chill lo-fi hip-hop track for the 'Rainy Window' theme. "
        "Style: Soft Rhodes Piano, Rain drops, Muffled lo-fi beat, Melancholy but cozy. "
        "Tempo: 85 BPM. Instrumental only, no vocals."
    )

    generator = TizTineMusicGenerator(api_key=api_key)
    output_filename = "tiztine_rainy_lofi_20s.mp3"
    
    print(f"[*] '우천' 테마 로파이 음원 생성 시작 (목표 길이: 20초)")
    result_path = generator.generate_from_image(image_path, prompt, output_filename)

    if result_path:
        print(f"[+] 성공: 음원이 생성되었습니다 -> {result_path}")
    else:
        print(f"[!] 실패: 음원 생성에 실패했습니다.")

if __name__ == "__main__":
    main()
