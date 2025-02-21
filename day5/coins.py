total_amount = int(input("Enter the amount: "))

ten_rupee_coins = total_amount // 10
print("The number of 10 rupee coins:", ten_rupee_coins)
total_amount %= 10

five_rupee_coins = total_amount // 5
print("The number of 5 rupee coins:", five_rupee_coins)
total_amount %= 5

two_rupee_coins = total_amount // 2
print("The number of 2 rupee coins:", two_rupee_coins)
total_amount %= 2

one_rupee_coins = total_amount
print("The number of 1 rupee coins:", one_rupee_coins)