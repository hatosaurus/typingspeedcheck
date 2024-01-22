from interface import *
from typingspeed import *

length_of_test = 10

master_list = get_words()
word_list = create_word_list(master_list, length_of_test)

start_time = None


def start():
    global start_time
    root.bind("<Return>", finish)
    start_time = get_time()
    main.create_widgets(word_list, retry_callback=start)
    main.typing.focus()
    return start_time


def finish(self):
    global word_list
    print("User hit enter.")
    root.unbind("<Return>")
    end_time = get_time()
    calculate_score(start_time, end_time, length_of_test)
    word_list = create_word_list(master_list, length_of_test)
    return word_list


def calculate_score(start, end, length):
    user_entry = str(main.retrieve_input())
    check_list = create_list(user_entry)
    words_per_minute = calculate_seconds(start, end, length)
    final_score = check_accuracy(check_list, word_list, length)
    main.show_results(final_score, words_per_minute)


def esc(self):
    root.destroy()


if __name__ == "__main__":
    root = Tk()
    main = Main(root)
    main.create_widgets(word_list, retry_callback=start)
    start_time = start()
    root.bind("<Return>", finish)
    root.bind("<Escape>", esc)
    # main.typing.focus()
    # root.overrideredirect(True)
    root.mainloop()


