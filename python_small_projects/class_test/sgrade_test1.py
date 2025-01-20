
class Score:
    """
    every row is an element of this class
    """
    ### attribute variable initiate
    tot_math=0
    tot_english=0
    tot_chinese=0
    count=0
    maxmath=0
    minmath=1000
    def __init__(self,stuid,math,english,chinese):
        self.stuid=stuid
        self.math=int(math)
        self.english=int(english)
        self.chinese=int(chinese)
        Score.tot_math += self.math
        Score.tot_english += self.english
        Score.tot_chinese += self.chinese
        Score.count +=1
        if self.math >Score.maxmath:
            Score.maxmath = self.math

        if self.math <Score.minmath:
            Score.minmath = self.math



def loaddata(f):
    scoretable=[]
    with open(f) as fin:
        for lin in fin:
            lin = lin.strip()
            scorerow = Score(lin.split('\t')[0],lin.split('\t')[1],lin.split('\t')[2],lin.split('\t')[3])
            scoretable.append(scorerow)
    return  print(Score.tot_math/Score.count,Score.tot_english/Score.count,Score.tot_chinese/Score.count,Score.minmath,Score.maxmath)
loaddata("input.txt")






