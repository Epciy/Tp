
dictt={'g': 610, 'f': 315, 'o': 282, 'a': 260, 'h': 257, 'n': 240, 'r': 224, 'c': 221, 'w': 219, 'p': 147, 'y': 129, 'u': 100, 'b': 99, 'i': 95, 'q': 67, 'l': 39, 'k': 39, 'x': 37, 'd': 36, 's': 28, 'm': 26, 'j': 11, 'z': 11, 't': 5, 'e': 4}
dic={'z': 11, 'y': 129, 'x': 37, 'w': 219, 'v': 0, 'u': 100, 't': 5, 
's': 28, 'r': 224, 'q': 67, 'p': 147, 'o': 282, 'n': 240, 'm': 26, 'l': 39, 'k': 39, 'j': 11, 'i': 95, 'h': 257, 'g': 
610, 'f': 315, 'e': 4, 'd': 36, 'c': 221, 'b': 99, 'a': 260}
d={" ":" "}
d1=[i for i in dictt.keys()]
d2=[i for i in dic.keys()]
for k,b in zip(d2,d1):
    d[k]=b
print(d)
message="or z f kcgrkcgh fnnggh mg ug rofo onaougugna fqgb cn u eorrofu"
sent=" "
for i in message:
    sent+=d[i]
print(sent)