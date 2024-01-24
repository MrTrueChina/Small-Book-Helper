# 这个脚本的功能是将子文件夹中所有的 "xxxx.jpe" 的图片批量修改为 "xxxx.jpeg"
# 这个功能用于将部分使用 .jpe 后缀的电脑可以识别但手机无法识别的图片后缀名改为手机可以识别的 .jpeg

# 导入
import os

# 0s.walk：递归遍历一个路径下的所有文件夹，返回一个三元数组，元素是 [当前遍历到的路径, 当前路径的直接子文件路径列表, 当前路径下的直接文件列表]
for path, dirs, files in os.walk(os.getcwd()):
    # 进一步遍历文件列表中的文件
    for file in files:
        # 拼接路径和文件名获得文件的带路径文件名
        oldFullName = os.path.join(path, file)
        # 移除其中的 .hack
        os.rename(oldFullName, oldFullName.replace('.jpe', '.jpeg'))
