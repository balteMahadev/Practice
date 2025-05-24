def decode_string(str):
    freq = {}
    for char in str:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def decode(dict):
    result = ""
    for key, value in dict.items():
        result += f"{key}{value}"
    return result

print(decode(decode_string("aaabbaacc")))
