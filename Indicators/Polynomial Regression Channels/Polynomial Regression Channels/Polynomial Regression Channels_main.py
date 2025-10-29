import clr
clr.AddReference("cAlgo.API")

from cAlgo.API import *
import math

class PolynomialRegressionChannels():
    I0 = 0

    def initialize(self):
        self.ai = [[0.0 for i in range(10)] for x in range(10)]
        self.b = [0.0 for i in range(10)]
        self.nn = 0
        self.sx = [0.0 for i in range(10)]
        self.x = [0.0 for i in range(10)]

    def calculate(self, index):
        self.sx[1] = api.Periods + 1
        self.nn = api.Degree + 1

        self.calculate_sx()
        self.calculate_syx(index)
        self.calculate_matrix()

        self.calculate_gauss_deviations(index)

    def calculate_sx(self):
        for i in range(1, (self.nn * 2 -2) + 1):
            sumValue = 0
            for n in range(self.I0, self.I0 + api.Periods + 1):
                sumValue += pow(n, i)

            self.sx[i + 1] = sumValue

    def calculate_syx(self, index):
        for i in range(1, self.nn + 1):
            sumValue = 0
            for n in range(self.I0, self.I0 + api.Periods + 1):
                if i == 1:
                    sumValue += api.Bars.ClosePrices[index - n]
                else:
                    sumValue += api.Bars.ClosePrices[index - n] * pow(n, i - 1)

            self.b[i] = sumValue

    def calculate_matrix(self):
        for j in range(1, self.nn + 1):
            for i in range(1, self.nn + 1):
                k = i + j - 1
                self.ai[i][j] = self.sx[k]

    def calculate_gauss_deviations(self, index):
        for k in range(1, self.nn):
            ll = 0
            mm = 0

            for i in range(k, self.nn + 1):
                if abs(self.ai[i][k]) > mm:
                    mm = abs(self.ai[i][k])
                    ll = i

            if ll == 0:
                return

            if ll != k:
                for j in range(1, self.nn + 1):
                    temp = self.ai[k][j]
                    self.ai[k][j] = self.ai[ll][j]
                    self.ai[ll][j] = temp

                bk = self.b[k]
                self.b[k] = self.b[ll]
                self.b[ll] = bk

            for i in range(k + 1, self.nn + 1):
                qq = self.ai[i][k] / self.ai[k][k]
                for j in range(1, self.nn + 1):
                    if j == k:
                        self.ai[i][j] = 0
                    else:
                        self.ai[i][j] = self.ai[i][j] - qq * self.ai[k][j]

                self.b[i] = self.b[i] - qq * self.b[k]

        self.x[self.nn] = self.b[self.nn] / self.ai[self.nn][self.nn]

        for i in reversed(range(1, self.nn)):
            t = 0
            for j in range(1, self.nn - i + 1):
                t += self.ai[i][i + j] * self.x[i + j]
                self.x[i] = 1 / self.ai[i][i] * (self.b[i] - t)

        sq = 0.0
        sq2 = 0.0

        for n in range(self.I0, self.I0 + api.Periods + 1):
            sumValue = 0

            for k in range(1, api.Degree + 1):
                sumValue += self.x[k + 1] * pow(n, k)

            api.Prc[index + api.Shift - n] = self.x[1] + sumValue
            sq += pow(api.Bars.ClosePrices[index - n] - api.Prc[index + api.Shift - n], 2)
            sq2 += pow(api.Bars.ClosePrices[index - n] - api.Prc[index + api.Shift - n], 2)

        sq = math.sqrt(sq / (api.Periods + 1)) * api.StandardDeviation
        sq2 = math.sqrt(sq2 / (api.Periods + 1)) * api.StandardDeviation2

        for n in range(self.I0, self.I0 + api.Periods + 1):
            api.Sqh[index + api.Shift - n] = api.Prc[index + api.Shift - n] + sq
            api.Sql[index + api.Shift - n] = api.Prc[index + api.Shift - n] - sq
            api.Sqh2[index + api.Shift - n] = api.Prc[index + api.Shift - n] + sq2
            api.Sql2[index + api.Shift - n] = api.Prc[index + api.Shift - n] - sq2