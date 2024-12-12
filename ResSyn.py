# encoding:gbk
import os
import subprocess



def sync_directory_to_plastic(directory, plastic_workspace):
    # �л���Ŀ��Ŀ¼
    # os.chdir(directory)

    # ��ȡĿ¼�е������ļ�����Ŀ¼
    for root, dirs, files in os.walk(directory):
        for file in files:
            # �����������ļ�·��
            file_path = os.path.join(root, file)

            # ʹ�� cm ��������ļ��� Plastic SCM
            try:
                # cm add ��������ļ����ݴ���
                subprocess.run(['cm', 'add', file_path], check=True, cwd=plastic_workspace)
                print(f"Added {file_path} to Plastic SCM.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to add {file_path} to Plastic SCM: {e}")

        # ������Ŀ¼��������ӿ�Ŀ¼�������Ҫ��
        # ע�⣺Plastic SCM Ĭ�ϻ���ٷǿ�Ŀ¼
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            # �����Ҫ��ӿ�Ŀ¼������ȡ��ע�������У���ͨ������Ҫ
            # subprocess.run(['cm', 'add', dir_path], check=True, cwd=plastic_workspace)
            print(f"Directory {dir_path} will be automatically tracked if it contains files.")

    # �ύ���ĵ��ֿ�
    try:
        # cm commit �����ύ����
        commit_message = "Sync directory resources to Plastic SCM"
        subprocess.run(['cm', 'checkin', '-m', commit_message], check=True, cwd=plastic_workspace)
        print("Committed changes to Plastic SCM.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit changes to Plastic SCM: {e}")

if __name__ == "__main__":
    # �滻�����Ŀ��Ŀ¼�� Plastic SCM �����ռ�Ŀ¼
    target_directory = r"D:\synfolder_test"
    plastic_workspace_directory = r"D:\UnrealProject\project3\Content"

    sync_directory_to_plastic(target_directory, plastic_workspace_directory)