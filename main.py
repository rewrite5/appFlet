import flet
from calculator import CalculatorApp

def main(page):
    page.title = "Calculadora Basica"
    #page.window_height = 300
    page.window_width = 325


    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)

flet.app(target=main, view=flet.WEB_BROWSER)
#flet.app(target=main)