public class Solution {
    public bool IsPalindrome(int x) {

        int num = x;
        int reverse = 0;
        int lenght = 0;

        for (int y = 0; y < x; y++){
            int digit = num%10;
            lenght++;
            num = num/10;
            reverse = reverse * 10 + digit;
            if(num==0){
                break;
            }
        }

        if (reverse == x){
            return true;
        }
        else return false;

    }
}
