/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    x=x.toString()
    var n=""
    for (var i =x.length-1;i>=0;i-- ){
        n+=x[i]
    }
    if(x==n){
        return true
    }else{
        return false
    }
};
