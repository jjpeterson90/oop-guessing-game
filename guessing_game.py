class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.last_guess = None
    
    def solved(self):
        print(self.last_guess == self.answer)
    
    def guess(self, user_guess):
        if self.answer == self.last_guess:
            print(f"You already solved it. The answer was {self.last_guess}!")
        elif user_guess < self.answer:
            print("Low")
        elif user_guess > self.answer:
            print("High")
        elif user_guess == self.answer:
            print("Correct!")
        self.last_guess = user_guess
        
game = GuessingGame(10)

game.guess(5)
game.guess(20)
game.solved()
game.guess(10)
game.solved()
game.guess(4)