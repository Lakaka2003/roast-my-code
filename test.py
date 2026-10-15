# TODO: Refactor this entire mess later
global user_count
x = 5

if x == True:
    f = open("data.txt", "r")
    while True:
        for i in range(10):
            for j in range(5):
                if j == 2:
                    print("debug")
                    user_input = eval("2 + 2")
                    try:
                        result = x / 0
                    except:
                        pass
