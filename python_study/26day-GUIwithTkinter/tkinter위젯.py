# 230322

from tkinter import *


# 윈도우를 생성하기 위한 Tk() 클래스 객체 생성
window  = Tk()

# 윈도우 셋팅
# 윈도우 타이틀 셋팅
window.title("my first GUI")
# 윈도우 초기 사이즈 설정
window.minsize(width=500 , height= 300)
# Label 을 추가하는 작업? 
# label 이란 ??? 
# Label 객체 생성
my_label = Label(text="make Label",font=('Arial',24,'bold'))
# lable 객체가 생성된 컴포넌트가 스크린에 보여지기 전에 어떻게 배치해야 하는지 설정
# pack() 스크린에 컴포넌트를 배치하며, 자동적으로 중앙에 위치하게 한다.
# my_label.pack()


# place --->위젯에 정확한 위치를 지정
my_label.place(x=0, y=0 )


# label 객체에 text에 해당하는 분 값 변경 
# case 1
my_label['text'] = 'New Text'
# case 2
my_label.config(text ='New Text')


# button 

# button을 누른 이벤트를 listener가 반응할 함수 생성
def clicked():
    string = input.get()
    my_label.config(text = string)



button = Button(text='Click',command=clicked)
# pack() 메서드를 호출해서 레이아웃이 스크린에 배치되도록 실행
button.pack()
# 현재 버틀을 눌러도 동작을 하지 않는다. --> why?
# listener가 존재하지 않기 때문이다.
# 이를 위해 객체를 생성할 때 command라는 키값에 함수를 입력 - 단 이때 함수의 괄호를 포함x
# 호출을 하는 것이 아닌 어떤 함수를 적용하겠다는 것만을 표시하는 것이기 때문에 괄호x


# Entry 
# 사용자로부터 데이터를 입력받는 곳
input = Entry(width = 10, )
input.pack()




# # text box
# text = Text(height= 5 , width= 30)
# # 커서의 위치를  textbox 안에 둔다.
# text.focus()
# # 초기에 textbox안에 값을 입력
# text.insert(END,"Example")
# # textbox의 현재 입력된 값을 받아온다.
# # 1.0은 첫번쨰 줄에서 글자 0으로 시작하는 텍스트를 의미한다.
# print(text.get('1.0',END))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# 윈도우 창을 유지하기 위한 메서드 
window.mainloop()

