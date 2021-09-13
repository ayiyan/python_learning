import re

with open('text.txt', ) as doc:
    doc_text = doc.read().replace(" ","")

doc = doc_text.split('\n')

def generate_key(doc_val, position):
    if re.match("\+\-",doc_val[position]) :
        tag = position + 2
        if re.match("\+\-",doc_val[tag]):
            key_list = doc_val[position+1].split("|")
            key_list_new = []
            key_list_new.append(key_list[1])
            key_list_new.append(key_list[2])
            key_list_new.append(key_list[3])
            yield key_list_new, tag

def generate_value(key,doc_val,start_val, stop_val):
        total = {}
        for position in range(start_val, stop_val):
            key_list = doc_val[position].split("|")
            if len(key_list)  > 1 :
                total = {
                    key[0] : key_list[1],
                    key[1] : key_list[2],
                    key[2] : key_list[3]
                }
            yield total

lock = False
key = None
line_number = 0
all_list = []
while line_number < len(doc):
    g_key = generate_key(doc, line_number)
    if lock is False:
        key,line_number = next(g_key)
        line_number = line_number + 1
    if key:
        lock = True
        g_value = generate_value(key, doc, line_number, len(doc))
        l = next(g_value)
        print(l)
        break

print(next(g_value))
print(next(g_value))
