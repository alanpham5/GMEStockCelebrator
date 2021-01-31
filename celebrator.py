
# Timer
import time
# Video
import os
import moviepy
from moviepy.editor import *
import pygame
# Source
import yfinance as yf
# Etc.
from random import randint

celebrations = [ "./celebration.mp4","./celebration2.mp4","./celebration3.mp4"]

def checkTicker(tickerName):
    ticker = yf.Ticker(tickerName)
    data = ticker.history()
    lastQuote = (data.tail(1)['Close'].iloc[0])
    return lastQuote
def celebrate(prev):
    quote = checkTicker('GME')
    if quote > prev and prev > 0:
        print(quote)
        clip = VideoFileClip(celebrations[randint(0,2)])
        pygame.display.set_caption("$GME TO THE MOON")
        clip.preview()
        pygame.quit()
    return quote

if __name__ == "__main__":
    previous = 0
    interval = input("Enter time interval (in minutes): ")
    while True:
        previous = celebrate(previous)
        time.sleep(60*float(interval))
