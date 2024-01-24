import os
import shutil


file_name = input("\n请输入占位文件的文件名，包含后缀名。占位文件需位于当前文件夹中\n")

# 获取当前执行位置的文件夹路径
current_dir = os.getcwd()

# 遍历当前文件夹中的所有子文件夹
for folder_name in os.listdir(current_dir):
    folder_path = os.path.join(current_dir, folder_name)
    
    # 判断是否是文件夹
    if os.path.isdir(folder_path):
        has_media_files = False
        
        # 遍历文件夹中的所有文件
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            
            # 判断文件是否是图片或视频文件
            if file.endswith(("m4v", "mp4", "mov", "wmv", "avi", "mpg", "mpeg", "rmvb", "rm", "flv", "asf", "mkv", "webm", "m4a", "png", "jpg", "jpeg", "gif", "webp", "bmp")):
                has_media_files = True
                break
        
        # 如果文件夹中既没有图片文件也没有视频文件，则复制传入的文件到文件夹中
        if not has_media_files:
            print(f'文件夹 {folder_path} 中没有图片和视频，补充占位文件')
            dst_file_path = os.path.join(folder_path, file_name)
            shutil.copy(file_name, dst_file_path)