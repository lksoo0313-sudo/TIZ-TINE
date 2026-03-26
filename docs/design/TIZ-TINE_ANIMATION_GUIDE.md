# ✨ TIZ-TINE: Looping Animation Guide (v1.0)

티즈틴(TIZ-TINE) 쇼츠 및 롱폼 LOFI 콘텐츠를 위한 시각적 생동감을 부여하는 애니메이션 규칙입니다.

---

## 🐶 1. 티즈틴 핵심 캐릭터 모션 (Core Action Patterns)

말티즈 특유의 부드럽고 가벼운 털의 질감을 살린 5가지 시그니처 루프입니다.

| 모션 이름 | 설명 | 루핑 주기(Cycle) | 추천 상황 |
| :--- | :--- | :--- | :--- |
| **Blinker** | 눈을 1~2초 간격으로 천천히 깜빡임 | Random (3s~5s) | 모든 상황 공통 |
| **Head Bobber** | 음악 비트에 맞춰 고개를 작게 까딱임 | 4 Beats (Sync with music) | 음악 감상 중인 티즈틴 |
| **Tail Wagger** | 꼬리를 좌우로 아주 느리게 흔듦 | 8 Beats | 아늑한 홈/침실 환경 |
| **Ear Twitcher** | 소리에 반응하듯 한쪽 귀를 아주 작게 들썩임 | Random (5s interval) | 카페, 비 오는 날 |
| **Paw Tapper** | 앞발 하나로 바닥을 톡톡 침 | 2 Beats (Sync with kick) | 흥겨운 비트의 LOFI |

---

## 🏙️ 2. 상황별 배경 애니메이션 (Ambient Environment)

배경 요소의 움직임은 티즈틴의 동작보다 더 느리고 차분해야 시선이 분산되지 않습니다.

- **Rainy Window**: 창문에 물방울이 맺혀 아래로 불규칙하게 흘러내리는 효과 (Alpha Overlay).
- **Home Study**: 탁상 스탠드의 불빛이 아주 미세하게 깜빡이거나 먼지가 떠다니는 효과.
- **Cozy Cafe**: 컵에서 김이 모락모락 올라오는 효과 (Steam loop).
- **Night Street**: 창밖 멀리 가로등이나 자동차 불빛이 지나가는 효과.

---

## ⚙️ 3. 제작 및 동기화 기술 가이드 (Technical Specs)

### **A. 프레임 속도 (Frame Rate)**
- **24fps** 추천: 애니메이션 특유의 감성을 살리기 위함.

### **B. 음악 동기화 (Audio Sync)**
- 모든 애니메이션은 기본적으로 **90 BPM(0.66초당 1비트)** 기준에 맞춰 루핑 주기를 배수로 설정합니다.
- 예: 4비트 주기의 고개 까딱임 = 2.64초마다 한 번의 Cycle 반복.

### **C. AI 생성 힌트 (Luma, Runway 등)**
- AI 비디오 생성 도구 사용 시 프롬프트 예시:
- `Subtle tail wagging, Gentle blinking, Tiz-tine nodding head to the beat, Cinematic lighting, 2D artistic aesthetic, Looping video, High quality anime style`

---

## 📝 4. 다음 단계 제안 (The First Shot)

1. **테스트 샷**: 비 오는 날, 방 안에서 헤드셋을 쓰고 공부하는 티즈틴의 **'Head Bobbing'** 영상 제작.
2. **에셋 분리**: 캐릭터와 배경을 분리하여 각기 다른 속도로 루핑되도록 레이어 작업.

---
*Created by Connect AI LAB J-Team for TIZ-TINE Project*
