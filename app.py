# region link dropbox
from typing import Dict, Union

# https://www.dropbox.com/scl/fi/kyeki5guuct76fm5ssbhi/Python.paper?rlkey=02o8x67hp4j4heutw3gncpoy4&dl=0

# end region link dropbox


# region learning variables type


# region learning variables type

character_name: str = "Christian"
character_age: int = 27
character_is_male: bool = True

print("variables type test 1 :::", character_name, character_age, character_age)
print("variables type test length 2 :::", len(character_name))
print("variables type test concatenate 3 :::", character_name + " has " + str(character_age))
print(f"Variables type test f format 4 ::: {character_name} has {character_age}")

# endregion learning variables type

# region learning variables list

list_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("list type test::: 1", list_numbers)
print("list type test::: 2 index ", list_numbers[len(list_numbers) - 1])
print("list type test::: 3 slice", list_numbers[:1])
print("list type test::: 4 append", list_numbers.append(11))

# endregion learning variables list

# region learning tuple type

elements_tuple: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
print("tuple type test::: 1", elements_tuple)
print("tuple type test::: 2 index ", elements_tuple[len(elements_tuple) - 1])
print("tuple type test::: 3 count", elements_tuple.count(1))
print("tuple type test::: 4 conversion", list(elements_tuple))

# endregion learning tuple type

# region learning dictionary and combination (Union)

persona_1: Dict[str, str] = {"name": "Christian"}
persona_2: Dict[str, str] = {"name": "Christian 2"}
persona_3: Dict[str, str] = {"name": "Christian 3"}
persona_4: Dict[str, Union[str, int]] = {"name": "Christian 3", "age": 27}

list_personas: list[dict[str, str] | dict[str, str | int]] = [persona_1, persona_2, persona_3, persona_4]
print("type dictionary and combination type ::: 1", list_personas)
list_personas.append({'age': 1})
print("type dictionary and combination type append ::: 2",list_personas )


# endregion learning dictionary and combination (Union)


# region learning Class TODO:


# endregion learning Class

# region learning functions


def change_name(new_name: str) -> str:
    return new_name


character_name = change_name('Kevin')
print(f"functions type::: {character_name} character name changed")

# endregion learning functions
