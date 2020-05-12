class LM(object):
    def main():
        string = str(input('Nhập số la mã: '))
        string = string.upper()
        total = 0
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        while string:
            if len(string) == 1 or val[string[0]] >= val[string[1]]:
                total += val[string[0]]
                string = string[1:]
            else:
                total += val[string[1]] - val[string[0]]
                string = string[2:]
        print(total)


    main()