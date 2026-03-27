import os
import sys
from google import genai
from google.genai import types

# --- API 키는 환경변수(GOOGLE_GENAI_API_KEY)로 설정하여 사용하세요 ---
API_KEY = os.environ.get("GOOGLE_GENAI_API_KEY")

def run_text_only():
    try:
        # 1. 제너레이터 초기화 (텍스트 전용 호출 테스트)
        client = genai.Client(api_key=API_KEY)
        
        # 2. 90 BPM 로파이 텍스트 프롬프트
        prompt = (
            "Create a 30-second nostalgic and cozy lo-fi hip-hop track. "
            "90 BPM, instrumental only with soft Rhodes piano and muffled drums. No vocals."
        )

        output_name = "assets/audio/tiztine_test_clip.mp3"
        print(f"[*] 이미지 제외, 텍스트 전용으로 '{output_name}' 생성을 시도합니다...")
        
        response = client.models.generate_content(
            model="lyria-3-clip-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO", "TEXT"],
            ),
        )

        # 3. 응답 파싱 및 저장
        found_audio = False
        for part in response.parts:
            if part.inline_data is not None:
                with open(output_name, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"\n[성공] 텍스트 기반 음원 저장이 완료되었습니다: {output_name}")
                found_audio = True
                break
        
        if not found_audio:
            print("\n[알림] 음원 데이터를 찾을 수 없습니다. 응답 내용:", response)

    except Exception as e:
        print(f"\n[오류 발생]: {e}")

if __name__ == "__main__":
    run_text_only()
