import pyautogui;
import time;

RETRIES = 1;


def getImageName(localPgnFile):
    localPgnFile = str(localPgnFile)
    pathArray = localPgnFile.split('/')
    nameWithPNG = pathArray[-1]

    return nameWithPNG

def resetMouse():
    pyautogui.moveTo(10, 10)

def findImage(localPgnFile):
    imageName = getImageName(localPgnFile);
    #print('Searching... ' + imageName)

    xCord = 0
    yCord = 0
    for i in range(RETRIES):
        try:
            xCord, yCord = pyautogui.locateCenterOnScreen(localPgnFile);
            #print(xCord, yCord);
            #print('Found: ' + imageName)
            time.sleep(1)
            break;
        except TypeError:
            1 == 1

    return xCord, yCord

def findImageAndClick(localPgnFile):
    buttonClicked = False;
    xCord, yCord = findImage(localPgnFile)
    if(xCord != 0 and yCord !=0):
        pyautogui.moveTo(xCord, yCord)
        pyautogui.click()

        buttonClicked = True;
    return buttonClicked;

def waitFormatch():
    # Loop till match is found for n time
    initialTime = time.time()
    timeDiference = 0;

    #Wait for the match popup
    while True:

        imageFound = findImageAndClick('./Resources/images/Accept_Button.PNG');

        if(imageFound):
            timeDiference = time.time() - initialTime;

            print('Match found in ' + str(int(timeDiference)+1) + ' seconds')


def main():
    waitFormatch();

main();
