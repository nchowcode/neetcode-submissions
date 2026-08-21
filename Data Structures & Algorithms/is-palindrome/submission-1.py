class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers from center, go outwards
        left = 0
        right = len(s) - 1


        # rac_car
        # 0 6
        # 1 5
        # 2 4
        # 3 3
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -=1
                continue
            if s[right].lower() == s[left].lower():
                right -= 1
                left += 1
            else:
                return False

        return True
            
            