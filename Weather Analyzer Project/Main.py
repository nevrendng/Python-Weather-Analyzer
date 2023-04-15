import WeatherAnalyzer
import Chart
import numpy as np


def main():
    weatherAnal = WeatherAnalyzer.WeatherAnalyzer()
   
    
    while True:
        print('1- Get Minimum Temperature of 1990-2019')
        print('2- Get Maximum Temperature of 1990-2019')
        print('3- Get Minimum Temperature of 1990-2019 Annually')
        print('4- Get Maximum Temperature of 1990-2019 Annually')
        print('5- Get Average Snowfall between 1990-2019 Annually')
        print("6- Get average maximum temperature ")
       
        
        choice = int(input("Choose an option:"))
        if choice == 1:
            print(weatherAnal.getMinTemp())
        elif choice == 2:
            print(weatherAnal.getMaxTemp())
        elif choice == 3:
            matrix = weatherAnal.getMinTempAnnually()
            for row in matrix:
                for col in row:
                    print(col, end=' ')
                print()
            break
           
        elif choice == 4:
            matrix = weatherAnal.getMaxTempAnnually()
            for row in matrix:
                for col in row:
                    print(col, end=' ')
                print()
        elif choice == 5:
            matrix = weatherAnal.getAvgSnowfallAnnually()
            for row in matrix:
                for col in row:
                    print(col, end=' ')
                print()
        
        else:
            choice = int(input("Choose an option:"))

    print("end of program")       



if __name__ == '__main__':
    main()