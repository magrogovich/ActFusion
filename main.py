import  wolframalpha
from googlesearch import search
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime




print('''
░█████╗░░█████╗░████████╗  ███████╗██╗░░░██╗░██████╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝██║░░░██║██╔════╝██║██╔══██╗████╗░██║
███████║██║░░╚═╝░░░██║░░░  █████╗░░██║░░░██║╚█████╗░██║██║░░██║██╔██╗██║
██╔══██║██║░░██╗░░░██║░░░  ██╔══╝░░██║░░░██║░╚═══██╗██║██║░░██║██║╚████║
██║░░██║╚█████╔╝░░░██║░░░  ██║░░░░░╚██████╔╝██████╔╝██║╚█████╔╝██║░╚███║
╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░  ╚═╝░░░░░░╚═════╝░╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝



''')

userInput = input('press enter to launch... ')
userWords = userInput.split(' ')
with open ('/home/user/actFusion/logs.txt','a') as log:
    while userWords[0].lower() != 'exit':
        
        userInput = input('[commands] >>>')
        userWords = userInput.split(' ')
        log.write(f"{userInput} | {datetime.now()}\n")


        if userWords[0].lower() == "wolf":
            client = wolframalpha.Client("HAG749-YW5GWRRUJP")

            res = client.query(userInput.lstrip('wolf'))
            try:
                print(next(res.results).text)
            except StopIteration:
                print("we dident found any thing!")

        elif userWords[0].lower() == "google":
            Tg = []
            c = 0
            for j in search(userInput.lstrip('google'), tld="co.in", num=10, stop=10, pause=2):
                print(f"{c} - '{j}'")
                c += 1
                Tg.append(j)
        elif userWords[0].lower() == "wiki":
            print(wikipedia.summary(userInput.lstrip('wiki')))
        elif userWords[0].lower() == 'open':
                driver = webdriver.Firefox()
                driver.get(Tg[int(userWords[1])])

        elif userWords[0].lower() == 'help':
            print('''   
            <google> for searching google
            <wolf> for searching wolframalpha
            <wiki> for searching wikipedia
            <exit> to exit
            <open + (choice)> to open a link from google search results
            ''')
    


