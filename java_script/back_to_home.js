/* 
Back to Home?

Mubashir has started his journey from home. Given a string of directions 
(N=North, W=West, S=South, E=East), he will walk for one minute in each direction. 
Determine whether a set of directions will lead him back to the starting position 
or not.
Examples

backToHome("EEWE") ➞ false

backToHome("NENESSWW") ➞ true

backToHome("NEESSW") ➞ false
*/


function back_to_home(coordinates) {
    let x = 0
    let y = 0
    coordinates = coordinates.toUpperCase()
    
    for (let i = 0; i < coordinates.length; i++) {
        if (coordinates[i] === 'N') { x++ }
        else if (coordinates[i] === 'S') { x-- }
        else if (coordinates[i] === 'E') { y++ }
        else if (coordinates[i] === 'W') { y-- }
    }

    if (x === 0 && y === 0) {
        return true
    } else { return false }
}

console.log(back_to_home('NENESSWW'))