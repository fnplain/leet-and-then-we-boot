using System.Collections.Generic;

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        Dictionary<int, int> map = new Dictionary<int, int>();
        int[] answer;

        for (int i = 0; i < nums.Length; i++){

            int current = nums[i];
            int x = target - current;

            if(map.ContainsKey(x))
            {
                return new int[] {map[x], i};
            }
            map[current] = i;

        }
        return null;
    }
}
