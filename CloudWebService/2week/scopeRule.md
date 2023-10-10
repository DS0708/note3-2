# JavaScript Scope Rule

## Variable Name Resolution
- `inner most matching variable`

```javascript
var x = 1;
console.log('1.x=',x);

function foo(){
    var x = 2;
    var y = 3;
    function bar(){
        var y = 4;
        console.log('3.x=',x,'y=',y);
    }
    bar();
}

foo();

console.log('last.x=',x);
```

## Static & Lexical
- `Function-level Scope` (Local Scope)
    - function안에 선언된 Variables
- `Module (File)-level Scope `(Local Scope)
    - 한 파일에 의해 선언된 Variables
- `Global Scope`
    - `global` 키워드를 통해 언제 어디서든 접근 가능
    - Variables created without declaration(Var 쓸 필요 없음)
- `Block-level Scope`
    - let
    - const

![Alt text](<Screenshot 2023-10-10 at 8.52.18 AM.png>)
> 오른쪽이 먼저 실행될 경우 에러 발생 왜냐하면 Typeless 언어 이기 때문이다.

## Function-Scope vs Module-Scope
- Variable 선언
    - Global 은 declaration없이 생성 가능
    - Local to a module, a function or a block

```javascript
var mv1 = 1; //module variable
gv1 = 2; //global variable

function foo(){
    gv2 = 4; //global variable
}

foo();

console.log(global.gv1);
console.log(global.gv2);
console.log(gv1);
console.log(gv2);
//console.log(global.mv1); //ERROR
```

## Global Scope
- global 이라는 object의 프로퍼티로 관리된다.
- gv 는 사실 global.gv
- 코드에 존재한다고(선언했다고) 만들어 지는 것이 아니라 값이 Assign될 때 생성된다.
- 권장하는 기능은 아님

## Closure
- Local variables in a function `can outlive the execution lifetime of the function` and be used outside the function
```javascript
var inc;
var dec;
var print;

function create_counter(v){
    var global_counter=v;
    inc = function(w) {global_counter+=w;}
    dec = function(w) {global_counter-=w;}
    print = function() {console.log(global_counter);}
}

create_counter(123);
print();

inc(1);
print();

dec(122);
print();

// 외부의 variable이 참조하고 있는 한 모든 variables은 살아있는다.
```
- global variable과 같은 효과를 낼 수 있음.
    - 프로그래머 만드는 사람이 정확하게 관리할 수 있는 Global variable
- Module Scope : Closure
    - moudle의 Local variables은 모듈 밖에서 접근 가능하지 않지만 사용될 수 는 있다.
    
 ![Alt text](<Screenshot 2023-10-10 at 9.28.57 AM.png>)
