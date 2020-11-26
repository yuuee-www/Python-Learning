import sys

def doSomething(blob, pattern):
    count = 0

    for x in range(len(blob) - len(pattern) + 1):
        if blob[x:x+len(pattern)] == pattern:
            count += 1
    print(count,end="")
    print("|",end="")
    return count

        
for line in sys.stdin:
    splitted_input = line.split(';')
    pattern = splitted_input[0]
    if pattern=="":
        print("0|0|0|0|0")
        break
    blobs = splitted_input[1].split('|')
    aList=[]
    s=0
    for a in range(len(blobs)):
        result = doSomething(blobs[a], pattern)
        aList.append(result)
    s=sum(aList)
    print(s)
        
'''
Given a pattern as the first argument and a string of blobs split by | show the number of times the pattern is present in each blob and the total number of matches.
输入：
The input consists of the pattern ("bc" in the example) which is separated by a semicolon followed by a list of blobs ("bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32" in the example). Example input: bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
输出：
The output should consist of the number of occurrences of the pattern per blob (separated by |). Additionally, the final entry should be the summation of all the occurrences (also separated by |).
Example output: 3|2|1|2|8 where 'bc' was repeated 3 times, 2 times, 1 time, 2 times in the 4 blobs passed in. And 8 is the summation of all the occurrences (3+2+1+2 = 8)
测试 1
测试输入下载测试 1 输入
;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
预期输出下载测试 1 输入
0|0|0|0|0
测试 2
测试输入下载测试 2 输入
b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
预期输出下载测试 2 输入
4|2|3|2|11
测试 3
测试输入下载测试 3 输入
aa;aaaakjlhaa|aaadsaaa|easaaad|sa
预期输出下载测试 3 输入
4|4|2|0|10
测试 4
测试输入下载测试 4 输入
bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
预期输出下载测试 4 输入
3|2|1|2|8
'''