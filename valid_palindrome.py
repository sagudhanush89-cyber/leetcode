class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-z0-9]','',s.lower())
        return clean == clean[::-1]
        print(isPalindrome("race a car"))