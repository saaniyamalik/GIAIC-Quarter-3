# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.


count_dictionary = {}
def main():
    while True:
        user_num = input("Enter your number ")
        if user_num == "":
            break
        else:
            user_num = int(user_num)
            
        if user_num in count_dictionary:
            count_dictionary[user_num] += 1
        else:
            count_dictionary[user_num] = 1

    print("-----------------------------")

    for user_num, count in count_dictionary.items():
        print(f"{user_num} appears {count} times.")


if __name__ == "__main__":
    main()