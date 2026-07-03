class Solution:
    def reverseWords(self, s: str) -> str:
        word =s.split()
        reversed_word=word[::-1]
        return " ".join(reversed_word)
        print(reversedWords("the shy is blue"))
        