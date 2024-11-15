def gen_sentences(path):
    with open(path, encoding="utf8") as file:
        for line in file:
            if line != '\n':
                line = line[:len(line)-1]
                tokens = line.split(' ')
                yield tokens


def case_sarcastically(text):
    output = ''
    count = 0
    for c in text:
        if c.upper() != c.lower() and count % 2 == 0:
            output += c.lower()
            count += 1
        elif c.upper() != c.lower() and count % 2 == 1:
            output += c.upper()
            count += 1
        else:
            output += c
    return output


def prefix(s, n):
    if n > len(s) or n < 1:
        raise ValueError()
    else:
        return s[:n]

def suffix(s, n):
    if n > len(s) or n < 1:
        raise ValueError()
    else:
        return s[-n:]

def sorted_chars(s):
    charSet = set()
    for c in s:
        charSet.add(c)
    return sorted(charSet)
