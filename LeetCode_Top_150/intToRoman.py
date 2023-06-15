class Solution:
    def intToRoman(self, num: int) -> str:
        dic={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        
        l=len(str(num))-1
        ans=""
        for i,k in enumerate(str(num)):
            ele=(10**(l-i))*int(k)
            print(ele)
            if ele==0:
                continue
            elif dic.get(ele)!=None:
                ans+=dic[ele]
            else:
                m=10**(len(str(ele))-1)
                temp=""
                while ele!=0:
                    if dic.get(ele):
                        temp=dic[ele]+temp
                        break
                    else:
                        temp=dic[m]+temp
                        ele-=m
                ans+=temp

        return ans


    
