def cal(last1,last2,opr):
    if opr=="+":
        return last1+last2
    elif opr=="-":
        return last2-last1
    elif opr=="*":
        return last1*last2
    elif opr=="/":
        return int(last2/last1)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+','-','/','*']
        stack=[]
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                last1=stack.pop(-1)
                last2=stack.pop(-1)
                calculation=cal(last1,last2,token)
                stack.append(calculation)
        print(stack)
        return stack[0]
