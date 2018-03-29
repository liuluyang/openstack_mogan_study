#coding:utf8


class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        in_block = False
        result = []
        for code in source:
            i = 0
            length = len(code)
            if not in_block:
                new_line = ''
            while i<length:
                check = code[i:i+2]
                if check=='/*' and not in_block:
                    in_block = True
                    i+=1
                elif check=='*/' and in_block:
                    in_block = False
                    i+=1
                elif check=='//' and not in_block:
                    break
                elif not in_block:
                    new_line+=code[i]
                i+=1
            if new_line and not in_block:
                result.append(new_line)
        return result

s = Solution()

source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ",
          "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ",
          "   testing */", "a = b + c;", "}"]
print s.removeComments(source)