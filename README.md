# 📝 My Daily Todo Tasker

![Python](https://img.shields.io/badge/Python-4B5563?style=flat&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-4B5563?style=flat&logo=streamlit&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-4B5563?style=flat&logo=visual-studio-code&logoColor=white) ![Git](https://img.shields.io/badge/Git-4B5563?style=flat&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-111827?style=flat&logo=github&logoColor=white)

**Streamlit**을 활용해 제작한 깔끔하고 직관적인 일상 관리용 웹 애플리케이션입니다. 미니멀한 UI를 통해 하루 일과를 정리하고, 공부 목표를 달성하며, 나만의 완벽한 하루를 디자인할 수 있도록 도와줍니다.

---

## 🎯 Project Overview & Core Experiences

Microsoft Data School 과정 중 당일 학습한 파이썬의 핵심 개념들을 실제 웹 애플리케이션에 접목하고, AI 에이전트와의 고도화된 협업을 경험하기 위해 개발한 토이 프로젝트입니다.

- **상태 관리 중심의 데이터 흐름(Data Flow) 이해**: `st.session_state`를 활용해 프론트엔드 UI의 입력값이 백엔드 자료구조에 실시간으로 매핑되고 변동되는 동적 웹 서비스의 라이프사이클을 이해했습니다.
- **UI/UX 한계 극복 및 커스터마이징**: Streamlit이 제공하는 기본 위젯의 레이아웃 한계를 넘기 위해 인라인 HTML/CSS 컴포넌트를 결합, 시각적으로 정돈된 미니멀한 스타일의 카드 레이아웃을 설계했습니다.
- **AI 에이전트 기반의 애자일 트러블슈팅**: 가상 환경(`venv`) 충돌, HTML 태그 렌더링 버그 등 개발 과정에서 마주한 다양한 예외 상황을 AI 에이전트와 유기적으로 소통하며 신속하게 해결하는 능력을 배양했습니다.

---

## 🎨 Key Features

- **Sidebar Task Planner**: Task Content, Category, Priority를 손쉽게 선택하고 추가할 수 있는 사이드바 플래너입니다.
- **Dynamic Category Icons**: 사용자가 선택한 활동에 따라 아이콘이 자동으로 매칭됩니다 (`📚 Study`, `☕ Daily`, `🏋️‍♀️ Workout`).
- **Priority Indicators**: 중요도에 따라 직관적인 컬러 점 배지가 표시됩니다 (`🔴 High`, `🟡 Medium`, `🟢 Low`).
- **Live Backend Visualizer**: "Behind the Scenes" 섹션을 통해 백엔드 데이터 구조가 실시간으로 어떻게 업데이트되는지 투명하게 확인할 수 있습니다.

---

## 🛠️ Tech Stack & Architecture

- **Language & Framework**: Streamlit <sub>![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)</sub> / Python <sub>![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)</sub>
- **State Management**: Streamlit Session State (`st.session_state`)
- **Styling Component**: Streamlit Markdown (인라인 HTML/CSS 내장형 레이아웃)
- **Development Environment**: Visual Studio Code <sub>![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white)</sub>
- **Version Control**: Git <sub>![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)</sub> / GitHub <sub>![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)</sub>

---

### 🗂️ Behind the Scenes: Data Structure

본 애플리케이션은 런타임 환경에서 세션 상태(Session State) 내부의 **List of Dictionaries(딕셔너리를 품은 리스트)** 구조로 데이터를 관리합니다. 할 일을 추가하거나 완료할 때마다 아래와 같은 JSON 구조가 실시간으로 확장 및 축소됩니다.

```json
[
  {
    "content": "Review Python Virtual Environments",
    "category": "Study",
    "priority": "High"
  },
  {
    "content": "Evening Running",
    "category": "Workout",
    "priority": "Low"
  }
]
```

---

## 🚀 How to Run Locally

본 프로젝트를 로컬 컴퓨터에서 복제하고 실행하려면 아래 단계를 순서대로 따라 하세요.

1. **저장소 클론 (Clone the repository)**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
   ```

2. **가상 환경 생성 및 활성화 (Set up venv)**

- Windows 환경:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

- Mac / Linux 환경:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. **필수 패키지 설치 (Install Streamlit)**
   ```bash
   pip install streamlit
   ```
   
4. **애플리케이션 실행 (Run the application)**
   ```bash
   streamlit run app.py
   ```

---
   
## 🖥️ Application Screenshot

<img src="https://github.com/user-attachments/assets/4ccfeaf7-3a8a-4303-bcff-c5d1ea7fc6fc" width="100%" alt="My Daily Todo Tasker Screenshot" />

*> 깔끔한 레이아웃과 실시간 백엔드 데이터 시각화가 적용된 메인 대시보드 화면입니다.*
