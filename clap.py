#!/usr/bin/env python3
import pyautogui

_ = input('Press Any Key To Start\n')

for i in range(1000):
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    print(i,end='\r')
