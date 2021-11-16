def clean_colors(stars):
    colors = set()
    for row in stars.values:
        colors.add(row[4].lower())
    return colors

def clean_spectral_classes(stars):
    spectral_classes = set()
    for row in stars.values:
        spectral_classes.add(row[5])
    return spectral_classes
def ListCagetorietoNumber(colum,list_):
    pos=0
    _number=[]
    for x in colum:
        pos=0
        for y in list_:
            if(x.lower() == y.lower()):
                _number.append(pos)
            pos+=1
    return _number
