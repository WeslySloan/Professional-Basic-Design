data = []
while True:
    try:
        line = input()
        if not line:
            break
        data.append(line.split())
    except EOFError:
        break

performance = {}
for row in data:
    name = row[0]
    sales = sum(map(int, row[1:]))
    performance[name] = sales


top_3 = sorted(performance.items(), key=lambda x: x[1], reverse=True)[:3]
for name, sales in top_3:
    print(name, sales)
