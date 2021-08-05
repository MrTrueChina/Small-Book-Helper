# 这个脚本的主要目标是在小薄本助手添加进 环境变量 Path 的时候给 cmd 窗口一个不用输入法的调用选择

import os
import sys

# 获取脚本文件的绝对路径，这是因为这个脚本可能通过 cmd 在其他位置调用
scriptAbsPath = os.path.abspath(sys.argv[0])

# 截取脚本文件夹的绝对路径
scriptFolderPath = os.path.dirname(scriptAbsPath)

# 调用 小薄本助手.py
os.system(scriptFolderPath + "\\小薄本助手.py")
