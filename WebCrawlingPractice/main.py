import matplotlib.font_manager as fm

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
print(len(font_list))

f = [f.name for f in fm.fontManager.ttflist]
print(f)

for i in f:
    if i == 'AppleGothic':
        print('"AppleGothic"이 있습니다.')