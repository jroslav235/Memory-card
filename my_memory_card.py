#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,  QLabel, QVBoxLayout, 
              QHBoxLayout, QPushButton, QRadioButton,
              QGroupBox, QButtonGroup)
#создание элементов интерфейса
app = QApplication([])
window = QWidget()
from random import randint,shuffle

#CОЗДАЕМ ПАНЕЛЬ ВОПРОСА
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
#
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
#
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

#создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2) 
AnsGroupBox.setLayout(layout_res)
#размещаем все виджеты в окне
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
#размещаем в одной строке обе панели, одна из них будет скрыватьсяб другая показываться:
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.show()
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
#теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

RadioGroup.setExclusive(False)
rbtn_1.setChecked(False)
rbtn_2.setChecked(False)
rbtn_3.setChecked(False)
rbtn_4.setChecked(False)
RadioGroup.setExclusive(True)

#fffff
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if 'Ответить' == btn_OK.test():
        show_result()
    else:
        show_question()        
#fffffffffffffffffff
from random import shuffle
answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно')
    print(int(window.score/window.total*100))
#класс вопрос и задача вопроса
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
#Вопросы
questions_list = []
questions_list.append(Question('Государственный язык Португалии', 'Португальский', 'Английский', 'Испанский', 'Французкий'))
questions_list.append(Question('Выбери перевод слова "переменная"','variable','variaction', 'variant', 'changing'))
questions_list.append(Question('Какой национальности нет', 'Смурфы', 'Энцы', 'Чульмцы', 'Алеуты'))
questions_list.append(Question('В каком году был создан первый телефон', '1876', '1923', '1763', '1879'))
questions_list.append(Question('Какой национальный напиток в Германии', 'пиво', 'coca-cola', 'морковный сок', 'квас'))
questions_list.append(Question('Какой язык програмирования мы изучаем', 'python', 'java', 'scratch', 'C++'))



def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) -1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.total = 0
window.score = 0
next_question()
window.show()
app.exec_()




















































































АРАХИ
АРАХИС
АРАХИС
АРАХИАРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС                             
АРАХИСАРАХИСАРАХИС
АРАХИС
АРААРАХИСХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХИС
ММ
АРАХИС
МАРАХИС
АРАХИС
АРАХИС
АРАХИС
АРАХ