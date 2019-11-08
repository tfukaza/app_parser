import csv

def buildDiv(app, queries, html, id=0):
    #Write the opening tag
    html.write('<div class="app"id="' + str(id) + '">')
    
    q_num = 0
    html.write('<div class="id_num"><h2>' + str(id) + '</h2></div>')

    for Q, A in zip(queries, app): 

        html.write('<h6 class="question ')
        if(A == ''):
            html.write('na ')
        html.write(str(q_num) + '">' + Q + '</h6>')
        html.write('<p class="response">' + A + '</p>')
        q_num = q_num + 1
    
    html.write('</div>')



def main():

    apps = open('apps.csv', 'r')
    html = open('apps.html', 'w+')

    reader = csv.reader(apps)
    
    queries = next(reader)

    id = 0;

    html.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="ie=edge"><title>Document</title>')
    #import css
    html.write('<link rel="stylesheet" href="styles.css">')
    html.write('</head><body>')

    for app in reader:
        buildDiv(app, queries, html, id)
        id = id + 1

    #import Js
    html.write('<script type="text/javascript" src="script.js"></script>')
    html.write('</body></html>')


if __name__ == "__main__":
        main()