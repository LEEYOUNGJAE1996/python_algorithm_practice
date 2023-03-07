from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

# 퀴즈 묶음 만들기
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(text=question_text, answer=question_answer))


quizbrain = QuizBrain(question_bank)

while not quizbrain.finish():
    quizbrain.go_quiz()
    result = quizbrain.correct(input(">>"))
    print(result)
    print(quizbrain.current_score(result))
print("You've complited quiz game")
print(f"Your score is :{quizbrain.score}")
