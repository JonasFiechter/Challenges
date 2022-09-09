/*
Find Number of Digits in Number

Create a function that will return an integer number corresponding 
to the amount of digits in the given integer num.
*/

function find_digits(number_) {
    if (typeof(number_) !== 'number') {
        return -1
    }
    return String(number_).length
}

const t = ['a', 'b', 'c', 'c']

console.log(t.indexOf('c'))
// console.log(find_digits('32'))