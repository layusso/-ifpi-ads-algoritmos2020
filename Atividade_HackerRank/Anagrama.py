#Esse código não é meu, ainda estou em progresso...

def main():

    cases = int(input())
    for i in range(cases):
        s = input()
        n = len(s)
        res = 0
        for j in range(1, n):
            cont = {}
            for l in range(n - j + 1):
                subs = list(s[l:l + l])
                subs.sort()
                subs = ''.join(subs)
                if subs in cnt:
                    cnt[subs] += 1
                else:
                    cnt[subs] = 1
                res += cnt[subs] - 1
        print(res)