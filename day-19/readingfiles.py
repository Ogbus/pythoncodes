from collections import Counter

# files = open('./day-19-files/barack-obamas-speech.txt')
# readings = files.readlines()
# number_of_words = 0
# line_count = 0
# for reading in readings:
#     if line_count == 0:
#         print('you are welcome')
#         line_count += 1
#     else:
#         line_count += 1

def counting_lines(param):
    files = open(param)
    readings = files.readlines()
    words = 0
    line_count = 0
    for reading in readings:
        if line_count == 0:
            print('you are welcome')
            line_count += 1
        else:
            line_count = line_count + 1
    for word in readings:
        wording = word.split()
        words += len(wording)
    print(reading)
    files.close()
    return('Number of lines are', line_count, 'and the number of words in the file are', words)
# print(counting_lines('./day-19-files/barack-obamas-speech.txt'))
# print(counting_lines('./day-19-files/donald_trump_speech.txt'))
print(counting_lines('./day-19-files/melina_trumps_speech.txt'))
print(counting_lines('./day-19-files/michelle_obamas_speech.txt'))
