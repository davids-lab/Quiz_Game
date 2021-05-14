class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.puntaje = 0

    def next_question(self):
        pregunta = self.question_list[self.question_number]
        self.question_number += 1
        respuesta_usuario = input(f"Q.{self.question_number} - {pregunta.text} (true/false): ").lower()
        self.check_answer(respuesta_usuario, pregunta.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, rta_usuario, rta_correcta):
        if rta_usuario.lower() == rta_correcta.lower():
            print("¡Muy bien! Acertarste")
            self.puntaje += 1
        else:
            print("Respuesta incorrecta")
        print(f"Respuesta correcta: {rta_correcta}")
        print(f"Puntaje actual:{self.puntaje}/{self.question_number}")
        print("\n")

