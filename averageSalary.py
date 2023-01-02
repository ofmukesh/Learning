class Solution:
    def average(self, salary: List[int]) -> float:
        mini=min(salary)
        maxi=max(salary)
        salary.remove(mini)
        salary.remove(maxi)
        s=sum(salary)
        return (s/len(salary))
