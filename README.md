# ormi-django-project2

## 주제: chatGPT를 이용한 싱가포르 여행계획 자동생성 플래너 챗봇 pt2. (백엔드 서버 구현, 배포, 도메인 연결)

### 목표
- openAI의 Chat Completion API를 활용하여 aws 서버에서 openAI chatgpt3.5 turbo 모델과 통신 후 프론트엔드에 DRF를 통하여 데이터 전송

### 개발환경
aiohttp==3.8.5
aiosignal==1.3.1
asgiref==3.7.2
async-timeout==4.0.2
attrs==23.1.0
certifi==2023.7.22
charset-normalizer==3.2.0
Django==4.2.3
django-cors-headers==4.2.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
frozenlist==1.4.0
idna==3.4
multidict==6.0.4
openai==0.27.8
PyJWT==2.8.0
python-dotenv==1.0.0
pytz==2023.3
requests==2.31.0
sqlparse==0.4.4
tqdm==4.65.0
typing_extensions==4.7.1
urllib3==2.0.4
yarl==1.9.2

### 개발기간
2023.07.26 ~ 2023.08.02

### 배포 URL
http://bundletripbychat.com/

### ERD 기획
![ormi-django-project2](https://github.com/sunse-kwon/ormi-django-project2/assets/94329884/26a4dad7-a963-48b0-b07a-a05392a25204)

위와 같이 기획 하였지만 실제 구현 시 저렇게 구현하지 못하였습니다. 

### 기능 기획
![django-rest-chatgpt-mindmap](https://github.com/sunse-kwon/ormi-django-project2/assets/94329884/fbfaf79e-45d9-4a63-ba19-d2d4b1ea6445)

위와 같이 기능기획을 하였으나, 좀더 구체적이지 못한 한계점이 있습니다. 

### 세부기능 :
- chatbot app을 통하여 chatGPT API과 통신
- user app 을 통하여 회원가입 기능 구현, simple jwt를 활용하여  로그인, token refresh 기능 구현
- project 내의 view.py 에서 jwt validation 기능 구현, 이를 활용하여 다이나믹 헤더 버튼을 구현 (로그인된 사용자에 한하여 로그아웃 버튼이 보임)
  

###프로젝트 진행하며 힘들었던 점

마치며 
