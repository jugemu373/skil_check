def decompress(s, i, count, char_count):
    new_count = count
    while i < len(s):
        if s[i].isdigit():
            start = i
            while s[i].isdigit():
                i += 1
            new_count = count * int(s[start:i])
        elif s[i] == "(":
            i, _ = decompress(s, i + 1, new_count, char_count)
            new_count = count
        elif s[i] == ")":
            return i + 1, count
        else:
            char_count[s[i]] += new_count
            new_count = count
            i += 1
    return i, count


def count_chars(s):
    char_count = {chr(i + ord("a")): 0 for i in range(26)}
    decompress(s, 0, 1, char_count)
    for c in sorted(char_count.keys()):
        print(f"{c} {char_count[c]}")


s = input().strip()
count_chars(s)
