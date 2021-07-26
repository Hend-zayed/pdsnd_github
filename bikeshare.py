import time
import pandas as pd
import numpy as np
##Refactoring Test
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    #Running this loop to ensure the correct user input gets selected else repeat
    while city not in CITY_DATA.keys():
        print("Please choose your city: 1. Chicago 2. New York City 3. Washington")
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\nInvalid input")
          
            print(f"\nYou have chosen {city.title()} as your city.")
   

    # TO DO: get user input for month (all, january, february, ... , june)

    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease enter the first 6 month and you can enter all months")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nInvalid input.")
        
            print(f"\nYou have chosen {month.title()} .")
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nPlease enter a day in the week ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')")
        day = input().lower()
        if day not in DAY_LIST:
            print("\nInvalid input. Please try again in one of the accepted input formats.")
           
            print(f"\nYou have chosen {day.title()}.")
            
  
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    zzz = df['Start Time'].dt
    df['hour'] = zzz.hour
    df['day_name'] = zzz.day_name().str.lower()
    df['month_name'] = zzz.month_name().str.lower()

    if(day != 'all'):
        df = df[df['day_name'] == day]
    
    if(month != 'all'):
        df = df[df['month_name'] == month]
    

    return df

def time_stats(df):
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # # TO DO: display the most common month
    popular_month = df['month_name'].mode()[0]
    print('Most Popular month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_name'].mode()[0]
    print('Most Popular day:', popular_day)

    # # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    # print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_startstation)

    # TO DO: display most commonly used end station
    popular_EndStation = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_EndStation)

    # TO DO: display most frequent combination of start station and end station trip
    df['combinationstation']  = " From station " +df['Start Station'] +" to station "+ df['End Station'] 
    popular_combinationstation = df['combinationstation'].mode()[0]
    print('Most Popular combinationstation:', popular_combinationstation)
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTripDuration= df['Trip Duration'].sum()
    print('total trip duration:', totalTripDuration)

    # TO DO: display mean travel time
    menTripDuration= df['Trip Duration'].mean()
    print('Avarage trip duration:', menTripDuration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    subs=df[df['User Type']=='Subscriber']
    print('Display counts of Subscriber', subs.shape[0])
   
    cust=df[df['User Type']=='Customer']
    print('Display counts of Customer', cust.shape[0])
   

    # TO DO: Display counts of gender
    if (city != 'washington'):
        Gendermale=df[df['Gender']=='Male']
        print('Display counts of Male', Gendermale.shape[0])
  
        GenderFemale=df[df['Gender']=='Female']
        print('Display counts of Female', GenderFemale.shape[0])
    
    # TO DO: Display earliest, most recent, and most common year of birth

        earliestbirthyear= df.nlargest(1,columns='Birth Year')['Birth Year'].values[0]
        print('earliest year of birth:', earliestbirthyear)
 
        recentbirthyear= df.nsmallest(1,columns='Birth Year')['Birth Year'].values[0]
        print('recent year of birth:', recentbirthyear)

        commonbirthyear = df['Birth Year'].mode()[0]
        print('most common year of birth:', commonbirthyear)
    else:
        print('there is no gender & birth year information in washington')
  


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def random_users(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    view_data = view_data.lower()
    while (view_data == 'yes'):
        print('the 5 rondom rows')
        print(df.sample(5))
        view_display = input('\nWould you like contiue? Enter yes or no\n')
        view_display = view_display.lower()
        if (view_display == 'no'):
            return random_users

def main():
    while True:
        city, month, day = get_filters()
        # city = 'chicago'
        # month = 'february'
        # day = 'tuesday'
        df = load_data(city, month, day)
        if df.size > 0:
            print(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df,city)
            random_users(df)
        else:
            print("No matching data")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
