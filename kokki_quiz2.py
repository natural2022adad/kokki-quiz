from PIL import ImageTk, Image
import tkinter as tk
import tkinter.messagebox as msg
import urllib.request
import io
import random
import csv
from bs4 import BeautifulSoup
import math
import mojimoji
import time
import threading

#初期設定
res = []
lunch_value = []
hints = []
score = 0
click_times = 0
with open("/home/haruki/array_output4.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        res.append(line)

bg_color = "#20b2aa" #全体の背景色:lightseagreen
hl_color= "#20b2fa" #https://www.colordic.org/
abg_color = "#00ced1"   #ラジオボタン選択時背景色:darkturquoise
new_res = []   #ランダムに０から１９９までの数を入れる。 出題がかぶらないように
print("初期化new_res",new_res)
num_ramdom = 0
for num_ramdom in range(200):
   new_res.append(num_ramdom)
random.shuffle(new_res)
print("シャッフル後new_res",new_res)
print("new_resの個数",len(new_res))

base = tk.Tk() #問題画面を作成
base.title("国旗当てクイズ")
base.geometry("550x550")
base.configure(
      bg=bg_color,  # 背景色を設定
      cursor="hand2",  # カーソル形状を設定
      borderwidth=1,  # 枠の太さを設定
      highlightbackground="#ffffff",   #非フォーカス時背景色
      relief="flat"  # 枠のスタイルを設定
   )
number = 0
title_text_sub1 = "さぁーやってまいりました！記念すべき第"
title_text_sub2 = str(number+1)
title_text_sub3 = "問(* ՞ټ՞)"
title_text_sub4 = "問((≡･♀･≡))"
title_text = title_text_sub1+title_text_sub2+title_text_sub4
Title = tk.Label(base, text=title_text, font=("MSゴシック", "14"), bg=bg_color)
title_text2 = "この国旗のどこの国のでしょうか☆(✿✪‿✪｡)♡？"
Title2 = tk.Label(base, text=title_text2, font=("MSゴシック", "14"), bg=bg_color)

radio_value = tk.IntVar()
radio_value.set(-1)

"""
def random_num(): #ランダムで正解の数を選出
   global num
   num = random.randint(0, 200)
   return num
"""

def random_num(number):   #問題の番号を決める。numに出題番号をいれて出題するため
   print("random_num(number)内のnumber",number)
   print("random_num(number)内のnew_res",new_res)
   #print("random_num(number)内の関数前num",num)
   num = new_res[number]
   print("random_num(number)内の関数後num",num)
   return num

def random_question(num):  #numを引数にして四択に使う数を選出
   global lunch_value
   lunch = []
   numless_new_res = []
   for copy_new_res in new_res:
      numless_new_res.append(copy_new_res)
   print("numless同期後new_res",new_res)
   numless_new_res.remove(num) #正解のnumを除いたリストから3つの数字をチョイス
   print("numless_remove同期後new_res",new_res)
   lunch = random.sample(numless_new_res, k=3)
   numless_new_res.append(num)
   print("numless_remove後append,new_res",new_res)
   print('lunch',lunch)
   lunch.append(num)
   print('numをappendした後lunch',lunch)
   lunch2 = {}
   lunch2 = set(lunch) #番号をバラバラにするためにsetに入れる
   print("出題国",res[num][0])
   print("random_question(num)内のnumber",number)
   lunch_value = [[0 for _ in range(2)] for _ in range(4)]
   print("lunch_value",lunch_value)
   an=0
   print("lunch2=",lunch2)
   for lunch_num in lunch2:
      lunch_value[an][0] = lunch_num
      if len(res[lunch_num][0]) > 12:
         hankaku = res[lunch_num][0]
         chg_value = mojimoji.zen_to_han(hankaku)
         lunch_value[an][1] = chg_value
         print("半角に変換完了",lunch_value[an][1])
         an += 1
         continue
      lunch_value[an][1] =res[lunch_num][0]
      an += 1
   print(lunch_value)
   return lunch_value

def hint_creat(num): #ヒントを格納
   hint1 = res[num][3]
   hint2 = hint1.replace("\\n","")
   hint3 = hint2.replace(",","")
   hint4 = hint3.replace("'","")
   hint41 = hint4.replace("[1]","")
   hint42 = hint41.replace("[1]","")
   hint43 = hint42.replace("[2]","")
   hint44 = hint43.replace("[3]","")
   hint45 = hint44.replace("[4]","")
   hint46 = hint45.replace("[5]","")
   hint47 = hint46.replace("[6]","")
   hint48 = hint47.replace("[7]","")
   hint49 = hint48.replace("[8]","")
   hint50 = hint49.replace("[9]","")
   hint51 = hint50.replace("[10]","")
   hint52 = hint51.replace("[11]","")
   hint53 = hint52.replace("[12]","")
   hint54 = hint53.replace("[13]","")
   hint5 = hint54.replace("[","")
   hint6 = hint5.replace("]","")
   hint7 = hint6.replace("{","")
   hint8 = hint7.replace("}","")
   hints = hint8
   return hints

num = random_num(number)
print("num",num)
lunch_value = random_question(num)
hints = hint_creat(num)

btn1 = tk.Radiobutton(base,text = lunch_value[0][1], variable = radio_value, value = lunch_value[0][0] )
btn2 = tk.Radiobutton(base,text = lunch_value[1][1], variable = radio_value, value = lunch_value[1][0] )
btn3 = tk.Radiobutton(base,text = lunch_value[2][1], variable = radio_value, value = lunch_value[2][0] )
btn4 = tk.Radiobutton(base,text = lunch_value[3][1], variable = radio_value, value = lunch_value[3][0] )
btn1.configure(bg=bg_color,highlightcolor=hl_color,width=20,anchor = 'w',cursor="hand2",highlightthickness=0,activebackground=abg_color,relief="flat" )  
btn2.configure(bg=bg_color,highlightcolor=hl_color,width=20,anchor = 'w',cursor="hand2",highlightthickness=0,activebackground=abg_color,relief="flat" )
btn3.configure(bg=bg_color,highlightcolor=hl_color,width=20,anchor = 'w',cursor="hand2",highlightthickness=0,activebackground=abg_color,relief="flat" )
btn4.configure(bg=bg_color,highlightcolor=hl_color,width=20,anchor = 'w',cursor="hand2",highlightthickness=0,activebackground=abg_color,relief="flat" )
go_btn = tk.Button(base,font=("Ubuntu", "14", "bold"), text='GO♬(*◔‿◔)♡',bg=bg_color,activebackground=abg_color, command=lambda:click(num))

def display_image_from_url(url):    #国旗イメージをwikiから摂ってくる
   print("URL=",url)
   if url ==  'last':
      url = 'https://pbs.twimg.com/media/D95SsnEUEAEkHHH.png'
   try:
      headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }
      request = urllib.request.Request(url, headers=headers) #https://qiita.com/hone-git/items/4f254c4599cb06f8a549を参照
      with urllib.request.urlopen(request) as u:
         raw_data = u.read()
   except Exception as e:
      print(f"Error fetching image: {e}")
      return
   try:
      image = Image.open(io.BytesIO(raw_data))
      photo = ImageTk.PhotoImage(image)
   except Exception as e:
      print(f"Error opening image: {e}")
      return
   return photo

def go(): #クイズの一問目を出題
   Title.pack(pady=10, padx=10)
   Title2.pack(pady=10, padx=10)
   label.pack(pady=30, padx=30)
   btn1.place(x=100,y=30)
   btn1.pack(pady=5, padx=30)
   btn2.pack(pady=5, padx=30)
   btn3.pack(pady=5, padx=30)
   btn4.pack(pady=5, padx=30)
   go_btn.pack(pady=30, padx=30)
   score_window_point.pack()
   global map_img
   global next_img
   map_img = display_image_from_url(res[num][4]) #地図をwikiから採って来るためにglobalの変数に入れないとだめ
   next_img = display_image_from_url(res[new_res[number+1]][1])
   print("go内num=",num)
   print("go内new_res[number]=",new_res[number])
   print("go内img=",img)
   print("go内map_img=",map_img)
   print("go内next_img=",next_img)
   base.mainloop()
   
def go_chg(img,number):  #2問目以降を出題
   radio_value.set(-1)
   label.config(image = img)
   print("最終問題チェック",number)
   if number <= 199:
      title_text = "それでは第",number+1,"問！"
   else:
      title_text = "おつかれ様＼(^o^)／"
      title_text2 = '200問終了^_^'
      base.geometry("900x900")
      Title.config(text = title_text)
      Title2.config(text = title_text2)
      btn1.pack_forget()
      btn2.pack_forget()
      btn3.pack_forget()
      btn4.pack_forget()
      #go_btn.pack_forget()
      return
   Title.config(text = title_text)
   print('go_chg(img,number)内lunch_value',lunch_value)
   btn1.config(text = lunch_value[0][1], variable = radio_value, value = lunch_value[0][0] )
   btn2.config(text = lunch_value[1][1], variable = radio_value, value = lunch_value[1][0] )
   btn3.config(text = lunch_value[2][1], variable = radio_value, value = lunch_value[2][0] )
   btn4.config(text = lunch_value[3][1], variable = radio_value, value = lunch_value[3][0] )
   go_btn.config(state="normal")
   #time.sleep(10.5)
   

def link_click(url):
    import webbrowser
    webbrowser.open_new(url)

def sub_window(nu): #正解の画面の設定
   global score
   sub_window = tk.Toplevel(base)
   sub_window.title('GoodJob!!')
   correct_text11 = 'Good(´∇`)Job!!'
   correct_text1 = 'YES!'
   correct_text2 = res[nu][0]
   correct_text3 = 'です！場所はコチラ'
   correct_text = correct_text1+correct_text2+correct_text3
   tk.Label(sub_window, text =correct_text11,bg=bg_color,font=("Ubutu", 14)).pack(pady=12, padx=12)
   tk.Label(sub_window, text =correct_text,bg=bg_color,font=("Ubutu", 10)).pack(pady=5, padx=5)
   map=tk.Label(sub_window,image=map_img,bg=bg_color)
   map.pack(pady=15, padx=30)
   tk.Label(sub_window,image=img,bg=bg_color).pack(pady=10, padx=100)
   tk.Button(sub_window, command=lambda:next_quiz(sub_window),bg=bg_color,activebackground=abg_color, text='次の問題へ').pack(pady=10, padx=10)
   #tk.Button(sub_window, command=sub_window.destroy,bg=bg_color,activebackground=abg_color, text='閉じる').pack(pady=10, padx=10)
   link=tk.Label(sub_window,text="wikiへいく",fg="blue",bg=bg_color,activebackground=abg_color,cursor="hand1")
   link.pack()
   link.bind("<Button-1>",lambda e:link_click(res[nu][2]))
   jpn_url = "https://earth.google.com/web/search/%e6%97%a5%e6%9c%ac/@36.21520551,138.22347208,1117.00176737a,113948.7741573d,35y,-0h,0t,0r/data=CnUaRxJBCiUweDM0Njc0ZTBmZDc3ZjE5MmY6MHhmNTQyNzVkNDdjNjY1MjQ0Gcu3Pqw3GkJAIfSLEvQXSGFAKgbml6XmnKwYAiABIiYKJAnt-CGuq8E5QBHs-CGuq8E5wBltntkB4H9IQCH2CsH9idFNwEICCAE6AwoBMEICCABKDQj___________8BEAA"
   #link2=tk.Label(sub_window,text="日本へいく",fg="blue",bg=bg_color,activebackground=abg_color,cursor="hand1")
   #link2.pack()
   #link2.bind("<Button-1>",lambda e:link_click(jpn_url))
   global number
   number += 1
   if number == 200:
      print('これが最後の問題です')
      sub_window.configure(
         bg=bg_color,  # 背景色を設定
         cursor="hand2",  # カーソル形状を設定
         borderwidth=1,  # 枠の太さを設定
         highlightbackground="#ffffff",   #非フォーカス時背景色
         relief="flat"  # 枠のスタイルを設定
      )
      points = score_plus(click_times)
      score += points
      score_window_point.config(text=score)
      return
   print('sub_window(nu)内number',number)
   global num
   global hints
   global lunch_value
   print('sub_window(nu)内global_num1',num)
   num = new_res[number]
   print('sub_window(nu)内global_num2',num)
   lunch_value = random_question(num)
   hints = hint_creat(num)
   print("sub_window(nu)内hints=",hints)
   
   sub_window.configure(
      bg=bg_color,  # 背景色を設定
      cursor="hand2",  # カーソル形状を設定
      borderwidth=1,  # 枠の太さを設定
      highlightbackground="#ffffff",   #非フォーカス時背景色
      relief="flat"  # 枠のスタイルを設定
   )
   points = score_plus(click_times)
   score += points
   score_window_point.config(text=score)

def sub_window_hint(hint): #ヒント画面の設定
   sub_window = tk.Toplevel(base)
   sub_window.title('ﾋﾝﾄ(¯(ｴ)¯)ﾉ')
   print('sub_window_hint内hint',hint)
   hint_len = len(hint)
   hint_len2 =math.ceil((hint_len/10)*5)
   hint_len3 =math.ceil(hint_len)+hint_len2+70
   width = str(hint_len3) 
   higth = "400x"
   xyz = "+100+100"
   size = higth+width+xyz
   print("geo=",size)
   sub_window.geometry(size) # 幅400px、高さ500px、位置は(500, 100)
   tk.Label(sub_window, text=hint, wraplength=330,justify="left", font=("Ubuntu", 12), bg=bg_color, fg="darkslategray",pady=5, padx=5).pack(pady=15, padx=30)
   tk.Button(sub_window, command=sub_window.destroy,bg=bg_color,activebackground=abg_color,font=("Ubuntu", 13), text='Close⊂(･▲･)⊃').pack()
   sub_window.configure(
      bg=bg_color,  # 背景色を設定
      cursor="hand2",  # カーソル形状を設定
      borderwidth=1,  # 枠の太さを設定
      highlightbackground="#ffffff",   #非フォーカス時背景色
      relief="flat"  # 枠のスタイルを設定
   )
   
def click(a):
   global click_times
   value = radio_value.get()
   if a == value:
      click_times += 1
      print("click_times=",click_times)
      global num
      go_btn.config(state="disabled")
      sub_window(num)
   elif value == -1:
      hint = msg.showwarning('з･)ぷっ','~(¯▽¯~)どれかえらんで(~¯▽¯)~')
   else:
      click_times += 1
      print("click_times=",click_times)
      hint = msg.askyesno('(¯┰¯;)ゞ','ﾏﾁｶﾞｴ(¯┰¯;)ゞヒントを見る？')
      if hint == True:
         global hints
         sub_window_hint(hints)
   

def next_quiz(window):
   #global num
   #global hints
   #global number
   #global lunch_value
   
   #hints= []
   #number += 1
   #num = random_num(number)
   #lunch_value = random_question(num)
   #hints = hint_creat(num)
   global img
   global next_img
   img = next_img
   print("next_quiz内go_chg前next_img=",next_img)
   print("next_quiz内go_chg前number=",number)
   go_chg(img,number)
   global map_img
   last = ''
   map_img = display_image_from_url(res[num][4]) #地図をwikiから採って来るためにglobalの変数に入れないとだめ
   if number >= 199:
      next_img = display_image_from_url('last')
   else:
      next_img = display_image_from_url(res[new_res[number+1]][1])
   #imglist = []
   #imglist.append([map_img,next_img])
   print("next_quiz内map_img=",map_img)
   print("next_quiz内next_img=",next_img)
   window.destroy()
   #return imglist
   
def score_plus(num): #スコアの加算
   global click_times
   max_points = 100
   points = max_points/num
   click_times = 0
   return points

img = display_image_from_url(res[num][1]) #国旗をwikiから採って来るためにglobalの変数に入れないとだめ
label = tk.Label(base, image = img,bg=bg_color) #国旗を表示する枠
score_window = tk.Toplevel(base)
score_window.title('score')
score_window_point = tk.Label(score_window,text=score)
go()
map_img = display_image_from_url(res[num][4]) #地図をwikiから採って来るためにglobalの変数に入れないとだめ
if number == 200:
      next_img = display_image_from_url('last')
else:
   print('go()後のelse内next_img',next_img)
   next_img = display_image_from_url(res[number][1])


# creating labels and Run the Tkinter event loop 
   
  
   
