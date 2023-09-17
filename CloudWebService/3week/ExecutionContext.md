# Execution Context

`Execution Context` : the `runtime environment`(object) where and when a function is executed.

### Types of Execution Context : Object
- `Object Context`. When a function is used as a method
- `Constructor Context`. When a function is used as `object constructor.`
- `Module Context`. When a module is excuted (imported) by the `require function`
- `Global Context`(called global). When a function is executed outside objects

### 1. Object Context (1/2)
```javascript
x = 119; // global variable

function foo(){ 
    var x = 112; 
    console.log(x, this.x, global.x);
    }

var y = {
    x : 113,
    m : foo,        //this == y
    bar : function(){return(this.x+x);}
};

var z = {
    x : 'hello',
    bla : foo
};

y.m();  // 112, 113, 119
z.bla(); // 112, 'hello', 119

y.bar(); // 113 + 119
```
> this는 method function을 실행하는 object

### 1. Object Context (2/2) : Nested Objects
```javascript
var x = 10;
function foo(){
    console.log(this.x);
};

var obj = {
    x : 11,
    y : {
        x : 12,
        f2 : foo
    },
    f1 : foo
};

obj.y.f2();     // 12
obj.f1();   //11
```

### 2. Constructor Context
```javascript
function Person(){
    this.x = 10;
    this.y = 5;
    console.log('Person instantiated');
}

var person1 = new Person();
person1.z = 777     // a new property is added
var person2 = new Person();
var person3 = Person(); // res == undefined

console.log(person1);
console.log(person2);
console.log(person3);
```

실행결과 
```Person instantiated
Person instantiated
Person instantiated
Person { x: 10, y: 5, z: 777 }
Person { x: 10, y: 5 }
undefined
```

> The `this` keyword in a constructor is used to refer to the `object to be created in the future.`

### 3. Module Context
```javascript
// File : m3.js
this.x = 10;
function foo () {
    console.log('foo');
}
function bar() {
    console.log('bar');
}
//this.y = foo;

module.exports.z = bar;
```

```javascript
//File : main.js
var mc = require('./m3');
console.log(mc);
```

```
실행결과 
{ x: 10, z: [Function: bar] }
```
> this.y 주석 처리를 안했을 경우에 { x: 10, y: [Function: foo], z: [Function: bar] } 으로 결과가 나오는 것으로 보아, `this == module.exports`

### 4. Global Context 
```javascript
x  = 119;
function foo(){
    var x = 112;
    console.log(x,this.x,global.x);
}
var y = {
    x : 113,
    m : foo,
    bar : function(){return(this.x+x);}
};
y.m();
foo();
```
```
실행결과
112 113 119
112 119 119
```
> function foo를 실행 시키는 주체인 Global 이 `this` 가 된다.

### Shared Access to Variables
- Function Closure
    - Inner functions share local variables in enclosing outer functions
- Execution Context
    - `Use of this`
    - Functions that belong to the same object can access the data properties of the object by this








