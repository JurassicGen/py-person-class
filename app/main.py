class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []

    for person_data in people:
        persons.append(Person(person_data["name"], person_data["age"]))

    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"]:
            person.husband = Person.people[person_data["husband"]]

    return persons
