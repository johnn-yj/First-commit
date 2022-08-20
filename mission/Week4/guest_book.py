g_book ='''
영준,123456789
리더,010-1234-5678
기창,010-5678-111
지현,111-1111-1111
코치,010-3333-3333
'''

test_file = open(g_book.txt)

print(g_book)

def worng_gbook ():
    a = g_book.write("g_book.txt")
    for line in g_book:
        line = line.rstrip()

        if not line.stratswith('010') or line.length()==13 or '-' in line:
            print(line)
            

worng_gbook()




