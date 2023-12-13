def decode(message_file):
    sortedlist = []
    handle = open(message_file)
    for line in handle:
        linetext = line.replace("\n", "")
        sortedlist.append(linetext)
    handle.close()

    sortedlist.sort(key=lambda text: int(text.split(" ")[0]))

    index = 0
    formatiterator = 1
    decodedstring = ""
    for text in sortedlist:
        if index % formatiterator == 0:
            decodedstring += text.split(" ")[1]+" "
            formatiterator += 1
            index = 0
        index += 1
    return decodedstring


def main():
    print(decode("text.txt"))


main()
