class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left, mid = 0;
        int right = nums.size() - 1;

        while(mid <= right)
        {
            if (nums[mid] == 0)
            {
                swap(nums[mid], nums[left]);
                left += 1;
                mid += 1;
            }
            else if (nums[mid] == 1)
            {
                mid += 1;
            }
            else {
                swap(nums[right], nums[mid]);
                right -= 1;
            }
        }
    }
};