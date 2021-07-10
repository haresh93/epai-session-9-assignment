import pytest
from faker import Faker
from datetime import date
import session9

fake = Faker()

def get_blood_group_frequencies(profiles):
    blood_groups = {}
    for profile in profiles:
        if profile["blood_group"] not in blood_groups:
            blood_groups[profile["blood_group"]] = 1
        else:
            blood_groups[profile["blood_group"]] += 1
    return blood_groups


def test_get_stats_on_profiles_using_named_tuple_invalid_arg():
    random_dict = {"foo": "bar", "bax": "baz"}

    with pytest.raises(TypeError) as execinfo:
        session9.get_stats_on_profiles_using_named_tuple(random_dict)

def test_get_stats_on_profiles_using_named_tuple_empty_list():
    profiles = []

    with pytest.raises(ValueError) as execinfo:
        session9.get_stats_on_profiles_using_named_tuple(profiles)

def test_get_stats_on_profiles_using_named_tuple_invalid_list():
    profiles = [{"foo": "bar", "bax": "baz"}]

    with pytest.raises(ValueError) as execinfo:
        session9.get_stats_on_profiles_using_named_tuple(profiles)

def test_get_stats_on_profiles_using_named_tuple():
    profiles = [fake.profile() for i in range(10000)]

    stats = session9.get_stats_on_profiles_using_named_tuple(profiles)

    assert isinstance(stats, tuple), "The return type is not a tuple"

    assert stats._fields == ("largest_blood_type", "mean_current_location", "oldest_person_age", "average_age")

    blood_groups = get_blood_group_frequencies(profiles)
    
    assert stats.largest_blood_type == max(blood_groups, key=blood_groups.get)
    assert stats.mean_current_location[0] == sum(p["current_location"][0] for p in profiles)/len(profiles)
    assert stats.mean_current_location[1] == sum(p["current_location"][1] for p in profiles)/len(profiles)
    assert stats.oldest_person_age == (date.today() - min(p["birthdate"] for p in profiles)).days
    assert stats.average_age == sum((date.today() - p["birthdate"]).days for p in profiles)/len(profiles)

def test_get_stats_on_profiles_using_dictionary_invalid_arg():
    random_dict = {"foo": "bar", "bax": "baz"}

    with pytest.raises(TypeError) as execinfo:
        session9.get_stats_on_profiles_using_dictionary(random_dict)

def test_get_stats_on_profiles_using_dictionary_empty_list():
    profiles = []

    with pytest.raises(ValueError) as execinfo:
        session9.get_stats_on_profiles_using_dictionary(profiles)

def test_get_stats_on_profiles_using_dictionary_invalid_list():
    profiles = [{"foo": "bar", "bax": "baz"}]

    with pytest.raises(ValueError) as execinfo:
        session9.get_stats_on_profiles_using_dictionary(profiles)

def test_get_stats_on_profiles_using_dictionary():
    profiles = [fake.profile() for i in range(10000)]

    stats = session9.get_stats_on_profiles_using_dictionary(profiles)

    assert isinstance(stats, dict), "The return type is not a dictionary"

    blood_groups = get_blood_group_frequencies(profiles)
    
    assert stats["largest_blood_type"] == max(blood_groups, key=blood_groups.get)
    assert stats["mean_current_location"][0] == sum(p["current_location"][0] for p in profiles)/len(profiles)
    assert stats["mean_current_location"][1] == sum(p["current_location"][1] for p in profiles)/len(profiles)
    assert stats["oldest_person_age"] == (date.today() - min(p["birthdate"] for p in profiles)).days
    assert stats["average_age"] == sum((date.today() - p["birthdate"]).days for p in profiles)/len(profiles)