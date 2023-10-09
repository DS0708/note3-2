# JavaScript Basics

- Data Types
    - Number, Boolean, String, Date, Object, Array
- Variables
    - Typeless
    - vars
- Operators
    - ==,===,Object.is() `===은 진짜 같은 놈만 true`
    - !=
    - '>',>=,<,<= , ||, &&
- Control Statements
    - if-else, switch-case, for, for-in, while, break, continue


### Object & Array
- Object (JSON) : key/value
```javascript
var obj1 = {first:'John',last : 'Smith'}
console.log(obj1);
```
- Array 
```javascript
var obj1 = {a:'abc',b:'def',c:'ghi'};
for(let x in obj1) {console.log(obj1[x])};

var obj2 = [10,20,3,4,5]
for(let i=0; i<obj2.length; i++) {console.log(obj2[i])};
```

### Functions
```javascript
function add (a,b) {return(a+b);}
var plus  = add;
var minus = function (a,b) {return(a-b);}
function calc (op,a,b){return op(a,b);}

console.log(calc(plus,1,2));
console.log(calc(minus,2,1));
```

### Error Handling
- Error가 생기면 Error라는 객체로 리턴
- Java와 같이 try catch 지원
```javascript
var foo = undefined;
try{
    if(foo==undefined) throw new Error('Undefined Function');
    else foo(1,2);
    console.log('after foo');
}catch (err){
    console.log(err);
}finally {
    console.log('finally');
}
console.log('finish');
```