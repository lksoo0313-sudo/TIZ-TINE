import os
import sys
from datetime import datetime
from pathlib import Path
import torch
import scipy.io.wavfile
import numpy as np
from transformers import AutoProcessor, MusicgenForConditionalGeneration

# 한글 출력 설정
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# 프로젝트 루트 경로 설정 (TIZ-TINE 폴더 기준)
PROJECT_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "assets" / "audio"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 프롬프트 설정 (우천 테마)
PROMPT = (
    "Chill Lo-fi Hip-hop, Rainy Window theme, Soft Rhodes Piano, "
    "Rain drops background, Muffled lo-fi boom-bap beat, "
    "Melancholy but cozy, 85 BPM, warm analog character, "
    "instrumental only, no vocals, high-fidelity."
)

MODEL_ID = "facebook/musicgen-small"
DURATION = 20  # 사용자 요청: 20초

def generate_music():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = OUTPUT_DIR / f"tiztine_rainy_lofi_20s_{timestamp}.wav"

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("  🎵 TIZ-TINE | 로컬 MusicGen 음원 생성 엔진 가동")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"  💻 실행 환경: {device.upper()}")
    
    print(f"  📥 모델 로드 중: {MODEL_ID}")
    processor = AutoProcessor.from_pretrained(MODEL_ID)
    model = MusicgenForConditionalGeneration.from_pretrained(MODEL_ID)
    model = model.to(device)

    inputs = processor(text=[PROMPT], padding=True, return_tensors="pt").to(device)
    
    sample_rate = model.config.audio_encoder.sampling_rate
    # MusicGen의 frame_rate는 기본 50Hz
    max_new_tokens = int(DURATION * 50)

    print(f"  🎶 '우천' 테마 음원 생성 시작 (목표: {DURATION}초)...")
    with torch.no_grad():
        audio_values = model.generate(**inputs, max_new_tokens=max_new_tokens)

    audio_data = audio_values[0].cpu().numpy()
    if audio_data.ndim == 2:
        audio_data = audio_data.T
    
    audio_int16 = (audio_data * 32767).astype(np.int16)
    scipy.io.wavfile.write(str(output_path), sample_rate, audio_int16)

    size_mb = output_path.stat().st_size / 1_048_576
    print(f"\n  🎉 출력 완료! 파일 크기: {size_mb:.1f} MB")
    print(f"  📁 저장 경로: {output_path.resolve()}")
    return output_path

if __name__ == "__main__":
    generate_music()
