# RESTful Web Services 

## Study and Learn
- Concepts of REST
- REST Architecture Style for Programmable Web
- Developing RESTful Web Services

## Motivation for RESTfuel Web Services
![Alt text](<Screenshot 2023-10-14 at 7.02.23 AM.png>)
> 이미 Web은 성공을 이루었지만 Open API에 대한 표준을 Programmable web은 제공하지 못하였다.

### Early Efforts for Open API
- SOAP-based Web Services : Heavyweight Architecture for Remote Service Invocation or Distributed Object Access
    - Reinvent or Ignore features that make Web successful
    - Use a number of new protocols and standars (e.g., SOAP, WSDL, UDDI)
    - `Unnecessary complexity or runtime overhead`

## RESTful Web Service 개념 설명
- REST : `Re`presentational `S`tate `T`ransfer

### REST based Programmable Web `Nothing New, but on HTTP!!`
![Alt text](<Screenshot 2023-10-14 at 7.11.02 AM.png>)
> REST라고 하는 것의 특징은 모든 것이 URI를 가지고 있는 리소스로써 취급된다 (Based on the HTTP Technology)

### How web applications work !
![Alt text](<Screenshot 2023-10-14 at 7.16.20 AM.png>)

### HTTP Requests & Responses
![Alt text](<Screenshot 2023-10-14 at 7.18.27 AM.png>)

### Representational State Transfer
- 클라이언트의 State
    - 클라이언트가 현재 processing중인 리소스의 Representation
- State Transfer
    - 이전의 리소스의 representation에서 하이퍼링크를 통해 새로운 리소스에 접근 하는 것

## REST 아키텍쳐 스타일 For Programmable WEB

### Resources
![Alt text](<Screenshot 2023-10-14 at 7.23.14 AM.png>)
- 클라이언트는 모든 것을 리소스로 본다.
- Something can be
    - DBMS에 저장되는 데이터 or 문서
    - 프로그램 실행 결과
- 예를 들어
    - Static : version 1.3의 소프트웨어
    - Dynamic : 가장 최근 버전의 소프트웨어
> 결론적으로 그 어떠한 것도 리소스가 될 수 있다.

### 리소스 Names & Addressability(접근가능성)
- 리소스는 이름이 있어야 하고 그 이름을 통해 접근 가능해야 한다.
- URI 가 Name의 역할을 한다.
    - 한번 할당되면 변하면 안됨
    - 그래야 Rest작동 가능
- `URI : Name and Address of a Resource`
- 모든 URI는 유니크해야한다.
- URI를 보고 어떤 것인지 유추할 수 있어야 함.

### URIs
![Alt text](<Screenshot 2023-10-14 at 7.32.06 AM.png>)

### Service 리소스의 호출
- 서비스 코드를 실행 시키려면 URL을 치면 됨
- URL 뒤에 APPEND해서 Argument를 준다.
    - ex) http://www.google.com/search?q=jellyfish
    - 검색엔진 서비스에게 argument로 jellyfish를 준다.
- `Service invocation`도 URL로 표현된다.
- `프로그램 호출도 URL로 표현될 수 있다.` (REST 모델에서는)

### URI Templates for Services
![Alt text](<Screenshot 2023-10-14 at 7.37.55 AM.png>)
- 유사한 리소스는 템플릿이라는 하나의 집합으로 묶어서 하나의 서비스 코드로 대응 시킬 수 있다.
- 서버의 부담이 굉장히 줄어든다.

### Representation
![Alt text](<Screenshot 2023-10-14 at 7.39.26 AM.png>)
- Representation이란 HTTP Request에 대한 Response를 나타낸 리소스의 상태이다.
- request에 대하여 서버가 지원하는 컨텐츠 타입으로 다양한 Representation을 지원한다.

> 결국에는 REST 모델에서 HTTP request를 보내면 Representation의 포맷에 맞춰 서버가 response를 보낸다.

### HTTP Uniform Interface for every resource
- HTTP Methods로만 서버에게 요청할 수 있음.
![Alt text](<Screenshot 2023-10-14 at 7.44.23 AM.png>)
- Advantages
    - 굉장히 단순하고 친숙하다. (새로운 기술과 프로토콜의 필요가 없음)
    - 이미 수 많은 회사 조직들에서 HTTP를 사용하고, 거의 모든 언어와 호환성이 있다.
    - HTTP서비스로 엄청난 동시 접속자를 수용할 수 있음 (Scalability)

### CRUD Management for a Resource
- POST : Create
- Get : Read
- Put : Update
- DELETE : Remove
- `HTTP 프로토콜에 근거하여 리소스에 대하여 CRUD를 할 수 있다.`

## Developing RESTful Web Services

### Interactions in RESTful Web Services
![Alt text](<Screenshot 2023-10-14 at 7.51.27 AM.png>)
> 굉장히 단순한 구조

![Alt text](<Screenshot 2023-10-14 at 7.52.44 AM.png>)
> 사실 개발한다는 것은 URL을 Annotating하는 것.

![Alt text](<Screenshot 2023-10-14 at 7.54.38 AM.png>)
> Annotating한 자바 코드

### RESTful Web Services : Client
![Alt text](<Screenshot 2023-10-14 at 7.57.06 AM.png>)
![Alt text](<Screenshot 2023-10-14 at 7.57.21 AM.png>)
> 이거 처리하는 코드 짜는 것임

## Summary
![Alt text](<Screenshot 2023-10-14 at 7.58.11 AM.png>)
![Alt text](<Screenshot 2023-10-14 at 7.59.08 AM.png>)

