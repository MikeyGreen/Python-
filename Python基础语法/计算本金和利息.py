def interest(money,rate):
    for i in range(len(money)):
        money[i] = money[i] * (1 + rate)
    return money
def main():
    amount = [1000,2000,3000,4000]
    rate = 0.01
    a = interest(amount,rate)
    print(amount)
    print(a)
main()
