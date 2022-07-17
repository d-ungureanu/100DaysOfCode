class User:

    def __init__(self, user_id, user_name):
        print("New user being created...")
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Daniel")
user_2 = User("002", "Zorro")

user_1.follow(user_2)

print(user_1.__dict__)
print(user_2.__dict__)
