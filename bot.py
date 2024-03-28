import csv

from command import Command
import numpy as np
from buttons import Buttons


class Bot:

    def __init__(self):
        # < - v + < - v - v + > - > + Y
        self.current_game_state = None
        self.fire_code = ["<", "!<", "v+<", "!v+!<", "v", "!v", "v+>", "!v+!>", ">+Y", "!>+!Y"]
        self.exe_code = 0
        self.start_fire = True
        self.remaining_code = []
        self.my_command = Command()
        self.buttn = Buttons()

    def fight(self, current_game_state, player, loaded_model):
        self.current_game_state = current_game_state

        # python Videos\gamebot-competition-master\PythonAPI\controller.py 1
        if player == "1":
            # print("1")
            # v - < + v - < + B spinning
            prediction = 0
            i = 0

            while prediction == 0 and i < 10:

                if (self.exe_code != 0):
                    self.run_command([], current_game_state.player1)
                diff = current_game_state.player2.x_coord - current_game_state.player1.x_coord
                if (diff > 60):
                    toss = np.random.randint(3)
                    if (toss == 0):
                        # self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player1)
                        self.run_command(
                            [">", "-", "!>", "v+>", "-", "!v+!>", "v", "-", "!v", "v+<", "-", "!v+!<", "<+Y", "-",
                             "!<+!Y"],
                            current_game_state.player1)
                    elif (toss == 1):
                        self.run_command([">+^+B", ">+^+B", "!>+!^+!B"], current_game_state.player1)
                    else:  # fire
                        self.run_command(
                            ["<", "-", "!<", "v+<", "-", "!v+!<", "v", "-", "!v", "v+>", "-", "!v+!>", ">+Y", "-",
                             "!>+!Y"],
                            current_game_state.player1)
                elif (diff < -60):
                    toss = np.random.randint(3)
                    if (toss == 0):  # spinning
                        # self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player1)
                        self.run_command(
                            ["<", "-", "!<", "v+<", "-", "!v+!<", "v", "-", "!v", "v+>", "-", "!v+!>", ">+Y", "-",
                             "!>+!Y"],
                            current_game_state.player1)
                    elif (toss == 1):  #
                        self.run_command(["<+^+B", "<+^+B", "!<+!^+!B"], current_game_state.player1)
                    else:  # fire
                        self.run_command(
                            [">", "-", "!>", "v+>", "-", "!v+!>", "v", "-", "!v", "v+<", "-", "!v+!<", "<+Y", "-",
                             "!<+!Y"],
                            current_game_state.player1)
                else:
                    toss = np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
                    if (toss >= 1):
                        if (diff > 0):
                            self.run_command(["<", "<", "!<"], current_game_state.player1)
                        else:
                            self.run_command([">", ">", "!>"], current_game_state.player1)
                    else:
                        self.run_command(["v+R", "v+R", "v+R", "!v+!R"], current_game_state.player1)
                self.my_command.player_buttons = self.buttn

                # Assume that you have a new row of data as a numpy array, called `new_data_row`
                new_data_row = np.array([
                    int(self.current_game_state.player1.player_id),
                    int(self.current_game_state.player2.player_id),
                    self.current_game_state.timer,
                    int(self.current_game_state.player1.player_buttons.up),
                    int(self.current_game_state.player1.player_buttons.down),
                    int(self.current_game_state.player1.player_buttons.left),
                    int(self.current_game_state.player1.player_buttons.right),
                    int(self.current_game_state.player1.player_buttons.A),
                    int(self.current_game_state.player1.player_buttons.B),
                    int(self.current_game_state.player1.player_buttons.X),
                    int(self.current_game_state.player1.player_buttons.Y),
                    int(self.current_game_state.player1.player_buttons.L),
                    int(self.current_game_state.player1.player_buttons.R),
                    int(self.current_game_state.player1.is_jumping),
                    int(self.current_game_state.player1.is_crouching),
                    int(self.current_game_state.player1.is_player_in_move),
                    self.current_game_state.player2.x_coord - self.current_game_state.player1.x_coord,
                    self.current_game_state.player2.y_coord - self.current_game_state.player1.y_coord,
                    int(self.current_game_state.player2.is_jumping),
                    int(self.current_game_state.player2.is_crouching),
                    int(self.current_game_state.player2.is_player_in_move)
                ])

                # Reshape the new data row to have a single sample with the appropriate number of features
                new_data_row = new_data_row.reshape(1, -1)

                # Make a prediction with the loaded model
                prediction = loaded_model.predict(new_data_row)

                # Print the prediction
                print('Prediction:', prediction[0][0])
                prediction = prediction[0][0]
                i += 1

        elif player == "2":

            prediction = 0
            i = 0

            while prediction == 0 and i < 10:

                if (self.exe_code != 0):
                    self.run_command([], current_game_state.player2)
                diff = current_game_state.player1.x_coord - current_game_state.player2.x_coord
                if (diff > 60):
                    toss = np.random.randint(3)
                    if (toss == 0):
                        # self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player2)
                        self.run_command(
                            [">", "-", "!>", "v+>", "-", "!v+!>", "v", "-", "!v", "v+<", "-", "!v+!<", "<+Y", "-", "!<+!Y"],
                            current_game_state.player2)
                    elif (toss == 1):
                        self.run_command([">+^+B", ">+^+B", "!>+!^+!B"], current_game_state.player2)
                    else:
                        self.run_command(
                            ["<", "-", "!<", "v+<", "-", "!v+!<", "v", "-", "!v", "v+>", "-", "!v+!>", ">+Y", "-", "!>+!Y"],
                            current_game_state.player2)
                elif (diff < -60):
                    toss = np.random.randint(3)
                    if (toss == 0):
                        # self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player2)
                        self.run_command(
                            ["<", "-", "!<", "v+<", "-", "!v+!<", "v", "-", "!v", "v+>", "-", "!v+!>", ">+Y", "-", "!>+!Y"],
                            current_game_state.player2)
                    elif (toss == 1):
                        self.run_command(["<+^+B", "<+^+B", "!<+!^+!B"], current_game_state.player2)
                    else:
                        self.run_command(
                            [">", "-", "!>", "v+>", "-", "!v+!>", "v", "-", "!v", "v+<", "-", "!v+!<", "<+Y", "-", "!<+!Y"],
                            current_game_state.player2)
                else:
                    toss = np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
                    if (toss >= 1):
                        if (diff < 0):
                            self.run_command(["<", "<", "!<"], current_game_state.player2)
                        else:
                            self.run_command([">", ">", "!>"], current_game_state.player2)
                    else:
                        self.run_command(["v+R", "v+R", "v+R", "!v+!R"], current_game_state.player2)
                self.my_command.player2_buttons = self.buttn

                # Assume that you have a new row of data as a numpy array, called `new_data_row`
                new_data_row = np.array([
                    int(self.current_game_state.player2.player_id),
                    int(self.current_game_state.player1.player_id),
                    self.current_game_state.timer,
                    int(self.current_game_state.player2.player_buttons.up),
                    int(self.current_game_state.player2.player_buttons.down),
                    int(self.current_game_state.player2.player_buttons.left),
                    int(self.current_game_state.player2.player_buttons.right),
                    int(self.current_game_state.player2.player_buttons.A),
                    int(self.current_game_state.player2.player_buttons.B),
                    int(self.current_game_state.player2.player_buttons.X),
                    int(self.current_game_state.player2.player_buttons.Y),
                    int(self.current_game_state.player2.player_buttons.L),
                    int(self.current_game_state.player2.player_buttons.R),
                    int(self.current_game_state.player2.is_jumping),
                    int(self.current_game_state.player2.is_crouching),
                    int(self.current_game_state.player2.is_player_in_move),
                    self.current_game_state.player1.x_coord - self.current_game_state.player2.x_coord,
                    self.current_game_state.player1.y_coord - self.current_game_state.player2.y_coord,
                    int(self.current_game_state.player1.is_jumping),
                    int(self.current_game_state.player1.is_crouching),
                    int(self.current_game_state.player1.is_player_in_move)
                ])

                # Reshape the new data row to have a single sample with the appropriate number of features
                new_data_row = new_data_row.reshape(1, -1)

                # Make a prediction with the loaded model
                prediction = loaded_model.predict(new_data_row)

                # Print the prediction
                print('Prediction:', prediction[0][0])
                prediction = prediction[0][0]
                i += 1

        return self.my_command

    def run_command(self, com, player):

        if self.exe_code - 1 == len(self.fire_code):
            self.exe_code = 0
            self.start_fire = False
            print("compelete")
            # exit()
            # print ( "left:",player.player_buttons.left )
            # print ( "right:",player.player_buttons.right )
            # print ( "up:",player.player_buttons.up )
            # print ( "down:",player.player_buttons.down )
            # print ( "Y:",player.player_buttons.Y )

        elif len(self.remaining_code) == 0:

            self.fire_code = com
            # self.my_command=Command()
            self.exe_code += 1

            self.remaining_code = self.fire_code[0:]

        else:
            self.exe_code += 1
            if self.remaining_code[0] == "v+<":
                self.buttn.down = True
                self.buttn.left = True
                print("v+<")
            elif self.remaining_code[0] == "!v+!<":
                self.buttn.down = False
                self.buttn.left = False
                print("!v+!<")
            elif self.remaining_code[0] == "v+>":
                self.buttn.down = True
                self.buttn.right = True
                print("v+>")
            elif self.remaining_code[0] == "!v+!>":
                self.buttn.down = False
                self.buttn.right = False
                print("!v+!>")

            elif self.remaining_code[0] == ">+Y":
                self.buttn.Y = True  # not (player.player_buttons.Y)
                self.buttn.right = True
                print(">+Y")
            elif self.remaining_code[0] == "!>+!Y":
                self.buttn.Y = False  # not (player.player_buttons.Y)
                self.buttn.right = False
                print("!>+!Y")

            elif self.remaining_code[0] == "<+Y":
                self.buttn.Y = True  # not (player.player_buttons.Y)
                self.buttn.left = True
                print("<+Y")
            elif self.remaining_code[0] == "!<+!Y":
                self.buttn.Y = False  # not (player.player_buttons.Y)
                self.buttn.left = False
                print("!<+!Y")

            elif self.remaining_code[0] == ">+^+L":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.L = not (player.player_buttons.L)
                print(">+^+L")
            elif self.remaining_code[0] == "!>+!^+!L":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.L = False  # not (player.player_buttons.L)
                print("!>+!^+!L")

            elif self.remaining_code[0] == ">+^+Y":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.Y = not (player.player_buttons.Y)
                print(">+^+Y")
            elif self.remaining_code[0] == "!>+!^+!Y":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.Y = False  # not (player.player_buttons.L)
                print("!>+!^+!Y")


            elif self.remaining_code[0] == ">+^+R":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.R = not (player.player_buttons.R)
                print(">+^+R")
            elif self.remaining_code[0] == "!>+!^+!R":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.R = False  # ot (player.player_buttons.R)
                print("!>+!^+!R")

            elif self.remaining_code[0] == ">+^+A":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.A = not (player.player_buttons.A)
                print(">+^+A")
            elif self.remaining_code[0] == "!>+!^+!A":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.A = False  # not (player.player_buttons.A)
                print("!>+!^+!A")

            elif self.remaining_code[0] == ">+^+B":
                self.buttn.right = True
                self.buttn.up = True
                self.buttn.B = not (player.player_buttons.B)
                print(">+^+B")
            elif self.remaining_code[0] == "!>+!^+!B":
                self.buttn.right = False
                self.buttn.up = False
                self.buttn.B = False  # not (player.player_buttons.A)
                print("!>+!^+!B")

            elif self.remaining_code[0] == "<+^+L":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.L = not (player.player_buttons.L)
                print("<+^+L")
            elif self.remaining_code[0] == "!<+!^+!L":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.L = False  # not (player.player_buttons.Y)
                print("!<+!^+!L")

            elif self.remaining_code[0] == "<+^+Y":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.Y = not (player.player_buttons.Y)
                print("<+^+Y")
            elif self.remaining_code[0] == "!<+!^+!Y":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.Y = False  # not (player.player_buttons.Y)
                print("!<+!^+!Y")

            elif self.remaining_code[0] == "<+^+R":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.R = not (player.player_buttons.R)
                print("<+^+R")
            elif self.remaining_code[0] == "!<+!^+!R":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.R = False  # not (player.player_buttons.Y)
                print("!<+!^+!R")

            elif self.remaining_code[0] == "<+^+A":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.A = not (player.player_buttons.A)
                print("<+^+A")
            elif self.remaining_code[0] == "!<+!^+!A":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.A = False  # not (player.player_buttons.Y)
                print("!<+!^+!A")

            elif self.remaining_code[0] == "<+^+B":
                self.buttn.left = True
                self.buttn.up = True
                self.buttn.B = not (player.player_buttons.B)
                print("<+^+B")
            elif self.remaining_code[0] == "!<+!^+!B":
                self.buttn.left = False
                self.buttn.up = False
                self.buttn.B = False  # not (player.player_buttons.Y)
                print("!<+!^+!B")

            elif self.remaining_code[0] == "v+R":
                self.buttn.down = True
                self.buttn.R = not (player.player_buttons.R)
                print("v+R")
            elif self.remaining_code[0] == "!v+!R":
                self.buttn.down = False
                self.buttn.R = False  # not (player.player_buttons.Y)
                print("!v+!R")

            else:
                if self.remaining_code[0] == "v":
                    self.buttn.down = True
                    print("down")
                elif self.remaining_code[0] == "!v":
                    self.buttn.down = False
                    print("Not down")
                elif self.remaining_code[0] == "<":
                    print("left")
                    self.buttn.left = True
                elif self.remaining_code[0] == "!<":
                    print("Not left")
                    self.buttn.left = False
                elif self.remaining_code[0] == ">":
                    print("right")
                    self.buttn.right = True
                elif self.remaining_code[0] == "!>":
                    print("Not right")
                    self.buttn.right = False

                elif self.remaining_code[0] == "^":
                    print("up")
                    self.buttn.up = True
                elif self.remaining_code[0] == "!^":
                    print("Not up")
                    self.buttn.up = False

            # write the current state of the buttons in the csv file
            # write the buttons name and time that are pressed in the csv file this will be in a single row

            with open('game_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    int(self.current_game_state.player1.player_id),
                    int(self.current_game_state.player2.player_id),
                    self.current_game_state.timer,
                    int(self.current_game_state.player1.player_buttons.up),
                    int(self.current_game_state.player1.player_buttons.down),
                    int(self.current_game_state.player1.player_buttons.left),
                    int(self.current_game_state.player1.player_buttons.right),
                    int(self.current_game_state.player1.player_buttons.A),
                    int(self.current_game_state.player1.player_buttons.B),
                    int(self.current_game_state.player1.player_buttons.X),
                    int(self.current_game_state.player1.player_buttons.Y),
                    int(self.current_game_state.player1.player_buttons.L),
                    int(self.current_game_state.player1.player_buttons.R),
                    int(self.current_game_state.player1.is_jumping),
                    int(self.current_game_state.player1.is_crouching),
                    int(self.current_game_state.player1.is_player_in_move),
                    self.current_game_state.player2.x_coord - self.current_game_state.player1.x_coord,
                    self.current_game_state.player2.y_coord - self.current_game_state.player1.y_coord,
                    int(self.current_game_state.player2.is_jumping),
                    int(self.current_game_state.player2.is_crouching),
                    int(self.current_game_state.player2.is_player_in_move),
                    int(self.current_game_state.player1.health - self.current_game_state.player2.health),
                ])

            self.remaining_code = self.remaining_code[1:]

        return
