# 📺 TIZ-TINE: First Music Short Upload Metadata (v1.0)

본 문서는 첫 번째 공식 티저 쇼츠 "City Pop Melody" 업로드를 위한 최적화된 메타데이터(SEO) 정보입니다.

---

## 📽️ 1. 영상 기본 정보 (Basic Info)

- **영상 제목(Title):** 
  > Tiz-Tine (티즈틴) - Midnight City Pop 🎧✨ #CityPop #Lofi #TizTine
- **설명란(Description):**
  > 🌙 "Midnight blue, 네온 사인이 그려내는 거리... 헤드폰 너머로 들리는 리듬."
  > 
  > 티즈틴의 첫 번째 공식 사운드 트랙 'Midnight City Pop'의 티저 영상입니다! 80년대 레트로 감성과 티즈틴의 아늑한 밤 산책을 함께 즐겨보세요.
  > 
  > Full track and more content coming soon! 🐾 
  > 
  > 🎶 **Track:** Midnight City Pop (Original)
  > 🎨 **Visual:** TIZ-TINE official v1.1
  > 
  > #Lofi #CityPop #AnimeLofi #ChillBeats #CharacterBrand #Maltese #티즈틴 #시티팝 #쇼츠
- **고정 댓글(Pinned Comment):**
  > 🎧 티즈틴의 공식 채널에 오신 것을 환영합니다! 이 노래가 마음에 드셨다면 구독과 좋아요 부탁드려요. 여러분은 밤에 어떤 음악을 주로 들으시나요? 댓글로 남겨주세요! 👇✨

---

## 🎨 2. 사용 에셋 위치 (Asset Locations)

- **숏츠 비주얼:** `assets/images/content/01_citypop_teaser.png` (9:16)
- **음악 파일:** (AI 생성 후 `assets/audio/citypop_v1.mp3`로 저장 권장)
- **로고 워터마크:** `assets/images/branding/tiztine_logo_symbol.png`

---

## 🛠️ 3. 즉시 실행 가능한 쇼츠 생성 명령어 (Command)

오디오 파일이 준비된 후, 터미널에서 아래 코드를 수정하여 실행하세요.

```python
# scripts/automation/run_teaser.py 등의 파일로 실행하거나 REPL에서 활용
from scripts.automation.shorts_generator import TizTineShortsGenerator

gen = TizTineShortsGenerator()
gen.generate_short(
    image_path="assets/images/content/01_citypop_teaser.png",
    audio_path="assets/audio/citypop_v1.mp3", # 파일 생성 후 경로 확인
    caption="Midnight City Pop with TIZ-TINE 🎧",
    logo_path="assets/images/branding/tiztine_logo_symbol.png",
    output_name="TizTine_CityPop_Teaser_Final.mp4"
)
```

---
*Created by Antigravity for TIZ-TINE Project Roadmap Step 3*
