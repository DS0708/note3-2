# Amazon S3

## part2

## AWS SDK for S3

### Install AWS SDK on Node.Js
- Command : "$ npm install aws-sdk"

### S3 SDK Install
- Window는 깃허브에서 설치 후 압축 풀기

[SDK에 대한 자세한 설명 (Document)](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest?AWS/S3.html)

### AWS SDK Credentials : Predefined Location
- 첫번째 방법
![Alt text](<Screenshot 2023-10-15 at 6.09.14 PM.png>)
> 자기가 만든 SDK를 사용하는 모든 앱에서 여기 있는 id, password가 사용 된다.

### 코드 (in-line)
- 두번째 방법 
![Alt text](<Screenshot 2023-10-15 at 6.11.44 PM.png>)
> `보안 위험이 있다.`

### Programmed Location
- 세번째 방법  
![Alt text](<Screenshot 2023-10-15 at 6.12.52 PM.png>)
> json파일로 저장하여 불러오기 가능 

## AWS-SDK : Major Methods
![Alt text](<Screenshot 2023-10-15 at 6.14.23 PM.png>)
### S3.createBucket
![Alt text](<Screenshot 2023-10-15 at 6.15.56 PM.png>)
### S3.upload
![Alt text](<Screenshot 2023-10-15 at 6.16.03 PM.png>)
> images 는 Folder name
### S3.listObjects
![Alt text](<Screenshot 2023-10-15 at 6.17.22 PM.png>)
> 버킷 내에 어떤 오브젝트가 있는지 확인하는 코드
### S3.getObject
![Alt text](<Screenshot 2023-10-15 at 6.18.02 PM.png>)
> 실제 S3에 있는 내용 자체를 읽어 오는 것
### S3.deleteObject
![Alt text](<Screenshot 2023-10-15 at 6.18.08 PM.png>)