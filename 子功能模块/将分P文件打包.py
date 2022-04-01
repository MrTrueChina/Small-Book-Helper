# 这个脚本的功能是将当前文件夹下所有的文件按照顺序重命名为 [当前文件夹名称]_p[0开始的数字]

import os
import shutil

# 输出提示
print("这个脚本的打包标准是这样的：")
print("1.只有名称为 XXXXX_pXX 的文件会被认为是分P的文件")
print("2.XXXXX_pXX 前面的 XXXXX_p 部分相同的文件会被打包")
print("3.符合打包标准的文件后缀名不同也会被打包")
print("4.打包的文件夹名称是 XXXXX_pXX 中的 XXXXX")
print("5.只会打包当前文件夹里的文件，不会打包当前文件夹里的文件夹里的文件")

# 确认打包提示
doPack = input("\n输入 Y 进行打包，输入其他内容放弃打包\n")

# 如果输入的不是 Y，直接结束运行
if(doPack != "Y" and doPack != "y"):
    exit()

# 获取当前文件所处的文件夹的完整路径
currentFloderPath = os.getcwd()

# 获取当前文件夹下所有文件
allFiles = os.listdir(currentFloderPath)

# 准备一个字典保存需要打包的文件和打包后的文件夹名称
packDictonary = dict()

# 遍历所有文件，确认需要打包的文件
for currentFile in allFiles:
    # 截取文件打包后的文件夹名称
    packName = currentFile[ : currentFile.rfind("_p")]

    # 如果这个打包后文件夹名称没有在字典里，给这个名称添加一个列表
    if(not packDictonary.__contains__(packName)):
        packDictonary[packName] = []

    # 将这个文件记录下来
    packDictonary[packName].append(currentFile)

# 去除所有只有一个文件的打包记录，这些文件不用打包
packDictonary = {key:val for key, val in packDictonary.items() if len(val) > 1}

# 如果没有可以打包的文件则直接结束
if(len(packDictonary.keys()) < 1):
    print("没有可以打包的文件")
    exit()

# 输出提示内容
print("\n将会打包出下列文件夹：\n")
for key in packDictonary.keys():
    print(key + " 含有：[" + ','.join(packDictonary[key]) + "]")
doPack = input("\n输入 Y 确认打包，输入其他内容放弃打包\n")

# 如果输入的不是 Y，直接结束运行
if(doPack != "Y" and doPack != "y"):
    exit()

# 遍历记录开始打包
for key in packDictonary.keys():
    # 创建文件夹
    os.mkdir(currentFloderPath + "/" + key)

    # 遍历文件移动到文件夹里
    for file in packDictonary[key]:
        # 移动文件到文件夹里
        shutil.move(currentFloderPath + "/" + file, currentFloderPath + "/" + key + "/" + file)
