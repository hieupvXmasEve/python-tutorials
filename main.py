print((lambda _: list(map(lambda _: _ // 2, _)))([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(
    (lambda some_list: list(map(lambda n: n // 2, some_list)))(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
)
