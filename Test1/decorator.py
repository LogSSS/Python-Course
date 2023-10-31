def decorator(self):
    def wrapped(numb):
        numb = str(self(numb)) + ' grn'
        print(numb)

    return wrapped


@decorator
def Task3(bob):
    return bob * 2
