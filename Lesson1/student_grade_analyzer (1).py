# Week 3 - Lesson 1
# Hands-on Exercise 1: Student Grade Analyzer

def get_grade(score):
    """Return the grade interpretation for a student's score."""
    if 90 <= score <= 100:
        return "Excellent"
    elif 80 <= score < 90:
        return "Very Good"
    elif 75 <= score < 80:
        return "Good"
    else:
        return "Failed"


def main():
    print("=" * 45)
    print("          STUDENT GRADE ANALYZER")
    print("=" * 45)

    # Ask how many students will be analyzed.
    while True:
        try:
            number_of_students = int(input("Enter number of students: "))
            if number_of_students > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    students = []

    # Collect each student's name and score.
    for i in range(number_of_students):
        print(f"\nStudent {i + 1}")
        name = input("Enter student name: ").strip()
        if not name:
            name = f"Student {i + 1}"

        while True:
            try:
                score = float(input("Enter score (0-100): "))
                if 0 <= score <= 100:
                    break
                print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid score. Please enter a number.")

        students.append({"name": name, "score": score})

    scores = [student["score"] for student in students]
    total_score = sum(scores)
    average_score = total_score / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    passed_students = sum(1 for score in scores if score >= 75)
    failed_students = len(scores) - passed_students

    print("\n" + "=" * 65)
    print("STUDENT RESULTS")
    print("=" * 65)
    print(f'{"Student Name":<25} {"Score":>8}  {"Status":<10} {"Grade"}')
    print("-" * 65)

    for student in students:
        score = student["score"]
        status = "Passed" if score >= 75 else "Failed"
        grade = get_grade(score)
        print(f'{student["name"]:<25} {score:>8.2f}  {status:<10} {grade}')

    print("-" * 65)
    print(f"Total Score       : {total_score:.2f}")
    print(f"Average Score     : {average_score:.2f}")
    print(f"Highest Score     : {highest_score:.2f}")
    print(f"Lowest Score      : {lowest_score:.2f}")
    print(f"Number Passed     : {passed_students}")
    print(f"Number Failed     : {failed_students}")
    print("=" * 65)


if __name__ == "__main__":
    main()
