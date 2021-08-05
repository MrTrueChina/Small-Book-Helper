# 这个脚本的功能是将当前文件夹下的所有 .txt 文件合并为一个和当前文件夹名称相同的 .txt 文件
# 【警告】为了便于操作，这个功能是覆盖性的，假设运行时有一个和当前文件夹名称相同的 .txt 文件，这个文件将会被覆盖掉

import os
import re

# 获取当前文件所处的文件夹的完整路径
currentFloderPath = os.getcwd()

# 根据路径获取文件夹名称
currentFloderName = os.path.basename(currentFloderPath)

# 以当前文件夹名称作为写入的文件的名称
mergedFileName = currentFloderName + ".txt"

# 拼接出写入的文件的完整路径
mergedFilePath = currentFloderPath + "\\" + mergedFileName

# 如果要写入的文件已存在，删除这个文件
if(os.path.exists(mergedFilePath)):
    os.remove(mergedFilePath)

# 获取当前文件夹中的文件名称列表
allFiles = os.listdir(currentFloderPath)

# 对 .txt 后缀的正则，re.I 是无视大小写
txtFilePattern = re.compile(r'.*\.txt$', re.I)

# 使用 UTF-8 编码打开要写入的文件，因为之前已经删除了这个文件，这里会创建一个新的
with open(mergedFilePath, 'w', encoding='utf-8') as mergedFile:
    # 遍历所有文件
    for currentFileName in allFiles:
        # 如果遍历到的文件不是 .txt 文件，跳过
        if(txtFilePattern.match(currentFileName) is None):
            continue
    
        # 如果遍历到的文件是合并后文件，跳过
        if(currentFileName == mergedFileName):
            continue

        # 写入遍历到的文件名，[:-4]：截取字符串从头开始到倒数第四个字符的内容
        mergedFile.write(currentFileName[:-4])

        # 写入换行和空行
        mergedFile.write("\n\n")

        # 以 UTF-8 编码打开要合并的文件
        with open(currentFileName, encoding='utf-8') as currentFile:
            # 读取文件内容写入到合并后文件中
            mergedFile.write(currentFile.read())

        # 写入换行和两个空行
        mergedFile.write("\n\n\n")
