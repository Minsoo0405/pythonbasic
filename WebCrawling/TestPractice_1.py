f = open("wordcount_result.txt", "r", encoding="utf-8")
data = f.readlines()
print(data[10])

new_list = list()
for i in data[:10]:
    new_list.append(i.replace("\n", ""))

print(new_list)

newDict = dict()
for i in new_list:
    newDict[i.split()[0]] = i.split()[1]

print(newDict)

import matplotlib
import matplotlib_inline.pyplot as plt

fig = plt.gof()
fig.set_size_inches(20,10)
matplotlib.re("font", family="AppleGothic", size=10)
plt.title("그래프 제목")
plt.xlabel("단어")
plt.ylabel("개수")
plt.bar(newDict.keys(), newDict.values(), color="#FF000")
plt.xticks(rotation=45)
plt.savefig('all_words.jpg')
plt.show()