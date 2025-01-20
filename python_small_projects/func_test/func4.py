def get_info(sid):
    return sid,"liaoyujing",20

sid,sname,sage=get_info(123)
print(sid,sname,sage)
print(get_info(1234))
print(type(get_info(1234)))