res = 0


def calculate_structure_sum(*d_s_s):
    global res
    for i in range(len(d_s_s)):
        if isinstance(d_s_s[i], int):
            res += d_s_s[i]
        elif isinstance(d_s_s[i], str):
            res += len(d_s_s[i])
        elif isinstance(d_s_s[i], list):
            d_s1 = d_s_s[i]
            for j in range(len(d_s1)):
                calculate_structure_sum(d_s1[j])
        elif isinstance(d_s_s[i], dict):
            d_s2 = [*d_s_s[i].items()]
            for j in range(len(d_s2)):
                calculate_structure_sum(d_s2[j])
        elif isinstance(d_s_s[i], tuple):
            d_s3 = d_s_s[i]
            for j in range(len(d_s3)):
                calculate_structure_sum(d_s3[j])
        elif isinstance(d_s_s[i], set):
            d_s4 = list(d_s_s[i])
            for j in range(len(d_s4)):
                calculate_structure_sum(d_s4[j])
        return res


d_s = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(d_s)
print(result)
