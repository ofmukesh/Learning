/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var ans=[]
    for (var i =0;i<nums.length;i++ ){
        for (var j = 0;j<nums.length-1;j++ ){
            if( i!=j ){
                var sum = nums[i]+nums[j];
                if (sum==target){
                    ans.push(i)
                    ans.push(j)
                    i=nums.length+1
                    break;
                }
            }
        }
    }
    return ans
};
