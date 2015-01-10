if __name__ == "__main__":
    n = input()
    inp = []
    while n != 0:
        inp.append(~input() & 0xFFFFFFFF)
        n -= 1

    print "\n".join(map(str,inp))