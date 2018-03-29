# coding:utf8

import re


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        files_dict = {}
        for files in paths:
            files = files.split()
            for file in files[1:]:
                file = re.findall('(.*)\((.*)\)', file)[0]
                name, content = file[0], file[1]
                if content not in files_dict:
                    files_dict[content] = [files[0]+'/'+ name]
                else:
                    files_dict[content].append(files[0]+'/'+ name)
        print files_dict
        return [files for files in files_dict.values() if len(files)>1]



print re.findall('(.*)\((.*)\)', 'fsf.txt(ajfk)')  # file name and content
# print re.findall('\((.*)\)','fsf.txt(ajfk)')  #file content
s = Solution()
print s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
                       "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
