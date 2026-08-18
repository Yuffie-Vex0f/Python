import wordcloud
txt='荷塘 采莲 今晚 路 叶子 想起 一条 这是 白天 树 知道 月光'
w=wordcloud.WordCloud(background_color='white',
                      width=150,
                      height=120,
                      max_font_size=48,
                      font_path='C:/Windows/Fonts/simhei.ttf')

w.generate(txt)
w.to_file('c:/data/test.png')
