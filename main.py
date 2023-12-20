def log_func(func):
    def inner():
        print("Start")
        func()
        print("Finish")
    return inner

@log_func
def fd():
    print("Hello")

fd()
