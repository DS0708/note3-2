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

### Structure of URI
![Alt text](<Screenshot 2023-10-12 at 10.19.56 PM.png>)
- user information, query, fragment : 는 보내는 시점에 따라 `Dynamic`
- Scheme : http, ftp, mailto, or file
- Hierarchical part starting with "//"
    - Authority Part
        - Optional Authentication Part : User Name & Password
        - Hostname : domain name or IP address
        - Optional Port Number (8080)
    - Path name
![Alt text](<Screenshot 2023-10-12 at 10.24.04 PM.png>)

### Path in URI vs Physical path
- URI 의 Path와 실제 서버의 Physical path는 다르기 때문에 매핑 테이블이 존재 해야 한다. 
- 실제 Physical path 를 사용하면 서버에 주소를 옮기면 다 바꿔야 한다.
![Alt text](<Screenshot 2023-10-12 at 10.27.29 PM.png>)

### URI: Path, Query, & Fragment
- Logical Information
    - In a URI, Path, Query, and Fragment are `logical information`
- Logical Mapping
    - The Path in a URI does not exactly correspond to that in the local file system(physical path)
- Preparation for Various Extensions
    - The query and fragment are resource-specific and must be processed by resource management services such as web servers -> `query와 fragment를 통해 프로그램의 argument 같은 것을 전달할 수 있다.`

### HTTP : Overview
- Foundation for data communication for `World Wide Web` (Internet)
- `Generic & Stateless` Application-level Protocol
    - for distributed, collaborative, hypermedia information systems
    - Can be used for `Client/Server Model-based other applications` with requests, responses, error codes, and headers
- `TCP/IP based communication protocol` to deliver data : HTML files, Image files

### Data for Http : Web Resources
- HTML documents
- ASCII text documents
- Preformatted documents : PDF files
- Images : PNG, JPEG, GIF, ...
- Video : MPEG
- Script programs : VRML, JAVA
> 합의된 doucuments들은 resources가 될 수 있음.

### Client/Server Model for HTTP
![Alt text](<Screenshot 2023-10-12 at 10.46.36 PM.png>)

### HTTP Message의 구조
- Start Line : `Request Line` or `Status Line`
    - Request Line : 'GET/test.html HTTP/1.1'
    - Status Line: 'Http/1.1 200 OK'
- Zero or more `Header Fields` followed by CRLF
    - Header Types : `General, Request, Response, Entity`
- An `empty line` (line with no contents)
    - `Header fields의 끝`
- A `Message Body`, Optionally

### Request Message
![Alt text](<Screenshot 2023-10-12 at 10.52.17 PM.png>)
- User-Agent -> Web Browser
- 첫줄은 Request Line
- 웹 브라우저가 URI를 파싱하여 HTTP 형식에 맞는 Document로 만들어 요청

### Response Message
![Alt text](<Screenshot 2023-10-12 at 10.53.57 PM.png>)
- 첫줄은 Status Line 

### HTTP : Methods
- `GET`
    - Retrieve the `content of a resource` from a web server by `specifying the URI`
    ![Alt text](<Screenshot 2023-10-12 at 10.59.35 PM.png>)
- HEAD
- `POST`
    - `Update the content of a resource` in a web server by sending new content
    ![Alt text](<Screenshot 2023-10-12 at 10.59.21 PM.png>)
- `PUT`
    - `Create a resource with the specified URI` and the content in the message body in a web server
    ![Alt text](<Screenshot 2023-10-12 at 11.01.15 PM.png>)
- `DELETE`
    - `Delete a resource `in a web server by specifying the URI.
    ![Alt text](<Screenshot 2023-10-12 at 11.02.11 PM.png>)
- CONNECT
- OPTIONS
- TRACE
![Alt text](<Screenshot 2023-10-12 at 10.56.37 PM.png>)
> HTTP 프로토콜을 이해하는 것은 8가지의 Methods를 이해하는 것
>> major 4가지를 이해 하는 것이 중요

### HTTP : Status codes
- `100 ~ 199 : Informational`
    - E.g., the request is received
- `200 ~ 299 : Success`
    - The request is successfully served.
- `300 ~ 399` : Redirection
    - 경로가 잘못 되었음
- `400 ~ 499` : Client Error
    - The request contains errors or cannot be finished
- `500 ~ 599` : Server Error
    - The server failed to process the request

### `Commonly Used Status Codes`
- 200 OK
    - The request is OK
- 201 Created
    - put에 대한 response
    - A new resource is created
- 301 Moved Permanently
    - The requested resource has moved to a new URL
- 303 See Other
    - The requested resource can be found under a different URL
- 400 Bad Request
    - The server did not understand the request
- 401 Unauthorized
    - The requested resource needs a username and a password
- 402 Payment Required
- 403 Forbidden
- 404 Not found

### Header Fields
- `General Header` : Used for both requests and responses
    - `Connection` : Whether the network communication is closed after the completion of a response or not
        - `Connection : close or Connection : Keep-alive`
- `Client Request Header` : Only for requests
    - `Host` : Specify the server computer name (or IP) and the port number
        - Host:www.konkuk.ac.kr:8080
    - `Accept` : Specify media types acceptable for the response
        - `Accept : text/plain, text/html`
    - `Accept-Charset` : Specify the character sets acceptable for the response
        - `Accept_Charset : iso-8859-5, unicode-1-1`
    - `Accept-Encoding` : Specify the content codings acceptable for the response
        - Accept-Encoding : compress, gzip
        - 서버가 압축해서 보낼때 이것들만 처리할 수 있다는 것을 나타냄
    - Accept-Language
        - `Acceot-Language : en,kr`
        - 그거 보내면 우리한테 도움이 안된다는 것을 공지
        - 서버에서는 가급적이면 영어나 한국어로 공지 한다.
    ![Alt text](<Screenshot 2023-10-13 at 12.05.48 AM.png>)
- `Server Response Header` : Only for responses
    - `Location` 
        - Redirect the client to the other URL for the resource
        - `Location:http://www.kku.ac.kr/test.html`
        - 요청한 resource가 다음 위치로 이동되었으니 여기를 방문해라 정도의 의미
    - `Server`
        - Specify the server software
        - `Server:Apache/2.2.14(Win32)`
- `Entity Header` : For meta information about the message body
    - `Allow` 
        - Specify the set of methods supported by the resource
        - `Allow : Get, HEAD, PUT`
        - client한테 이런 요청만 처리가 가능하다는 것을 알려줌
    - `Content-Encoding`
        - message body의 압축 type을 Specify
        - `Content-Encoding:gzip`
    - `Content-Language`
        - message body 에 있는 자연어를 명시
        - `Content-Language:en.kr`
    - Content-Length
        - message body의 사이즈를 나타냄
        - `Content-Length:88`
    - Last-Modified
        - 리소스가 수정된 날짜 시간을 Specify
        - `Last-Modified:Tue, 15 Nov 1994 12:45:26 GMT`
    - Content-Location
        - Specify the location of the resource whose content is in the message body
        - `Content-Location : http://www.konkuk.ac.kr/test.html`
    - Content-Type
        - Specify the media type of the message body
        - `Content-Type:text/html`

### Summary
- Hypertext & Hypermedia
    - 하이퍼 링크에 의해 연결된 Text blocks(pages) or multimedia object들의 `Network`
- Web Resource
    - A variety of documents or objects
- URIs
    - Name & Address Protocol for web resources
- HTTP
    - URIs를 support하기 위해 디자인된 Word Wide Web(Internet)을 위한 데이터 전송 프로토콜
    - Generic & Stateless
- HTTP의 Componenets
    - Methods, Status codes, Header Fields

