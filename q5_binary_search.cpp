#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int head = 0;
        int tail = nums.size()-1;

        while (head < tail){
            if (nums[(head+tail)/2] == target){
                cout<<(head+tail)/2<<endl;
                return (head+tail)/2;
            }
            else if (nums[(head+tail)/2] < target){
                head = (head+tail)/2 + 1;
            }
            else{
                tail = (head+tail)/2 -1;
            }
        }

        if (nums[(head+tail)/2] != target){
            cout<<"-1"<<endl;
            return -1;
        }
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