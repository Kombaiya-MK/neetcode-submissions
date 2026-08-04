public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for(int i=0;i<nums.Length;i++){
            for(int j=i+1;j<nums.Length;j++){
                int expect = nums[i]+nums[j];
                if(expect == target){
                    return new int[]{i,j};
                }
                else{
                    continue;
                }
            }
        }
        return new int[]{0,0};

    }
}
