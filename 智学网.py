from zhixuewang import Zhixuewang
import zhixuewang.exam
user = input('user:')
password =input('psword:')
zxw = Zhixuewang(user, password)
grades = zxw.get_self_grade()
score = 0
#print(list(grades[0]))#['subjectName'])
for grade in grades:
       if(grade.subjectName=='语文' or grade.subjectName=='数学' or grade.subjectName=='英语' ):
              score+=grade.score
       if(grade.subjectName=='政治' or grade.subjectName=='历史'):
              if(grade.score>=85):
                     score+=10
              elif(grade.score>=70):
                     score+=8
              elif(grade.score>=60):
                     score+=6
              else:
                     score+=4
       if(grade.subjectName=='物理' ):
              score+=grade.score*0.9
       if(grade.subjectName=='化学'):
              score+=grade.score*0.6
       print('科目:',grade.subjectName,'班级最高分:',grade.classRank.highScore,'年段最高分',grade.gradeRank.highScore)
       print('成绩:',grade.score)
       print('班级排名:',grade.classRank.rank)
       print('当前综合分为:',score)
