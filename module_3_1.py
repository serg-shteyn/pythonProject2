# Пространство имён

calls = 0
def string_info(string):
    global calls
    calls += 1
    result = (len(string),string.upper(),string.lower())
    return(result)

def is_contains(string,list_):
    global calls
    calls += 1
    list_lower = []
    for i in list_:
        list_lower.append(i.lower())
    if string.lower() in list_lower:
        return (True)
    else:
        return (False)

print(string_info('UnixFit'))
print(string_info('Begemot'))
print(is_contains('Zoonomaly',['Bear','Elefant','Zoo']))
print(is_contains('BanBan',['Kaban','Taran','BAnBan']))
print(calls)
