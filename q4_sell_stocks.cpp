#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {

        /*
            1x linear scan
            - keep track of smallest value in the array so far -> BUY LOW
            - is today a high price? -> aka. SELL HIGH

        */

        // int low_so_far = INT32_MAX;
        int s = *min_element(prices.begin(), prices.end());
        cout << s << endl;

        int minValue = INT_MAX;
        int maxProfitValue = 0;
        // complexity of O(n)
        for (auto i : prices)
        {
            // update smallest value
            if (i <= minValue)
            {
                minValue = i;
            }


            else
            {
                // update max profit value
                // currentProfit = current value at i - minValue so far
                // aka. is today a high price?
                // int curProfit = i - minValue;
                if (i-minValue > maxProfitValue)
                {
                    maxProfitValue = i-minValue;
                }
            }
        }
        return maxProfitValue;
    }
};

int main()
{
    Solution s;

    vector<int> prices = {7, 6, 9, 3, 1};
    s.maxProfit(prices);

    return 0;
}



// #include <iostream>
// #include <string>
// #include <vector>
// #include <algorithm>
// using namespace std;

// class Solution
// {
// public:
//     int maxProfit(vector<int> &prices)
//     {

//         /*
//             1x linear scan
//             - keep track of smallest value in the array so far -> BUY LOW
//             - is today a high price? -> aka. SELL HIGH

//         */

//         // int low_so_far = INT32_MAX;
//         int s = *min_element(prices.begin(), prices.end());
//         cout << s << endl;

//         int minValue = INT_MAX;
//         int maxProfitValue = 0;
//         // complexity of O(n)
//         for (auto i : prices)
//         {
//             // update smallest value
//             if (i <= minValue)
//             {
//                 minValue = i;
//             }


//             else
//             {
//                 // update max profit value
//                 // currentProfit = current value at i - minValue so far
//                 // aka. is today a high price?
//                 // int curProfit = i - minValue;
//                 if (i-minValue > maxProfitValue)
//                 {
//                     maxProfitValue = i-minValue;
//                 }
//             }
//         }
//         return maxProfitValue;
//     }
// };

// int main()
// {
//     Solution s;

//     vector<int> prices = {7, 6, 9, 3, 1};
//     s.maxProfit(prices);

//     return 0;
// }