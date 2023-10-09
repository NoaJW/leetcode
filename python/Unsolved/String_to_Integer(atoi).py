# Cannot pass case 54: input: "3.14159"
class MySolution:
    def myAtoi(self, str):
        str = str.strip()

        if len(str) > 0:
            if str[0] == "-" or str[0] == "+":
                if len(str[1:]) > 0:
                    if not(str[1] == "-" or str[1] == "+"):
                        for i in str[1:]:
                            try:
                                # if i.isdigit() == True
                                int(i)
                            except:
                                index = str.index(i)
                                if index == 1:
                                    return 0
                                else:
                                    return int(str[:index])
                    else:
                        return 0
                else:
                    return 0
            else:
                try:
                    int(str[0])

                    for i in str:
                        try:
                            int(i)
                        except:
                            index = str.index(i)
                            if index == 1:
                                return 0
                            else:
                                return int(str[:index])
                except:
                    return 0

            num = int(str)

            if num < (-2 ** 31):
                return -2 ** 31
            elif num >= (2 ** 31):
                return 2 ** 31 - 1
            else:
                return num
        else:
            return 0


class Solution:
    def myAtoi(self, str: str) -> int:
        space = 0
        output = ''
        sign = ''
        for s in str:
            if s == ' ' and space == 0:
                space = 1
            elif s == ' ' and space == 2:
                break
            else:
                if s != ' ':
                    space = 2
                    if s.isdigit() or s == '-' or s == '+':
                        if s == '-' or s == '+':
                            if sign == '' and output == '':
                                sign = s
                            else:
                                break
                        else:
                            output += s
                    elif not s.isdigit():
                        break

        if output == '':
            return 0
        else:
            if int(output) <= 2**31-1 and int(output) >= -2**31:
                if sign == '' or sign == '+':
                    return int(output)
                else:
                    return -int(output)
            else:
                if sign == '-':
                    return -2**31
                else:
                    return 2**31-1


s = Solution()
print(s.myAtoi("    -12362   "))
print(s.myAtoi("    -12362sdgsdgw   "))
print(s.myAtoi(" -91283472332 "))
print(s.myAtoi(""))
print(s.myAtoi("  - "))
print(s.myAtoi("  +23 "))
print(s.myAtoi("  -+234"))
print(s.myAtoi("  -abc"))
print(s.myAtoi(" 3.234"))
