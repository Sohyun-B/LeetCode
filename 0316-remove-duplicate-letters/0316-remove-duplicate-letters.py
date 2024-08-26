class Solution(object):
    def removeDuplicateLetters(self, s):
        alp_set = sorted(set(s))
        for char in alp_set:
            suffix = s[s.index(char):]
            if set(suffix )== set(s):
                return char + self.removeDuplicateLetters(suffix.replace(char,''))
        return ''