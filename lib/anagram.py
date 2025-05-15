# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower() 

    def match(self, word_list):
        matches = []
        for candidate in word_list:
            if self._is_anagram(candidate):
                matches.append(candidate)
        return matches

    def _is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return (
            candidate_lower != self.word and 
            sorted(candidate_lower) == sorted(self.word) 
        )