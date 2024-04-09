from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('The state language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
questions_list.append(Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
questions_list.append(Question('A traditional residence of the Yakut people', 'Urasa', 'Yurt', 'Igloo', 'Hut'))

app = QApplication([])

window = QWidget()
window.setWindowTitle("Memory card")

# Otazka

question = QLabel("Otazka")
button = QPushButton("Odpoved")

# Odpovede

RadioBoxGroup = QGroupBox("Odpovede")
rbtn_1 = QRadioButton("Moznost 1")
rbtn_2 = QRadioButton("Moznost 2")
rbtn_3 = QRadioButton("Moznost 3")
rbtn_4 = QRadioButton("Moznost 4")

# layout skupiny buttonov

layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()

layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)

layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)

layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

RadioBoxGroup.setLayout(layout_1)

# skupina buttonov

RadioButtons = QButtonGroup()
RadioButtons.addButton(rbtn_1)
RadioButtons.addButton(rbtn_2)
RadioButtons.addButton(rbtn_3)
RadioButtons.addButton(rbtn_4)

# Vysledok

AnsGroupBox = QGroupBox("Vysledky")
right_or_wrong = QLabel("Spravne")
answer = QLabel("Odpoved")

layout_ans = QVBoxLayout()

layout_ans.addWidget(right_or_wrong, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_ans.addWidget(answer, alignment=Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(layout_ans)

# layout okna

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioBoxGroup)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addWidget(button, stretch=2)

# hlavny layout

layout_main = QVBoxLayout()

layout_main.addLayout(layout_line1, stretch=2)
layout_main.addLayout(layout_line2, stretch=8)
layout_main.addStretch(1)
layout_main.addLayout(layout_line3, stretch=1)
layout_main.addStretch(1)
layout_main.setSpacing(5)

# Funkcie na prepinanie

def show_result():
    RadioBoxGroup.hide()
    AnsGroupBox.show()

    button.setText("Dalsia otazka")

def show_question():
    AnsGroupBox.hide()
    RadioBoxGroup.show()

    button.setText("Odpoved")

    RadioButtons.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioButtons.setExclusive(True)

# Funkcie na vyhodnotenie

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    answer.setText(q.right_answer)
    question.setText(q.question)

    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct("Spravne")
        window.score += 1
    else:
        show_correct("Nespravne")
    print("Štatistika: \n", "Celkový počet otázok: ", window.total, "\n", "Počet správnych odpovedí: ", window.score)
    print("Hodnotenie: ", (window.score / window.total * 100), "%")

def show_correct(textt):
    right_or_wrong.setText(textt)
    show_result()

def next_question():
    window.total += 1
    '''
    window.current_question += 1

    if window.current_question >= len(questions_list):
        window.current_question = 0
    '''
    # nahodna otazka
    current_question = randint(0, len(questions_list) - 1)
    
    q = questions_list[current_question]
    ask(q)
    # questions_list.remove(q)

def click_button():
    if button.text() == "Odpoved":
        check_answer()
    else:
        next_question()

# spustenie

button.clicked.connect(click_button)
window.setLayout(layout_main)

#window.current_question = -1
window.total = 0
window.score = 0

next_question()

window.resize(500, 400)
window.show()
app.exec()