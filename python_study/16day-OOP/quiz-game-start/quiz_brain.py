from question_model import Question

# TODO: asking the questions

# TODO: checking if the answer was correct

# TODO: checking if we're the end of the quiz


class QuizBrain:
    def __init__(self, quiz_bank):
        self.count = 0
        self.score = 0
        self.quiz = quiz_bank

    def go_quiz(self):
        """현재 문제를 출력만 하는 메소드"""
        print(
            f"Q.{self.count+1}: {self.quiz[self.count].text}(True or False)")

    def correct(self, answer):
        """사용자가 입력한 값과 문제의 정답을 비교하여 boolean으로 결과를 반환
            그리고 다음 문제로 인덱스 1 추가"""
        if self.quiz[self.count].answer == answer:
            print("You got it right!")
            print(f"The correct answer was : {self.quiz[self.count].answer}")
            self.count += 1
            return True
        else:
            print("You worng")
            print(f"The correct answer was : {self.quiz[self.count].answer}")
            self.count += 1
            return False

    def finish(self):
        """문제가 끝났는지 확인하는 메서드"""
        if self.count == len(self.quiz):
            return True
        else:
            return False

    def current_score(self, result):
        """현재 점수를 표시하는 메서드"""
        if result == True:
            self.score += 1
            string = "Your current Score is : "
            string += str(self.score)
            string += "/"
            string += str(self.count)
            print(string)
        else:
            string = "Your current Score is : "
            string += str(self.score)
            string += "/"
            string += str(self.count)
        return string
