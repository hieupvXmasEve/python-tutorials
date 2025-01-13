# TODO: write a program to-do-list using list with add, remove, and print
def main():
    todo_list = []
    # input from user
    todo_list.append(input("Enter a task: "))
    print(todo_list)
    todo_list.append(input("Enter another task: "))
    print(todo_list)
    todo_list.append(input("Enter a task: "))
    print(todo_list)


if __name__ == "__main__":
    main()
