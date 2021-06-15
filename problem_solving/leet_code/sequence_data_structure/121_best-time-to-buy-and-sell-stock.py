if __name__ == "__main__":
    nums = [7, 1, 5, 3, 6, 4]

    profit = 0
    min_price = 999999999999999999

    for price in nums:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    print(profit)
