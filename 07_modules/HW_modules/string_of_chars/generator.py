from collections import Counter
from test_instances_generator import user_input_tests as test


def test_repeated(word):
    duplicated = []
    for i in word:
        if word.count(i) > 1:
            duplicated.append(i)
    print(*duplicated)
    number_of_duplicates = Counter(duplicated).most_common(1)
    print(*number_of_duplicates)


def main():
    words_gen = []
    word = input('Enter a word that you want to test')
    test_repeated(word)
    number_of_words = int(input('How many words do you want to shuffle?'))
    for i in range(number_of_words):
        i = input("Enter variables: ")
        words_gen.append(i)

    test(words_gen)
if __name__ == "__main__":
    main()