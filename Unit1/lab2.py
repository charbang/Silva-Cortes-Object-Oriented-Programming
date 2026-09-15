class User:
    def __init__(self, name, email, age, password):
        self.__name = name
        self.__email = email
        self.__age = age
        self.__password = password
        self.posts = []

    @property
    def name(self):
        return self.__name

    def addPost(self, post):
        self.posts.append(post)

    def showPosts(self):
        for post in self.posts:
            post.show_post()


class Post:
    def __init__(self, text, description, likes, user):
        self.text = text
        self.description = description
        self.likes = likes
        self.user = user

    def createPost(self):
        print(f"{self.likes} likes")
        print(f"{self.user.name}: {self.description}")

    def show_post(self):
        print(f"{self.user.name} has post: {self.text}")


class Comments:
    def __init__(self, comment, likes, user):
        self.comment = comment
        self.likes = likes
        self.user = user

    def createComment(self):
        print(f"{self.likes} likes")
        print(f"{self.user.name}: {self.comment}")


class Message:
    def __init__(self, text, sender, receiver):
        self.text = text
        self.sender = sender
        self.receiver = receiver

    def createMessage(self):
        print(f"{self.text}")
        print(f"{self.sender.name} sends a message to {self.receiver.name}")


user = User("CharBang", "carlos@gmail.com", 18, "pass")
post = Post("Go in the way", "hey", 1, user)
user.addPost(post)
user.showPosts()