Задача №1. Описание Домашних животных

struct Animal:
    name: str,
    type: str,
    age: int,
    weight: float,
    vaccinated: bool

pussy_cat = Animal('Murka', 'Cat', 5, 5.35, True)
litle_doge = Animal('Spike', 'Dog', 7, 3.9, True)
big_doge = Animal('Boobik', 'Dog', 10, 31.1, True)
mu = Animal('Milka', 'Cow', 12, 482.5, True)
kukareku = Animal('Petya', 'Cock', 2, 5, False)

Задача №2. "Ритуалы и традиции в волшебном обществе"

struct Artifact:
    material: str,
    historyc_value: str,
    strenght: int

struct Ceremony_date:
    date: int,
    month: int,
    year: int

struct society_member:
    role: str,
    clothes: str,
    experience: int,
    artifact: struct

Во все 'Ceremony_date' все 'society_member' собираются вместе и колдуют с помощью 'Artifact'. От 'society_member.role' зависит что делает 'society_member', колдует мощно или просто носит приборы. От 'society_member.experience' зависит может ли 'society_member' использовать 'Artifact' с параметром 'strenght'
