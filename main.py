from Scrap import *
from CleanData import *


def main():


    Folder = "/Users/farawa/Twitter_Sentiment_Analysis/data/26FEB"
    nmbThreads = 2
    headBool = True
    swipeRate = 3
    nmbTrends = 3


    ##Start_Threads(nmbThreads,headBool,swipeRate,Folder,nmbTrends)
      

    DataFrame = ProcessData(Folder)




    print('Number of tweets : ',len(DataFrame.index),'\n')

    print(DataFrame.head(20))
    print('')



if __name__ == "__main__":

    main()