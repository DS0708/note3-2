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