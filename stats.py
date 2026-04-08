#ВАРИАНТ 10
import pandas as pd                          #необходимые библиотеки, в т. ч. для обработки даты из датафрейма и
import matplotlib.dates as mdates           #декоратор для логгирования
from logs import log

class Stats:                    #создал класс, далее на конструктор, методы накинул декоратор логгирования
    @log
    def __init__(self, file_path, date_col, price_col):  #путь к датафрейму, колонка для даты, колонка для цены
        self.file_path = file_path
        self.date_col = date_col
        self.price_col = price_col
        self.df = None   #задали атрибут, чтобы даже если датафрейм еще не прочитан не получали ошибку

    @log
    def read_file(self):           #читаем наши датафреймы
        self.df = pd.read_csv(self.file_path)

    @log
    def prepare_date(self):            #приводим дату к нормальному виду, без учета времени суток, часовых поясов 
        self.df[self.date_col] = pd.to_datetime(self.df[self.date_col])  #как в одном из данных датафреймов
        if self.df[self.date_col].dt.tz is not None:
            self.df[self.date_col] = self.df[self.date_col].dt.tz_localize(None)

    @log                    #рисуем график, ax позволяет рисовать несколько графиков в одном окне
    def plot(self, ax):
        self.read_file()          #получаем данные из датафреймов, приводим дату к нормальному виду
        self.prepare_date()
        ax.plot(self.df[self.date_col], self.df[self.price_col])  #закидваем для осей х и у данные, на х - даты, на у - цены
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))  #меняем формат даты на деню.месяц.год как на рисунке к лабе
        ax.tick_params(axis = 'x', rotation = 45) #повораживаем разметку оси х, т.е. даты на угол 45 как на рисунке к лабе и для удобства
        ax.grid(True, alpha = 0.5) #отрисовали полупрозрачную сетку на графике для удобства чтения данных










