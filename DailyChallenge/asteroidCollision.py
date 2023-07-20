class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i=0
        while i < len(asteroids)-1 and len(asteroids)!=1:
            # if i'th asteroid going to right and i'th+1 asteroid coming to left side 
            # eg. i'th ----> <----- i'th+1
            if 0<asteroids[i] and 0>asteroids[i+1]: 
                num1=abs(asteroids[i])
                num2=abs(asteroids[i+1])
                # destroy min size asteroid or destory both asteroids if both have same size 
                if num1<num2: 
                    asteroids.pop(i)
                elif num2<num1:
                    asteroids.pop(i+1)
                else:
                    asteroids.pop(i)
                    asteroids.pop(i)
                i-=1 if i!=0 else i
            else:
                i+=1
        return asteroids
