#ВАРИАНТ 10
import matplotlib.pyplot as plt
from stats import Stats
from logs import log


@log
def main():
    fig, ax = plt.subplots(figsize=(12, 6))       #задал фигуру, оси

    stat_crude = Stats('crude-oil-price.csv', 'date', 'price')    #один из датафреймов, путь к нему, названия столбцов с датой и ценой
    stat_crude.plot(ax)

    stat_brent = Stats('BrentOilPrices.csv', 'Date', 'Price')   #один из датафреймов, путь к нему, названия столбцов с датой и ценой
    stat_brent.plot(ax)                 #передаю данные для отрисовки фигуры на те же ось, чтобы кривые отрисовались на одном и том же графике

    plt.tight_layout()             #отрисовал график
    plt.show()

if __name__ == '__main__':        #выполнится, если файл запущен напрямую
    main()