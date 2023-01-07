class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=0;
        for customer in accounts:
            balance=sum(customer);
            wealth=max(wealth,balance);
        return wealth ;
