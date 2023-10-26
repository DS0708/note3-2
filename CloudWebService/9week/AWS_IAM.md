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



