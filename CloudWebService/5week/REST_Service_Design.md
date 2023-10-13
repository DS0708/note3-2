# RESTful 웹 서비스 설계

## Objectives
- Designing Steps
- An Example Project
- Representation
- HTTP Methods

## What to design
- Programming
    - URLs을 파싱하고 Representations을 HTTP로 만드는 것
- 상당히 일반적이여서 연습만 잘하면 여러가지 어플리케이션에서 사용 가능 

## Designing Steps
1. 리소스 선정 (주요한 관리대상으로 설정)
2. URI를 할당
    - 직관적으로 알아볼 수 있도록 잘 할당
3. 리소스 별로 Representation 결정, 그리고 포맷 결정
![Alt text](<Screenshot 2023-10-14 at 8.07.57 AM.png>)
4. 각 리소스가 어떤 HTTP methods와 매핑되는지 결정
![Alt text](<Screenshot 2023-10-14 at 8.08.05 AM.png>)
    - 리소스의 특징에 따라 결정
    - CRUD의 해석에 따라 결정

## An Example project : 1. Identify resources and 2. assign URLs
![Alt text](<Screenshot 2023-10-14 at 8.13.26 AM.png>)
![Alt text](<Screenshot 2023-10-14 at 8.13.42 AM.png>)
![Alt text](<Screenshot 2023-10-14 at 8.14.06 AM.png>)

### Resources and URIs
![Alt text](<Screenshot 2023-10-14 at 8.15.34 AM.png>)
> 어떠한 것도 리소스로 취급될 수 있고 리소스로 취급되는 것은 URL을 할당한다.

![Alt text](<Screenshot 2023-10-14 at 8.16.48 AM.png>)
> 개별적인 것(id)도 템플릿을 통해 가능

## An Example project : 3. Representations

### Representation in XML
![Alt text](<Screenshot 2023-10-14 at 8.17.50 AM.png>)
> customer에 대한 정보를 XML로 나타냄

![Alt text](<Screenshot 2023-10-14 at 8.18.17 AM.png>)
> JSON형태로도 나타낼 수 있다.

![Alt text](<Screenshot 2023-10-14 at 8.19.15 AM.png>)
![Alt text](<Screenshot 2023-10-14 at 8.19.23 AM.png>)
![Alt text](<Screenshot 2023-10-14 at 8.19.31 AM.png>)

## An Example project : 4. HTTP METHODS
![Alt text](<Screenshot 2023-10-14 at 8.20.50 AM.png>)

### Resource: /products
![Alt text](<Screenshot 2023-10-14 at 8.21.55 AM.png>)

### Bulk Operation
- 일부만 볼 수 있게 구현
![Alt text](<Screenshot 2023-10-14 at 8.22.50 AM.png>)

### 리소스 : /products/{id}
![Alt text](<Screenshot 2023-10-14 at 8.23.32 AM.png>)

### 리소스 : /orders/{id}
![Alt text](<Screenshot 2023-10-14 at 8.24.18 AM.png>)
![Alt text](<Screenshot 2023-10-14 at 8.24.43 AM.png>)
> 새롭게 만들어진 URL을 Location에 넣어서 준다.

### 리소스 : /products/{id} `PUT : Update`
- Request
![Alt text](<Screenshot 2023-10-14 at 8.25.49 AM.png>)
- response
![Alt text](<Screenshot 2023-10-14 at 8.26.34 AM.png>)

### PUT : Create
![Alt text](<Screenshot 2023-10-14 at 8.28.06 AM.png>)

### POST vs PUT
![Alt text](<Screenshot 2023-10-14 at 8.28.34 AM.png>)
> POST는 반복해서 보내면 여러개가 생성 PUT은 반복되어도 하나만 생성 ( 이것이 Idempotent하냐 안하냐임)

### DELETE
![Alt text](<Screenshot 2023-10-14 at 8.29.53 AM.png>)

## Summary

### Designing RESTful Services
![Alt text](<Screenshot 2023-10-14 at 8.30.38 AM.png>)
