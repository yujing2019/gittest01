strs=['hello yujing','error','hello duobaocat']


def printstr(str):
    if 'error' in str:
        raise Exception('error print')

    return str


def printstrs(strs):
    for str in strs:
        try:
            result=printstr(str)
            print(result,"success print")
        except Exception as e:
            print("print failure",e)




printstrs(strs)