# coding:utf-8
"""
Anagram，翻译成中文为"相同字母异序词"
"""
def is_Anagrm(s1,s2):
    s1, s2 = s1.lower(), s2.lower()
    lst1 = [0] * 26
    lst2 = [0] * 26
    length1, length2 = len(s1), len(s2)
    for i in range(length1):
        pos = ord(s1[i]) - ord('a')
        lst1[pos] += 1

    for i in range(length2):
        pos = ord(s2[i]) - ord('a')
        lst2[pos] += 1

    for i in range(26):
        if lst1[i] != lst2[i]:
            return False
    return True


print is_Anagrm("Abbc","cbaba")
print is_Anagrm("JKwwi", "wkjwi")


******************************************
#法二

def is_Anagram_2(s1, s2):
    s1, s2 = s1.lower(), s2.lower()
    len1, len2 = len(s1), len(s2)
    if len1 != len2:
        return False

    hash = [0] * 26
    for c in s1:
        pos = ord(c) - ord('a')
        hash[pos] += 1

    for c in s2:
        pos = ord(c) - ord('a')
        hash[pos] -= 1

    for x in hash:
        if x != 0:
            return False
        return True
