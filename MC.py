from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)



class Question():
    def __init__(self, ques, right_answer, wrong1, wrong2, wrong3):
        self.ques = ques
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []

questions_list.append(Question("как переводится 我不知道?", "я не знаю", "черный чай", "китай", "картошка"))
questions_list.append(Question("какой первый елемент таблицы мендлеева?", "водород", "углерод", "кислород", "гелий"))
questions_list.append(Question("проверь свою удачу", "...", "...", "...", "..."))
questions_list.append(Question("наступне питання?", "да", "нет", "не знаю", "наверное"))
 

app = QApplication([])
window = QWidget()
window.resize(400, 400)
window.setWindowTitle("Memory card")  

question = QLabel("переклади англійською")   
btn_ok = QPushButton("Answer")                




 
RadioGroupBox = QGroupBox("Варіанти відповідей")   


 
rbtn1 = QRadioButton("Bus")
rbtn2 = QRadioButton("Car")
rbtn3 = QRadioButton("Tax")
rbtn4 = QRadioButton("Shu")


 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)




 
ans_h_layout = QHBoxLayout()   
ans_v1_layout = QVBoxLayout()  
ans_v2_layout = QVBoxLayout()  


 
ans_v1_layout.addWidget(rbtn1)
ans_v1_layout.addWidget(rbtn2)
ans_v2_layout.addWidget(rbtn3)
ans_v2_layout.addWidget(rbtn4)


ans_h_layout.addLayout(ans_v1_layout)
ans_h_layout.addLayout(ans_v2_layout)


 
RadioGroupBox.setLayout(ans_h_layout)


 
AnsGroupBox = QGroupBox("Результат тесту")


lb_Result = QLabel("Відповідь вірна?")         
lb_Correct = QLabel("відповідь буде тут!")      


 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)





v_line = QVBoxLayout()  
h1_line = QHBoxLayout() 
h2_line = QHBoxLayout()
h3_line = QHBoxLayout() 


h1_line.addWidget(question, alignment=Qt.AlignCenter)


 
h2_line.addWidget(RadioGroupBox)
h2_line.addWidget(AnsGroupBox)


h3_line.addStretch(1)
h3_line.addWidget(btn_ok, stretch=2)
h3_line.addStretch(1)


v_line.addLayout(h1_line, stretch=2)
v_line.addLayout(h2_line, stretch=8)
v_line.addStretch(1)
v_line.addLayout(h3_line, stretch=1)
v_line.addStretch(1)



AnsGroupBox.hide()



def show_result():
    """Показати блок із результатом"""
    RadioGroupBox.hide()                    
    AnsGroupBox.show()                      
    btn_ok.setText("Наступне запитання")    




def show_question():
    """Показати нове питання"""
    AnsGroupBox.hide()                      
    RadioGroupBox.show()                    
    btn_ok.setText("Answer")                

 
    RadioGroup.setExclusive(False)           
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)           


answers = [rbtn1, rbtn2, rbtn3, rbtn4]




 
def ask(q: Question):
    """Встановлює нове запитання та перемішує варіанти"""
    shuffle(answers)                         


     
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)


    
    question.setText(q.ques)
    lb_Correct.setText(q.right_answer)


     
    show_question()




 
def show_correct(res):
    """Показує результат ('правильно' або 'неправильно')"""
    lb_Result.setText(res)   
    show_result()             




 
def check_answer():
    """Перевіряє, яку відповідь вибрав користувач"""
    if answers[0].isChecked():                
        show_correct("Correct!")             

        window.score += 1

        print("Пройшли запитань", window.total, "Скільки балів", window.score)
        print("Raiting", window.score / window.total * 100, "%")


    else:
        
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("INCORRECT!!")

            print("Raiting", window.score / window.total * 100, "%")



 
def next_question():
    window.total += 1

    print("Пройшли запитань", window.total, "Скільки балів", window.score)

    cur_question =  randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]   
    ask(q) 




 
def click_OK():
    if btn_ok.text() == "Answer":             
        check_answer()                 
    else:
        next_question()                     





 
btn_ok.clicked.connect(click_OK)


window.total = 0
window.score = 0

 
next_question()



 
window.setLayout(v_line)   


 
window.show()


 
app.exec()