class TrafficQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "A solid white line on the right edge of the highway slants in toward your left. This shows that:",
                "options": ["There is an intersection just ahead", "You are approaching a construction area", "You will be required to turn left just ahead", "The road will get narrower"],
                "answer": "The road will get narrower"
            },
            {
                "question": "What does a flashing yellow light mean?",
                "options": ["Merging traffic", "Proceed with caution", "Pedestrian crossing", "Come to a full stop"],
                "answer": "Proceed with caution"
            },
            {
                "question": "A diamon Shape sign is a",
                "options": ["Road Hazard Sign", "Interstate route site", "School crossing sign", "Speed limit sign"],
                "answer": "Road Hazard Sign"
            }
            # Add more questions here...
        ]
        self.score = 0

    def display_question(self, question_dict):
        print(question_dict["question"])
        for idx, option in enumerate(question_dict["options"], start=1):
            print(f"{idx}. {option}")
        user_answer = int(input("Enter your choice (1-4): "))
        return user_answer

    def check_answer(self, question_dict, user_answer):
        correct_answer = question_dict["options"].index(question_dict["answer"]) + 1
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {question_dict['answer']}")

    def start_quiz(self):
        print("Welcome to the Traffic Control Quiz!")
        print("Each question has 4 options. Enter the number corresponding to your choice.")
        print("Let's begin:")
        for question in self.questions:
            user_choice = self.display_question(question)
            self.check_answer(question, user_choice)
        print(f"You scored {self.score} out of {len(self.questions)}.")

# Start the quiz
if __name__ == "__main__":
    traffic_quiz = TrafficQuiz()
    traffic_quiz.start_quiz()
