import os
import sys
from google import genai
from google.genai import types

class TizTineMusicGenerator:
    """
    TIZ-TINE 전용 AI 음악 생성기 (v1.0)
    - Google Gemini Lyria 3 모델을 사용하여 Lo-fi 음원을 생성합니다.
    - 텍스트 프롬프트 및 이미지 입력을 지원합니다.
    """
    def __init__(self, api_key=None, output_dir="assets/audio"):
        self.api_key = api_key or os.environ.get("GOOGLE_GENAI_API_KEY")
        if not self.api_key:
            print("[!] 에러: GOOGLE_GENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
            sys.exit(1)
        
        self.client = genai.Client(api_key=self.api_key)
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)

    def generate_from_image(self, image_path, prompt, output_name="tiztine_music.mp3"):
        """
        이미지에서 영감을 받은 음악 생성
        """
        if not os.path.exists(image_path):
            print(f"[!] 에러: 이미지 파일을 찾을 수 없습니다. ({image_path})")
            return None

        print(f"[*] 이미지 기반 음원 생성 시작: {image_path}")
        
        with open(image_path, "rb") as f:
            image_data = f.read()

        response = self.client.models.generate_content(
            model="lyria-3-clip-preview",
            contents=[
                types.Part.from_bytes(data=image_data, mime_type="image/png"),
                prompt
            ],
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO", "TEXT"],
            ),
        )

        output_path = os.path.join(self.output_dir, output_name)
        
        # 응답 파싱 및 저장
        for part in response.parts:
            if part.inline_data is not None:
                with open(output_path, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"[+] 음원 저장 완료: {output_path}")
                return output_path
        
        print("[!] 음원 데이터를 응답에서 찾을 수 없습니다.")
        return None

if __name__ == "__main__":
    # 사용 예시 (API 키가 설정된 경우)
    # generator = TizTineMusicGenerator()
    # prompt = "Create a nostalgic and cozy lo-fi hip-hop track inspired by this rainy night scene with Tiz-Tine. 90 BPM, instrumental only."
    # generator.generate_from_image("assets/images/characters/v1.1_headset/04_rain.png", prompt, "tiztine_rain_lofi.mp3")
    print("[!] 음악 생성 엔진(Lyria 3)이 로드되었습니다. API 키 설정 후 실행 가능합니다.")
