def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def char_report(chars):
    sorted_dict=dict(sorted(chars.items(),key=lambda item: item[1],reverse=True))
    for c,n in sorted_dict.items():
        if c.isalpha():
            print(f"{c}: {n}")
        
