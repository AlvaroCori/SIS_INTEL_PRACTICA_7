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
