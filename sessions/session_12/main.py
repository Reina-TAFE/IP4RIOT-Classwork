from datetime import datetime


class User:
    def __init__(self, name, email):
        self.username = name
        self.email = email
        self.posts = []

    def createPost(self, title, content):
        post = Post(title, content)
        self.posts.append(post)

    def show_posts(self):
        for post in self.posts:
            post.display_post()


class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.now()

    def display_post(self):
        date_and_time = self.timestamp.strftime("%H:%M:%S %d %b, %Y")
        print()
        print(f"Title: {self.title} at {date_and_time}")
        print(f"Content: {self.content}")


def main():
    user_fred = User("Fred", "fred@example.com")
    user_jim = User("Jim", "jimothy@example.com")

    user_fred.createPost("Test Post", "Eat The Rich!!")
    user_jim.createPost("Test Post 1", "Call Aiden Crimes for all your 'legal' needs!")
    user_jim.createPost("Help, Wanted!", "Join our team of legal weasels today!")

    user_jim.show_posts()


if __name__ == '__main__':
    main()


