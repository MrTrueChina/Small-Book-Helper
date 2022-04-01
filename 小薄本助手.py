# 小薄本助手的总调用端

import os
import sys

# 获取脚本文件的绝对路径，这是因为这个脚本可能通过 cmd 在其他位置调用
scriptAbsPath = os.path.abspath(sys.argv[0])

# 截取脚本文件夹的绝对路径
scriptFolderPath = os.path.dirname(scriptAbsPath)

# 选择功能
subFolderNumberInput = input("====小薄本助手====\n请选择功能\n(S) 创建子文件夹\n(M) 以起点逻辑合并文本文件\n(RU) 图片括号数字后缀改前缀下划线\n(RP) 重命名文件名为分P名称\n(P) 将分p文件打包\n")

# S：Sub Folder
if(subFolderNumberInput == "S" or subFolderNumberInput == "s"):
    os.system(scriptFolderPath + "\\子功能模块\\创建当前文件夹的子文件夹.py")
    exit()

# M：Merge
if(subFolderNumberInput == "M" or subFolderNumberInput == "m"):
    os.system(scriptFolderPath + "\\子功能模块\\以起点逻辑合并文本文件.py")
    exit()

# RD：Rename Underline
if(subFolderNumberInput == "RU" or subFolderNumberInput == "ru"):
    os.system(scriptFolderPath + "\\子功能模块\\图片括号后缀改前缀下划线.py")
    exit()

# RD：Rename Page
if(subFolderNumberInput == "RP" or subFolderNumberInput == "rp"):
    os.system(scriptFolderPath + "\\子功能模块\\重命名文件名为分P名称.py")
    exit()

# P：Pack
if(subFolderNumberInput == "P" or subFolderNumberInput == "p"):
    os.system(scriptFolderPath + "\\子功能模块\\将分P文件打包.py")
    exit()

print("没有这个功能")
input()
exit()
