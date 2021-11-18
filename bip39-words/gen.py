#!/usr/bin/env python3

WORDS_PER_PAGE = 440


def print_pages(f, words, word_range):
    for word_no in word_range:
        word = words[word_no]
        f.write('<div class="grid-item"><tt>{:04d} {}</tt></div>'.format(
            word_no + 1,
            word.strip()
        ))

words = None
with open("english.txt") as f:
    words = f.readlines()

template = None
with open("template.html") as f:
    template = f.readlines()

total_pages = int(len(words) / WORDS_PER_PAGE) + 1
for page in range(total_pages):
    filename = "bip39-words-page-{}-of-{}.html".format(page + 1, total_pages)
    header = "Page {} of {}".format(page + 1, total_pages)
    with open(filename, "w") as f:
        for line in template:
            line = line.strip()
            if "%%ITEMS%%" in line:
                lower_bound = page * WORDS_PER_PAGE
                upper_bound = (page + 1) * WORDS_PER_PAGE
                if upper_bound > len(words):
                    upper_bound = len(words)

                print_pages(f, words, range(lower_bound, upper_bound))
            elif "%%HEADER%%" in line:
                f.write(line.replace("%%HEADER%%", header))
            else:
                f.write(line)
