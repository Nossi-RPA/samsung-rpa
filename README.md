# samsung-rpa
### 목차
+ [아나콘다 설치](#아나콘다-설치)
+ [VS code 설치](#vs-code-설치)
+ [VS code 환경 설정 하기](#vs-code-환경-설정-하기)



# 아나콘다 설치 
+ [설치 링크](https://www.anaconda.com/download/)
  + window, MacOS 자신에게 맞는 os 선택 후 다운로드 합니다.
 
+ [설치 가이드](https://wikidocs.net/165528) 
### 1. 설치 진행
+ 기본 설정으로 진행합니다. 
![image](https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/cd6cedc4-48c5-453e-b922-78c3bf041006)




### 2. window pc 설정
+ window pc의 경우 추가 설정 필요 반드시 아래 작업이 필요합니다.

<img width="1077" alt="스크린샷 2023-10-28 오후 2 35 19" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/49854e46-679e-4d15-bc06-0b9a54f9bbcf">
<img width="1071" alt="스크린샷 2023-10-28 오후 2 35 42" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/9db95f1d-6e72-49bf-835e-40fe4289b0b8">



----

# VS code 설치 
[설치 링크](https://code.visualstudio.com/download)
 + window, MacOS 자신에게 맞는 os 선택 후 다운로드 합니다.

----- 

# VS code 환경 설정 하기
### 1. Extensions 설치
<img width="346" alt="스크린샷 2023-10-28 오후 3 33 13" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/805d1c88-5945-4c96-9387-12445e233816">


 + python 설치 
 + python indent 설치
 + Python Extension Pack 설치
### 2. Window Command Prompt 선택 
<img width="683" alt="스크린샷 2023-10-28 오후 2 46 42" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/085ca217-f5c5-4428-a872-6c1e9128df68">

+ ctrl + shift + p
+ `>select default profile`
+ Command Prompt 선택 -> power shell일 경우 실행이 불가능합니다. 

### 3. python 버전 선택 
<img width="608" alt="스크린샷 2023-10-28 오후 2 55 33" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/36648213-2a43-4f80-a552-aad633e19687">

+ ctrl + shift + p
+ `>select interpreter`
+ 아나콘다가 정상적으로 다운 되었다면 python `3.x.x('base')`가 존재합니다.


### 4. jupyter(ipynb 파일 실행)
<img width="643" alt="스크린샷 2023-10-28 오후 3 37 57" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/196b06ba-2a40-46e6-8a01-d3e1b6f2cb1d">

+ 파일은 연 뒤 커널 선택 
+ python 환경
  
<img width="645" alt="스크린샷 2023-10-28 오후 3 38 39" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/6979d784-919a-4c65-9610-7887b99fded6">


+ `>select interpreter`에서 선택한 버전 선택.

### 5. 라이브러리 설치 
 <img width="667" alt="스크린샷 2023-10-28 오후 3 51 30" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/56d9ac41-69ea-4bd4-9198-de1015ba91a8">

+ 터미널 -> 새터미널 열기
+ `pip install -r requirements.txt` 

