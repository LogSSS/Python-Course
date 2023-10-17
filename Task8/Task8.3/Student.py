class Student:
    def __init__(self, name: str, credit: float) -> None:
        self.name = name
        self.__credit = credit

    def getCredit(self) -> str:
        if self.__credit < 50:
            return "Not credited"
        return "Credited"

    def setCredit(self, credit) -> None:
        if isinstance(credit, (list, tuple)):
            self.__credit = sum(credit)
        else:
            self.__credit = credit

    def deletter(self) -> None:
        self.__credit = 0
