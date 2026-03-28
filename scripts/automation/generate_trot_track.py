import os
import sys

# 프로젝트 루트 및 스크립트 경로 설정
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, "../../"))
sys.path.append(script_dir)

try:
    from music_generator import TizTineMusicGenerator
except ImportError:
    print("[!] 에러: music_generator.py를 찾을 수 없습니다.")
    sys.exit(1)

def main():
    # 1. 제너레이터 초기화 (출력 폴더: assets/audio)
    generator = TizTineMusicGenerator(output_dir=os.path.join(project_root, "assets", "audio"))
    
    # 2. 베이스 이미지 선택 (01_street)
    image_path = os.path.join(project_root, "assets", "images", "characters", "v1.1_headset", "01_street.png")
    
    # 3. 고도화된 트로트 프롬프트 (요청 사항 반영)
    prompt = (
        "Project: TIZ-TINE Modern Korean Trot. "
        "Style: Upbeat Modern Korean Trot Dance Track. "
        "Rhythm: Fast and driving 2/4 Trot rhythm (148 BPM), highly danceable. "
        "Instrumentation: Rich brass section with powerful staccato hits, brilliant saxophone solo, "
        "and a cheerful accordion melody that provides festive energy. "
        "Vocals: Strong, high-energy vocal performance using the traditional Korean 'Kkeokgi' (shaking/vibrato) technique. "
        "The lyrics and mood should celebrate the joy of life and success. Vibrant and festive atmosphere."
    )
    
    # 4. 음악 생성 실행 (Lyria 3 Pro 사용)
    output_name = "tiztine_trot_energetic.mp3"
    print(f"[*] 루나: 트로트 트랙 '{output_name}' 생성을 시작합니다. (모델: Lyria 3 Pro)")
    
    result_path = generator.generate_from_image(
        image_path, 
        prompt, 
        output_name=output_name, 
        model="models/lyria-3-pro-preview"
    )
    
    if result_path:
        print(f"\n[성공] 트로트 음원이 생성되었습니다: {result_path}")
        print("[!] 이제 해당 음원을 사용하여 유튜브 쇼츠 영상을 제작할 수 있습니다.")
    else:
        print("\n[실패] 음원 생성에 실패했습니다. API 키 및 모델 접근 권한을 확인하세요.")

if __name__ == "__main__":
    main()
