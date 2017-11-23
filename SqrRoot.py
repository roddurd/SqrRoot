def parse(input):
    try:
        return int(input)
    except:
        return "Error";
def cost(guess, num):
    return guess * guess - num;
def guessTheSquareRoot():
    number = "Error"
    keepGuessing = "yes"
    while (keepGuessing == "yes"):
        number = input("Enter a valid whole number: ")
        while (parse(number) == "Error"):
            number = input("Enter a valid whole number: ")
            parse(number)
        number = parse(number)
        guess = 0;
        alpha = 0.001
        for i in range(0, 5000):
            if i % 100 == 0:
                print("Guess " + str(i) + ": " + str(guess))
            if (abs(cost(guess, number)) < 0.001):
                if (abs(round(guess) - guess) < 0.001):
                    guess = round(guess)
                    break
            else:
                guess = guess - alpha * cost(guess, number)
        print("Final guess: " + str(guess))
        keepGuessing = input("Can I try another one? Yes or no: ")
guessTheSquareRoot();
