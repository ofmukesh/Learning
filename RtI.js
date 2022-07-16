/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var obj = {
        I:1,
        V:5,
        X:10,
        L:50,
        C:100,
        D:500,
        M:1000,
        IV:4,
        IX:9,
        XL:40,
        XC:90,
        CD:400,
        CM:900
    }
    var ans=0
    for (var i =0;i<s.length;i++ ){
        if (s[i]=="I"){
            if (s[i+1]=="V"){
                ans+=obj.IV
                i++
            }else if(s[i+1]=="X"){
                ans+=obj.IX
                i++
            }else{
                ans+=obj.I
            }
        }else if (s[i]=="X"){
            if (s[i+1]=="L"){
                ans+=obj.XL
                i++
            }else if(s[i+1]=="C"){
                ans+=obj.XC
                i++
            }else{
                ans+=obj.X
            }
        }else if (s[i]=="C"){
            if (s[i+1]=="D"){
                ans+=obj.CD
                i++
            }else if(s[i+1]=="M"){
                ans+=obj.CM
                i++
            }else{
                ans+=obj.C
            }
        }else{
            ans+=obj[s[i]]
        }
    }
        return ans
};
