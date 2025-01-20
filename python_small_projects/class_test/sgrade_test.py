class Sgrade:
    """
    student grades
    """

    def __init__(self,stu_id,chinese,math,english):
        """
        initiate method
        :param stu_id:
        :param chinese:
        :param math:
        :param english:
        :return:
        """
        self.stu_id=stu_id
        self.math=int(chinese)
        self.english=int(math)
        self.chinese=int(english)


class Sgradetable:
    """

    student grade table
    """
    def __init__(self):
        self.sgrade_table=[]
    def load_data(self,fname):
        """
        load sgradetable
        :param fname:
        :return:
        """
        with open(fname) as fin:
            for lin in fin:
                lin=lin.strip()
                stu_id,math,english,chinese=lin.split('\t')
                sgrade=Sgrade(stu_id,math,english,chinese)
                self.sgrade_table.append(sgrade)
        print("sgrade table size:",len(self.sgrade_table))

    def compute_avg_score(self):
        """
        calculate avg_score of every course
        :return:
        """
        tot_math = 0
        tot_chinese = 0
        tot_english = 0

        for sgrade in self.sgrade_table:
            tot_math += sgrade.math
            tot_english += sgrade.english
            tot_chinese += sgrade.chinese
        avg_math=tot_math/len(self.sgrade_table)
        avg_english = tot_english / len(self.sgrade_table)
        avg_chinese = tot_chinese / len(self.sgrade_table)
        return avg_math,avg_chinese,avg_english

    def compute_max_score(self):
        """
        calculate avg_score of every course
        :return:
        """
        max_math = 0
        max_chinese = 0
        max_english = 0

        for sgrade in self.sgrade_table:
            if sgrade.math>max_math:
                max_math=sgrade.math
            if sgrade.english>max_english:
                max_english=sgrade.english
            if sgrade.chinese>max_chinese:
                max_chinese=sgrade.chinese
        return  max_math, max_chinese,max_english

    def compute_min_score(self):
        """
        calculate avg_score of every course
        :return:
        """
        min_math = 1000
        min_chinese = 1000
        min_english = 1000

        for sgrade in self.sgrade_table:
            if sgrade.math < min_math:
                min_math = sgrade.math
            if sgrade.english < min_english:
                min_english = sgrade.english
            if sgrade.chinese < min_chinese:
                min_chinese = sgrade.chinese
        return min_math, min_chinese, min_english


Scoretable=Sgradetable()
Scoretable.load_data("input.txt")
print(Scoretable.compute_avg_score())
print(Scoretable.compute_max_score())
print(Scoretable.compute_min_score())

