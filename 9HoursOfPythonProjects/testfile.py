
def main():
    flag = False
    word_list = []
    word = ""

    start_char = "<"
    end_char = ">"

    with open("story.txt", "r") as file:
        story = file.read()

    for each_char in story:
        if each_char == start_char:
            flag = True
            continue

        if each_char == end_char:
            flag = False
            word_list.append(word)
            word = ""
            continue

        if flag:
            word += each_char
             

    print(word_list)
    word_dictionary = { each_word:"" for each_word in word_list}


    for each_item in word_dictionary:
        word_dictionary[each_item] = input(f"Please enter a value for {each_item}: ")

    for each_item in word_dictionary:
        story = story.replace(each_item, word_dictionary[each_item])

    print(story)
    

if __name__ == "__main__":
    main()