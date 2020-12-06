
# -*- coding: utf-8 -*-

def show_reverse_word(word):
    print(word[::-1])
    return

def show_reverse_statment(statement):
    words = statement.split(' ')
    for word in words:
        print(word[::-1], end=' ')
    return

def main():
    show_reverse_word('junyiacademy')
    show_reverse_statment('flipped class room is important')
    return


if __name__ == "__main__":
    main()