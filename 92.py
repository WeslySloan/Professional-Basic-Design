if __name__ == '__main__':
    students = []
    passed = []

    while True:
        try:
            line = input()
            name, m1, m2, quiz = line.split()
            avg = (int(m1) + int(m2) + int(quiz)) / 3
            students.append((name, avg))
            if avg >= 60:
                passed.append(name)
        except EOFError:
            break
    passed.sort()
    print(len(passed))
    for student in passed:
        print(student)
