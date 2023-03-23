/*
Less Than 100?
Given two numbers, return true if the sum of both numbers is less than 100. 
Otherwise return false.

Examples
lessThan100(22, 15) ➞ true
// 22 + 15 = 37

lessThan100(83, 34) ➞ false
// 83 + 34 = 117

lessThan100(3, 77) ➞ true
Notes
N/A
*/

namespace challenges.Challenges.Scripts
{
    public class ChallengeLessThan100
    {
        public bool LessThan100(int x, int y)
        {
            int sumResult = x + y;
            if (sumResult >= 100)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
    }
}