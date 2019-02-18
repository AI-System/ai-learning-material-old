# coding=utf-8

'''
可执行文件
'''
from db.model import Model
import getpass

# main
if __name__ == '__main__':
    m = Model("atm")
    print('atm')
    #登陆界面
    while True:
        #输出初始界面
        print("=" * 20, "自动取款机系统", "=" * 20)
        #输入登录名及密码并检验
        sUser_Name = input("请输入用户名：")
        sPass_Word = getpass.getpass("请输入密码(不可见)：")
        res = m.select(where=["name='%s'"%(sUser_Name),"password='%s'"%(sPass_Word)]) 
        if len(res) < 1:   
            print("账号或密码错误！")
            continue
        user = res[0] #取出当前账号信息
        #功能选择界面
        while True:
            print("=" * 20, "请选择业务", "=" * 20)
            print("{0:5} {1:18} {2:13}".format(" ", "1. 余额查询", "2. 存款"))
            print("{0:5} {1:20} {2:13}".format(" ", "3. 取款", "4. 退出程序"))
            print("=" * 50)
            key = input("请输入任务编号：")
            #功能模块
            if key == "1":
                print("=" * 20, "余额查询", "=" * 20)
                print('账号余额：',user['balance'])
                input("按回车键继续")
            elif key == "2":
                print("=" * 20, "存款", "=" * 20)
                num = int(input("请输入您的存款金额："))
                user['balance'] += num
                m.update(user) #执行数据库修改
                input("按回车键继续")
            elif key == "3": 
                print("=" * 20, "取款", "=" * 20)
                num = int(input("请输入您的取款金额："))
                user['balance'] -= num
                m.update(user) #执行数据库修改
                input("按回车键继续")
            elif key == "4":
                print("=" * 20, "退出 Bye!", "=" * 20)
                break
            else:
                print("=" * 20, "输入无效", "=" * 20)
                input("按回车键继续")
        break