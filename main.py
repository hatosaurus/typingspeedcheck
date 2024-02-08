from interface import *
from typingspeed import *
import time

length_of_test = 10

master_list = get_words()
word_list = create_word_list(master_list, length_of_test)

root = Tk()

main = Main(root)

start_time = None


def start():
    global start_time
    root.bind("<Return>", finish)
    start_time = time.time()
    print(f"Start time is {start_time}")
    main.create_widgets(word_list, retry_callback=start)
    main.typing.focus()
    return start_time


def finish(self):
    global word_list
    print("User hit enter.")
    root.unbind("<Return>")
    end_time = time.time()
    print(f"End time is {end_time}")
    calculate_score(start_time, end_time, length_of_test)
    word_list = create_word_list(master_list, length_of_test)
    return word_list


def calculate_score(start, end, length):
    user_entry = str(main.retrieve_input())
    check_list = create_list(user_entry)
    words_per_minute = calculate_wpm(start, end, user_entry)
    final_score = check_accuracy(check_list, word_list, length)
    main.show_results(final_score, words_per_minute)


def esc(self):
    root.destroy()


start()


if __name__ == "__main__":
    main.create_widgets(word_list, retry_callback=start)
    root.bind("<Return>", finish)
    root.bind("<Escape>", esc)
    root.mainloop()


