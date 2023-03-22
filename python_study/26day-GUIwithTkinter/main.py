# 230322

# import tkinter


# # 윈도우를 생성하기 위한 Tk() 클래스 객체 생성
# window  = tkinter.Tk()

# # 윈도우 셋팅
# # 윈도우 타이틀 셋팅
# window.title("my first GUI")
# # 윈도우 초기 사이즈 설정
# window.minsize(width=500 , height= 300)
# # Label 을 추가하는 작업? 
# # label 이란 ??? 
# # Label 객체 생성
# my_label = tkinter.Label(text="make Label",font=('Arial',24,'bold'))
# # lable 객체가 생성된 컴포넌트가 스크린에 보여지기 전에 어떻게 배치해야 하는지 설정
# # pack() 스크린에 컴포넌트를 배치하며, 자동적으로 중앙에 위치하게 한다.
# my_label.pack()

# # 윈도우 창을 유지하기 위한 메서드 
# window.mainloop()

def function(*args):
    for n in args:
        print(n)

function(1,2,3,4,5,56,7,8,8,9)