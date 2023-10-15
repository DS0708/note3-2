# AWS EC2

## part1

### Cloud Services
![Alt text](<Screenshot 2023-10-15 at 10.55.36 AM.png>)
> EC2는 IaaS에 해당

### Service & interface
![Alt text](<Screenshot 2023-10-15 at 10.58.23 AM.png>)
- EC2는 하드웨어 서버 위의 virtual server

## OverView
![Alt text](<Screenshot 2023-10-15 at 10.59.06 AM.png>)

## Launch EC2 Instance

### Login Page
![Alt text](<Screenshot 2023-10-15 at 11.00.37 AM.png>)
### Main page
![Alt text](<Screenshot 2023-10-15 at 11.00.52 AM.png>)
> EC2 선택
### EC2 Dashboard
![Alt text](<Screenshot 2023-10-15 at 11.04.38 AM.png>)
> 새로운 virtual machine 만들기 -> Launch Instance

### Choose AMI (OS)
![Alt text](<Screenshot 2023-10-15 at 11.06.47 AM.png>)
### 하드웨어 결정
![Alt text](<Screenshot 2023-10-15 at 11.07.15 AM.png>)
### Configure Instance
![Alt text](<Screenshot 2023-10-15 at 11.09.02 AM.png>)
### Add Storage
![Alt text](<Screenshot 2023-10-15 at 11.09.36 AM.png>)
### Add Tags
![Alt text](<Screenshot 2023-10-15 at 11.10.26 AM.png>)
> 관리를 위해서 Taggin을 함 (To search)
### configure Security Group
![Alt text](<Screenshot 2023-10-15 at 11.12.11 AM.png>)
> EC2를 다양한 방식으로 접근할 수 있는데 SSH만 열어준다는 것.
>> SSH는 TCP 프로토콜을 사용하고 22번 포트 사용
### Review
![Alt text](<Screenshot 2023-10-15 at 11.13.22 AM.png>)
> 나중에 실제 서버를 만드려면 Waring을 확인
### Key Pairs
![Alt text](<Screenshot 2023-10-15 at 11.14.42 AM.png>)
![Alt text](<Screenshot 2023-10-15 at 11.15.35 AM.png>)
> `다운로드하고 잘 저장해야함. AWS는 저장해주지 않는다.`
>> 잊어버리면 virtual machine 다시 만들어야 함
### Back to EC2 Dashboard
![Alt text](<Screenshot 2023-10-15 at 11.16.41 AM.png>)

> `Virtual Server is ready!!`
![Alt text](<Screenshot 2023-10-15 at 11.17.37 AM.png>)

