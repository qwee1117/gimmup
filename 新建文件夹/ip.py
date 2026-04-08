"""a"""
import pywinauto.mouse as m
from time import sleep

a = int(input())
sleep(3)
for i in range(a):
    m.click(coords=(1400, 700))
