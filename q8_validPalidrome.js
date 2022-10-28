/**
 * @param {string} s
 * @return {boolean}
 */


// you can store function as a variable in javascript
var isPalindrome = function (s) {

    // remove all non-alphanumeric characters
    // replace space with nothing
    var str = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase().replace(" ", "");
    
    // maintain front and back pointers, traverse towards the middle
    var front = 0
    var back = str.length - 1;

    // hard code if string is empty, return true
    if (s == "") { return true };


    // STOP CONDITION for front & back pointer:
    // since both index are integer number, just stop the loop when front is greater than back
    while (front < back) {

        // access and compare the character at front and back index, if they are different return false
        if (str[front] != str[back]) {
            return false;
        }

        // increment
        front++;
        back--;
    }
    return true;
};
// console.log(isPalindrome(" "));
