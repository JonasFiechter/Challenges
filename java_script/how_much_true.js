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

function how_much_is_true(array) {
    let x = 0
    for (let i = 0; i < array.length; i++) {
        if (typeof(array[i]) !== typeof(true)) {
            return -1
        } else if (array[i] == true) { x++ }
    } return x
}

console.log(how_much_is_true([true, false, false, true]))