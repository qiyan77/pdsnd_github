import time
import pandas as pd
import numpy as np

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
    city_name = input('Please enter a city name: ').lower().strip()
    while city_name != 'chicago' and city_name != 'new york city' and city_name != 'washington':
        city_name = input('Please enter a valid city name: ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_toview = input('Please enter the month to review: ').lower().strip()
    valid_months = ['january','february','march','april','may','june','all'] 
    while month_toview not in valid_months:
        month_toview = input('Please enter the month to review: ')
        
   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday). HINT: Use a while loop to handle invalid inputs
    day_toview = input('Please enter a day to review: ').lower().strip()
    valid_days = ['monday','tuesday','wednesday','thursday','friday','saturday', 'sunday','all']
    while day_toview not in valid_days:
        day_toview = input('Please enter a valid day to review: ')

    print('-'*40)
    return city_name, month_toview, day_toview


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(df['month'].mode()[0])


    # TO DO: display the most common day of week
    print(df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    df['common_start_hour'] = df['Start Time'].dt.hour
    print(df['common_start_hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0])
    
    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print((df['Start Station'] + df['End Station']).mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'Gender' in df:
        print(df['User Type'].count())
    


    # TO DO: Display counts of gender
        print(df['Gender'].count())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print(df['Birth Year'].min())
        print(df['Birth Year'].max())
        print(df['Birth Year'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
     """
    Asks user if the raw data need to be displayed.

    Returns:
        five rows of raw data.
    """
    row_count = 0
    while True:
        raw_datatoview = input('Do you want to review raw data: ').lower().strip()
        if raw_datatoview != 'yes'and raw_datatoview != 'no':
            raw_datatoview = input('Do you want to review raw data: ').lower().strip()
        elif raw_datatoview =='yes':
            try:
                print(df.iloc[[row_count]])
                print(df.iloc[[row_count + 1]])
                print(df.iloc[[row_count + 2]])
                print(df.iloc[[row_count + 3]])
                print(df.iloc[[row_count + 4]])
                row_count = row_count + 5
            except IndexError:
                print('No more raw data to display')
                break
        else:
            break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
