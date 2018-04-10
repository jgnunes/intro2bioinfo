def hamming(string1 , string2):

    dis = 0
    assert len(string1) == len(string2)

    for x, y in zip(string1, string2):
        if x != y:
            dis += 1
    return dis


if __name__ == "__main__":
    print(hamming('GGGCCGTTGGT','GGACCGTTGAC'))
