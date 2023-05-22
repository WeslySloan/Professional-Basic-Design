if __name__ == '__main__':
    values = []
    while True:
        try:
            value = float(input())
            values.append(value)
        except EOFError:
            break

sort = sorted(values, reverse=True)[:3]
print (format(sort[0], ".1f"), format(sort[1], ".1f"), format(sort[2], ".1f"),)
