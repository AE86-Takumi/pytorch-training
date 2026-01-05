def count_word(string):
    char_list = list(string);
    n = 0;
    i = 0;
    s = len(string);

    for i in string:
        if 65 <= char_list[i] <= 90:
            n += 1;
        if 97 <= char_list[i] <= 122:
            n += 1;
    print(n);

count_word("aiueo");