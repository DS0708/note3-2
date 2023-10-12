# Node.JS : Asynchronous Programming

- Node.JS를 하기 위해 Asynchronous Programming 개념을 정확히 이해할 필요가 있다.

---
### `Synchronous` Programming (Single Player)
- 알고리즘 (Flowchart)
- Control Sequence
    - 실행의 순서
    - Statements의 순서
    - Calling & Called Functions
- Data (Result) `Dependency`
    - Later execution requires `some results from earlier execution`

### `Synchronous` Programming (Multiple Players)
- Synchronized Collaboration
![Alt text](<Screenshot 2023-10-12 at 12.58.15 PM.png>)

> 오른쪽 worker가 작동이 안되면 서버가 마비될 수도 있다.

### `Asynchronous` Programming (Multiple Players)
- Callback Approach (완전 비동기적)
![Alt text](<Screenshot 2023-10-12 at 1.02.59 PM.png>)
> 중앙에 있는 서버는 result를 기다리지 않고 별도의 스레드를 만들어서 처리한다. 

- Promise Approach (비동기적이지만 약간 Synchronous하기도 함)
![Alt text](<Screenshot 2023-10-12 at 1.06.30 PM.png>)

> Site A는 request가 들어 오면 일단 Promise를 만들고 return(Synchronous)

> 그리고 Site A는 처리하여 Promise에 써줌

> 오른쪽 서버에서는 Promise가 필요할때 접근하여 사용

### `Asynchronous Programming` in Node.JS : `Callback Functions`
- Asynchronous I/O, Remote Service Access에 사용
- Site A에 query를 보내고 별도의 Callback을 만들어 Block되지 않고 처리하는 방식
- 이 Callback을 어떻게 사용하는가에 대하여 공부하는 게 중요함.
- Example : How to read and process a File
![Alt text](<Screenshot 2023-10-12 at 1.14.03 PM.png>)
    - Synchronous : readFileSync의 결과(response)를 받을때 까지 `Blocking` -> 느리다 `(Single Thread)`
    - ASynchronous : Callback function cb를 Argument로 넘겨준다. `(Multi thread)`

### Callback-based Asynchronous Programming
- Callback function의 return value는 Error 아니면 result이다.
- 독립적인 스레드를 하나 더 만들어서 처리한다. `Concurrency`
- Error, data 두 개의 Argumnet를 취한다. 
- Callback function안에 result를 프로세스 하는 코드를 넣어준다. 
- Callback 함수로 Ordering을 만들 수 있다. (별도의 강의)