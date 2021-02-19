# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if
# they consist of four octets,
# with values between 0 and 255, inclusive.


# my initial attempt
def is_valid_IP(string):
    results = []
    for i in string.split("."):
        if not i.isdigit():
            result = False
            results.append(result)
        elif (
            int(i) >= 0
            and int(i) <= 255
            and ((len(i) > 1 and i[0] != "0") or len(i) == 1)
        ):
            result = True
            results.append(result)
        else:
            result = False
            results.append(result)

    return len(results) == 4 and False not in results


# could use try except or nested if statements

# hadn't used all before
# all works for all iterable objects


def is_valid_IP(s):
    return s.count(".") == 3 and all(
        o.isdigit() and 0 <= int(o) <= 255 and str(int(o)) == o for o in s.split(".")
    )


# if statements arranged slightly differently in iterable comprehension
# [f(x) if condition else g(x) for x in sequence]
# or
# [f(x) for x in sequence if condition]
