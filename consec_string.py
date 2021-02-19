def longest_consec(strarr: list, k: int) -> str:
    strs = []
    if k > len(strarr) or k <= 0:
        return ""
    else:
        for i in range(len(strarr)):
            strs.append("".join(strarr[i:k]))
            k += 1
        strs.sort(key=len, reverse=True)
        return strs[0]
