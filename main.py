from interface import *
from typingspeed import *

length_of_test = 10


master_list = get_words()
word_list = create_word_list(master_list, length_of_test)
# main.create_widgets(word_list)

# start_time = get_time()
# user_entry = user_typing(word_list)
# end_time = get_time()
#
# check_list = create_list(user_entry)
# words_per_minute = calculate_seconds(start_time, end_time, length_of_test)
# final_score = check_accuracy(check_list, word_list, length_of_test)

# print(f"Your words per minute was {words_per_minute}. Your accuracy was {final_score}%!")


if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    app.create_widgets(word_list)
    root.mainloop()


