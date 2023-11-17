"""
Python program to find the number days that are above average temperature
"""

class TemperatureAnalytics():

    def days_above_avg_temp(self):
        """
        Return the average temperature and number of days above the average temperature
        """
        # Taking Number of days and temperature per day from user
        no_of_days = int(input('How many day\'s temperature? '))
        sum_of_temperatures = 0
        temperatures_list = []

        for day in range(1, no_of_days+1):
            next_day_temp = int(input("Day " + str(day) + "'s High Temperature:"))
            temperatures_list.append(next_day_temp)
            sum_of_temperatures += next_day_temp
        

        avg_temp = round(sum_of_temperatures/no_of_days, 2)
        above = 0

        result = {'avg':avg_temp, }

        for temp in temperatures_list:
            if temp > avg_temp:
                above += 1

        result['above_temp'] = above

        return result    

    

"""

"""
if __name__ == '__main__':
    instance = TemperatureAnalytics()

    print(instance.days_above_avg_temp())