import random
import time

length_of_test = 10
score = 0


def get_words():
    with open('words.txt', 'r') as f:
        all_words = [line.strip() for line in f]
    return all_words


def create_word_list(list):
    initial_list = []
    for i in range(length_of_test):
        word = random.choice(list)
        initial_list.append(word)
    word_list = " ".join(initial_list)
    # print(f"\n{final_word_list}\n")
    return word_list


master_list = get_words()

word_list = create_word_list(master_list)

# Start timer
start = time.time()

user_typing = input(f"\nType the words listed below with a space between each. Press enter when you are done.\n\n{word_list}\n\n")

# End timer
end = time.time()

# Calculate seconds
seconds = end - start
seconds_per_word = length_of_test / seconds
word_per_minute = int(60/seconds_per_word)

# Convert user entries to list
user_typing_list = user_typing.split()

# Convert words back to list and compare to user entry
check_list = word_list.split()
for word in check_list:
    index = check_list.index(word)
    if user_typing_list[index] == word:
        print(f"{word} is correct.")
        score += 1
    else:
        print(f"{word} is not correct, user typed {user_typing_list[index]}")

final_score = int(score / length_of_test * 100)

print(f"Your words per minute was {word_per_minute}. Your accuracy was {final_score}%!")