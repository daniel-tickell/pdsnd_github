"""
This python application was created as a deliverable for the 
Programming for Data Science with Python
Nanodegree 07/01/2021 by Daniel Tickell
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    print('Available Cities Data:')
    # Print out Index + 1 of City and name from CITY_DATA
    for key in list(CITY_DATA):
        print(str(list(CITY_DATA).index(key) + 1 ) + ': ' + str(key).title())
    
    # Create valid input BOOL for city
    city_prompt = True
    # execute loop until valid input is recieved. 
    city_input = input('Enter the number for the city you would like data for: ') 
    while city_prompt:
        # Check for user input 
        while city_input not in ('1','2','3'):
            city_input = input('Apologies but I need the corresponding number to the City you would like:  ')
        # Print conformation of selection        
        print('You have Selected: ' + str(list(CITY_DATA)[int(city_input) - 1]).title())
        city_prompt = False
    city = list(CITY_DATA)[int(city_input) - 1]
    

    # get user input for month (all, january, february, ... , june)
    # Create valid input BOOL for month
    month_prompt = True
    # execute loop until valid input is recieved. 

    for key in list(MONTHS):
        print(str(list(MONTHS).index(key) + 1 ) + ': ' + str(key).title())

    month_input = input('Enter the number or the month you would like: [Enter for all]: ') or 'all'
    while month_prompt:
     
        # Check to see if user selected default by hitting enter
        if month_input == 'all':
            month = 'all'
            month_prompt = False

        # Check to see if the user typed the month name
        elif month_input.title() in MONTHS:
            print('You have Selected: ' + month_input.title())
            month = month_input.title()
            month_prompt = False

        # Check to see if the user entered the month number
        elif month_input in ('1','2','3','4','5','6','7','8','9','10','11','12'):
            print('You have Selected: ' + str(MONTHS[int(month_input) - 1]).title())
            month = MONTHS[int(month_input) - 1]
            month_prompt = False

        # Otherwise prompt the user to provide valid input
        else:
            print(month_input)
            month_input = input('Apologies but I need the Month Name or Number [Enter for all]: ') or 'all'

    # get user input for day of week (all, monday, tuesday, ... sunday)


    # Create valid input BOOL for day of the week
    dow_prompt = True
    # execute loop until valid input is recieved. 
    for key in list(DAYS_OF_WEEK):
        print(str(list(DAYS_OF_WEEK).index(key) + 1 ) + ': ' + str(key).title())

    dow_input = input('Enter the name or corresponding number of the weekday you would like [Enter for all]: ') or 'all'
    while dow_prompt:
     
        # Check to see if user selected default by hitting enter
        if dow_input == 'all':
            day = 'all'
            dow_prompt = False

        # Check to see if the user typed the month name
        elif dow_input.title() in DAYS_OF_WEEK:
            print('You have Selected: ' + dow_input.title())
            day = dow_input.title()
            dow_prompt = False

        # Check to see if the user entered the month number
        elif dow_input in ('1','2','3','4','5','6','7'):
            print('You have Selected: ' + str(DAYS_OF_WEEK[int(dow_input) - 1]).title())
            day = DAYS_OF_WEEK[int(dow_input) - 1]
            dow_prompt = False

        # Otherwise prompt the user to provide valid input
        else:
            print(dow_input)
            dow_input = input('Apologies but I need the Month Name or Number [Enter for all]: ') or 'all'

    print('-'*40)
    return city, month, day


def load_data(city, month = 'all', day = 'all'):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Create filename from city ARGS
    filename = CITY_DATA.get(city)
    df = pd.read_csv(filename)

    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Convert End Time to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Create Month Column from Start Time
    df['month'] = df['Start Time'].dt.month

    #Check to see if month filter is required
    if month != 'all':
        # Apply Month Filter
        df = df[df['month'] == MONTHS.index(month) +1]

    # Create Day Column from Start Time
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #Check to see if day filter is required
    if day != 'all':
        # Apply Day Filter
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    # Display the Mode for Column 'month' values
    print('Most Common Month: ' + str(MONTHS[df['month'].mode()[0]]))

    # display the most common day of week
    # Display mode of day of week Column Values 
    print('Most Common Day of the week: ' + str(df['day_of_week'].mode()[0]))

    # display the most common start hour
    # Create Hour Column from start time
    df['hour'] = df['Start Time'].dt.hour
    # Display Mode for Hour Column Values
    print('Most Common hour: ' + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station(Mode of column value)
    print('Most Common Start Station: \n' + str(df['Start Station'].mode()[0]))

    # display most commonly used end station (Mode of column value)
    print('\nMost Common End Station: \n' + str(df['End Station'].mode()[0]))
    
    # display most frequent combination of start station and end station trip
    #Create a start and combination column
    df['start end combo'] = df['Start Station'] + ' ' + df['End Station']
    # display most commmon start end combination (Mode of column value)
    print('\nMost Common Station Combination (Start and End): \n' + str(df['start end combo'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Calculate total mins from duration col
    total_duration = df['Trip Duration'].sum()
    
    # Create Time Delta Column    
    df['time_delta'] = df['End Time'] - df['Start Time']

    # Display the total travel time
    print('Total Travel Time is: ' + str(df['time_delta'].sum()))

    # display mean travel time
    print('Mean Travel Time is: ' + str(df['time_delta'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    uniq_user_type = df['User Type'].value_counts().to_string()

    print('Count per User Type: \n' + uniq_user_type)

    # Display counts of gender
    if 'Gender' in df:
        uniq_gender = df['Gender'].value_counts().to_string()
        print('\nCount per Gender Type: \n' + uniq_gender)
    else:
        print('No Gender Data Available')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\nEarliest Birth Year: ' + str(int(df['Birth Year'].min())))
        print('Most Recent Birth Year: ' + str(int(df['Birth Year'].max())))
        print('Most Common Birth Year: ' + str(int(df['Birth Year'].mode())))
    else:
        print('No Birth Year Data Available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        # get user input and apply the filters
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #Run the stats functions
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Prompt user to see the raw data
        raw_data = input('\nWould you like to see 5 Lines of Raw Data? Enter yes or no. [no] \n') or 'no'
        raw_data_input = True
        x = 0
        y = 5
        while raw_data_input == True:
            if raw_data.lower() == 'yes':
                print(df[x:y])
                raw_data = input('\nWould you like to see 5 More Lines of Raw Data? Enter yes or no. [no] \n') or 'no'
                if raw_data == 'yes':
                    x += 5
                    y += 5
                else:
                    raw_data_input = False
            elif raw_data.lower() == 'no':
                raw_data_input = False
            else:
                raw_data = input('\nInvalid Response, Would you like to see 5 Lines of Raw Data? Enter yes or no. [no] \n') or 'no'

        # Prompt the user to restart the query    
        restart = input('\nWould you like to restart? Enter yes or no. [no] \n') or 'no'
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
        main()
"""
Creating a footer text block to refactor the end of the python script
"""
