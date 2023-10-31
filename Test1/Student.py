def Task2(dictStudent):
    bestStud(dictStudent)
    sameMarksStudents(dictStudent.copy())
    sameMarksStuff(dictStudent)


def bestStud(dictStudent):
    best_student = max(dictStudent, key=lambda x: sum(x['marks']))
    print('Best student is: ', best_student['name'], ' with marks: ', best_student['marks'])


def sameMarksStudents(dictStudent):
    bob = dictStudent.copy()
    for student in bob:
        student['marks'].copy().sort()

    same_marks = {}
    for student in bob:
        marks = tuple(student['marks'])
        if marks in same_marks:
            same_marks[marks].append(student['name'])
        else:
            same_marks[marks] = [student['name']]

    result = [group for group in same_marks.values() if len(group) > 1]

    print('Students with the same marks: ')
    for group in result:
        print(set(group))


def sameMarksStuff(dictStudent):
    marks = [student['marks'] for student in dictStudent]

    first_sublist = marks[0]
    equal_positions = []

    for i, sublist in enumerate(marks[1:]):
        if all(x == y for x, y in zip(first_sublist, sublist)):
            equal_positions.append(i + 1)

    print(equal_positions)
