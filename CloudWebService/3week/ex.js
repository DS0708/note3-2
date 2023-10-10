function Person(){
    this.x = 10;
    this.y = 5;
    console.log('Person instantiated');
}

var person1 = new Person();
person1.z = 777     // a new property is added
var person2 = new Person();
var person3 = Person(); // res == undefined

//var person4 = new persone3();

console.log(person1);
console.log(person2);
console.log(person3);
//console.log(person4);
