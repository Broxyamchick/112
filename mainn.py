from character import Character, Is_alive

player1 = Character("Vasya", damage=10)
player2 = Character("petya", hp=20)

print(player1)
print(player2)


print("напишите 1 чтобы продолжить или что-то другое чтобы закончить")
answer = int(input())
if answer==1:
    player2.attack(player1)
    player1.attack(player2)
    print(player1)
    print(player2)
    if Is_alive==("true"):
        print ("Vasya win")
    else:
        if answer == 1:
            player2.attack(player1)
            player1.attack(player2)
            print(player1)
            print(player2)
            if Is_alive == ("true"):
                print("Vasya win")
            else:
                print ("Vasya win")


else:
    print('Goodbye')












