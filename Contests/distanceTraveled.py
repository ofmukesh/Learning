def countKM(ans,main,add):
    if main>=5 and add>0:
        main-=4
        add-=1
        ans+=50
        return countKM(ans,main,add)
    elif (main>=5 and add<=0) or main<5:
        ans+=main*10
        return ans

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank<5:
            return mainTank*10
        return countKM(0,mainTank,additionalTank)
