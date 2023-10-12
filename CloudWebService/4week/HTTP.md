# HTTP: Hypertext & URI

### Contents
- Hypertext & Hypermedia
- Resources
- Overview
- Methods
- Status Codes
- Header Fields
- Summary
---

### Hypertext & Hypermedia
- 전통적인 Text Documents
    - A `Sequence` of Text Blocks
    - `Single Thread` of Writing
 - `Hypertext Documents`
    - `A Network of Text Blocks connected by Hyperlinks (e.g., URLs)`
    - `Multiple Threads` of Writing
![Alt text](<Screenshot 2023-10-12 at 6.09.43 PM.png>)
![Alt text](<Screenshot 2023-10-12 at 6.09.55 PM.png>)
![Alt text](<Screenshot 2023-10-12 at 6.11.22 PM.png>)
> 이런 식으로 코드화 되어 있는 것을 웹 브라우저가 시각화해서 우리가 보는 웹사이트 형태로 만들어짐
>> Hyperlink를 클릭하면 또 다른 HTML 문서로 이동
![Alt text](<Screenshot 2023-10-12 at 6.11.35 PM.png>)

### Resources
- Files on a computer
    - ID : Full Path Name.
        - E.g., C:/users/gildong/pictures/121.png
    - Can be referenced `inside its host computer`
- 인터넷의 `Web Resources` 로 확장 됨
    - ID : URL, URI, or IRI
        - E.g., http://www.rws.ac.kr/pictures/gildong.png
        - 다른 컴퓨터에서도 ID를 통해 접근 가능
    - Program-Accessible Objects (data files or program files) to be referenced and accessed from any machine in the Internet
- `Absract Resources in Semantic Web`
    - ID : URL, URI, or IRI
    - In addition to retrievable objects, `Non-accessible ones` such as human beings and corporations in the real world are also included.

### Resource Management (Storage)
- `Services` : Running Processes
    - To store resources
    - To allow other services to access resources
- `File Systems` on a host computer : Files
    - Can serve requests only from its host computer
- `Web Servers` in the Internet : Web Resources
    - Can serve requests from any computers in the Internet
> 웹 서버는 리퀘스트를 프로세싱 하고 모든 자료는 파일시스템에 있음.
![Alt text](<Screenshot 2023-10-12 at 6.39.39 PM.png>)

### Uniform Resource Identifiers (URI) : Hyperlinks
- 인터넷에 있는 모든 resource들을 구분할 수 있게 하는 ID 체계
- Identifier for a Resource to specify
    - `Name` of the resource
    - `Protocol` to access the resource (프로토콜 까지 포함)
- Types of URIs
    - `URL` : Uniform Resource Locators `(Web Addresses)`
    - `URN` : Uniform Resource Names
    - `IRI` : Internationalized Resource Identifiers. May Contain characters from `Unicode`. (다국어가 resource identifier에 포함될 수 있다.)


    