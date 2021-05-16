if __name__ == "__main__":
    data = list([index for index in range(9, 1, -1)])

    isa = True
    isd = True
    for index in range(1, 8):
        if data[index] > data[index - 1]:
            isd = False
        elif data[index] < data[index - 1]:
            isa = False

    if isa:
        print("ascending")
    elif isd:
        print("descending")
    else:
        print("mixed")
