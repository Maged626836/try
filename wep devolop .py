from tkinter import TRUE
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *



def app():
    def check_name(data):
        if len(data['u_n'])>7:
            return('user','اسم المستخدم طويل يجب ان لا يتعدى 7 احرف')
            print("اسم المستخدم طويل يجب ان لا يتعدى 7 احر")
    popup("hi",
    put_text("العدد").onclick(lambda: toast("1000")))
    put_html('<center><h3>النظام</h3><img src ="https://st.depositphotos.com/1898481/3858/i/600/depositphotos_38585251-stock-photo-unnamed.jpg" width =150></center>')
    data = input_group(
        'مشترك جديد ',
        [
            input('اسم المستخدم' ,name= 'u_n'),
            input('كود المستخدم' ,name= 'u_c', type= PASSWORD)
            
        ],validate=check_name
    )
    put_text('new user :').style('color:red;font-width:bold;')
    put_text('user name : %r'%data["u_n"])




start_server(app,port= 4567 ,debug=True)