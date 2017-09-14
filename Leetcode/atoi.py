class Solution(object):
    def remove_whitespaces(self, string):
        # clean up whitespace and return early if no chars
        no_wspace = string.strip()
        if no_wspace.isspace() or len(no_wspace) == 0 or no_wspace == "":
            return ""

        return no_wspace

    def get_sign(self, string):
        signs = {'+', '-'}
        sign = ''
        # grab sign if there is one
        if len(string) > 0 and string[0] in signs:
            sign = string[0]
            string = string[1:]

        return (sign, string)

    def build_integer(self, string):
        # build integer string
        result, i = 0, 0
        while i < len(string) and string[i].isdigit():
            result = result * 10 + ord(string[i]) - ord('0')
            i += 1
        return result

    def myAtoi(self, string):
        max_int = 2147483647
        # have to cast it to string because for some reason
        # the type is an int
        no_spaces_string = self.remove_whitespaces(string)  
        sign, clean_string = self.get_sign(no_spaces_string)
        result = self.build_integer(clean_string)
        
        if sign and sign == '-':
            result *= -1
            
        # check if digitized exceeds 32-bit
        if result >= max_int:
            return max_int
        else:
            if result < 0:
                return max(result, -2**31)
            else:
                return result

if __name__ == "__main__":
    quit = ["q", "quit"]
    s = input("Enter a string: ")
    while s not in quit:
        print("the integer is: ", Solution.myAtoi(s))
        s = input("Enter a string: ")