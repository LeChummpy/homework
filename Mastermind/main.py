import lampe
import turtle
import collections
import copy

window = turtle.Screen()
lines = []
currentLine = [0]

colors = ["nothing", "red", "blue", "green", "pink", "yellow", "brown"]
code = ["red","blue","red","red"]
currentColorSelection = ["","","",""]

turtle.tracer(False,0)

for i in range(10):
    line = []
    for j in range(4):
        l = lampe.Lampe(50*j-20, 40*i-200, 20, "gray")
        l.anschalten()
        line.append([l, 0])
        turtle.update()
    for j in range(2):
        for k in range(2):
            l = lampe.Lampe(10*k-65, 40*i+10*j-200, 5, "red")
            l.anschalten()
            line.append([l, 0])
            turtle.update()
    lines.append(line)
l = lampe.Lampe(250, -180, 40, "blue")
l.anschalten()
line.append([l, 0])
turtle.update()

def onclick(x,y):
    def checkWhichLampClicked(x,y,lines):
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if (x>lines[i][j][0].gibPos()[0]-lines[i][j][0].gibRadius() and x<lines[i][j][0].gibPos()[0]+lines[i][j][0].gibRadius() and y>lines[i][j][0].gibPos()[1]-lines[i][j][0].gibRadius() and y<lines[i][j][0].gibPos()[1]+lines[i][j][0].gibRadius()):
                    return (j, i)

    def getScore(ColorSelection, Code):
        #ColorSelection and Code of same length
        # returns tuple, [0] number of how many at right place, [0] number of how many colors right
        ColorSelection = copy.copy(ColorSelection)
        Code = copy.copy(Code)
        numberRightPlace = 0
        numberRightColor = 0
        for i in range(len(ColorSelection)):
            if (ColorSelection[i]==Code[i]):
                numberRightPlace+=1
                ColorSelection[i], Code[i] = "-", "-"
        for i in range(len(ColorSelection)):
            if (ColorSelection[i]!="-"):
                if (ColorSelection[i] in Code):
                    numberRightColor += 1
                    Code[Code.index(ColorSelection[i])] = "-"
                    ColorSelection[i] = "-"
        return (numberRightPlace, numberRightColor)

    indices = checkWhichLampClicked(x,y,lines)
    if (indices!=None and currentLine[0]!=None):
        if(currentLine[0]>=len(lines)-1):
            currentLine[0] = None
            print("Du hast verloren!, der Code war eigentlich ", code)

        elif (indices[1]==currentLine[0]): #wenn gelickter Knopf einer der Vier in aktueller Reihe
            if (indices[0]<4):
                lines[currentLine[0]][indices[0]][1] += 1
                if (lines[currentLine[0]][indices[0]][1]>=6):
                    lines[currentLine[0]][indices[0]][1] = 1
                currentColorSelection[0], currentColorSelection[1], currentColorSelection[2], currentColorSelection[3] = colors[lines[currentLine[0]][0][1]], colors[lines[currentLine[0]][1][1]], colors[lines[currentLine[0]][2][1]], colors[lines[currentLine[0]][3][1]]
                print(currentColorSelection)
                currentColor = currentColorSelection[indices[0]]
                currenltyClickedButton = lines[indices[1]][indices[0]][0]
                currenltyClickedButton.aendereFarbe(currentColor)
                turtle.update()

        elif(indices[1]==len(lines)-1): #Wenn blauer geklickt
            if (currentColorSelection[0]==code[0] and currentColorSelection[1]==code[1] and currentColorSelection[2]==code[2] and currentColorSelection[3]==code[3]):
                currentLine[0] = None
                print("Das ist der Code, Du hast gewonnen!")
            else:
                score = getScore(currentColorSelection, code)
                for i in range(score[0]):
                    currentScoreDisplayLamp = lines[currentLine[0]][4+i][0]
                    currentScoreDisplayLamp.aendereFarbe("black")
                    turtle.update()
                for i in range(score[1]):
                    currentScoreDisplayLamp = lines[currentLine[0]][4+score[0]+i][0]
                    currentScoreDisplayLamp.aendereFarbe("white")
                    turtle.update()
                currentLine[0] += 1
                print("Neuer Versuch, viel Erfolg!", currentLine)


window.onscreenclick(onclick)
window.listen()
input("Press any key to quit...")
