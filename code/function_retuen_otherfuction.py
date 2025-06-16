def display():
    def show():
        return "show function"
    print("display function")
    return show
r_sh = display()
print(r_sh())