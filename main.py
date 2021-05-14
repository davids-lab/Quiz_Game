from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

#Creando una lista de objetos
for elemento_lista in question_data:
    question_bank.append(Question(elemento_lista["question"], elemento_lista["correct_answer"]))

#Imprimiendo el objeto dentro de la lista con atributo text
# print(question_bank[1].text)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Terminaste el quiz")
print(f"Tu puntaje final es: {quiz.puntaje}/{quiz.question_number}")