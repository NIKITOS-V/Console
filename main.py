from Functions import Functions
import multiprocessing
import time


class CONSOLE:
    NL = "\n"
    TAB = "\t"

    def __init__(self):
        self.RunApp = 1
        self.GoodJobTimeToSleep = 2

        self.AllCommandsDict = {'sin': (self.Schedule, 'Вывод графика y = sin(x)',
                                        'время вывода в секундах', 'ключи визуализации'),
                                'cos': (self.Schedule, 'Вывод графика y = cos(x)',
                                        'время вывода в секундах', 'ключи визуализации'),
                                'tan': (self.Schedule, 'Вывод графика y = tan(x)',
                                        'время вывода в секундах', 'ключи визуализации'),
                                'cos_sin': (self.Schedule,
                                            'Вывод графика y = sin(x) и y = cos(x) в одной системе координат',
                                            'время вывода в секундах', 'ключи визуализации'),

                                'commands': (self.PrintCommand, 'Выводит список команд визуализации с их описанием'),
                                'keys': (self.PrintKeys, 'Выводит список ключей визуализации с их описанием'),
                                'good_job': (self.GoodJob, ':)'),
                                'end': (self.StopApp, 'Завершает работу консоли')}

        self.VisualKeysDict = {'-v': (' ', 'Ключ, используемый по умолчанию', 'все графические функции'),
                               '-l1': ('-', 'Заменяет пробел на используемый символ левее графика функции',
                                       'sin , cos, tan'),
                               '-l2': ('~', 'Заменяет пробел на используемый символ левее графика функции',
                                       'sin , cos, tan'),
                               '-l3': ('*', 'Заменяет пробел на используемый символ левее графика функции',
                                       'sin , cos, tan'),
                               '-l4': ('0', 'Заменяет пробел на используемый символ левее графика функции',
                                       'sin , cos, tan'),
                               '-r1': ('-', 'Заменяет пробел на используемый символ правее графика функции',
                                       'sin , cos, tan'),
                               '-r2': ('~', 'Заменяет пробел на используемый символ правее графика функции',
                                       'sin , cos, tan'),
                               '-r3': ('*', 'Заменяет пробел на используемый символ правее графика функции',
                                       'sin , cos, tan'),
                               '-r4': ('0', 'Заменяет пробел на используемый символ правее графика функции',
                                       'sin , cos, tan'),
                               '-c1': ('-', 'Заменяет пробел на используемый символ в промежутке между осью координат и'
                                            ' графика функции', 'sin , cos, cos_sin'),
                               '-c2': ('~', 'Заменяет пробел на используемый символ в промежутке между осью координат и'
                                            ' графика функции', 'sin , cos, cos_sin'),
                               '-c3': ('*', 'Заменяет пробел на используемый символ в промежутке между осью координат и'
                                            ' графика функции', 'sin , cos, cos_sin'),
                               '-c4': ('0', 'Заменяет пробел на используемый символ в промежутке между осью координат и'
                                            ' графика функции', 'sin , cos, cos_sin'),
                               '-lr1': ('-', 'Заменяет пробел на используемый символ левее и правее графика функции',
                                        'cos_sin'),
                               '-lr2': ('~', 'Заменяет пробел на используемый символ левее и правее графика функции',
                                        'cos_sin'),
                               '-lr3': ('*', 'Заменяет пробел на используемый символ левее и правее графика функции',
                                        'cos_sin'),
                               '-lr4': ('0', 'Заменяет пробел на используемый символ левее и правее графика функции',
                                        'cos_sin'),
                               }

        self.Func = Functions()

    def MainLoop(self):
        while self.RunApp:
            self.UserCommand = input(f"{self.NL * 2}Console: ").split()

            try:
                self.AllCommandsDict[self.UserCommand[0]][0]()
            except KeyError:
                print(f"{self.NL}CONSOLE ERROR: Unknown command (write 'commands' for information)")

    def Schedule(self):
        AllFunctionsDict = {'sin': self.Func.SIN, 'cos': self.Func.COS, 'tan': self.Func.TAN,
                            'cos_sin': self.Func.COS_SIN}

        Function = AllFunctionsDict[self.UserCommand[0]]

        try:
            Time = float(self.UserCommand[1])

        except IndexError:
            print(f"{self.NL}FUNCTION ERROR: Function needs execution time (write 'commands' for information)")
            return

        except ValueError:
            print(f"{self.NL}FUNCTION ERROR: Time must be of type int or float (write 'commands' for information)")
            return

        try:
            Function(Key=self.UserCommand[2], Symbol=self.VisualKeysDict[self.UserCommand[2]][0])

        except KeyError:
            print(f"{self.NL}FUNCTION ERROR: Unknown visual code (write 'keys' for information)")
            return

        except IndexError:
            Function(Key='-v', Symbol=self.VisualKeysDict['-v'][0])

        except ValueError:
            print(f"{self.NL}FUNCTION ERROR: This function does not support this key "
                  f"(write 'keys' for information)")
            return

        Process = multiprocessing.Process(target=Function)

        Process.start()
        Process.join(Time)

        if Process.is_alive():
            Process.terminate()
            self.Func.ClearBuffer()

    def PrintCommand(self):
        print(f"{self.NL}{self.TAB}Вид записи: имя_функции значение_параметра_1 значение_параметра_2{self.NL}")

        for command in self.AllCommandsDict.keys():
            Instruction = self.AllCommandsDict[command]
            print(f"{self.TAB}{command}: ")
            print(f"{self.TAB*2}Описание: {Instruction[1]}")
            try:
                print(f"{self.TAB*2}Обязательные параметры: {Instruction[2]}")
                print(f"{self.TAB*2}Необязательные параметры: {Instruction[3]}")
            except IndexError:
                pass
            print()

    def PrintKeys(self):
        print(f"{self.NL}")

        for key in self.VisualKeysDict.keys():
            print(f"{self.TAB}{key}: ")
            print(f"{self.TAB * 2}Используемый символ: {self.VisualKeysDict[key][0]}")
            print(f"{self.TAB * 2}Описание: {self.VisualKeysDict[key][1]}")
            print(f"{self.TAB * 2}Используется: {self.VisualKeysDict[key][2]}")
            print()

    def GoodJob(self):
        print(f"{self.NL * 2}{self.TAB * 2} Thank you !")
        time.sleep(self.GoodJobTimeToSleep)
        self.StopApp()

    def StopApp(self):
        self.RunApp = 0


if __name__ == "__main__":
    Console = CONSOLE()
    Console.MainLoop()
