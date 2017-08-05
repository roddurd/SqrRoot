def parse(input):
        try:
                return int(input)
        except:
                return "Error";

def cost(guess, num):
        return guess * guess - num;
def guessTheSquare():
        number = "Error"
        keepGuessing = "yes"
        while (keepGuessing == "yes" or keepGuessing == "ya"):
                number = input("Enter a valid whole number: ")
                while (parse(number) == "Error"):
                        number = input("Enter a valid whole number: ")
                        parse(number)
                number = parse(number)
                guess = 0;
                alpha = 0.001
                for i in range(0, 3000):
                        if (abs(cost(guess, number))<0.00000000001):
                                if (abs(round(guess) - guess)<0.00000000001):
                                        guess = round(guess)
                        else:
                                guess = guess - alpha * cost(guess, number)

                print("Final guess: " + str(guess))
                keepGuessing = input("Can I try another one? Yes or no: ")

guessTheSquare();