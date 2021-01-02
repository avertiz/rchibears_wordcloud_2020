from wordcloud import WordCloud as wc

def main():
    week1 = wc(name = 'week1', start_time=1600016400, end_time=1600621199)
    week1.createFile()

if __name__ == '__main__':
    main()