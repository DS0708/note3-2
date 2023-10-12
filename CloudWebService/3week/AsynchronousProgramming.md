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

### Promise Object
![Alt text](<Screenshot 2023-10-12 at 5.29.57 PM.png>)
- util.promisify를 통해 promise 객체로 변환 가능
- then 안에 Callback 함수 같은 것을 정의 
- Catch 를 통해 ERROR 처리
- Promise 객체 리턴 
- 실행 순서
![Alt text](<Screenshot 2023-10-12 at 5.29.46 PM.png>)
> ReadFile 이 끝나야 function(text)가 실행될 수 있다. (Asynchronous)

### How to Build `Custom Promise Object`
- 위에는 Util에 있는 Promise를 가져다 쓴 것임
- 그럼 Promise는 어떻게 만들어 질까 ?
![Alt text](<Screenshot 2023-10-12 at 5.32.31 PM.png>)
- Promise 의 Argument로 들어가는 Function
    - resolve : result값 처리
    - reject : Error 처리
- 이러한 구조만 알아두면 거의 모든 객체를 Promise화 시킬 수 있다.
![Alt text](<Screenshot 2023-10-12 at 5.36.44 PM.png>)
- `function cb(err,data) -> Asynchronous Execution`

### Callback vs Promise : Different Objectives
- `Callback function`
    - Contain code `to process result values`
    - The processing of function result is `asynchronously performed in the context of called function`
- `Promise object`
    - Contain code to `confirm the result status` : success or error
    - The processing of function result is `synchronously performed in the context of calling function`
![Alt text](<Screenshot 2023-10-12 at 5.46.40 PM.png>)
> 코드는 Promise가 더 복잡하지만 그만큼 더 유연하게 사용 가능

### `Async&await` (How to execute Asynchronous Functions Synchronously)
- Promise를 선호하는 이유 : Async&await와 같이 사용함으로써 거의 완벽하게 synchronous할 수 있다. 
![Alt text](<Screenshot 2023-10-12 at 5.52.45 PM.png>)
- `code 설명 (only promise)`
![Alt text](<Screenshot 2023-10-12 at 5.54.14 PM.png>)
> 높은 확률로 p3 -> p2 -> p1 순으로 실행된다.
 - `code 설명 (with async & await)`
 ![Alt text](<Screenshot 2023-10-12 at 5.58.52 PM.png>)
 > 요구 사항은 Promise로 구현되어야한다.
