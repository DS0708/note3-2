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