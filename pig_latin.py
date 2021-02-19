# my solution


def pig_it(text):
    text_list = text.split(" ")
    empty_list = []

    for i in text_list:
        if i.isalnum():
            i = i[1:] + i[0] + "ay"
            empty_list.append(i)
        else:
            empty_list.append(i)

    return " ".join(empty_list)


# list comprehension again
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
