def PrintData(**Data) :
    if "uid" in Data :
        print("The user id:", Data["uid"])
    if "name" in Data :
        print("The username:", Data["name"])
    if "age" in Data :
        print("The user age:", Data["age"])


PrintData(uid = int(input()), name = str(input()), age = int(input()))
PrintData(uid = int(input()), name = str(input()))
PrintData(name = str(input()))