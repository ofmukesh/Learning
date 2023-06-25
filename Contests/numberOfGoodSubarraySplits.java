class Solution {
    public int numberOfGoodSubarraySplits(int[] nums) {
        
        List<Integer> lit=new ArrayList<>();
        
        long mod3=1000000007L;
        int len=nums.length;
        
        
        for(int i=0;i<len;i++){
            
            if(nums[i]==1)
                lit.add(i);
        }
        
        long ans=0;
        
        if(lit.size()>0)
            ans=1;
        
        long dpans=ans;
        
        for(int i=lit.size()-2;i>=0;i--){
            
            int leftInd=lit.get(i);
            int rightInd=lit.get(i+1);
            
            int df=rightInd-leftInd;
            long mul=((long)df%mod3*(long)dpans%mod3)%mod3;
            dpans=mul;
            ans=mul;
        }
        
        return (int)ans;
        
    }
}
