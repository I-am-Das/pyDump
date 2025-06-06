def dec_fun(original_function):
    def wrapper1():
        print("=============================")
        original_function()
        print("#############################")
    return wrapper1
@dec_fun
def abc():
    print("hello")
abc()
