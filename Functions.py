import time
from copy import deepcopy

from numpy import sin, cos, tan, fabs


class Functions:
    NL = '\n'

    ConstValueDict = {
        'SinRange': 63,
        'SinLenStr': 161,
        'SinSleep': 0.05,
        'SinValue': 10,

        'CosRange': 63,
        'CosLenStr': 161,
        'CosSleep': 0.05,
        'CosValue': 10,

        'TanRange': 32,
        'TanSleep': 0.05,
        'TanLenStr': 161,
        'TanValue': 10,

        'CosSinRange': 63,
        'CosSinSleep': 0.05,
        'CosSinLenStr': 161,
        'CosSinValue': 10,
    }

    def __init__(self):
        self.ValueDict = None
        self.Buffer = None

        self.ClearBuffer()

    def ClearBuffer(self):
        self.Buffer = None

        self.ValueDict = deepcopy(self.ConstValueDict)

    def SIN(self, V_Key=0, Symbol=0, CF_Key=0, Value=0):
        if CF_Key == '-cf':
            if Value >= 1:
                self.ValueDict['SinRange'] = round(self.ValueDict['SinRange'] * fabs(Value))
                self.ValueDict['SinValue'] = round(self.ValueDict['SinValue'] * Value)
            else:
                self.ValueDict['SinRange'] = int(self.ValueDict['SinRange'] * fabs(Value))
                self.ValueDict['SinValue'] = int(self.ValueDict['SinValue'] * Value)

        SinSleep = self.ValueDict['SinSleep']
        SinRange = self.ValueDict['SinRange']
        SinValue = self.ValueDict['SinValue']

        if V_Key in ('-v', '-l1', '-l2', 'l3', '-l4'):
            self.Buffer = {number: f"{Symbol * round((1 + sin(number / SinValue)) * 80)}0" for number in range(SinRange)}
            return

        elif V_Key in ['-r1', '-r2', '-r3', '-r4']:
            self.Buffer = {number: '' for number in range(SinRange)}
            SinLenStr = self.ValueDict['SinLenStr']

            for number in range(SinRange):
                Sin = f"{' ' * round((1 + sin(number / SinValue)) * 80)}0"
                self.Buffer[number] = f"{Sin}{Symbol * (SinLenStr - len(Sin))}"
            return

        elif V_Key in ['-c1', '-c2', '-c3', '-c4']:
            self.Buffer = {number: '' for number in range(SinRange)}
            SinLenStr = round(self.ValueDict['SinLenStr'] / 2)

            for number in range(SinRange):
                Sin = f"{' ' * round((1 + sin(number / SinValue)) * 80)}0"
                LenSin = len(Sin)

                self.Buffer[number] = f"{Sin}{Symbol * (SinLenStr - LenSin)}" if LenSin < SinLenStr else (
                    f"{Sin[0: SinLenStr]}{Symbol * (LenSin - SinLenStr - 1)}{Sin[LenSin - 1]}" if LenSin > SinLenStr
                    else Sin)
            return

        elif V_Key != 0:
            a = 1 / 0

        while True:
            for number in range(SinRange):
                print(self.Buffer[number])
                time.sleep(SinSleep)

    def COS(self, V_Key=0, Symbol=0, CF_Key=0, Value=0):
        if CF_Key == '-cf':
            if Value >= 1:
                self.ValueDict['CosRange'] = round(self.ValueDict['CosRange'] * fabs(Value))
                self.ValueDict['CosValue'] = round(self.ValueDict['CosValue'] * Value)
            else:
                self.ValueDict['CosRange'] = int(self.ValueDict['CosRange'] * fabs(Value))
                self.ValueDict['CosValue'] = int(self.ValueDict['CosValue'] * Value)

        CosSleep = self.ValueDict['CosSleep']
        CosRange = self.ValueDict['CosRange']
        CosValue = self.ValueDict['CosValue']

        if V_Key in ['-v', '-l1', '-l2', 'l3', '-l4']:
            self.Buffer = {number: f"{Symbol * round((1 + cos(number / CosValue)) * 80)}0" for number in range(CosRange)}
            return

        elif V_Key in ['-r1', '-r2', '-r3', '-r4']:
            self.Buffer = {number: '' for number in range(CosRange)}
            CosLenStr = self.ValueDict['CosLenStr']

            for number in range(CosRange):
                Cos = f"{' ' * round((1 + cos(number / CosValue)) * 80)}0"
                self.Buffer[number] = f"{Cos}{Symbol * (CosLenStr - len(Cos))}"
            return

        elif V_Key in ['-c1', '-c2', '-c3', '-c4']:
            self.Buffer = {number: '' for number in range(CosRange)}
            CosLenStr = round(self.ValueDict['CosLenStr'] / 2)

            for number in range(CosRange):
                Cos = f"{' ' * round((1 + cos(number / CosValue)) * 80)}0"
                LenCos = len(Cos)

                self.Buffer[number] = f"{Cos}{Symbol * (CosLenStr - LenCos)}" if LenCos < CosLenStr else (
                    f"{Cos[0: CosLenStr]}{Symbol * (LenCos - CosLenStr - 1)}{Cos[LenCos - 1]}" if LenCos > CosLenStr
                    else Cos)
            return

        elif V_Key != 0:
            a = 1 / 0

        while True:
            for number in range(CosRange):
                print(self.Buffer[number])
                time.sleep(CosSleep)

    def TAN(self, V_Key=0, Symbol=0, CF_Key=0, Value=0):
        if CF_Key == '-cf':
            if Value >= 1:
                self.ValueDict['TanRange'] = round(self.ValueDict['TanRange'] * fabs(Value))
                self.ValueDict['TanValue'] = round(self.ValueDict['TanValue'] * Value)
            else:
                self.ValueDict['TanRange'] = int(self.ValueDict['TanRange'] * fabs(Value))
                self.ValueDict['TanValue'] = int(self.ValueDict['TanValue'] * Value)

        TanSleep = self.ValueDict['TanSleep']
        TanRange = self.ValueDict['TanRange']
        TanValue = self.ValueDict['TanValue']

        if V_Key in ['-v', '-l1', '-l2', 'l3', '-l4']:
            self.Buffer = {number: f"{Symbol * round((90 + tan(number / TanValue)))}0" for number in range(TanRange)}
            return

        elif V_Key in ['-r1', '-r2', '-r3', '-r4']:
            self.Buffer = {number: '' for number in range(TanRange)}
            TanLenStr = self.ValueDict['TanLenStr']

            for number in range(TanRange):
                Tan = f"{' ' * round((90 + tan(number / TanValue)))}0"
                self.Buffer[number] = f"{Tan}{Symbol * (TanLenStr - len(Tan))}"
            return

        elif V_Key != 0:
            a = 1 / 0

        while True:
            for number in range(TanRange):
                print(self.Buffer[number])
                time.sleep(TanSleep)

    def COS_SIN(self, V_Key=0, Symbol=0, CF_Key=0, Value=0):
        if CF_Key == '-cf':
            if Value >= 1:
                self.ValueDict['CosSinRange'] = round(self.ValueDict['CosSinRange'] * fabs(Value))
                self.ValueDict['CosSinValue'] = round(self.ValueDict['CosSinValue'] * Value)
            else:
                self.ValueDict['CosSinRange'] = int(self.ValueDict['CosSinRange'] * fabs(Value))
                self.ValueDict['CosSinValue'] = int(self.ValueDict['CosSinValue'] * Value)

        CosSinSleep = self.ValueDict['CosSinSleep']
        CosSinRange = self.ValueDict['CosSinRange']
        CosSinValue = self.ValueDict['CosSinValue']

        if V_Key in ['-v', '-c1', '-c2', '-c3', '-c4']:
            self.Buffer = {number: '' for number in range(CosSinRange)}

            for number in range(CosSinRange):
                Sin = f"{' ' * round((1 + sin(number / CosSinValue)) * 80)}0"
                Cos = f"{' ' * round((1 + cos(number / CosSinValue)) * 80)}0"

                LenSin = len(Sin)
                LenCos = len(Cos)

                self.Buffer[number] = (f"{Cos}{Symbol * (LenSin - LenCos - 1)}{Sin[-1]}" if LenSin > LenCos else
                                       (Sin if LenSin == LenCos else f"{Sin}{Symbol * (LenCos - LenSin - 1)}{Cos[-1]}"))
            return

        elif V_Key in ['-lr1', '-lr2', '-lr3', '-lr4']:
            self.Buffer = {number: '' for number in range(CosSinRange)}
            CosSinLenStr = self.ValueDict['CosSinLenStr']

            for number in range(CosSinRange):
                Sin = f"{' ' * round((1 + sin(number / CosSinValue)) * 80)}0"
                Cos = f"{' ' * round((1 + cos(number / CosSinValue)) * 80)}0"

                LenSin = len(Sin)
                LenCos = len(Cos)

                self.Buffer[number] = (
                    f"{Symbol * (LenCos - 1)}{Cos[-1]}{Sin[LenCos - LenSin: LenSin]}{Symbol * (CosSinLenStr - LenSin)}"
                    if LenSin > LenCos else (
                        f"{Symbol * (LenSin - 1)}{Sin[-1]}{Symbol * (CosSinLenStr - LenSin)}" if LenSin == LenCos
                        else (
                            f"{Symbol * (LenSin - 1)}{Sin[-1]}{Cos[LenSin - LenCos: LenCos]}{Symbol * (CosSinLenStr - LenCos)}")))
            return

        elif V_Key != 0:
            a = 1 / 0

        while True:
            for number in range(CosSinRange):
                print(self.Buffer[number])
                time.sleep(CosSinSleep)
