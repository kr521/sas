#-*- encoding=UTF-8 -*- 
#for my System Admin System by machao 

import Tkinter 
from Tkinter import * 
from FileDialog import * 
import ConfigParser
import os 
root = Tk() 
root.title('System Configration System') 
root.geometry('800x600') 
t = Tkinter.Text(root,height=20,width=100,bg='grey',wrap = 'word' ) 

# global 
CONF = 0




def Readlogfile():
    """声明日志文件"""
    logfile = "/tmp/scs.log"

def ConfigrationLoad(conf):
    """配置文件赋值
    默认配置文件样例
    [ssh_key]
    key_file = /tmp/ceshi
    pub_key = /tmp/ceshi.pub
    pri_key = /tmp/ceshi
    pub_key_mod = 644
    pri_key_mod = 600
    """
    value = ";".join(["%s=%s" % (k, v) for k, v in conf.items()])
    print "value = " + value
    return value
    
def ReadDefaultConfigrationFile():
    """声明默认配置文件"""
    config = ConfigParser.ConfigParser()
    filename = "/tmp/csc.cfg"
    if filename and os.path.isfile(filename):
        config.readfp(open(filename,"rb"))
        CONF = config.get("ssh_key","key_file")
        print CONF 
    else:
        print "File error"

def ReadConfigrationFile():
    """声明配置文件"""
    t.delete(1.0, 'end') 
    fd = LoadFileDialog(root)
    filename = fd.go() 
    config = ConfigParser.ConfigParser()
    if filename and os.path.isfile(filename):
        config.readfp(open(filename,"rb"))
        value = { "key_file":config.get("ssh_key","key_file")}
        ConfigrationLoad(value)
    else:
        print "File error"
        
def SaveConfigrationFile():
    """存配置文件"""
    fd = SaveFileDialog(root) 
    filename= fd.go() 
    file = open(filename, 'w') 
    content = t.get(1.0, END) 
    file.write(content) 
    file.close()   

def CreateNewSSHKeyFile(): 
    """生成新的KEY"""
    t.delete(1.0, 'end') 
    comm="ssh-keygen -f " + CONF.filename
    print comm
    #result = os.popen(comm).readlines() 
    #t.insert(INSERT, "\n".join(result), "a") 

def LoadSSHKeyFile():
    """读取ssh_key"""
    t.delete(1.0, 'dend')
    if os.path.isfile(keyinfo.dir+keyinfo.name_pri):
        #load key
        print keyinfo.file_dir + keyinfo.name_pri
    else:
        print 'error'
        
def Default():
    print "null"
        
def openfile(): 
    t.delete(1.0, 'end') 
    fd = LoadFileDialog(root) 
    filename = fd.go() 
    content = open(filename, 'r') 
    lines= content.readlines() 
    for line in lines: 
        t.insert('end',line) 
#    file.close() 
def savefile(): 
    fd = SaveFileDialog(root) 
    filename= fd.go() 
    file = open(filename, 'w') 
    content = t.get(1.0, END) 
    file.write(content) 
    file.close() 
def threads(): 
    t.delete(1.0, 'end') 
    result = os.popen('ps -ef | grep httpd | grep -v grep|wc -l').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
def status(): 
    t.delete(1.0, 'end') 
    result = os.popen('sh status.sh').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
def total(): 
    t.delete(1.0, 'end') 
    result = os.popen('sh conn.sh').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
def start(): 
    t.delete(1.0, 'end') 
    result = os.popen('service httpd start').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
def stop(): 
    t.delete(1.0, 'end') 
    result = os.popen('service httpd stop').readlines()     
    t.insert(INSERT, "\n".join(result), "a") 
def restart(): 
    t.delete(1.0, 'end')
    result = os.popen('service httpd restart').readlines() 
    t.insert(INSERT, "\n".join(result), "a") 
def about(): 
    t.delete(1.0, 'end') 
    w = Label(root,text="系统管理工具，测试用。") 
    w.pack(side=TOP) 
 
menubar = Menu(root) 
ReadDefaultConfigrationFile
()
filemenu = Menu(menubar,tearoff=0) 
filemenu.add_command(label="打开新配置", command=ReadConfigrationFile)
filemenu.add_command(label="读取默认配置", command=ReadDefaultConfigrationFile) 
filemenu.add_command(label="保存配置文件", command=SaveConfigrationFile)
filemenu.add_separator() 
filemenu.add_command(label="退出", command=root.quit) 
menubar.add_cascade(label="文件", menu=filemenu) 

filemenu = Menu(menubar,tearoff=0) 
filemenu.add_command(label="生成SSH_KEY", command=CreateNewSSHKeyFile)
filemenu.add_command(label="读取SSH_KEY", command=Default) 
filemenu.add_command(label="查看SSH_KEY", command=Default)
filemenu.add_separator() 
filemenu.add_command(label="查看机器列表", command=Default)
filemenu.add_command(label="添加新机器", command=Default) 
filemenu.add_command(label="修改机器信息", command=Default)
menubar.add_cascade(label="机器管理", menu=filemenu) 

 
##创建下拉菜单File，然后将其加入到顶级的菜单栏中 
#filemenu = Menu(menubar,tearoff=0) 
#filemenu.add_command(label="打开配置文件", command=openfile) 
#filemenu.add_command(label="保存配置文件", command=savefile) 
#filemenu.add_separator() 
#filemenu.add_command(label="退出", command=root.quit) 
#menubar.add_cascade(label="nginx配置管理", menu=filemenu) 
 
##创建一个下拉菜单Edit 
#editmenu = Menu(menubar, tearoff=0) 
#editmenu.add_command(label="总线程数", command=threads) 
#editmenu.add_command(label="状态", command=status) 
#editmenu.add_command(label="连接数", command=total) 
#menubar.add_cascade(label="nginx基本监控查看",menu=editmenu) 
 
##创建下拉菜单status 
#editmenu = Menu(menubar, tearoff=0) 
#editmenu.add_command(label="启动nginx", command=start) 
#editmenu.add_command(label="停止nginx",command=stop) 
#editmenu.add_command(label="重启nginx", command=restart) 
#menubar.add_cascade(label="nginx操作",menu=editmenu) 
##创建下拉菜单Help 
#helpmenu = Menu(menubar, tearoff=0) 
#helpmenu.add_command(label="about", command=about) 
#menubar.add_cascade(label="查看版本和帮助", menu=helpmenu) 
#显示菜单 
root.config(menu=menubar) 
 
#显示菜单 
t.pack() 
mainloop() 