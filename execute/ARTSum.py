# -*- encoding: utf-8 -*-
"""
@File       : ARTSum.py    
@Contact    : daihepeng@sina.cn
@Repository : https://github.com/phantomdai
@Modify Time: 2021/3/17 2:48 下午
@Author     : phantom
@Version    : 1.0
@Descriptions : 
"""
import numpy as np

from execute.utl.Utl import execute_utl
from myutl.Utl import Utl


class ART(object):
    """
    该类实现了ARTSum算法的逻辑
    """

    def __init__(self):
        self.candidateTestCase = []  # 候选测试用例
        self.S = np.zeros(60)  # 计算距离
        self.executedTestCase = []  # 记录执行过的测试用例
        self.allTestFrame = Utl().get_test_frames()

    def init_s(self, tf):
        """
        初始化S
        :param tf:第一个执行的测试用例的测试帧
        :return: null
        """
        self.executedTestCase.append(tf)
        if "NA" in tf:
            self.S[1] = 1
        elif "NP" in tf:
            self.S[2] = 1
        if "YW" in tf:
            self.S[4] = 1
        elif "NW" in tf:
            self.S[5] = 1
        if "YD" in tf:
            self.S[7] = 1
        elif "ND" in tf:
            self.S[8] = 1
        if "YS" in tf:
            self.S[10] = 1
        elif "NS" in tf:
            self.S[11] = 1
        if "N1" in tf:
            self.S[13] = 1
        elif "N2" in tf:
            self.S[14] = 1
        elif "N3" in tf:
            self.S[15] = 1
        elif "N4" in tf:
            self.S[16] = 1
        elif "N5" in tf:
            self.S[17] = 1
        elif "N6" in tf:
            self.S[18] = 1
        elif "N7" in tf:
            self.S[19] = 1
        elif "N8" in tf:
            self.S[20] = 1
        elif "N9" in tf:
            self.S[21] = 1
        elif "N10" in tf:
            self.S[22] = 1
        elif "N11" in tf:
            self.S[23] = 1
        elif "N12" in tf:
            self.S[24] = 1
        if "DOT" in tf:
            self.S[26] = 1
        if "UR" in tf:
            self.S[28] = 1
        elif "LR" in tf:
            self.S[29] = 1
        elif "NR" in tf:
            self.S[30] = 1
        if "NB" in tf:
            self.S[32] = 1
        elif "CB" in tf:
            self.S[33] = 1
        if "QM" in tf:
            self.S[35] = 1
        elif "ST" in tf:
            self.S[36] = 1
        elif "PL" in tf:
            self.S[37] = 1
        elif "RM" in tf:
            self.S[38] = 1
        if "PR" in tf:
            self.S[40] = 1
        elif "BR" in tf:
            self.S[41] = 1
        if "BL" in tf:
            self.S[43] = 1
        elif "EL" in tf:
            self.S[44] = 1
        elif "LL" in tf:
            self.S[45] = 1
        if "BW" in tf:
            self.S[47] = 1
        elif "EW" in tf:
            self.S[48] = 1
        elif "WW" in tf:
            self.S[49] = 1
        if "YB" in tf:
            self.S[51] = 1
        elif "YE" in tf:
            self.S[52] = 1
        elif "YY" in tf:
            self.S[53] = 1
        elif "EN" in tf:
            self.S[54] = 1
        elif "NE" in tf:
            self.S[55] = 1
        elif "NN" in tf:
            self.S[56] = 1
        if "CO" in tf:
            self.S[58] = 1
        elif "NL" in tf:
            self.S[59] = 1

    def update_candidate_test_case(self):
        """
        每次选择测试用例都需要更新候选测试用例集
        :return:
        """
        self.candidateTestCase = execute_utl().generate_ART_candidate_test_cases()

    def get_source_test_case(self):
        """
        选择下一个原始测试用例
        :return: 选择的测试用例编号
        """

        # 一个临时的字典，记录测试用例的编号以及对应的测试帧，来节约时间
        tempDict = {}

        candidateTestFrame = []
        for key in self.candidateTestCase:
            candidateTestFrame.append(self.allTestFrame[str(key)])
            tempDict[str(key)] = self.allTestFrame[str(key)]

        maxSourceChoiceArray = np.zeros(60)
        maxValue = 0
        testFrame = ""

        for tf in candidateTestFrame:
            sourceChoiceArray = np.zeros(60)
            tempValue = 0

            if "NA" in tf:
                sourceChoiceArray[1] = 1
                tempValue += (len(self.executedTestCase) - self.S[1])
            elif "NP" in tf:
                sourceChoiceArray[2] = 1
                tempValue += (len(self.executedTestCase) - self.S[2])
            if "YW" in tf:
                sourceChoiceArray[4] = 1
                tempValue += (len(self.executedTestCase) - self.S[4])
            elif "NW" in tf:
                sourceChoiceArray[5] = 1
                tempValue += (len(self.executedTestCase) - self.S[5])
            if "YD" in tf:
                sourceChoiceArray[7] = 1
                tempValue += (len(self.executedTestCase) - self.S[7])
            elif "ND" in tf:
                sourceChoiceArray[8] = 1
                tempValue += (len(self.executedTestCase) - self.S[8])
            if "YS" in tf:
                sourceChoiceArray[10] = 1
                tempValue += (len(self.executedTestCase) - self.S[10])
            elif "NS" in tf:
                sourceChoiceArray[11] = 1
                tempValue += (len(self.executedTestCase) - self.S[11])
            if "N1" in tf:
                sourceChoiceArray[13] = 1
                tempValue += (len(self.executedTestCase) - self.S[13])
            elif "N2" in tf:
                sourceChoiceArray[14] = 1
                tempValue += (len(self.executedTestCase) - self.S[14])
            elif "N3" in tf:
                sourceChoiceArray[15] = 1
                tempValue += (len(self.executedTestCase) - self.S[15])
            elif "N4" in tf:
                sourceChoiceArray[16] = 1
                tempValue += (len(self.executedTestCase) - self.S[16])
            elif "N5" in tf:
                sourceChoiceArray[17] = 1
                tempValue += (len(self.executedTestCase) - self.S[17])
            elif "N6" in tf:
                sourceChoiceArray[18] = 1
                tempValue += (len(self.executedTestCase) - self.S[18])
            elif "N7" in tf:
                sourceChoiceArray[19] = 1
                tempValue += (len(self.executedTestCase) - self.S[19])
            elif "N8" in tf:
                sourceChoiceArray[20] = 1
                tempValue += (len(self.executedTestCase) - self.S[20])
            elif "N9" in tf:
                sourceChoiceArray[21] = 1
                tempValue += (len(self.executedTestCase) - self.S[21])
            elif "N10" in tf:
                sourceChoiceArray[22] = 1
                tempValue += (len(self.executedTestCase) - self.S[22])
            elif "N11" in tf:
                sourceChoiceArray[23] = 1
                tempValue += (len(self.executedTestCase) - self.S[23])
            elif "N12" in tf:
                sourceChoiceArray[24] = 1
                tempValue += (len(self.executedTestCase) - self.S[24])
            if "DOT" in tf:
                sourceChoiceArray[26] = 1
                tempValue += (len(self.executedTestCase) - self.S[26])
            if "UR" in tf:
                sourceChoiceArray[28] = 1
                tempValue += (len(self.executedTestCase) - self.S[28])
            elif "LR" in tf:
                sourceChoiceArray[29] = 1
                tempValue += (len(self.executedTestCase) - self.S[29])
            elif "NR" in tf:
                sourceChoiceArray[30] = 1
                tempValue += (len(self.executedTestCase) - self.S[30])
            if "NB" in tf:
                sourceChoiceArray[32] = 1
                tempValue += (len(self.executedTestCase) - self.S[32])
            elif "CB" in tf:
                sourceChoiceArray[33] = 1
                tempValue += (len(self.executedTestCase) - self.S[33])
            if "QM" in tf:
                sourceChoiceArray[35] = 1
                tempValue += (len(self.executedTestCase) - self.S[35])
                self.S[35] = 1
            elif "ST" in tf:
                sourceChoiceArray[36] = 1
                tempValue += (len(self.executedTestCase) - self.S[36])
                self.S[36] = 1
            elif "PL" in tf:
                sourceChoiceArray[37] = 1
                tempValue += (len(self.executedTestCase) - self.S[37])
                self.S[37] = 1
            elif "RM" in tf:
                sourceChoiceArray[38] = 1
                tempValue += (len(self.executedTestCase) - self.S[38])
                self.S[38] = 1
            if "PR" in tf:
                sourceChoiceArray[40] = 1
                tempValue += (len(self.executedTestCase) - self.S[40])
                self.S[40] = 1
            elif "BR" in tf:
                sourceChoiceArray[41] = 1
                tempValue += (len(self.executedTestCase) - self.S[41])
                self.S[41] = 1
            if "BL" in tf:
                sourceChoiceArray[43] = 1
                tempValue += (len(self.executedTestCase) - self.S[43])
                self.S[43] = 1
            elif "EL" in tf:
                sourceChoiceArray[44] = 1
                tempValue += (len(self.executedTestCase) - self.S[44])
                self.S[44] = 1
            elif "LL" in tf:
                sourceChoiceArray[45] = 1
                tempValue += (len(self.executedTestCase) - self.S[45])
                self.S[45] = 1
            if "BW" in tf:
                sourceChoiceArray[47] = 1
                tempValue += (len(self.executedTestCase) - self.S[47])
                self.S[47] = 1
            elif "EW" in tf:
                sourceChoiceArray[48] = 1
                tempValue += (len(self.executedTestCase) - self.S[48])
                self.S[48] = 1
            elif "WW" in tf:
                sourceChoiceArray[49] = 1
                tempValue += (len(self.executedTestCase) - self.S[49])
                self.S[49] = 1
            if "YB" in tf:
                sourceChoiceArray[51] = 1
                tempValue += (len(self.executedTestCase) - self.S[51])
                self.S[51] = 1
            elif "YE" in tf:
                sourceChoiceArray[52] = 1
                tempValue += (len(self.executedTestCase) - self.S[52])
                self.S[52] = 1
            elif "YY" in tf:
                sourceChoiceArray[53] = 1
                tempValue += (len(self.executedTestCase) - self.S[53])
                self.S[53] = 1
            elif "EN" in tf:
                sourceChoiceArray[54] = 1
                tempValue += (len(self.executedTestCase) - self.S[54])
                self.S[54] = 1
            elif "NE" in tf:
                sourceChoiceArray[55] = 1
                tempValue += (len(self.executedTestCase) - self.S[55])
                self.S[55] = 1
            elif "NN" in tf:
                sourceChoiceArray[56] = 1
                tempValue += (len(self.executedTestCase) - self.S[56])
                self.S[56] = 1
            if "CO" in tf:
                sourceChoiceArray[58] = 1
                tempValue += (len(self.executedTestCase) - self.S[58])
                self.S[58] = 1
            elif "NL" in tf:
                sourceChoiceArray[59] = 1
                tempValue += (len(self.executedTestCase) - self.S[59])
                self.S[59] = 1

            if tempValue > maxValue:
                maxSourceChoiceArray = sourceChoiceArray
                testFrame = tf
        # 更新S
        for index in range(len(self.S)):
            self.S[index] += maxSourceChoiceArray[index]
        # 将选择的测试用例添加到执行的测试用例集中
        self.executedTestCase.append(testFrame)
        index = 0
        for key, value in tempDict.items():
            if value == testFrame:
                index = int(key)
            else:
                pass
        return index

