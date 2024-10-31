# Подсчет количества слов (chars) в тексте (text)
text = 'Ballnghlhui lhyBBB AAAOnnn lLlLhgf ddeswea bibifvkkekrevfhuorelcdwwl ffew rnukiwxcnr'
chars = 'ballon'

def get_chars(chars):
    search = {}
    for i in chars:
        if i.lower() not in search:
            search[i.lower()]=1
        else:
            search[i.lower()]+=1

    return search

def count_ballon(chars_dict,text):
    search2 = {}
    for i in text:
        if i.lower() in chars_dict:
            if i.lower() not in search2:
                search2[i.lower()]=1
            else:
                search2[i.lower()]+=1
    return search2

def check(ch,t,result = 0):
    for key, val  in ch.items():
        if key not in t:
            print(f"Из строки:\n{text}\nМожно составить {result} слов ({chars})")
            print(f"Не хватает символа '{key}' для составления {result+1} слова")
            exit()
        if t[key] < val:
            print(f"Из строки:\n{text}\nМожно составить {result} слов ({chars})")
            print(f"Не хватает символа '{key}' для составления {result + 1} слова")
            exit()
        else:
            t[key] -= val
    result+=1
    check(ch,t,result)

ch = get_chars(chars)
t = count_ballon(ch,text)
check(ch,t,result=0)