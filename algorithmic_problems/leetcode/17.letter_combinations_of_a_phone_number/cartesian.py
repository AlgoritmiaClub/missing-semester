class Solution:
    def cartesian(self, set1, set2):
        result = []

        if set1 and not set2:
            return list(set1)
        elif not set1 and set2:
            return list(set2)

        for element1 in set1:
            for element2 in set2:
                result.append(element1 + element2)
        return result

    def letterCombinations(self, digits: str) -> list[str]:
        letter_to_digits = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        for number in digits:
            res = self.cartesian(res, letter_to_digits[number])
        return res
