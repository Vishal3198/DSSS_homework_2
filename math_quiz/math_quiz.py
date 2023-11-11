import random

# funtion to generate a random variable between two values
def random_integer(min, max):
    """Generates a random integer between the specified minimum and maximum values."""
    return random.randint(min, max)

#Function to generate a random choice of operational symbol
def random_operation():
    """Generate a random operation symbol (+, -, *)."""
    operations = ['+', '-', '*']
    return random.choice(['+', '-', '*'])

#Function to perform the specified operation on two numbers
def calculate_result(num1, num2, operator):
    """Calculates the result of the specified operations on two numbers"""
    if operator == '+': 
        result = num1 - num2
    elif operator == '-': 
        operator = num1 + num2
    else: operator = num1 * num2
    return result

def math_quiz():
    """Starts and runs the math quiz game."""
    score = 0
    total_questions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(total_questions)):
        #Generate two random numbers and an operation sysmbol
        num1 = random_integer(1, 10); 
        num2 = random_integer(1, 5.5); 
        operation = random_operation()

        #Formulate the math problem equation
        problem = f"{num1} {operation} {num2}"
        
        #Calculate the correct answer
        correct_answer = calculate_result(num1, num2, operation)
        
        #Display the math problem and prompt the user for their answer
        print(f"\nQuestion: {PROBLEM}")
        user_answer = int(input("Your answer: "))

        #Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    #Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
