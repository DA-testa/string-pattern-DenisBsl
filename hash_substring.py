# python3
# 221RDB188 Deniss Buslajevs 8. grupa
def read_input():
    data = input()
    if "F" in data:
        #data = input()
        #with open("tests/" + data) as f:
        with open("tests/06") as f:
            pat = f.readline().rstrip()
            str = f.readline().rstrip()
    elif "I" in data:
            pat = input().rstrip()
            str = input().rstrip()
    else:
        exit

    return (pat, str)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_hash(pattern: str) -> int:
    B, Q = 256, 101
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result

def get_occurrences(pattern, text):
    output = []
    B, Q = 256, 101
    pattern_len = len(pattern)
    main_text_len = len(text)

    mp = 1
    for _ in range(1, pattern_len):
        mp = (mp * B) % Q

    phash = get_hash(pattern)
    thash = get_hash(text[:pattern_len])

    for i in range(main_text_len - pattern_len + 1):
        if phash == thash:
            check_string = True
            for k in range(pattern_len):
                if text[i + k] != pattern[k]:
                    check_string = False
                    break
            if (check_string):
                output.append(i)
        if i < main_text_len - pattern_len:
            thash = get_hash(text[i+1:pattern_len+i+1])

    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

