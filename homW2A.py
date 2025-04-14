class Player: #агрегация слабая
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, players):
        self.players = players  

    @property
    def get_team(self):
        return [player.name for player in self.players]



p1 = Player('Bob')
p2 = Player('Alice')


tm = Team([p1, p2])

print(*tm.get_team)

 
'=========================================2==============================================='
print('\n\n')
'========================================================================================='
class Employee: #агрегация слабая
    def __init__(self, name):
        self.name = name


class CompanyA:
    def __init__(self, employee):
        self.employees = [employee]


class CompanyB:
    def __init__(self, employee):
        self.employees = [employee]


emp = Employee('John')

company_a = CompanyA(emp)
company_b = CompanyB(emp)

print(company_a.employees[0].name, ' ', company_b.employees[0].name)


'=========================================3==============================================='
print('\n\n')
'========================================================================================='
class Room: #kompoziciya
    def __init__(self):
        ...

    def room_count(self):
        ...
class House:
    def __init__(self, num_rooms):
        self.rooms = [Room() for _ in range(num_rooms)]

    def room_count(self):
        return len(self.rooms)

house = House(2)
print("Number of rooms:", house.room_count())

'=========================================4==============================================='
print('\n\n')
'========================================================================================='
class Page: #kompoziciya
    def __init__(self):
        ...

    def page_count(self):
        ...

class Book:
    def __init__(self, num_pages):
        self.pages = [Page() for _ in range(num_pages)]

    def page_count(self):
        return len(self.pages)


book = Book(3)
print("Pages in book:", book.page_count())
'=========================================5==============================================='
print('\n\n')
'========================================================================================='
class CPU:
    def __init__(self, model):
        self.model = model

class RAM:
    def __init__(self, size):
        self.size = size

class Computer:
    def __init__(self):
        self.cpu = CPU("Intel i7")
        self.ram = RAM("16GB")

    def show_info(self):
        print("Computer has:")
        print(f"CPU: {self.cpu.model}")
        print(f"RAM: {self.ram.size}")


pc = Computer()
pc.show_info()

'=========================================6==============================================='
print('\n\n')
'========================================================================================='
class Playlist:
    def __init__(self,playlist):
        self.playlist = playlist
class Song:
    def __init__(self,*song):
        self.song = song


test = Song('Marshall','Eminem')
test2 = Playlist(test.song)

print(f'Song still exists: {bool(test.song)}')
print(*test2.playlist)

del test2.playlist

print(f'Song still exists: {bool(test.song)}')
try:
    print(*test2.playlist)
except AttributeError:
    print("Playlist was deleted")
'=========================================7==============================================='
print('\n\n')
'========================================================================================='
class Paragraph: #strong
    def __init__(self, text):
        self.text = text


class Document:
    def __init__(self, texts):
        self.paragraphs = [Paragraph(text) for text in texts]

    def get_paragraphs_count(self):
        return len(self.paragraphs)


doc = Document(["pervyi", "vtoroi", "tretii"])
print("Paragraphs before document deletion:", doc.get_paragraphs_count())

del doc

try:
    print("Paragraphs after document deletion:", doc.get_paragraphs_count())
except NameError:
    print("Paragraphs after document deletion: 0")

# 7. Композиция и удаление объектов
# Создай класс Document и класс Paragraph. При удалении документа все
# параграфы должны быть уничтожены. Проверь, что параграфов больше не
# существует.
# Ожидаемый вывод:
# Paragraphs after document deletion: 0