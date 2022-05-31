class GuessingGame:
    def __init__(self, answer):
        self.answer = answer
        self.last_guess = None
    
    def solved(self):
        return self.last_guess == self.answer
    
    def guess(self, user_guess):
        if self.answer == self.last_guess:
            return f"You already solved it. The answer was {self.last_guess}!"
        elif user_guess < self.answer:
            self.last_guess = user_guess
            return "Low"
        elif user_guess > self.answer:
            self.last_guess = user_guess
            return "High"
        elif user_guess == self.answer:
            self.last_guess = user_guess
            return "Correct!"
        
game = GuessingGame(10)

print(game.guess(5))
print(game.guess(20))
print(game.solved())
print(game.guess(10))
print(game.solved())
print(game.guess(4))