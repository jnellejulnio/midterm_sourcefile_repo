raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
]

PASSING_GRADE = 75

student_scores = {}


for record in raw_records:

    fields = record.split(",")

    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    name = fields[0]

    try:
        scores = [int(score) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    if name == "" or len(scores) != 3:
        print(f"Skipped invalid record: {record}")
        continue

    student_scores[name] = scores


print("ORGANIZED STUDENT RECORDS")

for name in sorted(student_scores):
    scores = student_scores[name]
    print(f"{name}: {scores}")


ranking = []

passed_count = 0
failed_count = 0
sum_of_averages = 0


for name, scores in student_scores.items():

    if not scores:
        continue

    total = sum(scores)
    number_of_scores = len(scores)
    average = total / number_of_scores
    highest_score = max(scores)
    lowest_score = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    sum_of_averages += average

    result = (
        average,
        name,
        highest_score,
        lowest_score,
        remark
    )

    ranking.append(result)

ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

for rank, record in enumerate(ranking, start=1):

    average, name, highest_score, lowest_score, remark = record

    print(
        f"{rank:<5}"
        f"{name:<11}"
        f"{average:<9.2f}"
        f"{highest_score:<9}"
        f"{lowest_score:<8}"
        f"{remark}"
    )

if len(ranking) > 0:

    class_average = sum_of_averages / len(ranking)

    highest_ranked = ranking[0]

    lowest_ranked = ranking[-1]

    highest_average, highest_name, _, _, _ = highest_ranked
    lowest_average, lowest_name, _, _, _ = lowest_ranked

else:
    class_average = 0
    highest_name = "N/A"
    highest_average = 0
    lowest_name = "N/A"
    lowest_average = 0

print("\nCLASS SUMMARY")
print(f"Number of Students: {len(ranking)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")
print(f"Highest: {highest_name} - {highest_average:.2f}")
print(f"Lowest: {lowest_name} - {lowest_average:.2f}")