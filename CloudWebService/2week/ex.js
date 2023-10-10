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