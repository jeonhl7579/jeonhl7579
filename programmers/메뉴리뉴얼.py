def dfs(visited, result, menu, idx, n, answer):
    if idx == n:
        answer.append("".join(result))
        return

    for i in range(len(menu)):
        if visited[i] == True:
            continue
        visited[i] = True
        result.append(menu[i])
        dfs(visited, result, menu, idx+1, n, answer)
        for j in range(i+1, len(menu)):
            visited[j] = False
        result.pop()


def solution(orders, course):
    max_menu = 0
    menu = []
    for order in orders:
        o = list(order)
        if len(order) > max_menu:
            max_menu = len(order)
        for i in o:
            if i not in menu:
                menu.append(i)

    store = []
    for cou in course:
        if cou > max_menu:
            continue
        result = []
        answer = []
        visited = [False]*len(menu)
        dfs(visited, result, sorted(menu), 0, cou, answer)

        dict = {}
        for an in answer:
            cnt = 0
            for order in orders:
                check = [False]*len(an)
                for id in range(len(an)):
                    if an[id] in order:
                        check[id] = True
                if False not in check:
                    cnt += 1
            if cnt >= 2:
                dict[an] = cnt

        if len(dict) > 0:
            max_value = max(dict.values())
            for i, j in dict.items():
                if j == max_value:
                    store.append(i)

    # print(store)
    store = sorted(store)
    return store
