/*Find the Smallest and Biggest Numbers

Create a function that takes an array of numbers and return both the 
minimum and maximum numbers, in that order.*/

function find_min_max(array) {
    let min = array[0]
    let max = array[0]
    for (let i = 0; i < array.length; i++) {
        if (array[i] < min) { min = array[i] }
        else if (array[i] > max) { max = array[i] }
    }
    return ([min, max])
}

console.log(find_min_max([12, 23, 4, 5, 6, 7, 1, 2]))