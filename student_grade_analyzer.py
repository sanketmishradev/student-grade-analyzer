import statistics
import os

# ─────────────────────────────────────────
#  Student Grade Analyzer
#  Tech: Python (statistics, os modules)
# ─────────────────────────────────────────

GRADE_SCALE = [
    (90, "A+", "Outstanding"),
    (80, "A",  "Excellent"),
    (70, "B",  "Good"),
    (60, "C",  "Average"),
    (50, "D",  "Below Average"),
    (0,  "F",  "Fail"),
]

def get_grade(score):
    for threshold, grade, remark in GRADE_SCALE:
        if score >= threshold:
            return grade, remark
    return "F", "Fail"

def bar_chart(subjects, scores):
    print("\n📊 Score Bar Chart")
    print("─" * 45)
    max_score = 100
    bar_width = 30
    for subject, score in zip(subjects, scores):
        filled = int((score / max_score) * bar_width)
        bar = "█" * filled + "░" * (bar_width - filled)
        grade, _ = get_grade(score)
        print(f"  {subject:<15} {bar} {score:>3}% [{grade}]")
    print("─" * 45)

def analyze(students):
    print("\n" + "═" * 55)
    print("          📋  STUDENT GRADE REPORT")
    print("═" * 55)

    all_averages = []

    for student in students:
        name    = student["name"]
        subjects = student["subjects"]
        scores   = student["scores"]
        avg      = round(statistics.mean(scores), 2)
        grade, remark = get_grade(avg)
        highest  = max(scores)
        lowest   = min(scores)
        best_sub = subjects[scores.index(highest)]
        weak_sub = subjects[scores.index(lowest)]

        all_averages.append((name, avg, grade))

        print(f"\n  👤 Student : {name}")
        print(f"  📈 Average  : {avg}%  →  Grade: {grade}  ({remark})")
        print(f"  🏆 Best     : {best_sub} ({highest}%)")
        print(f"  ⚠️  Weakest  : {weak_sub} ({lowest}%)")
        bar_chart(subjects, scores)

    # ── Class Summary ──
    print("\n" + "═" * 55)
    print("          🏫  CLASS SUMMARY")
    print("═" * 55)
    avgs = [a for _, a, _ in all_averages]
    class_avg = round(statistics.mean(avgs), 2)
    topper = max(all_averages, key=lambda x: x[1])
    weakest = min(all_averages, key=lambda x: x[1])

    print(f"  Total Students : {len(students)}")
    print(f"  Class Average  : {class_avg}%")
    print(f"  🥇 Topper      : {topper[0]} ({topper[1]}% — {topper[2]})")
    print(f"  📉 Needs Help  : {weakest[0]} ({weakest[1]}% — {weakest[2]})")

    passed  = sum(1 for _, a, _ in all_averages if a >= 50)
    failed  = len(students) - passed
    print(f"  ✅ Passed      : {passed}  |  ❌ Failed: {failed}")
    print("═" * 55)

def input_students():
    students = []
    print("\n╔══════════════════════════════════╗")
    print("║   🎓 Student Grade Analyzer      ║")
    print("╚══════════════════════════════════╝\n")

    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("  ⚠️  Name cannot be empty.")
            continue

        subjects = []
        scores   = []
        print(f"\n  Enter subjects & scores for {name}:")
        print("  (type 'done' as subject name to finish)\n")

        while True:
            subject = input("    Subject name: ").strip()
            if subject.lower() == "done":
                if len(subjects) < 2:
                    print("  ⚠️  Please enter at least 2 subjects.")
                    continue
                break
            try:
                score = float(input(f"    Score for {subject} (0-100): "))
                if not 0 <= score <= 100:
                    raise ValueError
                subjects.append(subject)
                scores.append(score)
            except ValueError:
                print("  ⚠️  Enter a valid score between 0 and 100.")

        students.append({"name": name, "subjects": subjects, "scores": scores})
        print(f"\n  ✅ {name} added!\n")

    return students

def demo_mode():
    """Pre-loaded demo data so you can see output instantly."""
    return [
        {
            "name": "Rahul Shah",
            "subjects": ["Math", "Physics", "Chemistry", "English", "CS"],
            "scores":   [88, 76, 91, 65, 95],
        },
        {
            "name": "Priya Patel",
            "subjects": ["Math", "Physics", "Chemistry", "English", "CS"],
            "scores":   [72, 85, 68, 90, 78],
        },
        {
            "name": "Amit Kumar",
            "subjects": ["Math", "Physics", "Chemistry", "English", "CS"],
            "scores":   [45, 52, 38, 60, 55],
        },
    ]

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n  Choose mode:")
    print("  [1] Enter student data manually")
    print("  [2] Run with demo data\n")
    choice = input("  Your choice (1/2): ").strip()

    if choice == "1":
        students = input_students()
        if not students:
            print("\n  ⚠️  No students entered. Exiting.")
            return
    else:
        students = demo_mode()
        print("\n  ✅ Loaded demo data for 3 students...")

    analyze(students)

if __name__ == "__main__":
    main()
