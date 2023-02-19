import codecs
al = open('all.txt', 'w',encoding='UTF-8')
a = []
for k in range(1,100 + 1):
    st = open('words/html/word_raw' + str(k) + '.txt', 'r',encoding='UTF-8')
    s = st.read()
    st.close()
    t = []
    
    for i in range(len(s) - 100):
        if s[i:i + 25] == '<td data-bind="html: en">':
            for j in range(25,100):
                if s[i + j:i + j + 5] == "</td>":
                    print(s[i + 25:i + j])
                    t.append(s[i + 25:i + j])
                    a.append(s[i + 25:i + j])
                    break
        if s[i:i + 25] == '<td data-bind="html: ja">':
            for j in range(25,100):
                if s[i + j:i + j + 5] == "</td>":
                    print(s[i + 25:i + j])
                    t.append(s[i + 25:i + j])
                    a.append(s[i + 25:i + j])
                    break


    f = codecs.open('words/only/UNIT' + str(k).zfill(3) + '.txt', 'w',"utf-8")
    for ti in range(len(t)):
        f.write(t[ti])
        if ti % 2 == 0:
            f.write(",")
        elif ti == len(t) - 1:
            break
        else:
            f.write("\n")
    f.close()

for ai in range(len(a)):
    if ai % 2 == 0:
        al.write(a[ai])
    else:
        al.write("\n")

for ai in range(len(a)):
    if ai % 2 == 0:
        None
    else:
        al.write(a[ai])
        al.write("\n")
al.close()