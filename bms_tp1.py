class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.posts = []

    def display(self):
        print(f'name : {self.name}, user_name : {self.username}')

    def __repr__(self):
        return f"{self.name}의 회원정보"


class post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"{self.author}가 작성한 {self.title}"


members = []
posts = []
members_username=[]

# 터미널에서 유저를 추가하는 기능
while True:
    name = input("이름을 입력해주세요: ").strip()
    username = input("닉네임 입력해주세요: ").strip()
    if username in members_username:
        print("입력한 닉네임은 사용중입니다. 다른 닉네임을 입력해주세요.")
        continue
    password = input("패스워드를 입력해주세요: ").strip()

    members.append(Member(name, username, password))
    members_username.append(username)

# 유저를 계속 추가하는 기능
    if input("회원을 계속 추가하시겠습니까? (y/n): ").lower() == "y":
        print()
        continue
    else:
        break
print()

# 터미널에서 게시글을 입력하는 기능
while True:
    title = input("게시글 제목을 입력해주세요: ").strip()
    content = input("게시글 내용을 입력해주세요: ").strip()
    author = input("게시글 작성자를 입력해주세요: ").strip()

    if author in members_username:
        posts.append(post(title, content, author))
    else:
        print("닉네임을 다시 확인해주세요.")
        continue

# 게시물을 계속 추가하는 기능
    if input("게시물을 계속 추가하시겠습니까? (y/n): ").lower() == "y":
        print()
        continue
    else:
        break
print()


print("현재 유저 목록:")
for member in members:
    print(f"유저명 : {member.username}")



# 6.1 특정 유저가 작성한 게시글의 제목을 모두 프린트하기
target_user = input('누구의 게시글을 찾을까요?')  

print(f"{target_user} 님이 작성한 게시글 제목:")
for post in posts:
    if post.author == target_user:
        print(post.title)

# 6.2
target_word = input('입력한 단어가 포함된 게시글 제목 :') 

print(f"post에 '{target_word}'가 포함된 게시글 제목:")
for post in posts:
    if target_word in post.content:
        print(post.title)