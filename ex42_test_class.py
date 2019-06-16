import datetime


class User(object):
    # Text to be display when call help(User)
    """A member of FriendFace. For now we are 
    only storing their name and birthday.
    But soon we will store an uncomfortable 
    amount of user information."""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyymmdd

        # Extract first and last name
        name_pieces = full_name.split(" ")
        # splitis the name on position 1
        self.first_name = name_pieces[0]
        # splits the name on the last position
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2019, 6, 15)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:])
        dob = datetime.date(yyyy, mm, dd)  # date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user1 = User("Dave Bowman", "19710315")

user2 = User("Manuel Lameira", "19820712")

print(f"The User {user1.name} has an age of {user1.age()}")

print(f"The User {user2.name} has an age of {user2.age()}")

print(
    f"The user {user1.first_name} has {user1.last_name} as last name and has an age of {user1.age()}")
