# REST Server & Client Framework : Express & Axios

![Alt text](<Screenshot 2023-10-14 at 8.50.28 AM.png>)
- 서버 Frame work : Express.JS
- Client Frame work : Axios

![Alt text](<Screenshot 2023-10-14 at 8.51.55 AM.png>)

### Uniform Resource Identifiers (URI) : `Hyperlinks`
![Alt text](<Screenshot 2023-10-14 at 8.53.38 AM.png>)

### UIR 구조 
![Alt text](<Screenshot 2023-10-14 at 8.55.17 AM.png>)

## Express.JS : 도움이 되는 Site
- 도움이 되는 site
    - [Express.JS](http://expressjs.com/en/5x/api.html)
    - [javatpoint](https://www.javatpoint.com/expressjs-tutorial)

## REST 서버 프레임워크 구조
![Alt text](<Screenshot 2023-10-14 at 8.59.24 AM.png>)
![Alt text](<Screenshot 2023-10-14 at 9.01.12 AM.png>)
> 복잡해보이지만 단순한 구조임

## Example Server Code
![Alt text](<Screenshot 2023-10-14 at 9.07.07 AM.png>)

## Express.JS 
![Alt text](<Screenshot 2023-10-14 at 9.08.46 AM.png>)
- Middleware Request Handlers : `respond to every request`
- Router Request Handlers : `respond to a request with specified method and path`

### Example Server #1
![Alt text](<Screenshot 2023-10-14 at 9.35.16 AM.png>)
 - middleware : request에 무조건 반응하는 핸들러
 - router : 특정 조건에 맞는 request에만 반응하는 핸들러
 - next : linked-list로 연결된 다음 핸들러를 호출
![Alt text](<Screenshot 2023-10-14 at 9.37.39 AM.png>)
 - res.send가 호출되면 거기서 부터 멈춘다.
 - 이것이 기본적인 구성
 - 핸들러들이 체인으로 연결되어 있어 첫번째부터 쭉 실행된다.
 - ERROR핸들러는 error발생시에만 호출됨

 ### Example Server #1: `ERROR`
![Alt text](<Screenshot 2023-10-14 at 9.38.26 AM.png>)
 - get 은 skip (error 밑에)
 - get은 조건 맞으면 실행 아니면 skip
![Alt text](<Screenshot 2023-10-14 at 9.39.33 AM.png>)

## Request Object : Properties
![Alt text](<Screenshot 2023-10-14 at 9.41.14 AM.png>)
![Alt text](<Screenshot 2023-10-14 at 9.42.12 AM.png>)
- 더 자세한 정보는 위의 링크를 통해 들어가면 확인할 수 있다.
- req.send하면 핸들러가 끝남.
- param은 가급적 사용하지 말라.

## Express Method for Middleware Request Handlers
![Alt text](<Screenshot 2023-10-14 at 9.43.28 AM.png>)

## Express Method for Router Request Handlers
![Alt text](<Screenshot 2023-10-14 at 9.43.58 AM.png>)

## Response Methods
![Alt text](<Screenshot 2023-10-14 at 9.46.12 AM.png>)

## REST Client Framework : Axios

- [axios_github](https://github.com/axios/axios)
- [axios_website](https://axios-http.com/docs/intro)

## 구조 
![Alt text](<Screenshot 2023-10-14 at 9.49.19 AM.png>)
- Request를 생성 Response를 프로세싱
- 서버와 반대

## Axios Methods
![Alt text](<Screenshot 2023-10-14 at 9.49.58 AM.png>)
- 아주 간단하다.
- config가 들어가 있음.

## 스키마 : Request Configuration
![Alt text](<Screenshot 2023-10-14 at 9.50.38 AM.png>)
- config에 들어갈 수 있는 것

## 스키마 : Response
![Alt text](<Screenshot 2023-10-14 at 9.51.12 AM.png>)
- 파싱된 결과가 자동으로 들어온다.

## Example #1 : GET
![Alt text](<Screenshot 2023-10-14 at 9.52.41 AM.png>)
- await이 되려면 async를 써야한다.
## Example #2 : GET
![Alt text](<Screenshot 2023-10-14 at 9.53.29 AM.png>)
## Example #3 : POST
![Alt text](<Screenshot 2023-10-14 at 9.55.04 AM.png>)
- axios(config)만 넣어서 실행할 수 있다.
## Example #4 : POST
![Alt text](<Screenshot 2023-10-14 at 9.56.50 AM.png>)
- post함수를 사용하여 실행가능 (첫번째가 Host, 두번째가 data)

## Install Express.JS
![Alt text](<Screenshot 2023-10-14 at 9.57.21 AM.png>)
