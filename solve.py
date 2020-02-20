from collections import OrderedDict

import heapq

def readFile():
    f = open('/home/ahmed/Downloads/d_tough_choices.txt', 'r+')
    '''
    read B, L, D
    '''
    line = f.readline()
    line = line.split()
    B = line[0]
    L = line[1]
    D = line[2]

    '''
    read score
    '''
    Scores = f.readline().split()

    booksToScores = dict()
    for i in range(len(Scores)):
        booksToScores[i] = int(Scores[i])

    libraryPerBooksPerDays = dict()

    libraries = []
    libToBooks = dict()
    heap = []
    libraryPerBooksPerDay = dict()
    for i in range(int(L)):
        l = f.readline().split()
        books_ids = f.readline().split()
        sign_up_days = l[1]
        heap.append((int(sign_up_days), i))
        books_per_days = l[2]
        libraryPerBooksPerDay[i] = books_per_days
        t = []

        for book in books_ids:
            t.append((book, booksToScores[int(book)]))

        t.sort(key=lambda x: x[1])
        libToBooks[i] = t[:]

    heapq.heapify(heap)

    f.flush()
    f.close()

    return D, heap, booksToScores, libToBooks, libraryPerBooksPerDay

def solution():

    signedUp = []

    scanned = OrderedDict()

    totalBooks = set()

    d, signUpHeap, booksToScores, libToBooks, libraryPerBooksPerDay = readFile()
    # signUpHeap, libToBooks, booksToScores, d, libraryPerBooksPerDay  = readFile()

    # print(booksToScores)
    # print(libToBooks)
    # print(signUpHeap)
    # print(libraryPerBooksPerDay)
    # print(d)
    days = 0

    for i in range(int(d)):

        # Signup cycle
        cost, lib = heapq.heappop(signUpHeap)

        if cost != days:
            heapq.heappush(signUpHeap, (cost, lib))
            days += 1
        else:
            days = 0

        # Books cycle
        # print(libraryPerBooksPerDay)
        for currLib in signedUp:
            # print(libraryPerBooksPerDay)
            # print(currLib)
            # print(libraryPerBooksPerDay[currLib])

            booksToBeScanned = libraryPerBooksPerDay[currLib]

            j = 0

            while j < int(booksToBeScanned) and len(libToBooks[currLib]) > 0:
                # print(libToBooks[currLib][0].pop())
                book = libToBooks[currLib].pop()

                if book not in totalBooks:

                    if currLib not in scanned:
                        scanned[currLib] = [book]
                    else:
                        scanned[currLib].append(book)

                    j += 1

            # print(scanned)
        signedUp.append(lib)

    out(scanned)


def out(scanned):

    f = open('output3.txt', 'w')

    f.write(str(len(scanned)))
    f.write('\n')

    for lib, books in scanned.items():
        f.write(str(lib) + ' ' + str(len(books)))
        f.write('\n')

        books = [str(b[0]) for b in books]

        f.write(' '.join(books))
        f.write('\n')

    f.close()


solution()