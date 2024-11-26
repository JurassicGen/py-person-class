class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    persons = []

    for person_data in people:
        persons.append(Person(person_data.get("name"), person_data.get("age")))

    for person_data in people:
        person = Person.people.get(person_data.get("name"))

        if "wife" in person_data and person_data.get("wife"):
            person.wife = Person.people.get(person_data.get("wife"))
        elif "husband" in person_data and person_data.get("husband"):
            person.husband = Person.people.get(person_data.get("husband"))

    return persons
