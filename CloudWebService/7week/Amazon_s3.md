# Amazon Simple Storage Service : S3

## part1

## Virtual File on Cloud Computing
![Alt text](<Screenshot 2023-10-15 at 4.50.48 PM.png>)
> How to return a data file ?

## AWS S3 : Concept
- 정의 : `어디서나, 다양한 방법으로 원하는 양의 데이터를 저장하고, 검색할 수 있도록 구축된 객체 스토리지`
- 요약
    - 객체 기반의 무제한 파일 저장스토리지
    - 저장하고 이용한 만큼 지불하는 종량 스토리지
    - 웹서버처럼 이용가능
    - 이용빈도가 잦지 않다면 저렴하게 보관 가능
    - URL을 통해 손쉽게 파일 공유가능

## AWS S3 : Organization
- `Bucket`
    - 데이터를 저장하기 위한 Amazon S3의 Top-level Object Container
    - 버킷에 데이터를 무한정으로 저장 가능
    - 모든 Object는 어떤 버킷에 포함된다.
    - 리전 설정
- `Folder`
    - 내부 Container
- `Object`
    - Amazon S3에 저장되는 기본 객체
    - 파일
## AWS S3 : Advantages
- 따라올 수 없는 내구성, 가용성 및 확장성
    - 내부에 저장된 오브젝트 보존 가능성
- 쿼리 지원
    - S3에 저장된 데이터에 대해 직접 분석
- 유연한 관리
    - 각 스토리지 개별적으로 확인 및 제어
- 간편하고 유연한 데이터 전송
    - Amazon S3 Transfer Acceleration
    - AWS Direct Connect
## AWS S3 : Service Category
- `Standard Storage`
    - 일반적인 스토리 옵션
    - 내구성은 99.99999% (아주 높은 내구성)
    - 높은 비용
    - 중요한 데이터를 서비스에 저장해야 하는 경우 사용
- `RRS, Reduced Redundancy Storage`
    - Standard Storage보다 낮은 99.99% 내구성
    - 저렴한 가격
## AWS S3 : Use Cases
- 백업 및 복구
- 데이터 아카이빙
- 데이터 레이크 및 빅 데이터 분석
- 하이브리드 클라우드 스토리지
- 클라우드 네이티브 애플리케이션 데이터
- 재해 복구
## AWS S3 : Storage Shared by AWS Services
![Alt text](<Screenshot 2023-10-15 at 5.50.31 PM.png>)

<br>
<br>
<br>


## 지금부터는 관리에 대한 얘기

## Amazon S3 Dashboard
![Alt text](<Screenshot 2023-10-15 at 5.51.58 PM.png>)
> 로그인 후 이용

## S3 Dashboard : Bucket Creation
![Alt text](<Screenshot 2023-10-15 at 5.52.40 PM.png>)
## Bucket Configuration
![Alt text](<Screenshot 2023-10-15 at 5.53.02 PM.png>)
## Bucket Options
![Alt text](<Screenshot 2023-10-15 at 5.53.25 PM.png>)
## Bucket Review
![Alt text](<Screenshot 2023-10-15 at 5.54.50 PM.png>)
## Bucket List
![Alt text](<Screenshot 2023-10-15 at 5.55.04 PM.png>)
> 버킷 확인
## Folder Creation (1/2)
![Alt text](<Screenshot 2023-10-15 at 5.56.09 PM.png>)
> Create Folder 선택
## Folder Creation (2/2)
![Alt text](<Screenshot 2023-10-15 at 5.56.31 PM.png>)
## Upload to Bucket (1/3)
![Alt text](<Screenshot 2023-10-15 at 5.57.18 PM.png>)
> 객체 업로드
## Upload to Bucket (2/3)
![Alt text](<Screenshot 2023-10-15 at 5.57.33 PM.png>)
> 파일 업로드
## Upload to Bucket (3/3)
![Alt text](<Screenshot 2023-10-15 at 5.58.09 PM.png>)
## Object List
![Alt text](<Screenshot 2023-10-15 at 5.58.01 PM.png>)
## Public Access
![Alt text](<Screenshot 2023-10-15 at 6.00.46 PM.png>)
> Access Denied
## Make Object Pulbic
![Alt text](<Screenshot 2023-10-15 at 6.01.49 PM.png>)
> Make Public를 선택하면 외부에서도 접근 가능
## Re : Public Access
![Alt text](<Screenshot 2023-10-15 at 6.02.12 PM.png>)

<br><br><br>

> `S3 Object를 사용할 때는 비용이라는 것이 어마무시할 수도 있으므로 잘 생각하고 사용할 것.` 