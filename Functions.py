import time
from numpy import sin, cos, tan


class Functions:
    NL = '\n'

    def __init__(self):
        self.SinRange = 63
        self.SinLenStr = 161
        self.SinSleep = 0.05

        self.CosRange = 63
        self.CosLenStr = 161
        self.CosSleep = 0.05

        self.TanRange = 32
        self.TanSleep = 0.05

        self.CosSinRange = 63
        self.CosSinSleep = 0.05
        self.CosSinLenStr = 161

        self.Buffer = None

    def ClearBuffer(self):
        self.Buffer = None

    def SIN(self, Key=0, Symbol=0):
        if Key in ['-v', '-l1', '-l2', 'l3', '-l4']:
            self.Buffer = {number: f"{Symbol * round((1 + sin(number / 10)) * 80)}0" for number in range(self.SinRange)}
            return

        elif Key in ['-r1', '-r2', '-r3', '-r4']:

            self.Buffer = {number: '' for number in range(self.SinRange)}

            for number in range(self.SinRange):
                Sin = f"{' ' * round((1 + sin(number / 10)) * 80)}0"
                self.Buffer[number] = f"{Sin}{Symbol * (self.SinLenStr - len(Sin))}"
            return

        elif Key in ['-c1', '-c2', '-c3', '-c4']:
            self.Buffer = {number: '' for number in range(self.SinRange)}
            SinLenStr = round(self.SinLenStr / 2)

            for number in range(self.SinRange):
                Sin = f"{' ' * round((1 + sin(number / 10)) * 80)}0"
                LenSin = len(Sin)

                self.Buffer[number] = f"{Sin}{Symbol * (SinLenStr - LenSin)}" if LenSin < SinLenStr else (
                    f"{Sin[0: SinLenStr]}{Symbol * (LenSin - SinLenStr - 1)}{Sin[LenSin - 1]}" if LenSin > SinLenStr
                    else Sin)
            return

        elif Key != 0:
            int('')

        while True:
            for number in range(self.SinRange):
                print(self.Buffer[number])
                time.sleep(self.SinSleep)

    def COS(self, Key=0, Symbol=0):
        if Key in ['-v', '-l1', '-l2', 'l3', '-l4']:
            self.Buffer = {number: f"{Symbol * round((1 + cos(number / 10)) * 80)}0" for number in range(self.CosRange)}
            return

        elif Key in ['-r1', '-r2', '-r3', '-r4']:
            self.Buffer = {number: '' for number in range(self.CosRange)}

            for number in range(self.CosRange):
                Cos = f"{' ' * round((1 + cos(number / 10)) * 80)}0"
                self.Buffer[number] = f"{Cos}{Symbol * (self.CosLenStr - len(Cos))}"
            return

        elif Key in ['-c1', '-c2', '-c3', '-c4']:
            self.Buffer = {number: '' for number in range(self.CosRange)}
            CosLenStr = round(self.CosLenStr / 2)

            for number in range(self.CosRange):
                Cos = f"{' ' * round((1 + cos(number / 10)) * 80)}0"
                LenCos = len(Cos)

                self.Buffer[number] = f"{Cos}{Symbol * (CosLenStr - LenCos)}" if LenCos < CosLenStr else (
                    f"{Cos[0: CosLenStr]}{Symbol * (LenCos - CosLenStr - 1)}{Cos[LenCos - 1]}" if LenCos > CosLenStr
                    else Cos)
            return

        elif Key != 0:
            int('')

        while True:
            for number in range(self.CosRange):
                print(self.Buffer[number])
                time.sleep(self.CosSleep)

    def TAN(self, Key=0, Symbol=0):

        if Key in ['-v', '-l1', '-l2', 'l3', '-l4']:
            self.Buffer = {number: f"{Symbol * round((90 + tan(number / 10)))}0" for number in range(self.TanRange)}
            return

        elif Key in ['-r1', '-r2', '-r3', '-r4']:
            self.Buffer = {number: '' for number in range(self.TanRange)}

            for number in range(self.TanRange):
                Tan = f"{' ' * round((90 + tan(number / 10)))}0"
                self.Buffer[number] = f"{Tan}{Symbol * (self.CosLenStr - len(Tan))}"
            return

        elif Key != 0:
            int('')

        while True:
            for number in range(self.TanRange):
                print(self.Buffer[number])
                time.sleep(self.TanSleep)

    def COS_SIN(self, Key=0, Symbol=0):
        if Key in ['-v', '-c1', '-c2', '-c3', '-c4']:
            self.Buffer = {number: '' for number in range(self.CosSinRange)}

            for number in range(self.CosSinRange):
                Sin = f"{' ' * round((1 + sin(number / 10)) * 80)}0"
                Cos = f"{' ' * round((1 + cos(number / 10)) * 80)}0"

                LenSin = len(Sin)
                LenCos = len(Cos)

                self.Buffer[number] = (f"{Cos}{Symbol * (LenSin - LenCos - 1)}{Sin[-1]}" if LenSin > LenCos else
                                       (Sin if LenSin == LenCos else f"{Sin}{Symbol * (LenCos - LenSin - 1)}{Cos[-1]}"))
            return

        elif Key in ['-lr1', '-lr2', '-lr3', '-lr4']:
            self.Buffer = {number: '' for number in range(self.CosSinRange)}

            for number in range(self.CosSinRange):
                Sin = f"{' ' * round((1 + sin(number / 10)) * 80)}0"
                Cos = f"{' ' * round((1 + cos(number / 10)) * 80)}0"

                LenSin = len(Sin)
                LenCos = len(Cos)

                self.Buffer[number] = (
                    f"{Symbol * (LenCos - 1)}{Cos[-1]}{Sin[LenCos - LenSin: LenSin]}{Symbol * (self.CosSinLenStr - LenSin)}"
                    if LenSin > LenCos else (
                        f"{Symbol * (LenSin - 1)}{Sin[-1]}{Symbol * (self.CosSinLenStr - LenSin)}" if LenSin == LenCos
                        else (
                            f"{Symbol * (LenSin - 1)}{Sin[-1]}{Cos[LenSin - LenCos: LenCos]}{Symbol * (self.CosSinLenStr - LenCos)}")))
            return

        while True:
            for number in range(self.CosSinRange):
                print(self.Buffer[number])
                time.sleep(self.CosSinSleep)
