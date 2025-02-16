from PyQt5.QtWidgets import QApplication, QButtonGroup
from PyQt5.QtCore import QTimer
import sys
from memo___card_layout import window, lb_question, lb_right_answer, lb_result, gb_question, gb_answer, \
    btn_next, btn_rest, btn_menu, btn_back, sp_rest, rb_ans1, rb_ans2, rb_ans3, rb_ans4
from memo___app import menu_win
from random import choice, shuffle

# Створюємо QApplication перед створенням будь-якого QWidget
app = QApplication(sys.argv)

class Question:
    """Клас для зберігання запитань і підрахунку правильних відповідей."""
    def init(self, question, answer, wrong1, wrong2, wrong3):
        self.question = question
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.count_ask = 0
        self.count_right = 0

    def got_right(self):
        """Фіксує правильну відповідь."""
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        """Фіксує неправильну відповідь."""
        self.count_ask += 1


questions = [
    Question('Яблуко', 'apple', 'application', 'pineapple', 'apply'),
    Question('Дім', 'house', 'horse', 'hurry', 'hour'),
    Question('Миша', 'mouse', 'mouth', 'muse', 'museum'),
    Question('Число', 'number', 'digit', 'amount', 'summary')
]

RadioGroup = QButtonGroup()
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
for rb in radio_buttons:
    RadioGroup.addButton(rb)


class Quiz:
    """Клас для управління грою."""
    def init(self):
        self.cur_q = None
        self.new_question()

    def new_question(self):
        """Вибирає нове запитання та перемішує варіанти відповідей."""
        self.cur_q = choice(questions)
        lb_question.setText(self.cur_q.question)
        lb_right_answer.setText(self.cur_q.answer)
        answers = [self.cur_q.answer, self.cur_q.wrong1, self.cur_q.wrong2, self.cur_q.wrong3]
        shuffle(answers)
        for rb, text in zip(radio_buttons, answers):
            rb.setText(text)
        RadioGroup.setExclusive(False)
        for rb in radio_buttons:
            rb.setChecked(False)
        RadioGroup.setExclusive(True)

    def check_answer(self):
        """Перевіряє відповідь користувача."""
        for answer in radio_buttons:
            if answer.isChecked():
                if answer.text() == lb_right_answer.text():
                    self.cur_q.got_right()
                    lb_result.setText('✅ Вірно!')
                else:
                    lb_result.setText('❌ Не вірно!')
                    self.cur_q.got_wrong()
                break
        else:
            lb_result.setText('❌ Ви не обрали відповідь!')
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Наступне запитання')

    def next_question(self):
        """Змінює запитання."""
        self.new_question()
        gb_question.show()
        gb_answer.hide()
        btn_next.setText('Відповісти')


quiz = Quiz()

def click_ok():
    """Обробляє натискання кнопки 'Відповісти' / 'Наступне запитання'."""
    if btn_next.text() == 'Відповісти':
        quiz.check_answer()
    else:
        quiz.next_question()


btn_next.clicked.connect(click_ok)


def rest():
    """Ховає вікно на певний час, потім знову показує."""
    window.hide()
    n = sp_rest.value() * 60000
    QTimer.singleShot(n, window.show)


btn_rest.clicked.connect(rest)


def menu_generation():
    """Перехід у меню."""
    menu_win.show()
    window.hide()


btn_menu.clicked.connect(menu_generation)


def back_menu():
    """Повернення з меню."""
    menu_win.hide()
    window.show()


btn_back.clicked.connect(back_menu)


if name == "main":
    # Це найважливіший момент - обов'язково спочатку створіть QApplication
    app = QApplication(sys.argv)  # Це викликає QApp перед QWidget

    # Показуємо вікно після ініціалізації
    window.show()

    app.exec_()  # Запуск головного циклу подій