# 📝 My Daily Todo Tasker

**Streamlit**을 활용해 제작한 깔끔하고 직관적인 일상 관리용 웹 애플리케이션입니다. 미니멀한 UI를 통해 하루 일과를 정리하고, 공부 목표를 달성하며, 나만의 완벽한 하루를 디자인할 수 있도록 도와줍니다.

---

## 🎨 Key Features

- **Sidebar Task Planner**: Task Content, Category, Priority를 손쉽게 선택하고 추가할 수 있는 사이드바 플래너입니다.
- **Dynamic Category Icons**: 사용자가 선택한 활동에 따라 아이콘이 자동으로 매칭됩니다 (`📚 Study`, `☕ Daily`, `🏋️‍♀️ Workout`).
- **Priority Indicators**: 중요도에 따라 직관적인 컬러 점 배지가 표시됩니다 (`🔴 High`, `🟡 Medium`, `🟢 Low`).
- **Live Backend Visualizer**: "Behind the Scenes" 섹션을 통해 백엔드 데이터 구조가 실시간으로 어떻게 업데이트되는지 투명하게 확인할 수 있습니다.

---

## 🛠️ Tech Stack & Architecture

![Python](https://img.shields.io/badge/Python-4B5563?style=flat&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-4B5563?style=flat&logo=streamlit&logoColor=white) ![Git](https://img.shields.io/badge/Git-4B5563?style=flat&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-111827?style=flat&logo=github&logoColor=white)

- **Framework**: Streamlit
- **State Management**: Streamlit Session State (`st.session_state`)
- **Styling**: Streamlit Markdown 내 인라인 HTML/CSS 적용

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
