# ESTsoft-BE-bootcamp-project-3-DRF

## 주제: ChatGPT를 활용한 싱가포르 여행계획 자동생성 플래너 챗봇 - Backend

### 목표
- openAI Chat Completions과 통신 후 DRF 서버와 프론트엔드 페이지 간 통신하는 Backend Server 구현
- AWS EC2, Uwsgi, Nginx를 활용한 Backend Server 배포

### 개발환경
![Django REST framework](https://img.shields.io/badge/Django_REST_framework-092E20?style=for-the-badge&logo=django&logoColor=white)

- 주요 라이브러리 버전
```
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
```

### 배포
  ![Nginx](https://img.shields.io/badge/Nginx-269539?style=for-the-badge&logo=nginx&logoColor=white)
  ![Uswgi](https://img.shields.io/badge/uwsgi-488A99?style=for-the-badge&logo=uwsgi&logoColor=white)
  ![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)

### 개발기간
2023.07.26 ~ 2023.08.02

### 배포 URL
http://bundletripbychat.com/

### ERD 기획
![ormi-django-project2](https://github.com/sunse-kwon/ormi-django-project2/assets/94329884/26a4dad7-a963-48b0-b07a-a05392a25204)

- ERD 설계를 진행할 당시 참고한 sample code는 text-davinci-003 을 사용하여 role의 구분없이 prompt로 user의 input 메시지를 일괄적으로 통합하여, ERD 모델 설계도 user의 질문을 prompt, gpt의 응답을 response 로 구성하였습니다.
- 위 ERD 설계에 따라 view 및 model을 구현하였지만, 기존 HTML/CSS 프로젝트와 연결할 시점에, input 메시지를 전송할때 형식이 다름을 인지하고, 이에, gpt-3.5-turbo 를 사용한 ChatCompletion API을 사용하여 view, model을 수정하였습니다.
- 그렇기에 해당 ERD 설계를 충분히 고려하여 모델을 생성하지 못했음이 한계점입니다. 

### 기능 기획
![django-rest-chatgpt-mindmap](https://github.com/sunse-kwon/ormi-django-project2/assets/94329884/fbfaf79e-45d9-4a63-ba19-d2d4b1ea6445)

- 위와 같이 기능기획을 하였으나, 구체적이지 못한 한계점이 있습니다. 특히 Token을 사용하여 인증할 계획을 갖고있었으나, JWT에 대한 이해가 전혀 없는 상태에서 기능을 기획했기에 어떤 부분이 필요한지 자세히 설명할 수 없었습니다. 

### 세부기능
- chatbot app을 통하여 ChatGPT API과 통신 후 Frontend와 통신하는 API 구현.
- user app 을 통하여 회원가입 API 구현, Simple JWT를 활용하여 로그인, token refresh API 구현.
- project 내의 view.py 에서 JWT Validation API 구현, 이를 활용하여 다이나믹 웹페이지 버튼을 구현 (로그인된 사용자에 한하여 로그아웃 버튼이 보임).

### 프로젝트 진행하며 어려웠던 점
- 모놀리식과는 다르게 DRF로 구현하는 과정에서, 프론트엔드와 백엔드 프로젝트를 분리하여, 두가지 프로젝트를 오가며 개발해야 하는 점이 개념을 이해하기 어려웠습니다.
- JWT에 대한 이해가 없이 인증을 구현하려고 하여, 토큰이 작동하는 방식을 이해하기 위해, 많은 시행착오를 겪어야 했습니다. 특히 Simple JWT로 Token Validation을 구현하려고 하는 과정에서, 토큰을 전송할때, Bearer 라는 앞의 불필요한 문자열을 제거한 후 access toeken 자체만 넣어주어야 함을 배웠습니다.
- AWS 서버에 Uwsgi 와 Nginx를 이용하여 배포하였지만, Docker를 활용한 배포 방식이 현업에서 많이 사용됨에 따라서, docker를 추가적으로 더 공부하여 해당 프로젝트를 도커화 해야겠다는 생각을 하였습니다.
- github page와 개인적으로 구매한 도메인의 연결작업이 힘들었습니다. custom domain을 연결하였을때, 서버와 통신을 할 수 없었는데, 깃허브 페이지만 구매한 도메인으로 연결해주었고, 그 안에서 동작하는 서버와 통신하는 서브 도메인을 연결해주지 않아서 일어나는 문제였습니다. 서버와 통신하는 서브 도메인을 설정해주어야 한다는 점이 초심자의 입장에서는 생소하게 다가왔고, 도메인에 관해 더 많은 공부가 필요함을 느꼈습니다.
- 비동기 통신을 하는 여러 방법중 HTML/CSS 프로젝트에서는 fetch 만 사용하였는데, ajax, axios 등 여러가지 비동기 통신방법이 있음을 알았고, axios 코드를 가져와 동작하게는 하였지만 비동기 통신에 대한 깊은 이해없이 쓰다보니, 많이 헤메었던것 같습니다.
- 다이나믹 웹페이지를 구현함에 있어 장고 template language를 사용할 수 없음을 알게 되었고, template language와 비슷한 방법을 구현하기위해, 프론트엔드 프레임워크들이 필요함을 알게 되었습니다. 해결 방법을 생각하던 중, 구현해 두었던 token validation API를 사용하여, 유효한 토큰에 한하여, response 를 보내주고, 그렇지 않다면, error를 보내주도록 하여, 토큰이 유효한 경우 로그아웃 버튼이, 그렇지 않을 경우 로그인 버튼이 보이도록 다르게 구성하였습니다.
- https를 구현함에 있어, 서버로 보내주는 URL에 대해서는 https 적용하도록 해주었지만, github page에서 custom domain으로 가는 url에 대하여 https를 적용하는데 실패하였습니다. 

### 마치며
이번 DRF 프로젝트를 하면서 API에 대한 이해가 많이 생겼던 것 같고, 동시에 저의 부족한 점을 많이 느꼈습니다. 장고 DRF를 구현하고, 프론트엔드 프로젝트와 백엔드 프로젝트를 연결시켜, 저만의 웹서비스를 구현할 수 있었던 좋은 경험이었습니다.
