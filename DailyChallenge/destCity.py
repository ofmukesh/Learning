# store the paths in hashmap and find which city have not any path in the hashmap 
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities={}
        for path1,path2 in paths:
            cities[path1]=path2

        for path1,path2 in paths:
            if not cities.get(path2):
                return path2
        
