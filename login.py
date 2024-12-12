# encoding:gbk
import subprocess

'''

'''
def isExitWorkPlace():
    # 执行命令并获取输出
    result = subprocess.run('D: && cd D:\\UnrealProject\\Project3 && cm status', capture_output=True, text=True, shell=True,encoding="utf-8")
    # print(type(result))
    # 输出命令的返回信息
    print(result.stdout)
    # 将命令的返回信息写入txt文件
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(result.stdout)
    # 检查命令的返回信息
    if result.returncode == 0:
        print("Command executed successfully") # 有返回值，存在plastic workplace
        return True
    else:
        print("Command failed with return code:", result.returncode)
        return False
    # if result.stdout

isExitWorkPlace()
