#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 100)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0
        self.label_error.setText('')
        self.label_max_el.setText('Максимальный элемент: ')
        self.label_sum.setText('Сумма единиц перед максимальным элементом: ')

    def solve(self):
        list_information_max_num = find_max(self.tableWidget)
        if not list_information_max_num:
            self.label_error.setText('Введены некорректные данные!')
        else:
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1]) + ';' + str(list_information_max_num[2]) + ']')
            self.label_error.setText('')
            # -*- решение задания -*-
            row = 0
            col = 0
            number_of_units = 0  # количество единиц, стоящих перед нашим числом
            flag = False
            n = 0
            while row < self.tableWidget.rowCount():
                while col < self.tableWidget.columnCount():
                    item = float(self.tableWidget.item(row, col).text())
                    n += 1
                    if item == 1:
                        number_of_units += 1
                        col += 1
                    elif item == list_information_max_num[0]:
                        flag = True
                        break
                    else:
                        col += 1
                if flag:
                    break
                row += 1
                col = 0
            self.label_sum.setText('Сумма единиц перед максимальным элементом: ' + str(number_of_units))
            if n - 1 == number_of_units:
                self.tableWidget.setItem(list_information_max_num[1], list_information_max_num[2],
                                         QTableWidgetItem(str(number_of_units)))
            elif number_of_units == self.tableWidget.columnCount() * self.tableWidget.rowCount():
                self.tableWidget.setItem(list_information_max_num[1], list_information_max_num[2],
                                         QTableWidgetItem(str(number_of_units-1)))


def find_max(table_widget):
    """
    находим максимальное число из таблицы и его координаты
    :param table_widget: таблица
    :return: [max_num, row_max_number, col_max_number], если выкинуто исключение,
            то None
    """

    row_max_number = 0  # номер строки, в котором находится максимальне число
    col_max_number = 0  # номер столбца, в котором находится максимальне число
    try:
        max_num = float(table_widget.item(row_max_number, col_max_number).text())  # Максимальное значение
        row = 0
        col = 0
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number >= max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number]
    except Exception:
            return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
