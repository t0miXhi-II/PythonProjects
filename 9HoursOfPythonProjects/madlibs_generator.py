

def main():
    flag = False
    start_char = "<"
    end_char = ">"
    word_list = set()
    word = ""

    with open("story.txt", "r") as file:
        story = file.read()

        for i, char in enumerate(story):
            if char == start_char:
                flag = True

            if char == end_char:
                flag = False
                word_list.add(word)
                word = ""
                continue

            if flag and char != start_char:
                word += char

    for i, each_word in enumerate(word_list):
        print(f"{i + 1}) {each_word}")

    word_dict = { word_item: "" for word_item in word_list }
    #print(word_dict)
    #print(word_dict['emotion2'])

    for each_item in word_dict:
        word_dict[each_item] = input(f"Enter a word for {each_item}: ")

    print(word_dict)

    for each_item in word_dict:
        #print(each_item)
        story = story.replace(each_item, word_dict[each_item])

    print(story)

if __name__ == "__main__":
    main()

