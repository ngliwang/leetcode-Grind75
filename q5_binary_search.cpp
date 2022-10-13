#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // cout<<target;

        int head = 0;
        int tail = nums.size() - 1;
        int middle = nums.size() / 2;

        int head_val = nums[head];
        int tail_val = nums[tail];
        int middle_val = nums[middle];

        // if size of array is 1 or 0 return -1
        if(nums.size() < 2 && middle_val != target)
        {
            return -1;
        }

        if(nums.size() == 2){
            if(head_val == target){
                return 0;
            }else if(middle_val == target){
                return 1;
            }else if(tail_val == target){
                return 2;
            }else{
                return -1;
            }
        }

        if (middle_val == target){
            return middle;
        }
        
        while(middle_val != target && head != tail){
            if (middle_val > target){
                tail = middle - 1;
            }else{
                head = middle + 1;
            }
            middle = (tail - head) / 2 + head;
            middle_val = nums[middle];
            // cout<<"middle_val: "<<middle_val<<endl;

            if (middle_val == target){
                cout<<"mid index: "<<middle<<endl;
                return middle;
            }else{
                cout<<"index not found"<<endl;
                return -1;
            }

        }

        // if (middle_val == target) {
        //     return middle;
        // }

        // // means that value belongs to the bigger region
        // if (middle_val < target) {
        //     // compute the new head and search there
        //     // +1 because middle has been checked
        //     head = middle + 1;
        //     head_val = nums[head];

        //     middle = (head + tail) / 2;
        //     middle_val = nums[middle];

        //     cout<<"middle value"<<middle_val<<endl;
        // }
        // else{
        //     // compute the tail and search there
        //     tail = middle - 1;

        //     tail_val = nums[tail];

        //     middle = (head + tail) / 2;
        //     middle_val = nums[middle];

        //     cout<<"middle value"<<middle_val<<endl;
        // }


        return 0;
    }
};

int main()
{
    Solution s;

    vector<int> nums = {-1,0,3,5,9,12};
    s.search(nums, 9);
    return 0;
}