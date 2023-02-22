#%%
import numpy as np
import pandas as pd
import random,time

all_dic = { 'attach':['貼上'] , 'attain': ['獲得','獲取'], 'collapse':['倒塌'] , 'manner':['禮儀','禮節'], 
'insist':['堅持'],'resist':['抵抗'], 'assist':['協助','幫助'], 'staff':['員工'], 'betray':['背叛'], 'appreciate':['欣賞'],
'apologize':['道歉','致歉'],'attempt':['嘗試'],'adapt':['適應'],'inquire':['查詢'],'victims':['受害者'],'pollution':['汙染'],
'bother':['煩惱','打擾'], 'blame':['責備','責罵'],'confirm':['堅信','確認'],'crime':['犯罪'],'commit':['承諾'],'punish':['處罰'],
'composure':['鎮靜','沉著冷靜']}

# %%
count = 1
score = 0
detail_content = ''

print('想要答題數目')
question_number = int(input())
while count <= question_number :
    question,answer =random.choice(list(all_dic.items()))
    print(f'問題(請翻譯):{question}')
    input_answer = input()
    if input_answer in answer:
        score += 1
        result = 'O'
    else:
        result = 'X'

    detail_content += f'第{count}題，題目{question}，正確答案:{answer}，答題情形:{input_answer} ，結果{result}+\n'

    count +=1 
    time.sleep(0.5)
print(f'答對比例:{score}/{question_number},({score/question_number})')
print(detail_content)
time.sleep(100)
# %%
score