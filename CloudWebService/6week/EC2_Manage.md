# Manage EC2

## part2

## Resources for EC2 Instance
![Alt text](<Screenshot 2023-10-15 at 11.20.04 AM.png>)
> 주요한 리소스
>> EC2를 관리한다는 것은 이러한 리소스를 관리하는 것

## State of EC2 Instance
![Alt text](<Screenshot 2023-10-15 at 11.21.56 AM.png>)

## Manage EC2 Instance
![Alt text](<Screenshot 2023-10-15 at 11.23.05 AM.png>)
> AWS Web Console을 통해 EC2 Management를 수행가능

## Operate EC Instance : Stop (No Payment)
![Alt text](<Screenshot 2023-10-15 at 11.26.09 AM.png>)
- Stop하면 요금이 발생하지 않음
- 이 머신 정지
- Waring 메세지가 뜬다.
- 하드웨어에서 내려 버린다는 것.
- Stopping -> Stopped (완전히 소멸)
- Start로 다시 실행 가능

## Dynamically-Assigned Public IP for EC2
![Alt text](<Screenshot 2023-10-15 at 11.28.15 AM.png>)
> stop 시켰다가 Restart시키면 이 IP가 바뀐다. 
>> 기존에 IP를 사용했던 프로그램들은 무용지물이 된다.
>>> Statistically-Assigned IPs 로 해결할 수 있음.

## Elastic IPs : Statistically-Assigned IPs
![Alt text](<Screenshot 2023-10-15 at 11.30.08 AM.png>)
![Alt text](<Screenshot 2023-10-15 at 11.30.34 AM.png>)
> Create Elastic IP
![Alt text](<Screenshot 2023-10-15 at 11.31.00 AM.png>)
> Elastic IPs created!
>> 명시적으로 삭제할때 까지는 계속 존재하는 IP

## 할당
![Alt text](<Screenshot 2023-10-15 at 11.32.04 AM.png>)
![Alt text](<Screenshot 2023-10-15 at 11.32.13 AM.png>)
![Alt text](<Screenshot 2023-10-15 at 11.33.54 AM.png>)
> 이제 삭제해도 유지 가능

## Security Group
![Alt text](<Screenshot 2023-10-15 at 11.36.07 AM.png>)
> launch-wizard-6 선택
## Inbound Rules
![Alt text](<Screenshot 2023-10-15 at 11.35.28 AM.png>)
> `Open MQTT Port : 1883`

