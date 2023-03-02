from Scrap import *
from CleanData import *


def main():


    Folder = "/Users/farawa/Twitter_Sentiment_Analysis/data/2MAR"
    nmbThreads = 2
    headBool = True
    swipeRate = 5
    nmbTrends = 4


    Start_Threads(nmbThreads,headBool,swipeRate,Folder,nmbTrends)
      

    DataFrame = ProcessData(Folder)


if __name__ == "__main__":

    main()