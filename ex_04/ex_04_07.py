def computegrade(score):
    """
    Compute grade based on the given score.

    Args:
    score (float): The score for which the grade is to be computed.

    Returns:
    str: The grade as a string.
    """
    if score < 0.0 or score > 1.0:
        return 'Invalid score'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'

# Example usage
score_input = input("Enter a score between 0.0 and 1.0: ")
try:
    score = float(score_input)
    grade = computegrade(score)
    print(f"The grade for the score {score} is: {grade}")
except ValueError:
    print("Please enter a numeric value for the score.")
