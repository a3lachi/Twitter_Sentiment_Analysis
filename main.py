from Scrap import *


def main():
    # Start_Threads(Number of threads , Headless mode , Swipe Rate ,Folder to save data in ./data folder , Number of trends to scrap )
    try :
        Start_Threads(3,False,20,"26FEB",40)
        print('Threads ended with sucess.')
    except : 
        print('Failed launching threads.')



if __name__ == "__main__":

    main()