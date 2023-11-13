import random


def function_a(min_value, max_value):
    """Generate a random integer between min_value and max_value (inclusive)."""
    return random.randint(min_value, max_value)


def function_b():
    """Generate a random arithmetic operator (+, -, *)."""
    return random.choice(['+', '-', '*'])


def function_c(n1, n2, operator):
    """Calculate the result of the arithmetic operation specified by the given operator."""
    expression = f"{n1} {operator} {n2}"
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    else:
        result = n1 * n2
    return expression, result


def math_quiz():
    """Conduct a math quiz game."""
    score, total_questions = 0, 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1, n2, operator = function_a(1, 10), function_a(1, 5), function_b()

        problem, answer = function_c(n1, n2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0  # Assume wrong answer for invalid input

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
