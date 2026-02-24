# 고양이 vs 강아지 분류 웹 서비스 🐱🐶

이 프로젝트는 Xception 딥러닝 모델(`best_model_xception.keras`)을 활용하여 사용자가 업로드한 사진이 고양이인지 강아지인지 판별해 주는 간단하고 직관적인 웹 서비스입니다.

## 🚀 주요 기능
- **이미지 업로드**: 드래그 앤 드롭 및 클릭 방식을 통해 손쉽게 이미지 업로드 가능.
- **실시간 예측**: 업로드된 이미지를 즉시 딥러닝 모델로 분석하여 예측 결과 및 확신도(%) 제공.
- **반응형 UI**: 깔끔하고 현대적인 디자인으로 직관적인 사용자 경험 제공.

## 🛠 사용된 기술 (Tech Stack)
- **Backend**: Python, Flask, TensorFlow (Keras)
- **Frontend**: HTML5, Vanilla CSS, Vanilla JavaScript
- **Model**: 사전 학습된 모델 (`best_model_xception.keras`) 
  - *입력 이미지 전처리 크기: 150x150 픽셀 기반 학습*

## 📁 프로젝트 구조
```text
dog-cat-class/
│
├── app.py                      # Flask 백엔드 서버 (라우팅, 이미지 전처리 및 모델 예측)
├── best_model_xception.keras    # 예측에 사용될 학습된 모델 파일
├── inspect_model.py             # (참고용) 모델 구조를 분석하는 스크립트
│
├── templates/
│   └── index.html               # 메인 웹페이지 HTML (디자인 및 인터페이스)
│
└── static/
    └── style.css                # 웹페이지 스타일링 (CSS)
```

## ⚙️ 실행 방법 (How to run)

### 1. 가상 환경 설정
프로젝트를 실행하려면 `tensorflow`, `flask`, `pillow` 등의 패키지가 필요합니다. 터미널을 열고 Anaconda(또는 Miniconda) 가상 환경(`.conda` 등)을 활성화합니다. (여기서는 `DS`를 예시로 사용합니다.)

```bash
conda activate DS
```

### 2. 필수 라이브러리 설치
필요한 파이썬 모듈이 모두 설치되어 있는지 확인합니다.

```bash
pip install tensorflow flask pillow
```

### 3. 서버 실행
모든 설치가 완료되었다면, 백엔드 서버를 실행합니다.

```bash
python app.py
```
성공적으로 실행되면 터미널에 `* Running on http://127.0.0.1:5000`와 같은 표시가 나타납니다.

### 4. 웹페이지 접속 및 테스트
1. 브라우저(Chrome, Safari 등)를 열고 `http://127.0.0.1:5000` 로 접속합니다.
2. 고양이 또는 강아지의 사진을 버튼을 눌러 선택하거나 회색 점선 영역에 끌어다 놓습니다.
3. [분류하기] 버튼을 누르면 AI가 잠시 분석한 후 결과를 화면에 보여줍니다.
