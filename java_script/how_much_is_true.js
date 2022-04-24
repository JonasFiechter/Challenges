/* 
How Much is True?
Create a function which returns the number of true values there are in an array.

Examples
countTrue([true, false, false, true, false]) ➞ 2

countTrue([false, false, false, false]) ➞ 0

countTrue([]) ➞ 0
Notes
Return 0 if given an empty array.
All array items are of the type bool (true or false).
*/


function count_true(arr=[]) {
    let count = 0
    for (const i of arr) {
        if (i) {count += 1}
    }
    return count
}

console.log(count_true([false, false, false, false]))