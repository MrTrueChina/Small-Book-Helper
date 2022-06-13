# 小薄本助手的总调用端

import os
import sys

# 获取脚本文件的绝对路径，这是因为这个脚本可能通过 cmd 在其他位置调用
scriptAbsPath = os.path.abspath(sys.argv[0])

# 截取脚本文件夹的绝对路径
scriptFolderPath = os.path.dirname(scriptAbsPath)

# 显示使用说明
print("====小薄本助手====")
print("请选择功能")
print("(SF) 创建子文件夹")
print("(MQ) 以起点逻辑合并文本文件")
print("(RU) 图片括号数字后缀改前缀下划线")
print("(RP) 重命名文件名为分P名称")
print("(P) 将分p文件打包")
print("(KCRH) 砍口垒功能，递归移除文件夹中所有名字中带有\".hack\"的文件的文件名中的\".hack\"")

# 选择功能
subFolderNumberInput = input("\n")

# 选择功能字符串转为全小写
subFolderNumberInput = subFolderNumberInput.lower()

# SF：Sub Folder
if(subFolderNumberInput == "sf"):
    os.system(scriptFolderPath + "\\子功能模块\\创建当前文件夹的子文件夹.py")
    exit()

# MQ：Merge by QiDian
if(subFolderNumberInput == "mq"):
    os.system(scriptFolderPath + "\\子功能模块\\以起点逻辑合并文本文件.py")
    exit()

# RD：Rename Underline
if(subFolderNumberInput == "ru"):
    os.system(scriptFolderPath + "\\子功能模块\\图片括号后缀改前缀下划线.py")
    exit()

# RD：Rename Page
if(subFolderNumberInput == "rp"):
    os.system(scriptFolderPath + "\\子功能模块\\重命名文件名为分P名称.py")
    exit()

# P：Pack
if(subFolderNumberInput == "p"):
    os.system(scriptFolderPath + "\\子功能模块\\将分P文件打包.py")
    exit()

# KCRH：Kan Colle Remove Hack
if(subFolderNumberInput == "kcrh"):
    os.system(scriptFolderPath + "\\子功能模块\\移除Hack部分文件名.py")
    exit()

print("没有这个功能")
input()
exit()
