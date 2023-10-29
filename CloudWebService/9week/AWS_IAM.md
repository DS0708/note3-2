# AWS IAM 

## IAM : Authentication (Identity) & Authorization (Access)
![Alt text](<Screenshot 2023-10-26 at 7.58.27 AM.png>)
- Authentication : Identity Management
    - Verify `who the current user is`
    - Credentials : `ID & Password, Certificate & Private Key` or `Token`
    - `아이디나 비밀번호를 통해 유저를 인증한다.`
- Authorization : Access Management (Control)
    - Verify `what the authenticated user can do (access)`
    - Manage (`Who`, What `Actions`, Which `Resource/Services`)
    - `Policies` : a set of permissions (Actions of Service, Resources)
    - `인증된 유저가 할 수 있는 액션 과 리소스 서비스가 무엇인지 확인한다.`
- `AWS Identity & Access Management (IAM)`
    - Who : `Identity`
    - Action : `Access` Operations
    - Resource : `AWS Resources` & `Services`

## Security Framework
![Alt text](<Screenshot 2023-10-26 at 8.06.11 AM.png>)

## Human Users
- Root User (Super User)
    - created by AWS
    - Owns all the privileges (roles and policies)
    - The `account for billing and payment`
    - `루트 유저로 무엇을 하려고 하면 안된다.` -> `IAM 유저로만 작업 해야함`
- IAM Users (Individual Users)
    - Created `by the root user`
    - Owns those privileges to be explicitly granted by the root user
- Groups
    - A group of IAM users that share `the common set of privileges`

## AWS Services
![Alt text](<Screenshot 2023-10-26 at 8.09.11 AM.png>)

## AWS Resources
![Alt text](<Screenshot 2023-10-26 at 8.10.00 AM.png>)
> 이러한 것들을 IAM에서 퍼미션으로 관리

## Identity (User) Management : `IAM User Registration`
1. AWS Account (Root) `Creation`
2. Root User `Sign-In`
3. Go to IAM Dashboard
4. IAM User : Registration
5. Authorization : Permissions for IAM User
6. Create User
7. Access Key & Secret Key 발급
    - csv, 메일 등 다양하게 발급 받을 수 있음
8. IAM Dashboard의 Users 창에서 퍼미션 관리 가능

## Identity (User) Management : `User Group Registration`
1. Create New Group (대쉬보드에서)
2. Group name설정
3. Attach Policy 
4. Review -> Create group (최종)
5. Dashboard의 Groups에서 관리 가능

## Identity (User) Management : `Authentication`
1. Access Type
![Alt text](<Screenshot 2023-10-26 at 8.21.54 AM.png>)
2. IAM User Sign-in
3. Web Console : Aws Services
4. IAM 대쉬보드 에서 관리 가능

![Alt text](<Screenshot 2023-10-26 at 8.23.29 AM.png>)
![Alt text](<Screenshot 2023-10-26 at 8.23.42 AM.png>)
![Alt text](<Screenshot 2023-10-26 at 8.23.48 AM.png>)
> 이런식으로 코드 상에서 사용 가능

## Authorization
![Alt text](<Screenshot 2023-10-26 at 12.22.36 PM.png>)
> 플랫폼을 공부할때는 전체적으로 공부하고 필요한 것을 세부적으로 해야함.
- Access `Policies` (Rules)
- Access `Control` (Runtime System)
![Alt text](<Screenshot 2023-10-26 at 12.24.16 PM.png>)

# AWS IAM (Identity and Access Management) : `Authorization` (part 1 : Attach Policy to Identity)

## Permission & Policy
- Permission
    - A single Instance of Access Rule
    - Rule : (`Identity`, `Actions` on Resource, `Resource`)
- Policy
    - 퍼미션들의 집합
        - Permission : (?,Action,Resource)
        - Attached to IAM Identity
        ![Alt text](<Screenshot 2023-10-26 at 12.26.13 PM.png>)

### Policy
- AWS Managed Policies 
    - AWS가 만들어놓은 `흔히 사용되는 케이스`
    - ARN
- Customer Managed Policies
    - Policies created by IAM users as AWS Resources with ARNs
- Inline Policies
    - No ARNs
    - Policies embedded in IAM Users
![Alt text](<Screenshot 2023-10-26 at 12.32.33 PM.png>)

## Access Management : Permissions & Policies Creation
![Alt text](<Screenshot 2023-10-26 at 12.35.08 PM.png>)
> 실습 때 만들어 볼 것

## Attach Policy to User Group
- Policy 만든 것을 그룹에 권한에 추가 가능

## Attach Policy to IAM User
- 그룹이 가지고 있는 권한을 줄 수 있고
- 개별적으로 또 다른 Policy도 부여할 수 있다.

> 강의자료가 너무 오래돼서 자세한 건 실습을 통해 하기

# AWS IAM (Identity and Access Management) : `Authorization` (part 2 : Attach Policy to AWS Service) `Role`
![Alt text](<Screenshot 2023-10-29 at 9.34.43 PM.png>)

## IAM Identity : Users vs AWS Service
![Alt text](<Screenshot 2023-10-29 at 9.36.50 PM.png>)
- Users : Identity 에 대한 퍼미션은 파란색
- AWS Service : AWS Service 에 대한 것은 빨간색

## Role
![Alt text](<Screenshot 2023-10-29 at 9.42.44 PM.png>)
- Role는 Identity가 아닌 AWS Service에 권한을 주기 위해 만든 것.
- 즉 권한을 가지는 주체가 AWS Service라고 생각하면 됨

## Role For EC2
- EC2에게 S3를 Full Access 할 수 있는 퍼미션을 주는 것도 가능
![Alt text](<Screenshot 2023-10-29 at 9.47.54 PM.png>)
- 대표적으로 AWS Service는 다음과 같이 크게 3가지로 나뉘어짐

## 방법 (Role creation)
1. Role creation 
2. AWS Service 중 EC2 선택
3. Choose Permission Policy
    - AWS 가 기본적을 만들어놓은 것들도 있음
    - AmazonS3FullAccess 선택
4. Name 설정 
5. Create Role
6. 결과화면 (Review)
    ![Alt text](<Screenshot 2023-10-29 at 9.50.25 PM.png>)
    ![Alt text](<Screenshot 2023-10-29 at 9.50.50 PM.png>)

## EC2 Instance : Attach Role
1. Instances에서 권한을 줄 해당 EC2 선택
2. Instance Setting에 Attach/Replace IAM Role 선택
3. 아까 만들어 놓은 Role 선택 후 Apply
4. 성공 메시지
5. 결과 화면
    ![Alt text](<Screenshot 2023-10-29 at 9.53.38 PM.png>)
> 장점 : 아이디 패스워드 없이 서버에게 퍼미션을 줄 수 있음

## Role For `Rambda`
1. Create Policy for Rambda
2. Select Service
    - ex) IoT에 대한 서비스 와 액션 선택
3. Select Resources
    - All resources 선택함
4. Name, Review & Create
5. Create Role
6. AWS Service로 람다 선택
7. 만들어놨던 Policy선택
8. Create Role

## Lambda : Role
1. Function name 
2. Runtime 엔진 설정
3. Role 설정
4. Create Lambda function

## Role for `IoT Rules` to Invoke S3
1. Create Rule
2. Rule에 연결될 서비스 선택 (S3 선택)
3. Action 선택 (S3 버킷, Key 등 선택)
4. create role 선택
    - 이전과의 차이는 자동적으로 Role이 생성된다. (AWS가 알아서 생성)
5. Add Action



