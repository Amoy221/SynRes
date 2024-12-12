# encoding:gbk
import os
import subprocess



def sync_directory_to_plastic(directory, plastic_workspace):
    # 切换到目标目录
    # os.chdir(directory)

    # 获取目录中的所有文件和子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 构建完整的文件路径
            file_path = os.path.join(root, file)

            # 使用 cm 命令添加文件到 Plastic SCM
            try:
                # cm add 命令添加文件到暂存区
                subprocess.run(['cm', 'add', file_path], check=True, cwd=plastic_workspace)
                print(f"Added {file_path} to Plastic SCM.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to add {file_path} to Plastic SCM: {e}")

        # 对于子目录，可以添加空目录（如果需要）
        # 注意：Plastic SCM 默认会跟踪非空目录
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            # 如果需要添加空目录，可以取消注释以下行，但通常不需要
            # subprocess.run(['cm', 'add', dir_path], check=True, cwd=plastic_workspace)
            print(f"Directory {dir_path} will be automatically tracked if it contains files.")

    # 提交更改到仓库
    try:
        # cm commit 命令提交更改
        commit_message = "Sync directory resources to Plastic SCM"
        subprocess.run(['cm', 'checkin', '-m', commit_message], check=True, cwd=plastic_workspace)
        print("Committed changes to Plastic SCM.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit changes to Plastic SCM: {e}")

if __name__ == "__main__":
    # 替换成你的目标目录和 Plastic SCM 工作空间目录
    target_directory = r"D:\synfolder_test"
    plastic_workspace_directory = r"D:\UnrealProject\project3\Content"

    sync_directory_to_plastic(target_directory, plastic_workspace_directory)