#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Crear una aplicación para memorizar información
#modulos
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout

#ventana
app = QApplication([])
widget_1 = QWidget()
widget_1.show()
v_line = QVBoxLayout()
widget_1.resize(400,200)

#Texto y alineación
question = QLabel("¿Cual es el país mas visitado por turistas?") 
question.show()
widget_1.setLayout(v_line)
v_line.addWidget(question, alignment = Qt.AlignCenter)

#Formulario y alineación
RadioGroupBox = QGroupBox("Opciones")
h_line = QHBoxLayout()
v_line.addLayout(h_line)
h_line.addWidget(RadioGroupBox)

#Opciones y alineación
rbtn_1 = QRadioButton("España")
rbtn_2 = QRadioButton("Italia")
rbtn_3 = QRadioButton("&Francia")
rbtn_4 = QRadioButton("Japón")
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

#Elementos de mensaje al responder, y botón
verdict = QLabel(".")
v_line.addWidget(verdict, alignment = Qt.AlignCenter)
answer1 = QLabel("La respuesta era Francia.")
answer1.show()
answer1.hide()
button = QPushButton("Responder")
v_line.addWidget(answer1, alignment = Qt.AlignCenter)
v_line.addWidget(button)


#Funcion de respuesta
def show_correct_answer():
    #RadioGroupBox.hide()
    #answer1.show()
    #verdict.show()
    

    if rbtn_3.isChecked():
        RadioGroupBox.hide()
        answer1.show()
        verdict.show()
        print("ugh")
        verdict.setText("¡Correcto!")
        button.setText("Siguente pregunta")
    elif rbtn_1.isChecked() or rbtn_2.isChecked() or rbtn_4.isChecked():
        RadioGroupBox.hide()
        answer1.show()
        verdict.show()
        verdict.setText("Incorrecto...")
        print("ayyayaya")
        button.setText("Siguente pregunta")
    else:
        print("nothing :(")
    
        
#Función llamada
button.clicked.connect(show_correct_answer)
app.exec_()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------