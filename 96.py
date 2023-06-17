fin = open('shopping.txt', 'r')
foot = open('buy.txt', 'w')

lines = fin.readlines()

for line in lines:
    words = line.split()
    i_name = words[0]
    n = int(words[1])
    cost = int(words[2])
    total = n * cost
    fout.write(f'{i_name} \t{total:7d}\n')

fin.clse()
fout.close()
