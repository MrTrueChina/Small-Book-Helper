# 这个脚本的功能是在当前文件夹下创建指定数量的子文件夹

import os # 导入 os 模块

# 获取当前文件所处的文件夹的完整路径
currentFloderPath = os.getcwd()

# 根据路径获取文件夹名称
currentFloderName = os.path.basename(currentFloderPath)

# 获取需要创建的子文件夹的数量的输入内容，此时获取到的是字符串
subFolderNumberInput = input("请输入创建的子文件夹的数量，将会从0开始创建到指定数量\n")

# 将输入的字符串转为数字
try:
    # 强转
    subFolderNumber = int(subFolderNumberInput)
except BaseException:
    # 强转失败给出提示
    print("需要输入数字")
    input()
    exit()

# 如果收入的是负数则提示后结束
if(subFolderNumber < 0):
    print("不能输入负数")
    input()
    exit()

# 循环指定次数
for i in range(subFolderNumber + 1):
    # 拼接出子文件夹名称，i 需要先转换为字符串
    currentSubFolderName = currentFloderName + " " + str(i)
    # 拼接出子文件夹的完整路径
    currentSubFolderPath = currentFloderPath + "\\" + currentSubFolderName

    print("创建子文件夹：" + currentSubFolderName)

    # 根据子文件夹是否存在进行处理
    if(os.path.exists(currentSubFolderPath)):
        # 子文件夹存在，提示并跳过
        print("文件夹已存在，跳过")
        continue
    else:
        # 子文件夹不存在，创建子文件夹
        os.mkdir(currentSubFolderPath)
        print("文件夹已创建")
