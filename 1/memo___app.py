from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win = QWidget()

# Додаємо елементи для меню
lb_quest = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть вірну відповідь:')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь')

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

lb_header_stat = QLabel('Статистика')
lb_header_stat.setStyleSheet('font-size: 19px; font-weight: bold;')
lb_statistic = QLabel()

# Лейаути для розміщення елементів
vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

# Основний layout
h1_main = QHBoxLayout()
h1_main.addLayout(vl_labels)
h1_main.addLayout(vl_lineEdits)

menu_win.setLayout(h1_main)
menu_win.resize(400, 300)