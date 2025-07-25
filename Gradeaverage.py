def calculate_average(scores):
    average = sum(scores) / len(scores)
    return average

def check_pass_fail(average, pass_mark=40):
    if average >= pass_mark:
        return "Pass"
    else:
        return "Fail"

if __name__ == "__main__":
    print("Enter 5 test scores:")
    scores = []
    for i in range(5):
        score = float(input(f"Score {i+1}: "))
        scores.append(score)

    average_score = calculate_average(scores)
    result = check_pass_fail(average_score)

    print(f"\nAverage Score: {average_score:.2f}")
    print(f"Result: {result}")
