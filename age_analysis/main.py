from dataclasses import dataclass, field
from random import random


@dataclass
class AgeGroup:
    TYPES = ['20s', '30s', '40s', '50s', '60s', '70s']

    type: str = '20s'
    initial_count: int = 5
    annual_increment: float = 1
    annual_decrement_prob: float = 0.2

    def initial_age(self):
        return {'20s': 25,
                '30s': 35,
                '40s': 45,
                '50s': 55,
                '60s': 65,
                '70s': 75,
                '80s': 85,
                '90s': 95}.get(self.type, 25)

    @staticmethod
    def age_group_type(age):
        if age > 20 and age <= 30:
            return '20s'
        elif age > 30 and age <= 40:
            return '30s'
        elif age > 40 and age <= 50:
            return '40s'
        elif age > 50 and age <= 60:
            return '50s'
        elif age > 60 and age <= 70:
            return '60s'
        elif age > 70 and age <= 80:
            return '70s'
        elif age > 80 and age <= 90:
            return '80s'
        elif age > 90:
            return '90s'


class Population:
    def __init__(self, age_groups):
        self.age_groups = {age_group.type: age_group
                           for age_group in age_groups}
        self.people = []
        for age_group_type, age_group in self.age_groups.items():
            for i in range(age_group.initial_count):
                self.people.append(age_group.initial_age())

    def increment_year(self, year=1):
        self.people = [age + year for age in self.people]
        self.add_new_people()
        self.remove_existing_people()

    def add_new_people(self):
        for age_group_type, age_group in self.age_groups.items():
            for i in range(age_group.annual_increment):
                self.people.append(age_group.initial_age())

    def remove_existing_people(self):
        for people_age in self.people:
            age_group_type = AgeGroup.age_group_type(people_age)
            age_group = self.age_groups[age_group_type]

            r = random()
            if r <= age_group.annual_decrement_prob:
                print(f'remove: {people_age}')
                self.people.remove(people_age)

    def average(self):
        return round(sum(self.people) / len(self.people), 2)

    def analysis(self):
        print(f'total: {len(self.people)}, avg: {self.average()}')


def main():
    age_groups = [
        AgeGroup('20s', 5, 1, 0.1),
        AgeGroup('30s', 5, 1, 0.05),
        AgeGroup('40s', 7, 1, 0.03),
        AgeGroup('50s', 7, 0, 0.03),
        AgeGroup('60s', 7, 0, 0.03),
        AgeGroup('70s', 5, 0, 0.03),
        AgeGroup('80s', 1, 0, 0.1),
        AgeGroup('90s', 0, 0, 0.1)
    ]

    population = Population(age_groups)

    print("Current")
    population.analysis()
    for i in range(10):
        print(f'\nYear {i}')
        population.increment_year(1)
        population.analysis()


if __name__ == "__main__":
    main()
