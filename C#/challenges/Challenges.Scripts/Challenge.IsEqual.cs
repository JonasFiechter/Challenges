/*
Are the Numbers Equal?
Create a function that takes two integers and checks if they are equal.

Examples
IsEqual(5, 6) ➞ false

IsEqual(1, 1) ➞ true

IsEqual(36, 35) ➞ false
Notes
N/A
*/

namespace challenges.Challenges.Scripts
{
    public class ChallengeIsEqual
    {
        public bool IsEqual(int x, int y)
        {
            if (x == y)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}