import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("欢迎来到猜数字游戏！")
    print("我想了一个1到100之间的数字。")

    while True:
        try:
            guess = int(input("请输入你的猜测: "))
            attempts += 1

            if guess < number_to_guess:
                print("太低了，再试一次。")
            elif guess > number_to_guess:
                print("太高了，再试一次。")
            else:
                print(f"恭喜你！你在{attempts}次尝试中猜对了数字。")
                break
        except ValueError:
            print("请输入一个有效的整数。")

if __name__ == "__main__":
    guess_the_number()
