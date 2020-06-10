class Data :
    def __init__(self, name, price) :
        self.name = name
        self.price = price
        self.item_sold = 0
        self.item_profit = 0

    def add(x) :
        Product_list.append(x)
        print("Added. Product: " + x.name + ".\nSell price: " + str(x.price))

    def update(x) :
        for i in range(len(Product_list)) :
            if Product_list[i].name == x.name :
                Product_list[i].price = x.price
                print("Updated. Product: " + x.name + ".\nSell Price: " + str(x.price))
                break

    def sell(x1, n1) :
        for i in Product_list :
            if x1 == i.name :
                i.item_sold += n1
                total_list[0] += n1
                total_list[1] += n1 * i.price
                print("Sold. Product: " + i.name + ".\nNumber of sold: " + str(n1))
                break
            
    def display() :
        for i in Product_list :
            print("Product: " + i.name + ".\nTotal number of sold: " + str(i.item_sold))
        print("Total product sold: " + str(total_list[0]) + "\nProfit: " + str(total_list[1]))

Product_list = []
total_list = [0,0]
print("Welcome to Old Farmer Market, what can I help you?")
while True :
    x0 = str(input())
    if x0[0] == "a" :
        Data(x0[2:], int(input())).add()
        
    elif x0[0] == "u" :
        Data(x0[2:], int(input())).update()

    elif x0[0] == "s" :
        Data.sell(x0[2:], int(input()))

    elif x0[0] == "d" :
        Data.display()
    
    else :
        print("Thanks for visiting Old Farmer Market. Wish you have a good day. Bye bye.")
        break