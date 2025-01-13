def main():
    numbers = [1, 2, 3, 4, 5]
    print(numbers)
    print(len(numbers))  # 5
    print(numbers[2])  # 3
    print(numbers[2:4])  # [3, 4]
    print(numbers[2:])  # [3, 4, 5]
    print(numbers[:4])  # [1, 2, 3, 4]
    print(numbers[::2])  # [1, 3, 5]
    print(numbers[::-1])  # [5, 4, 3, 2, 1]
    print(numbers[1:3:2])  # [2]
    print(numbers[1::2])  # [2, 4]
    print(numbers[::-2])  # [5, 3, 1]
    print(numbers[1::-2])  # [3, 1]

    numbers.append(6)
    print(numbers)  # [1, 2, 3, 4, 5, 6]

    numbers.insert(2, 7)
    print(numbers)  # [1, 2, 7, 3, 4, 5, 6]

    numbers.remove(2)
    print(numbers)  # [1, 7, 3, 4, 5, 6]

    numbers.extend([8, 9])
    print(numbers)  # [1, 7, 3, 4, 5, 6, 8, 9]


if __name__ == "__main__":
    main()
