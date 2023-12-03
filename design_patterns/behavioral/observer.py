#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：observer.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-09-28 11:20 
"""


class Observer:
    """观察者的基类"""

    def update(self, observer):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for o in self.__observers:
            o.update(self)


class WaterHeater(Observable):
    """热水器：战胜寒冬的有利武器"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print("current temperature is:", self.__temperature)
        self.notify_observers()


class WashingMode(Observer):
    """该模式用于洗澡用"""

    def update(self, observable):
        if isinstance(observable,
                      WaterHeater) and 50 <= observable.get_temperature() < 70:
            print("水已烧好，温度正好！可以用来洗澡了。")


class DrinkingMode(Observer):
    """该模式用于饮用"""

    def update(self, observable):
        if isinstance(observable, WaterHeater) and observable.get_temperature() >= 100:
            print("水已烧开！可以用来饮用了。")


def test_water_heater():
    heater = WaterHeater()
    washing_observe = WashingMode()
    drinking_observe = DrinkingMode()
    heater.add_observer(washing_observe)
    heater.add_observer(drinking_observe)
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(100)


if __name__ == "__main__":
    test_water_heater()
