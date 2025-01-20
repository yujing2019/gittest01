patients_data={'s001':'normal','s002':'lazy eyes','s003':'shortsighted','s004':'farsighted'}


def eyetest(data,k):
    if 'lazy' in data[k]:
        raise Exception('patient number' +str(k)+' is lazy eyes')


def eyetests(patients_data):
    for p in patients_data.keys():
        try:
            r=eyetest(patients_data,p)
            print(p,'can be corrected')
        except Exception as e:
            print(p,e,'cannont be corrected')


eyetests(patients_data)



