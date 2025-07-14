import os
import shutil
import logging


def organize_images(source_dir):
    """将图片按名称分类到同名文件夹中"""
    # 配置日志记录
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # 检查源目录是否存在
    if not os.path.exists(source_dir):
        logging.error(f"源目录不存在: {source_dir}")
        return

    # 定义支持的图片格式
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}

    # 遍历源目录中的所有文件
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # 跳过子目录
        if os.path.isdir(file_path):
            continue

        # 获取文件扩展名并检查是否为图片
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext not in image_extensions:
            logging.debug(f"跳过非图片文件: {filename}")
            continue

        # 获取不带扩展名的文件名作为文件夹名
        folder_name = os.path.splitext(filename)[0]
        folder_path = os.path.join(source_dir, folder_name)

        try:
            # 创建同名文件夹（如果不存在）
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                logging.info(f"创建文件夹: {folder_path}")

            # 移动图片到对应的文件夹
            new_file_path = os.path.join(folder_path, filename)
            shutil.move(file_path, new_file_path)
            logging.info(f"移动文件: {filename} -> {folder_name}/")

        except Exception as e:
            logging.error(f"处理文件 {filename} 时出错: {str(e)}")


if __name__ == "__main__":
    # 使用示例 - 请替换为实际的图片文件夹路径
    IMAGE_DIR = "database"
    organize_images(IMAGE_DIR)