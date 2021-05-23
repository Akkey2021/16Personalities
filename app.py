import streamlit as st

st.title('性格診断 ~内向的・外向的~')
st.write('''
## 次の6問に5段階で回答してください。
よくあてはまる場合には4を、まったく当てはまらない場合には0をつけてください。
''')




a= st.slider("問1 自己紹介に困ることはない",0,4,2)
b= st.slider("問2 外出するよりも家で過ごすほうが好きだ",0,4,2)
c= st.slider("問3 人と会話するときは、自分から話しかけることが多い",0,4,2)
d= st.slider("問4 多くの人と行動を共にした後はぐったりと疲れる",0,4,2)
e= st.slider("問5 新しいコミュニティの中に入っても早く馴染めるほうだ",0,4,2)
f= st.slider("問6 人前で話すとき必要以上に緊張してしまう",0,4,2)

if b==4:
    b=0
elif b==3:
    b=1

if d==4:
    d=0
elif d==3:
    d=1

if f==4:
    f=0
elif f==3:
    f=1

#st.write(b)

total = a+b+c+d+e+f

if st.checkbox('結果を見る'):
    if total < 13:
        st.write('あなたは内向的な性格です')
    else:
        st.write('あなたは外向的な性格です')

