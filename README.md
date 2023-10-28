# samsung-rpa
### 목차
+ [아나콘다 설치](#아나콘다-설치)
+ [VS code 설치](#vs-code-설치)
+ [VS code 환경 설정 하기](#vs-code-환경-설정-하기)



# 아나콘다 설치 
+ [설치 링크](https://www.anaconda.com/download/)
  + window, MacOS 자신에게 맞는 os 선택 후 다운로드 합니다.
### 1. 설치 진행
+ 기본 설정으로 진행합니다. 
![img](https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/7e2c68a6-c0cd-4d39-8f06-20eed3e4690d)


### 2. window pc 설정
+ window pc의 경우 추가 설정 필요 반드시 아래 작업이 필요합니다.
![img_1](https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/9f6f3a45-7965-45e7-8b52-da60bb53fae1)
![img_2](https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/4406f8e1-950b-4058-ac88-3d5a6aa6acae)


----

# VS code 설치 
[설치 링크](https://code.visualstudio.com/download)
 + window, MacOS 자신에게 맞는 os 선택 후 다운로드 합니다.

----- 

# VS code 환경 설정 하기
### 1. Extensions 설치
<img width="346" alt="image" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/5be98bbb-c2cf-4367-a31c-8e04e16ef74c">

 + python 설치 
 + python indent 설치
 + Python Extension Pack 설치
### 2. Window Command Prompt 선택 
![img_4](https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/3f0659cb-ea94-45b3-946c-dc02be26f83d)
+ ctrl + shift + p
+ `>select default profile`
+ Command Prompt 선택 -> power shell일 경우 실행이 불가능합니다. 

### 3. python 버전 선택 
![img_5](https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/8b088dba-45f1-4dae-a34a-53e161446663)

+ ctrl + shift + p
+ `>select interpreter`
+ 아나콘다가 정상적으로 다운 되었다면 python `3.x.x('base')`가 존재합니다.


### 4. jupyter(ipynb 파일 실행)
<img width="643" alt="image" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/3955f916-0dc3-4f68-b893-f38cb022b845">

+ 파일은 연 뒤 커널 선택 
+ python 환경
<img width="645" alt="image" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/11be0128-f6e4-438c-b9ce-cc9388badf33">

+ `>select interpreter`에서 선택한 버전 선택.

### 5. 라이브러리 설치 
<img width="667" alt="image" src="https://github.com/Nossi-RPA/samsung-rpa/assets/61634628/c92e3e48-394f-4715-ac46-42e9a6c86b76">

+ 터미널 -> 새터미널 열기
+ `pip install -r requirements.txt` 

