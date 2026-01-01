def swap_case(s):
    LIST = list(s)
    final_Str = []
    for i in LIST:
        if i.isupper():
            final_Str.append(i.lower())
        elif i.islower():
            final_Str.append(i.upper())
    return "".join(final_Str)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

