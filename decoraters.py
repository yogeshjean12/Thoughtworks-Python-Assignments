
def string_1(arg):
    def outer():
        return arg()+" inner outer "
    return outer

def string_2(arg1):
    def inner():
        return " outer inner "+arg1()
    return inner

@string_1
@string_2
def string():
    return "inside"
print(string())