# Задание "Свой YouTube".
import time
class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname                        # Имя пользователя.
        self.password = password                        # Пароль.
        self.age = age                                  # Возраст.
    def __hash__(self):
        return hash((self.password))
    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title: str, duration, adult_mode: bool = False):
        self.title = title                              # Заголовок видео.
        self.duration = duration                        # Продолжительность видео.
        self.time_now = 0                               # Пауза (секунд.время).
        self.adult_mode = adult_mode                    # Ограничение по возрасту.
    def __eq__(self, other):
        return self.title == other.title
    def __contains__(self, item):
        return item in self.title
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'\U0001F5FF Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, word: str):
        cinema = []
        for video in self.videos:
            if word.upper() in video.title.upper():
                cinema.append(video.title)
        return cinema

    def watch_video(self, title):
        if self.current_user is None:
            print('\U0001F534 Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('\U0001F51E Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now, end=" ")
                    time.sleep(1)  # Пауза на 1 секунду
                print('\U0001F3AC Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
