from  tkinter import * #tkinter안 모든 함수 다 불러옴 그리고 불러온 함수이름만 적어서 사용할수 있음
import pandas as pd
import os #폴더 만들고 삭제
import tkinter.ttk
from tkinter import ttk


#디렉토리와 폴더의 거의 같은 의미 리눅스&맥=디렉토리 윈도우=폴더 다르게 부름df.to_excel('foo.xlsx', sheet_name='sheet1')
print(os.getcwd())#현재 디렉토리 위치 알려줌


data = pd.read_csv("seoul.csv", encoding='cp949')
print(data.loc[0][0])


#.현재폴더 ..상위폴더
#dat=pd.read_csv("./파일명.csv")

def click():
    print("버튼이 클릭!")
    word = combobox.get()#아레 엔트리 상자의 내용을 text로 넣는다
    oup.delete(0.0, END)#텍스트 박스 내용 삭제 0번째부터 끝까지
    print(word)


    try:
        def_word = data.loc[data['word'] == word, 'def'].values[0]
        # print(data.loc[data['word']])
        print(def_word)


    except:
        def_word = "단어 뜻 없다!"
        #dat=window_add(dat)

    oup.insert(END, def_word)

window = Tk()
window.title("서울시 실외운동기구 현황")
window.geometry("540x300+100+100") #출력창 크기& 위치(+x값,+y값)
# window.resizable(False,False) #창 늘리기 상하,좌우 불가!

#입력상자 설명 레이블
label = Label(window, width=30, text="시설별 기구 종류(목록보고 선택!) ") #Label은 라벨링 텍스트를 넣을수 있는공간
label.grid(row=0, column=0, sticky="w") #W는 west다 고정시킬 위치 grid는 위치에 장착??


values=[ data.loc[i][0] for i in range(56) ]
combobox = ttk.Combobox(window, width=26, height=15, background="#7FFFD4", values=values)
combobox.grid(row=1, column=0, sticky='w')
combobox.set("목록 선택")

# 02 텍스트 입력이 가능한 상자(Entry)
# entry = Entry(window, width=30, borderwidth=3, bg="#7FFFD4") #entry는 입력을 넣을수 있는 상자
# entry.grid(row=2, column=0,  sticky="w")

# 03제출 버튼 추가
btn = Button(window ,  text="제출", width=5, command=click, borderwidth=3, overrelief="solid")
btn.grid(row=1, column=0,  sticky="S")

# 04 설명 레이블-의미
min=Label(window, text="\n보유기구:")
min.grid(row=3, column=0, sticky= "w")


# 05 텍스트 박스 입력 상자
# columnspan=2 (4,0)~,(4,1)위치까지 분포
oup = Text(window, width = 100, height = 50, wrap = WORD, background="#7FFFD4")
oup.grid(row=4, column=0, columnspan=2, sticky= W)

window.mainloop()