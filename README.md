# EPAI Session 9

## get_stats_on_profiles_using_named_tuple

Takes a list of dictionaries of faker profiles as input.
Computes the statistics on the list of all the profiles and returns a Stats namedtuple with the following properties

1. largest_blood_type - This is the Blood Group of the maximum profiles in the dataset
2. mean_current_location - This is the Mean of all the locations in the dataset
3. oldest_person_age - The age of the oldest person in the dataset
4. average_age - The average age of all the people in the dataset

It converts the list of dictionaries to a namedtuple of Profile to compute the statistic over the list of namedtuples.


## get_stats_on_profiles_using_dictionary

Takes a list of dictionaries of faker profiles as input.
Computes the statistics on the list of all the profiles and returns a dictionary with the following keys

1. largest_blood_type - This is the Blood Group of the maximum profiles in the dataset
2. mean_current_location - This is the Mean of all the locations in the dataset
3. oldest_person_age - The age of the oldest person in the dataset
4. average_age - The average age of all the people in the dataset

It performs all the statistics on the given list of dictionaries itself.

