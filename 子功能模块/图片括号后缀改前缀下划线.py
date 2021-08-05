# 这个脚本的功能是将 名称(数字) 的图片批量修改为 数字_名称
# 旨在处理部分图片以类型作区分每个类型各自有一套编号，在保存到同一个文件夹下导致产生大量的 名称(数字) 图片且顺序混乱的情况

import os
import re
import shutil

# 获取当前文件所处的文件夹的完整路径
currentFloderPath = os.getcwd()

# 根据路径获取文件夹名称
currentFloderName = os.path.basename(currentFloderPath)

# 获取当前文件夹中的文件名称列表  
allFiles = os.listdir(currentFloderPath)

# 选择重命名方式，是移动还是重命名
renameModel = ""
while (["R","r","C","c"].__contains__(renameModel) != True):
    renameModel = input("请选择重命名方式：\n(R)：直接重命名当前文件夹中的图片（这会改变现有文件，比较危险）\n(C)：将当前文件夹下的图片以新的文件名复制到重命名文件夹中\n")


# 如果是复制到重命名文件中，需要进行重命名文件夹的处理
if(["C","c"].__contains__(renameModel)):
    # 拼接出重命名文件夹
    renameFolderPath = currentFloderPath + "\\" + "重命名文件夹"
    # 如果重命名文件夹存在，为了防止覆盖数据不进行操作
    if(os.path.exists(renameFolderPath)):
        print("当前文件夹下含有\"重命名文件夹\"，为防止覆盖数据，需要在没有这个文件夹时才能运行")
        input()
        exit()
    # 不存在重命名文件夹，创建重命名文件夹，为后续操作做准备
    os.mkdir(renameFolderPath)

# 对图片后缀的正则，re.I 是无视大小写
imageFilePattern = re.compile(r'.*\.(bmp|jpg|jpeg|png|tif|gif|pcx|tga|exif|fpx|svg|psd|cdr|pcd|dxf|ufo|eps|ai|raw|WMF|webp|avif|apng)$', re.I)

# 遍历所有文件
for currentFile in allFiles:
    # 不是图片后缀，跳过
    if(imageFilePattern.match(currentFile) is None):
        continue

    # 分割当前文件的文件名和后缀，分割出的是一个数组，[0] 是文件名 [1] 是后缀名
    currentFileNames = os.path.splitext(currentFile)

    # 以分割出的文件名作为重命名后的文件的文件名
    newFileName = currentFileNames[0]

    # 转换出新文件名
    if(currentFileNames[0].endswith(")")):
        # 如果是括号后缀的，改成前缀的
        try:
            # 获取最后出现的左括号的位置，这个方法如果找不到会报异常
            leftParenthesisIndex = currentFileNames[0].rindex("(")
        except BaseException:
            # 发生异常，视为 0 前缀
            newFileName = "0_" + newFileName
        else:
            # 没发生异常，就是找到了，截取括号内的内容
            suffix = currentFileNames[0][leftParenthesisIndex + 1: -1]
            # 拼接出新的文件名
            newFileName = suffix + "_" + currentFileNames[0][: leftParenthesisIndex]
    else:
        # 不是括号后缀，视为 0 前缀
        newFileName = "0_" + newFileName
    
    print("重命名文件 " + currentFileNames[0] + currentFileNames[1] + "，新文件名 = " + newFileName + currentFileNames[1])

    # 如果是直接重命名模式，直接重命名
    if(renameModel == "R" or renameModel == "r"):
        # 拼接出新的完整文件路径
        newFilePath = currentFloderPath + "\\" + newFileName + currentFileNames[1]
        # 重命名
        os.rename(currentFile, newFilePath)
    
    if(renameModel == "C" or renameModel == "c"):
        # 拼接出新的完整文件路径
        newFilePath = renameFolderPath + "\\" + newFileName + currentFileNames[1]
        # 以新的文件名复制到重命名文件夹中
        shutil.copy2(currentFile, str(newFilePath))
