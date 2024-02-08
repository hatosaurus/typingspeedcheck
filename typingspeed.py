import random


def get_words():
    with open('words.txt', 'r') as file:
        all_words = [line.strip() for line in file]
    return all_words


def create_word_list(list, length_of_test):
    initial_list = []
    for i in range(length_of_test):
        word = random.choice(list)
        initial_list.append(word)
    word_list = " ".join(initial_list)
    # print(f"\n{final_word_list}\n")
    return word_list


def user_typing(words):
    typing = input(f"\nType the words listed with a space between each. Press enter when you are done.\n\n{words}\n\n")
    return typing


def calculate_seconds(start, end, length_of_test):
    seconds = end - start
    print(f"Total time taken: {seconds} seconds.")
    seconds_per_word = length_of_test / seconds
    print(f"Seconds per word: {seconds_per_word}")
    word_per_minute = int(60/seconds_per_word)
    return word_per_minute


def create_list(string):
    # Convert user entries to list
    typing_list = string.split()
    return typing_list


def check_accuracy(userlist, wordlist, length_of_test):
    # Convert words back to list and compare to user entry
    score = 0
    check_list = wordlist.split()
    for word in check_list:
        index = check_list.index(word)
        try:
            if userlist[index] == word:
                # print(f"{word} is correct.")
                score += 1
            else:
                print(f"{word} is not correct, user typed {userlist[index]}")
        except IndexError:
            print("Word missing, skipped.")
            continue
    final_score = int(score / length_of_test * 100)
    return final_score