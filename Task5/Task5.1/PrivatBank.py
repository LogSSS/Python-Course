import requests as rq
import json


def getCourse() -> dict:
    return json.loads(rq.get("https://api.privatbank.ua/p24api/pubinfo?json&amp;exchange&amp;coursid=5&amp").text)


def USDtoUAH() -> float:
    return float(getCourse()[1]["buy"])


def EURtoUAH() -> float:
    return float(getCourse()[0]["buy"])


def UAHtoUSD() -> float:
    return float(getCourse()[1]["sale"])


def UAHtoEUR() -> float:
    return float(getCourse()[0]["sale"])
