class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1

        while i < j:
            # print(s[i].isalnum(), s[j].isalnum())

            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    # print(s[i], s[j])
                    return False
            
                i += 1
                j -= 1

        return True