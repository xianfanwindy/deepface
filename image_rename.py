import os
import re

def batch_rename_images(folder_path, target_text=None):
    """
    批量重命名指定文件夹中的图片文件
    
    参数:
    folder_path (str): 要处理的文件夹路径
    target_text (str, optional): 要从文件名中删除的特定文本。如果为None，则尝试自动检测并删除非标准字符
    """
    if not os.path.exists(folder_path):
        print(f"错误：文件夹 '{folder_path}' 不存在")
        return
    
    try:
        # 获取文件夹中的所有文件
        files = os.listdir(folder_path)
        renamed_count = 0
        
        for file in files:
            old_path = os.path.join(folder_path, file)
            
            # 跳过子目录
            if not os.path.isfile(old_path):
                continue
                
            # 只处理图片文件（可以根据需要添加更多扩展名）
            if not file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                continue
                
            # 提取文件名和扩展名
            filename, ext = os.path.splitext(file)
            
            if target_text:
                # 如果提供了目标文本，则直接删除它
                new_filename = filename.replace(target_text, '')
            else:
                # 否则尝试自动检测并删除非标准字符
                # 这里假设标准格式是"DH+数字"，使用正则表达式提取
                match = re.match(r'(DH\d+)', filename)
                if match:
                    new_filename = match.group(1)
                else:
                    # 如果没有匹配到标准格式，则跳过该文件
                    print(f"跳过: {file} (无法识别标准格式)")
                    continue
            
            # 构建新的文件路径
            new_file = new_filename + ext
            new_path = os.path.join(folder_path, new_file)
            
            # 执行重命名
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"已重命名: {file} -> {new_file}")
                renamed_count += 1
                
        print(f"重命名完成！共处理了 {renamed_count} 个文件")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    # 指定要处理的文件夹路径
    folder_path = "database"
    
    # 询问是否使用自动模式
    use_auto_mode = 'y'
    
    if use_auto_mode:
        batch_rename_images(folder_path)
    else:
        target_text = input("请输入要从文件名中删除的特定文本: ").strip()
        batch_rename_images(folder_path, target_text)    