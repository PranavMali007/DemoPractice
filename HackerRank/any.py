from xmlrpc.client import boolean

if __name__ == '__main__':
    s = input().strip()

    print(any(c.isalnum() for c in s))  # 1
    print(any(c.isalpha() for c in s))  # 2
    print(any(c.isdigit() for c in s))  # 3
    print(any(c.islower() for c in s))  # 4
    print(any(c.isupper() for c in s))  # 5
