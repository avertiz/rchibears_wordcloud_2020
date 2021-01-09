from Rchibears import Rchibearstext as txt

def main():
    week_dict = {
        'week1':[1600016400, 1600621199],
        'week2':[1600621200, 1601225999],
        'week3':[1601226000, 1601830799],
        'week4':[1601830800, 1602202799],
        'week5':[1602202800, 1603040399],
        'week6':[1603040400, 1603757699],
        'week7':[1603757700, 1604265899],
        'week8':[1604265900, 1604858399],
        'week9':[1604858400, 1605575699],
        'week10':[1605575700, ],
        # 'week11':[],
        'week12':[1606699200, 1607277599],
        'week13':[1607277600, 1607882399],
        'week14':[1607882400, 1608487199],
        'week15':[1608487200, 1609091999],
        'week16':[1609092000, 1609709099],
        'week17':[1609709100]
    }
    week3 = txt(name = 'week3', start_time=1601226000, end_time=1601830799)
    week3.createFile(filepath=r'C:\Users\andre\Documents\rchibears_wordcloud_2020\textfiles\\')

if __name__ == '__main__':
    main()