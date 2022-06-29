from itertools import combinations


def solution(orders, course):
    max_menu = 0
    menu = []
    store = []
    for order in orders:
        o = list(order)
        if len(order) > max_menu:
            max_menu = len(order)
        for i in o:
            if i not in menu:
                menu.append(i)
    for cou in course:
        dict = {}
        for i in combinations(sorted(menu), cou):
            cnt = 0
            for order in orders:
                check = [False]*len(i)
                for j in range(len(i)):
                    if i[j] in order:
                        check[j] = True
                if not False in check:
                    cnt += 1
            if cnt >= 2:
                dict[i] = cnt

        if len(dict) > 0:
            max_value = max(dict.values())
            for i, j in dict.items():
                if j == max_value:
                    store.append("".join(i))
    # print(store)
    store = sorted(store)
    return store
