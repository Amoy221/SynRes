# encoding:gbk
import subprocess

'''

'''
def isExitWorkPlace():
    # ִ�������ȡ���
    result = subprocess.run('D: && cd D:\\UnrealProject\\Project3 && cm status', capture_output=True, text=True, shell=True,encoding="utf-8")
    # print(type(result))
    # �������ķ�����Ϣ
    print(result.stdout)
    # ������ķ�����Ϣд��txt�ļ�
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(result.stdout)
    # �������ķ�����Ϣ
    if result.returncode == 0:
        print("Command executed successfully") # �з���ֵ������plastic workplace
        return True
    else:
        print("Command failed with return code:", result.returncode)
        return False
    # if result.stdout

isExitWorkPlace()
