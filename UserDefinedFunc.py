def char_freq(text):
    freq = {}  
    for chr in text:
        if chr != " ":  
            if chr in freq:
                freq[chr] += 1
            else:
                freq[chr] = 1
    return freq

if __name__ == "__main__":
    text_inp = input("Enter string: ")
    result = char_freq(text_inp)

    output = []
    for k, v in result.items():
        output.append(f"{k}={v}")
    print(", ".join(output))
