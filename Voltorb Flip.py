# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:25:53 2020

@author: Madison Koelzer
"""


from graphics import *

### CONSTANTS ###
WIN_LENGTH = 800
WIN_HEIGHT = 800
WIN_TITLE = "Voltorb Flip Auto Solver"
WIN_COLOR = "Light Grey"

### END CONSTANTS ###
class Node:
    def __init__(self, r_values, r_bombs,
             c_values, c_bombs, 
             poss, objects):
        self.r_values = r_values
        self.r_bombs = r_bombs
        self.c_values = c_values
        self.c_bombs = c_bombs
        self.poss = poss
        self.objects = objects
        # self.value = None
        self.perc_bomb = None
    


# Checks that the input is valid
# Params:   win     => Main Graphwin object
#           board   => Created board (as defined in main)
# returns bool value of true if board is valid, false otherwise
# If false, prints out message explaining why invalid

def checkInput(win, board):
    inputs = [
        [board[0][5][0][1], board[0][5][1][1]],
        [board[1][5][0][1], board[1][5][1][1]],
        [board[2][5][0][1], board[2][5][1][1]],
        [board[3][5][0][1], board[3][5][1][1]],
        [board[4][5][0][1], board[4][5][1][1]],
        [board[5][0][0][1], board[5][0][1][1]],
        [board[5][1][0][1], board[5][1][1][1]],
        [board[5][2][0][1], board[5][2][1][1]],
        [board[5][3][0][1], board[5][3][1][1]],
        [board[5][4][0][1], board[5][4][1][1]]
        ]
    for i in inputs:
        print(i)
        for j in i:
            text = j.getText()
            textstr = -1 
            
            print("j: " + text)
            try:
                textstr = int(text)
            except ValueError:
                print("Value was not an integer. Try Again")
                return False
        value0 = int(i[0].getText())
        value1 = int(i[1].getText())
        if (value0 + value1 < 5):
            print("Data is too small. Try again")
            return False
        elif (value1 > 5):
            print("There cannot be more than 5 bombs. Please try again")
            return False
        elif ((value1 == 5 and not value0 == 0) or 
              (value0 == 0 and not value1 == 5)):
            print("Invalid Value")
            return False
        elif (value1 == 4 and (value0 < 1 or value0 > 3)):
            print("Invalid Value")
            return False
        elif (value1 == 3 and (value0 < 1 or value0 > 6)):
            print("Invalid Value")
            return False
        elif (value1 == 2 and (value0 < 1 or value0 > 9)):
            print("Invalid Value")
            return False
        elif (value1 == 1 and (value0 < 1 or value0 > 12)):
            print("Invalid Value")
            return False
        elif (value1 == 0 and (value0 < 1 or value0 > 15)):
            print("Invalid Value")
            return False
        print("\n")
    rowValues = 0
    rowBombs = 0
    columnValues = 0
    columnBombs= 0
    i = 0
    while (i < 10):
        if (i < 5):
            rowBombs += int(inputs[i][1].getText())
            rowValues += int(inputs[i][0].getText())
        else:
            columnBombs += int(inputs[i][1].getText())
            columnValues += int(inputs[i][0].getText())
        i += 1
    if (rowBombs != columnBombs):
        print("Number of bombs in columns is not the same as" +
              " the number of bombs in the rows")
        return False
    elif (rowValues != columnValues):
        print("Value count in columns is not the same as" +
              " the value count in the rows")
        return False
    return True

# Replaces entries with Text values
# Params:   win     => Main Graphwin object
#           board   => Created board (as defined in main)
# returns board with all entries replaced by their values
# Also redraws board

def replaceEntries(win, board):
    inputs = [
        [board[0][5][0][1], board[0][5][1][1]],
        [board[1][5][0][1], board[1][5][1][1]],
        [board[2][5][0][1], board[2][5][1][1]],
        [board[3][5][0][1], board[3][5][1][1]],
        [board[4][5][0][1], board[4][5][1][1]],
        [board[5][0][0][1], board[5][0][1][1]],
        [board[5][1][0][1], board[5][1][1][1]],
        [board[5][2][0][1], board[5][2][1][1]],
        [board[5][3][0][1], board[5][3][1][1]],
        [board[5][4][0][1], board[5][4][1][1]]
        ]
    for i in inputs:
        for j in i:
            j.undraw()
        
    board[0][5][0][1] = Text(board[0][5][0][1].getAnchor(),
                             board[0][5][0][1].getText()) 
    board[0][5][1][1] = Text(board[0][5][1][1].getAnchor(),
                             board[0][5][1][1].getText()) 
    board[1][5][0][1] = Text(board[1][5][0][1].getAnchor(),
                             board[1][5][0][1].getText()) 
    board[1][5][1][1] = Text(board[1][5][1][1].getAnchor(),
                             board[1][5][1][1].getText()) 
    board[2][5][0][1] = Text(board[2][5][0][1].getAnchor(),
                             board[2][5][0][1].getText()) 
    board[2][5][1][1] = Text(board[2][5][1][1].getAnchor(),
                             board[2][5][1][1].getText()) 
    board[3][5][0][1] = Text(board[3][5][0][1].getAnchor(),
                             board[3][5][0][1].getText()) 
    board[3][5][1][1] = Text(board[3][5][1][1].getAnchor(),
                             board[3][5][1][1].getText()) 
    board[4][5][0][1] = Text(board[4][5][0][1].getAnchor(),
                             board[4][5][0][1].getText()) 
    board[4][5][1][1] = Text(board[4][5][1][1].getAnchor(),
                             board[4][5][1][1].getText()) 
    board[5][0][0][1] = Text(board[5][0][0][1].getAnchor(),
                             board[5][0][0][1].getText()) 
    board[5][0][1][1] = Text(board[5][0][1][1].getAnchor(),
                             board[5][0][1][1].getText()) 
    board[5][1][0][1] = Text(board[5][1][0][1].getAnchor(),
                             board[5][1][0][1].getText()) 
    board[5][1][1][1] = Text(board[5][1][1][1].getAnchor(),
                             board[5][1][1][1].getText()) 
    board[5][2][0][1] = Text(board[5][2][0][1].getAnchor(),
                             board[5][2][0][1].getText()) 
    board[5][2][1][1] = Text(board[5][2][1][1].getAnchor(),
                             board[5][2][1][1].getText()) 
    board[5][3][0][1] = Text(board[5][3][0][1].getAnchor(),
                             board[5][3][0][1].getText()) 
    board[5][3][1][1] = Text(board[5][3][1][1].getAnchor(),
                             board[5][3][1][1].getText()) 
    board[5][4][0][1] = Text(board[5][4][0][1].getAnchor(),
                             board[5][4][0][1].getText()) 
    board[5][4][1][1] = Text(board[5][4][1][1].getAnchor(),
                             board[5][4][1][1].getText()) 
    inputs = [
        [board[0][5][0][1], board[0][5][1][1]],
        [board[1][5][0][1], board[1][5][1][1]],
        [board[2][5][0][1], board[2][5][1][1]],
        [board[3][5][0][1], board[3][5][1][1]],
        [board[4][5][0][1], board[4][5][1][1]],
        [board[5][0][0][1], board[5][0][1][1]],
        [board[5][1][0][1], board[5][1][1][1]],
        [board[5][2][0][1], board[5][2][1][1]],
        [board[5][3][0][1], board[5][3][1][1]],
        [board[5][4][0][1], board[5][4][1][1]]
        ]
    for i in inputs:
        for j in i:
            j.setSize(24)
            j.draw(win)
        #print(i)
    return board

# Creates a picture and displays it in one of the 16 possible squares
# Params:   win     => Main GraphWin object
#           board   => Created board (as defined in main)
#           x, y    => The coordinates of the square to define
#           options => An array of possible numbers. length is always 4.
#                       0 means not possible, 1 means possible
#                       Ex. [0, 0, 1, 1] means either 2 or 3, but not 0 or 1
# Returns objects drawn as array

def showPossibleGrid(win, board, x, y, options, previous=[]):
    for i in previous:
        i.undraw()    
    
    myRectangle = board[x][y]
    p1 = myRectangle.getP1()
    p2 = myRectangle.getP2()
    pMid = Point((p2.getX() - p1.getX()) / 2 + p1.getX(),
        (p2.getY() - p1.getY()) / 2 + p1.getY() )

    counter = 0
    for i in options:
        if(i):
            counter += 1

    if (counter == 0):
        text = Text(pMid, "ERROR") #throw an error
        text.draw(win)
        return [text]
    elif (counter == 1):
        num = 0
        while (True):
            if (options[num]): break
            num += 1

        if (num != 0):
            text = Text(pMid, str(num))
            text.draw(win)
            return [text]
        else:
            oval0 = Oval(p1, p2)
            oval0.setFill("red")
            oval0.draw(win)
            return [oval0]
    elif (counter > 1):
        rec0 = Rectangle(p1, pMid)
        rec1 = Rectangle(pMid, Point(p2.getX(), p1.getY()))
        rec2 = Rectangle(pMid, Point(p1.getX(), p2.getY()))
        rec3 = Rectangle(pMid, p2)
        grid = [rec0, rec1, rec2, rec3]     
        for i in [rec0, rec1, rec2, rec3]:
            i.draw(win)
        if (options[0]):
            oval0 = Oval(rec0.getP1(), rec0.getP2())
            oval0.setFill("red")
            oval0.draw(win)
            grid.append(oval0)
        if (options[1]):
            t1 = Text(rec1.getCenter(), "1")
            t1.draw(win)
            grid.append(t1)
        if (options[2]):
            t2 = Text(rec2.getCenter(), "2")
            t2.draw(win)
            grid.append(t2)
        if (options[3]):
            t3 = Text(rec3.getCenter(), "3")
            t3.draw(win)
            grid.append(t3)
        return grid

# Updates board to show simple possibility list, initializes nodes for each
#       tile, and returns a list of these nodes
# Params:   win     => Main GraphWin object
#           board   => Created board (as defined in main)
#           
# Returns 2d array of nodes
def initiateSolvedBoard(win, board):
    rows = [
        [int(board[0][5][0][1].getText()), int(board[0][5][1][1].getText())],
        [int(board[1][5][0][1].getText()), int(board[1][5][1][1].getText())],
        [int(board[2][5][0][1].getText()), int(board[2][5][1][1].getText())],
        [int(board[3][5][0][1].getText()), int(board[3][5][1][1].getText())],
        [int(board[4][5][0][1].getText()), int(board[4][5][1][1].getText())]
        ]
    columns = [
        [int(board[5][0][0][1].getText()), int(board[5][0][1][1].getText())],
        [int(board[5][1][0][1].getText()), int(board[5][1][1][1].getText())],
        [int(board[5][2][0][1].getText()), int(board[5][2][1][1].getText())],
        [int(board[5][3][0][1].getText()), int(board[5][3][1][1].getText())],
        [int(board[5][4][0][1].getText()), int(board[5][4][1][1].getText())]
        ]
    poss = []
    j = 0
    while(j < 5):
        i = rows[j]
        print(str(i[0]) + ", " + str(i[1]))
        print(i[0] + i[1])
        if (i[1] == 0): #no bombs
            if (i[0] == 5): #all 1s
                block = [0, 1, 0, 0]
                row = [block, block, block, block, block]
                poss.append(row)
            elif (i[0] == 6): #1s or 2s
                block = [0, 1, 1, 0]
                row = [block, block, block, block, block]
                poss.append(row)
            else: #1s, 2s, or 3s
                block = [0, 1, 1, 1]
                row = [block, block, block, block, block]
                poss.append(row)
        elif (i[0] + i[1] == 5): #can only be bombs or 1s
            if (i[1] == 5): #all bombs
                block = [1, 0, 0, 0]
                row = [block, block, block, block, block]
                poss.append(row)
            else: #limit to bombs and 1s
                block = [1, 1, 0, 0]
                row = [block, block, block, block, block]
                poss.append(row)
        elif (i[0] + i[1] == 6): #can only be bombs, 1s, or 2s
            if (i[0] == 6): #all 1s or 2s
                block = [0, 1, 1, 0]
                row = [block, block, block, block, block]
                poss.append(row)
            elif (i[1] == 4): #can only be bombs and 2s 
                block = [1, 0, 1, 0]
                row = [block, block, block, block, block]
                poss.append(row)
            else: #bombs, 1s, or 2s
                block = [1, 1, 1, 0]
                row = [block, block, block, block, block]
                poss.append(row)
        else: #all possible
            if (i[1] == 4 and i[0] == 3): #bombs or 3
                block = [1, 0, 0, 1]
                row = [block, block, block, block, block]
                poss.append(row)
            else: #all possible
                block = [1, 1, 1, 1]
                row = [block, block, block, block, block]
                poss.append(row)
        j += 1
    poss2 = [[], [], [], [], []]
    j = 0
    while(j < 5):
        i = columns[j]
        if (i[1] == 0): #no bombs
            if (i[0] == 5): #all 1s
                block = [0, 1, 0, 0]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
            elif (i[0] == 6): #1s or 2s
                block = [0, 1, 1, 0]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
            else: #1s, 2s, or 3s
                block = [0, 1, 1, 1]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
        elif (i[0] + i[1] == 5): #can only be bombs or 1s
            if (i[1] == 5): #all bombs
                block = [1, 0, 0, 0]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
            else: #limit to bombs and 1s
                block = [1, 1, 0, 0]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
        elif (i[0] + i[1] == 6): #can only be bombs, 1s, or 2s
            if (i[0] == 6): #all 1s or 2s
                block = [0, 1, 1, 0]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
            elif (i[1] == 4): #can only be bombs and 2s 
                block = [1, 0, 1, 0]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
            else: #bombs, 1s, or 2s
                block = [1, 1, 1, 0]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
        else: #all possible
            if (i[1] == 4 and i[0] == 3): #bombs or 3
                block = [1, 0, 0, 1]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
            else: #all possible
                block = [1, 1, 1, 1]
                k = 0
                while(k < 5):
                    poss2[k].append(block)
                    k += 1
        j += 1
    
    possibilities = []
    i = 0
    while (i < 5):
        row = []
        j = 0
        while (j < 5):
            block = []
            k = 0
            while (k < 4):
                if (poss[i][j][k] == 1 and poss2[i][j][k] == 1):
                    block.append(1)
                else:
                    block.append(0)
                k += 1            
            grid = showPossibleGrid(win, board, i, j, block)
            row.append([block, grid])
            j += 1
        possibilities.append(row)
        i += 1

    print(possibilities)   
    
    my_nodes = []
    for i in range(0, 5):
        row_nodes = []
        for j in range(0, 5):
            rowValues = rows[i][0]
            rowBombs = rows[i][1]
            columnValues = columns[j][0]
            columnBombs = columns[j][1]
            blockPoss = possibilities[i][j][0]
            blockObjects = possibilities[i][j][1]
            my_node = Node(rowValues, rowBombs, columnValues, columnBombs,
                           blockPoss, blockObjects)
            row_nodes.append(my_node)
        my_nodes.append(row_nodes)

    return my_nodes

# Creates an array of possible board configurations
# Params:   nodes   => 2d array of node objects
#           result  => 2d array of current configuration
#           x       => row position of node
#           y       => column poisition of node
#           
# Returns list of possible board configurations
def generatePossResults(nodes, result = [[], [], [], [], []], x = 0, y = 0):
    configs = []
    for z in range(0, 4):
        if (nodes[x][y].poss[z]):
            result[x].append(z)
            
            i, j = x, y
            row_values = col_values = col_bombs = row_bombs = 0
            while (i >= 0):
                col_values += result[i][y]
                if (result[i][y] == 0):
                    col_bombs += 1
                i -= 1
            while (j >= 0):
                row_values += result[x][j]
                if (result[x][j] == 0):
                    row_bombs += 1
                j -= 1
                       
            xl_yl = (x < 4 and y < 4 and 
                     row_values <= nodes[x][y].r_values and 
                     row_bombs <= nodes[x][y].r_bombs and
                     col_values <= nodes[x][y].c_values and 
                     col_bombs <= nodes[x][y].c_bombs)
            xl_ye = (x < 4 and y == 4 and 
                     row_values == nodes[x][y].r_values and 
                     row_bombs == nodes[x][y].r_bombs and
                     col_values <= nodes[x][y].c_values and
                     col_bombs <= nodes[x][y].c_bombs)
            xe_yl = (x == 4 and y < 4 and 
                     row_values <= nodes[x][y].r_values and 
                     row_bombs <= nodes[x][y].r_bombs and
                     col_values == nodes[x][y].c_values and
                     col_bombs == nodes[x][y].c_bombs)
            xe_ye = (x == 4 and y == 4 and 
                     row_values == nodes[x][y].r_values and 
                     row_bombs == nodes[x][y].r_bombs and
                     col_values == nodes[x][y].c_values and
                     col_bombs == nodes[x][y].c_bombs)
            
            try:
                if (result[0][0] == 3
                    and result[0][1] == 1
                    and
                    result[0][2] == 1
                    and
                    result[0][3] == 1
                    and
                    result[0][4] == 0
                    and
                    result[1][0] == 1
                    and
                    result[1][1] == 1
                    and
                    result[1][2] == 1
                    and
                    result[1][3] == 1
                    and
                    result[1][4] == 3
                    # and
                    # result[0][4] == 0
                    # and
                    # result[0][4] == 0
                    ):
                    print("Testing: ")
                    print(str(result) + ", " + str(xl_yl) + ", " + str(xl_ye) + ", " + str(xe_yl) + ", " + str(xe_ye))
                    print("\n")
            except IndexError:
                print("")
            
            if (xl_yl or xl_ye or xe_yl or xe_ye):
                ### If all checks pass, generatePossResults and add to configs
                if(y < 4):
                    j = y + 1
                    returns = generatePossResults(nodes, result, x, j)
                elif(x < 4):
                    i = x + 1
                    j = 0
                    returns = generatePossResults(nodes, result, i, j)
                else:
                    returns = [[]]
                    for i in result:
                        j = i.copy()
                        returns[0].append(j)
                        
                ### Add results to configs
                if (returns != None):
                    for i in returns:
                        j = i.copy()
                        configs.append(j) 
            result[x].pop()
    
    if (configs == []):
        return None
    return configs

# Using configurations, update and display nodes
# Params:   nodes   => 2d array of node objects
#           configs  => 2d array of current configuration
#           x       => row position of node
#           y       => column poisition of node
#           
# Returns updated nodes
def updateNodes(win, board, nodes, configs, x = 0, y = 0):
    count = 0
    size = 0
    poss = [0, 0, 0, 0]
    
    # print("Configs is: ")
    # print(configs)
    for config in configs:
        p = config[x][y]
        if (p == 0):
            count += 1
            # print(str(x) + ', ' + str(y) + ': ' + str(count))
        poss[p] = 1
        size += 1
    
    nodes[x][y].poss = poss
    nodes[x][y].objects = showPossibleGrid(win, board, x, y, poss, 
                                            nodes[x][y].objects)
    
    nodes[x][y].perc_bomb = count / size
    
    if (y < 4):
        y += 1
    elif (x < 4):
        y = 0
        x += 1
    else:
        return nodes
    
    nodes = updateNodes(win, board, nodes, configs, x, y)
    return nodes

# Using configurations, have user flip best options until game is over
# Also, updates nodes and configs based on inputted data.
# Params:   win     => Main GraphWin object
#           board   => Created board (as defined in main)
#           nodes   => 2d array of node objects
#           configs => 2d array of current configuration
#           
# Returns array containing updated nodes (slot 0) and configs (slot 1)
# Returns None if board is already solved
def inputOnNode(win, board, nodes, configs):
    myX = None
    myY = None
    
    initialized = False
    for x in range(0, 5):
        for y in range(0, 5):
            count = 0
            greaterThanTwo = False
            if (nodes[x][y].poss[2] or nodes[x][y].poss[3]):
                greaterThanTwo = True
            for k in nodes[x][y].poss:
                if (k):
                    count += 1            
            if (not initialized):
                if (count > 1 and greaterThanTwo):
                    myX, myY = x, y
                    initialized = True
            elif (nodes[x][y].perc_bomb < nodes[myX][myY].perc_bomb 
                  and count > 1 and greaterThanTwo):
                myX, myY = x, y
    if (myX == None):
        return None ### Board is already solved ###
    
    #print(str(myX) + ", " + str(myY))
    board[myX][myY].setFill("yellow")
    
    x1 = 110
    x2 = 690
    y1 = 710
    y2 = 790
    textSize = 16
    inputSize = 30
    
    rec = Rectangle(Point(x1, y1), Point(x2, y2))
    
    textRec = Rectangle(Point(x1, y1), Point(x2 - x1, y2))
    text = Text(textRec.getCenter(), 
                "Please enter the value for the highlighted cell: ")
    text.setSize(textSize)
    
    inputRec = Rectangle(Point(x2 - x1, y1), Point(x2, y2))
    userInput = Entry(inputRec.getCenter(), 
                int((inputRec.getP2().getX() - inputRec.getP1().getX()) / 25))
    userInput.setSize(inputSize)
    
    rec.draw(win)
    text.draw(win)
    userInput.draw(win)
    
    done = False
    
    while (not done):
        win.getMouse()
        ### Series of checks to make sure input is valid ###
        try:
            inputNum = int(userInput.getText())
        except ValueError:
            text.setText("Value was not an integer. Try Again:")
            continue
        if (inputNum > 3 or inputNum < 0):
            text.setText("Value was out of bounds. Try Again:")
            continue
        if (not nodes[myX][myY].poss[inputNum]):
            text.setText("That wasn't a possible value. Try Again:")
            continue
        ### End series of checks ###
        
        done = True
        text.undraw()
        userInput.undraw()
        board[myX][myY].setFill(WIN_COLOR)
        
        text = Text(rec.getCenter(), "")
        text.setSize(textSize)
        
        if (inputNum == 0):
            text.setText("Bomb! Too bad, better luck next time!")
            text.draw(win)
            return None
        
        newConfigs = []
        for config in configs:
            if (config[myX][myY] == inputNum):
                newConfigs.append(config)
                    
        configs = newConfigs
        nodes = updateNodes(win, board, nodes, configs)
        
        text.undraw()
        rec.undraw()
        
        return [nodes, configs]

# Takes the mouse, finds where it is, and returns the option it is over.
# If it is not over any option, loop back and wait for a real selection
# Params:   win             => Main GraphWin object
#           mouse           => Pointer received from getMouse() function
#           optionLocations => array of option boundaries
#
# Returns string value of menu option selected.
# Options include: 
        
def menuSelect(win, mouse, optionLocations):
    return None

        
def main():
    ### CREATE THE BOARD ###

    
    win = GraphWin(WIN_TITLE, WIN_LENGTH, WIN_HEIGHT)
    win.setBackground(WIN_COLOR)
    ### END BOARD ###

    ### Rectangle around 6 x 6 board ###
    borderRectCorner1 = Point(WIN_LENGTH / 8, WIN_HEIGHT / 8)
    borderRectCorner2 = Point(WIN_LENGTH - WIN_LENGTH / 8,
                              WIN_HEIGHT - WIN_HEIGHT / 8)

    borderRect = Rectangle(borderRectCorner1, borderRectCorner2)
    #borderRect.draw(win)
    ### END RECT ###

    ### 6 x 6 board ###

    borderLength = borderRectCorner2.getX() - borderRectCorner1.getX()
    borderHeight = borderRectCorner2.getY() - borderRectCorner1.getY()

    board = []
    for i in range(0, 6):
        arr = []
        y1 = borderRectCorner1.getY() + (i * (borderHeight / 6))
        y2 = y1 + (borderHeight / 6)
        for j in range(0, 6):
            x1 = borderRectCorner1.getX() + (j * (borderLength / 6))
            x2 = x1 + (borderLength / 6)
            if (i == 5 and j == 5) or (j != 5 and i != 5):
                r = Rectangle(Point(x1, y1), Point(x2, y2))
                r.draw(win)
            else:
                r1 = Rectangle(Point(x1, y1), Point(x2, y2 - (y2 - y1) / 2))
                r1Entry = Entry(r1.getCenter(), int((x2 - x1) / 25))

                r2 = Rectangle(Point(x1, y1 + (y2 - y1) / 2), Point(x2, y2))
                r2Entry = Entry(r2.getCenter(), int((x2 - x1) / 25))

                r1.draw(win)
                r1Entry.draw(win)
                r1.setFill("grey")
                #r1Entry.setTextColor("white")
                r1Entry.setSize(30)

                r2.draw(win)
                r2Entry.draw(win)
                r2.setFill("red")
                r2Entry.setSize(30)

                r = [[r1, r1Entry], [r2, r2Entry]]
            arr.append(r)
        board.append(arr)
    print(board[0][5][0][1])
    print("\n")
    ### END BOARD ###

    ### Menu Options Drawn to board ###
    
    halfNodeLength = WIN_LENGTH / 16 #50
    
    continueX1 = borderRectCorner2.getX() + halfNodeLength 
    continueX2 = borderRectCorner2.getX() - halfNodeLength 
    continueY1 = int(WIN_HEIGHT * 3 / 32)
    continueY2 = borderRectCorner1.getY() - continueY1
    
    continueButton = Rectangle(Point(continueX1, continueY1), 
                              Point(continueX2, continueY2))
    continueButton.setFill("light green")
    
    continueText = Text(continueButton.getCenter(), "Continue")
    continueText.setSize(15)
    
    continueButton.draw(win)
    continueText.draw(win)
    
    restartX1 = WIN_LENGTH - continueX1
    restartX2 = restartX1 + 2 * halfNodeLength
    restartY1 = continueY1 
    restartY2 = continueY2     
    
    restartButton = Rectangle(Point(restartX1, restartY1), 
                              Point(restartX2, restartY2))
    restartButton.setFill("red")
    
    restartText = Text(restartButton.getCenter(), "Restart")
    restartText.setSize(15)
    
    restartButton.draw(win)
    restartText.draw(win)
    
    buttons = [restartButton, continueButton]
        
    ### End Menu Options ###

    ### TEMP CODE, MAKE SURE TO DELETE
    #showPossibleGrid(win, board, 3, 4, [1, 1, 1, 1])
    
    inputs = [
        [board[0][5][0][1], board[0][5][1][1]],
        [board[1][5][0][1], board[1][5][1][1]],
        [board[2][5][0][1], board[2][5][1][1]],
        [board[3][5][0][1], board[3][5][1][1]],
        [board[4][5][0][1], board[4][5][1][1]],
        [board[5][0][0][1], board[5][0][1][1]],
        [board[5][1][0][1], board[5][1][1][1]],
        [board[5][2][0][1], board[5][2][1][1]],
        [board[5][3][0][1], board[5][3][1][1]],
        [board[5][4][0][1], board[5][4][1][1]]
        ]
    # inputs[0][0].setText(7)
    # inputs[0][1].setText(1)
    # inputs[1][0].setText(4)
    # inputs[1][1].setText(1)
    # inputs[2][0].setText(6)
    # inputs[2][1].setText(0)
    # inputs[3][0].setText(4)
    # inputs[3][1].setText(1)
    # inputs[4][0].setText(4)
    # inputs[4][1].setText(3)
    # inputs[5][0].setText(4)
    # inputs[5][1].setText(1)
    # inputs[6][0].setText(5)
    # inputs[6][1].setText(1)
    # inputs[7][0].setText(5)
    # inputs[7][1].setText(0)
    # inputs[8][0].setText(6)
    # inputs[8][1].setText(2)
    # inputs[9][0].setText(5)
    # inputs[9][1].setText(2)
    
    inputs[0][0].setText(6)
    inputs[0][1].setText(1)
    inputs[1][0].setText(7)
    inputs[1][1].setText(0)
    inputs[2][0].setText(5)
    inputs[2][1].setText(2)
    inputs[3][0].setText(6)
    inputs[3][1].setText(1)
    inputs[4][0].setText(2)
    inputs[4][1].setText(3)
    inputs[5][0].setText(7)
    inputs[5][1].setText(2)
    inputs[6][0].setText(4)
    inputs[6][1].setText(1)
    inputs[7][0].setText(5)
    inputs[7][1].setText(2)
    inputs[8][0].setText(4)
    inputs[8][1].setText(1)
    inputs[9][0].setText(6)
    inputs[9][1].setText(1)
    
    ### END OF TEMP CODE
    
    
    done = False
    while (not done):
        mouse = win.getMouse()
        done = checkInput(win, board)
    replaceEntries(win, board)
    
    nodes = initiateSolvedBoard(win, board)

    configs = generatePossResults(nodes)
    print("c: " + str(configs))
    
    if (configs == None):
        print("There are no possible configurations for this board. Check" + 
              " your input and try again.")
        win.getMouse()
        win.close()
        main()
        return
    nodes = updateNodes(win, board, nodes, configs)
    
    ### Temp Code ###
    #print(nodes)
    # for x in nodes:
    #     for y in x:
    #         print(y.perc_bomb)
    #         print(y.poss)
    #         print('\n')
    ### End of Temp Code ###
    done = False
    while (not done):
        results = inputOnNode(win, board, nodes, configs)
        if (results == None):
            done = True
        else:
            nodes = results[0]
            configs = results[1]
    
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done
    main()
main()
