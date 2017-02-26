def main():
    s, t = map(int, input().split())

    c = list(map(int, input().split()))
    c = list(map(lambda x: t // x, c))

    print(sum(c))
    print(' '.join(map(str, c)))

main()
