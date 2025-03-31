import art


def add(n1,n2):
    return n1 + n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2
def sub(n1,n2):
    return n1-n2

opareter ={
    "+": add,
    "*":mul,
    "/": div,
    "-":sub
}
def calc():
    print(art.logo)
    should_continue = True
    number1 = float(input("enter the first number: "))
    while should_continue:
        for op in opareter:
            print(op)
        oper = input('pick operator: ')
        number2 = float(input("enter the second number: "))
        answer = opareter[oper](number1,number2)

        print(f"{number1} {oper} {number2} = {answer}")

        choice = input(f"do you want to continue with {answer},type y or type n :").lower()
        if choice =="y":
            number1 = answer
        else:
            should_continue = False
            print("\n"*20)
            calc()



calc()