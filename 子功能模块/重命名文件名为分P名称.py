# 这个脚本的功能是将当前文件夹下所有的文件按照顺序重命名为 [当前文件夹名称]_p[0开始的数字]

import os # 导入 os 模块

# 获取当前文件所处的文件夹的完整路径
currentFloderPath = os.getcwd()

# 根据路径获取文件夹名称
currentFloderName = os.path.basename(currentFloderPath)

# 获取当前文件夹下所有文件
allFiles = os.listdir(currentFloderPath)

# 遍历所有文件重命名
for i in range(len(allFiles)):
    # 重名前的完整名称
    oldFullName = allFiles[i]
    
    # 后缀名
    suffix = ""
    if (oldFullName.rfind(".") != -1):
        suffix = oldFullName[oldFullName.rfind(".") : ]

    # 新的名称 = [当前文件夹名称]_p[i]
    newName = currentFloderName + "_p" + str(i) + suffix

    os.rename(allFiles[i], newName)
