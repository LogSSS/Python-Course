class Student:

    def __init__(self, name: str, marks: dict[str:list[int]] = None) -> None:
        self.name = name
        self.marks = marks or {}

    def __str__(self) -> str:
        return f'{self.name} {self.marks}'

    def subject(self) -> list[str]:
        return list(self.marks.keys())

    def markBySubject(self, subject: str) -> list[int]:
        if subject in self.marks:
            return self.marks[subject]
        else:
            return []

    def averageMarkBySubject(self, subject: str) -> float:
        if subject in self.marks:
            return sum(self.marks[subject]) / len(self.marks[subject])
        else:
            return 0.0

    def averageMark(self) -> float:
        if not self.marks:
            return 0.0
        return sum([sum(self.marks[subject]) / len(self.marks[subject]) for subject in self.marks]) / len(self.marks)

    def isCredited(self) -> bool:
        if not self.marks:
            return False
        return all([self.averageMarkBySubject(subject) >= 4.0 for subject in self.marks])

    def addSubject(self, subject: str, marks: list[int]) -> None:
        if subject not in self.marks:
            self.marks[subject] = marks
        else:
            self.marks[subject] += marks

    def addMark(self, subject: str, mark: int) -> None:
        if subject not in self.marks:
            self.marks[subject] = [mark]
        else:
            self.marks[subject].append(mark)

    def calculate_average(self) -> dict[str, float]:
        averages = {'Name': self.name}
        for subject, marks_list in self.marks.items():
            if marks_list:
                average_mark = sum(marks_list) / len(marks_list)
            else:
                average_mark = 0.0
            averages[subject] = average_mark
        return averages
