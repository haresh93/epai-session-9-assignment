from faker import Faker
from collections import namedtuple
from collections import Counter
from datetime import date


def get_stats_on_profiles_using_named_tuple(profiles: list) -> "Stats":
    """
    Takes a list of dictionaries of faker profiles as input.
    Computes the statistics on the list of all the profiles and returns a Stats namedtuple with the following properties

    1. largest_blood_type - This is the Blood Group of the maximum profiles in the dataset
    2. mean_current_location - This is the Mean of all the locations in the dataset
    3. oldest_person_age - The age of the oldest person in the dataset
    4. average_age - The average age of all the people in the dataset

    It converts the list of dictionaries to a namedtuple of Profile to compute the statistic over the list of namedtuples.
    """

    
    if type(profiles) != list:
        raise TypeError("A list needs to be provided as an argument")

    if not len(profiles):
        raise ValueError("An empty list is provided")

    Profile = namedtuple("Profile", ("job", "company", "ssn", "residence", "current_location", 
        "blood_group", "website", "username", "name", "sex", "address", "mail", "birthdate"))
    
    
    Stats = namedtuple("Stats", ("largest_blood_type", "mean_current_location", "oldest_person_age", "average_age"))

    Stats.__doc__ = "Represents the various statistics on the complete profile list"
    Stats.largest_blood_type.__doc__ = "This is the Blood Group of the maximum profiles in the dataset"
    Stats.mean_current_location.__doc__ = "This is the Mean of all the locations in the dataset"
    Stats.oldest_person_age.__doc__ = "The age of the oldest person in the dataset"
    Stats.average_age.__doc__ = "The average age of all the people in the dataset"

    try:
        profiles_tuple = [Profile(**p) for p in profiles]
    except:
        raise ValueError("The valid list of fake profiles need to be sent.")

    return Stats(
        largest_blood_type = Counter(p.blood_group for p in profiles_tuple).most_common(1)[0][0],
        mean_current_location = (sum(p.current_location[0] for p in profiles_tuple)/len(profiles_tuple),
            sum(p.current_location[1] for p in profiles_tuple)/len(profiles_tuple)),
        oldest_person_age  = (date.today() - max(profiles_tuple, key = lambda item: (date.today() - item.birthdate).days).birthdate).days,
        average_age = sum((date.today() - p.birthdate).days for p in profiles_tuple)/len(profiles_tuple)
    )

def get_stats_on_profiles_using_dictionary(profiles: list) -> "dict":
    """
    Takes a list of dictionaries of faker profiles as input.
    Computes the statistics on the list of all the profiles and returns a dictionary with the following keys

    1. largest_blood_type - This is the Blood Group of the maximum profiles in the dataset
    2. mean_current_location - This is the Mean of all the locations in the dataset
    3. oldest_person_age - The age of the oldest person in the dataset
    4. average_age - The average age of all the people in the dataset

    It performs all the statistics on the given list of dictionaries itself.
    """

    if type(profiles) != list:
        raise TypeError("A list needs to be provided as an argument")

    if not len(profiles):
        raise ValueError("An empty list is provided")

    fields = ("job", "company", "ssn", "residence", "current_location", 
        "blood_group", "website", "username", "name", "sex", "address", "mail", "birthdate")

    for field in fields:
        for profile in profiles:
            if field not in profile:
                raise ValueError("The valid list of fake profiles need to be sent.")

    return {
        "largest_blood_type": Counter(p["blood_group"] for p in profiles).most_common(1)[0][0],
        "mean_current_location": (sum(p["current_location"][0] for p in profiles)/len(profiles),
            sum(p["current_location"][1] for p in profiles)/len(profiles)),
        "oldest_person_age": (date.today() - max(profiles, key = lambda item: (date.today() - item["birthdate"]).days)["birthdate"]).days,
        "average_age": sum((date.today() - p["birthdate"]).days for p in profiles)/len(profiles)
    }
