def boy_and_girl(boy, girl):
    print(f"There're {boy} boys!")
    print(f"And there're {girl} girls!")
    print(f"So crazy!")


boy_and_girl(30, 20)

print("Use variables from our scripts:")
amount_of_boy = 20
amount_of_girl = 30


boy_and_girl(amount_of_boy, amount_of_girl)


boy_and_girl(2 + 3, 6 * 7)

print(f"The another way to run this script")
amount_of_boy = 10
amount_of_girl = 20


boy_and_girl(amount_of_boy + 3, amount_of_girl + 5)

# use input() and run it
boy_and_girl(input(),input())

