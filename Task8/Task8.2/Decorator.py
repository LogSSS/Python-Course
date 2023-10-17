from typing import Callable, Any
import re


class Decorator:

    def makeBold(self: Callable) -> Callable[[str], None]:
        def wrapped(str: str) -> None:
            str = "<b>" + str + "</b>"
            self(str)

        return wrapped

    def makeItalic(self: Callable) -> Callable[[str], None]:
        def wrapped(str: str) -> None:
            str = "<i>" + str + "</i>"
            self(str)

        return wrapped

    def palindrome(self: Callable) -> Callable[[str], bool]:
        def wrapped(str: str) -> bool:
            str = re.sub(r'[^a-zA-Zа-яА-Я]', '', str).lower()
            return self(str)

        return wrapped

    def check(self: Callable) -> Callable[[dict], str | dict]:
        def wrapped(dict: dict) -> str | dict:
            if len(set(dict.values())) != len(dict.values()):
                return "Неможливо здійснити обмін через втрату даних"
            return self(dict)

        return wrapped

    def validate(self: Callable) -> Callable[[Any], bool]:
        def wrapped(arr: Any) -> bool:
            if type(arr) == str:
                arr = list(arr)
            if type(arr) == int or type(arr) == float:
                arr = list(str(arr).replace(".", "").replace("-", ""))
            return self(arr)

        return wrapped
