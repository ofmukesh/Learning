class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        s=purchaseAmount//10
        n=s*10
        l=purchaseAmount-n
        if l>4:
            return 100-(n+10)
        else:
            return 100-n
