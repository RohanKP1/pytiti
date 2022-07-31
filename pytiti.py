from os import system, name
import sys
import time

class Gstructure():
    
    BOLD = 1
    WHITE = 37
    RED = 91
    GREEN = 92
    YELLOW = 93
    BLUE = 94
    GAME_MAP = [[ "" for _ in range(3)] for _ in range(3)]

    def __init__(self) -> None:

        if "-h" in self.check_argument():
            self.clear()
            print(f"""This is a simple {self.styled_text("TiC TAc TOE",Gstructure.BLUE,Gstructure.BOLD)} GamE

> iN each turn you have to enter the coordinates of the cell to put your choice In,

          coordinates are given as:

     (7)    │    (8)    │    (9)    
────────────┼───────────┼────────────
     (4)    │    (5)    │    (6)
────────────┼───────────┼────────────
     (1)    │    (2)    │    (3)

> How to put coordinates correctly:
          Enter your number (1-9) : {self.styled_text("1",Gstructure.YELLOW,Gstructure.BOLD)}

> Enter {self.styled_text("Ctrl+C",Gstructure.YELLOW,Gstructure.BOLD)} to exit the game anytime.            
            """)

        elif "-p" or "" in self.check_argument():     
            choice = ["O","X"]
            turn = 0
            index = 0
            while self.check_win(choice[index])[0] == 0:
                self.clear()
                print(self.styled_text("\t\t   Tik Tak Toe\n" ,Gstructure.YELLOW ,Gstructure.BOLD))
                turn += 1
                if turn%2 == 0:
                    index = 1
                    print(self.styled_text("\t\t    X\'s turn\n",Gstructure.BLUE))
                else:
                    index = 0
                    print(self.styled_text("\t\t    O\'s turn\n",Gstructure.BLUE))    
                self.print_game(Gstructure.GAME_MAP, len(Gstructure.GAME_MAP))
                
                T = int(input("\n\nEnter your number (1-9) : "))
                if  T == 7: x,y = 0,0
                elif T == 8: x,y = 0,1
                elif T == 9: x,y = 0,2
                elif T == 4: x,y = 1,0
                elif T == 5: x,y = 1,1
                elif T == 6: x,y = 1,2
                elif T == 1: x,y = 2,0
                elif T == 2: x,y = 2,1
                elif T == 3: x,y = 2,2
                else: x,y = 3,3
                        
                try:
                    if Gstructure.GAME_MAP[x][y] == "":
                        self.update_chance(x,y,choice[index])
                    elif Gstructure.GAME_MAP[x][y] == "O" or "X":
                        print(self.styled_text("\n\t     Index already occupied!",Gstructure.RED,Gstructure.BOLD))
                        time.sleep(2)
                        turn -= 1    
                except IndexError:
                    print(self.styled_text("\n\t\tIndex out of Range!",Gstructure.RED,Gstructure.BOLD))
                    time.sleep(2)
                    turn -= 1    

            self.clear()
            print(self.styled_text("\t\t   Tik Tak Toe\n" ,Gstructure.YELLOW ,Gstructure.BOLD))      
            self.print_game(Gstructure.GAME_MAP, len(Gstructure.GAME_MAP)) 

            if self.check_win(choice[index])[0] == -1:
                print(self.styled_text(f"\n\n\t\t   It\'s a DRAW!",Gstructure.GREEN,Gstructure.BOLD))
            else:                
                print(self.styled_text(f"\n\n\t\t     {choice[index]} won!",Gstructure.GREEN,Gstructure.BOLD))  

    def styled_text(self, text: str, color: int = 0, style: int = 0) -> str:
        return f"\033[{int(style)};{color}m{text}\033[39m"

    def print_game(self, map: list, ran: int) -> str:
        try:
            for col in range (0,ran):
                for row in range (0,ran):
                    if row!=2:
                        pole="\t│"
                    else:
                        pole=""    
                    print("\t"+map[col][row]+pole,end="")
                if col!=2: 
                    print("")
                    for _ in range(0,48):
                        if(_%16==0 and _!=0):
                            print("┼",end="")
                        else:
                            print("─",end="")
                    print("")                
        except IndexError:
            print(self.styled_text("Index out of Range!",Gstructure.RED,Gstructure.BOLD))
        

    def update_chance(self, x: int, y: int, player: str = "X") -> None:
        if Gstructure.GAME_MAP[x][y] == "":
            Gstructure.GAME_MAP[x][y] = player
        else:
            pass                   

    def check_win(self, choice : str) -> list:
        super_list = Gstructure.GAME_MAP[0] + Gstructure.GAME_MAP[1] + Gstructure.GAME_MAP[2]
        while "" in super_list:
            for col in range (3):
                if Gstructure.GAME_MAP[col][0] == Gstructure.GAME_MAP[col][1] ==  Gstructure.GAME_MAP[col][2] != "":
                    Gstructure.GAME_MAP[col][0] = Gstructure.GAME_MAP[col][1] = Gstructure.GAME_MAP[col][2] = self.styled_text(choice,Gstructure.RED,Gstructure.BOLD)
                    return [1,Gstructure.GAME_MAP[col][1]]

            for row in range (3):
                if Gstructure.GAME_MAP[0][row] == Gstructure.GAME_MAP[1][row] ==  Gstructure.GAME_MAP[2][row] != "":
                    Gstructure.GAME_MAP[0][row] = Gstructure.GAME_MAP[1][row] = Gstructure.GAME_MAP[2][row] = self.styled_text(choice,Gstructure.RED,Gstructure.BOLD)
                    return [1,Gstructure.GAME_MAP[1][row]]

            if  Gstructure.GAME_MAP[0][0] == Gstructure.GAME_MAP[1][1] ==  Gstructure.GAME_MAP[2][2] != "":
                Gstructure.GAME_MAP[0][0] = Gstructure.GAME_MAP[1][1] = Gstructure.GAME_MAP[2][2] = self.styled_text(choice,Gstructure.RED,Gstructure.BOLD)
                return [1,Gstructure.GAME_MAP[1][1]]

            elif Gstructure.GAME_MAP[0][2] == Gstructure.GAME_MAP[1][1] ==  Gstructure.GAME_MAP[2][0] != "":
                Gstructure.GAME_MAP[0][2] = Gstructure.GAME_MAP[1][1] = Gstructure.GAME_MAP[2][0] = self.styled_text(choice,Gstructure.RED,Gstructure.BOLD)
                return [1,Gstructure.GAME_MAP[1][1]]

            else:
                return [0] 
        return [-1]                   

    def clear(self) -> None:
        if name == 'nt':
                _ = system('cls')
        else:
                _ = system('clear') 

    def check_argument(self) -> list:
        return sys.argv[1:]  
                             
if __name__ == "__main__":
    try:
        Gstructure()
    except KeyboardInterrupt:
        exit(130)               
