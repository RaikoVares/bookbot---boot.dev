

def main():
    path = "books/frankenstein.txt"
    book = get_Book_Text(path)
    words_in_book = f"There are {count_Words(book)} words in this book"
    print(book, words_in_book)


def get_Book_Text(path):
    with open(path) as f:
        return f.read()

def count_Words(book):
    words = book.split()
    count = 0
    for i in range(len(words)):
        count += 1
    return count

main()