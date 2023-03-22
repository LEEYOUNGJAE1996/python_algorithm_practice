# 230322
from tkinter import *


# 윈도우를 생성하기 위한 Tk() 클래스 객체 생성
window  = Tk()

# 윈도우 셋팅
# 윈도우 타이틀 셋팅
window.title("Mile to km Converter")
# window 창에 여유분?? 페이지 양옆 여백
window.config(padx= 30, pady= 30)
# Label 을 추가하는 작업? 
# label 이란 ??? 
# Label 객체 생성
equal = Label(text="is equal to",font=('Arial',24,'bold'))
equal.grid(column=0, row= 1)
miles = Label(text="miles",font=('Arial',24,'bold'))
miles.grid(column=2, row= 0)
km = Label(text="km",font=('Arial',24,'bold'))
km.grid(column=2, row= 1)
result = Label(text="0",font=('Arial',24,'bold'))
result.grid(column=1, row= 1)




# button 
# button을 누른 이벤트를 listener가 반응할 함수 생성
def clicked():
    miles_value = float(input.get())
    km_value = miles_value * 1.609344
    result.config(text=f'{round(km_value,3)}')
    
    


button = Button(text='Calculate',command=clicked)
button.grid(column=1, row=2)
# 현시하는 것이기 때문에 괄호x


# Entry 
# 사용자로부터 데이터를 입력받는 곳
input = Entry(width = 10, )
input.grid(column= 1 , row = 0)
window.mainloop()
