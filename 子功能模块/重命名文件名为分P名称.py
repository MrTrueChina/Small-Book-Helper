# 这个脚本的功能是将当前文件夹下所有的文件按照顺序重命名为 [当前文件夹名称]_p[0开始的数字]

import os # 导入 os 模块

# 选择重命名规则的提示
print("请选择重命名方式：")
print("（FP）重命名为 {文件夹名称}_p{页码}")
print("（FN）重命名为 {文件夹名称}_{文件原名}")
print("（FPN）重命名为 {文件夹名称}_p{页码}_{文件原名}")

# 接收重命名规则
renameRule = input("\n")

# 将重命名规则改为小写
renameRule = renameRule.lower()

# 输入错误则发出提示后结束运行
if(renameRule != "fp" and renameRule != "fn" and renameRule != "fpn"):
    print("没有选择重命名方式，取消重命名")
    exit()

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
    
    # 后缀名和文件名
    fileName = oldFullName
    suffix = ""
    if (oldFullName.rfind(".") != -1):
        fileName = oldFullName[ : oldFullName.rfind(".")]
        suffix = oldFullName[oldFullName.rfind(".") : ]

    # FP（Folder Part/Page）：新的名称 = [当前文件夹名称]_p[i]
    if(renameRule == 'fp'):
        newName = currentFloderName + "_p" + str(i) + suffix

    # FN（Folder Name）：新的名称 = [当前文件夹名称]_p[原始文件名]
    if(renameRule == 'fn'):
        newName = currentFloderName + "_" + fileName + suffix
    
    # FP（Folder Part/Page Name）：新的名称 = [当前文件夹名称]_p[i]_[原始文件名]
    if(renameRule == 'fpn'):
        newName = currentFloderName + "_p" + str(i) + "_" + fileName + suffix

    os.rename(allFiles[i], newName)
