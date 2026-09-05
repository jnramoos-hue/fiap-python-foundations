<div align="center">

# Chapter 4: Dictionaries and Tuples

![Python](https://img.shields.io/badge/Python-Dictionaries%20%26%20Tuples-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FIAP](https://img.shields.io/badge/FIAP-Nano%20Course-ED145B?style=for-the-badge)
![Chapter](https://img.shields.io/badge/Chapter-04-6C63FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-2EA44F?style=for-the-badge)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=900&color=3776AB&center=true&vCenter=true&width=800&lines=Working+with+key-value+pairs;Managing+data+with+dictionaries;Understanding+immutable+tuples;Building+modular+Python+programs)](https://git.io/typing-svg)

</div>

## About This Chapter

Chapter 4 of the **FIAP Python Foundations Nano Course** introduced dictionaries and tuples as new ways to organize and access data in Python.

The chapter progressed from basic dictionary creation and key-based access to small user-management operations such as inserting, searching, deleting and listing records. It also introduced tuples, immutability, `enumerate()` and the use of functions and modules to organize the program.

> This repository contains introductory learning evidence. The exercises demonstrate foundational Python practice and do not represent advanced Python knowledge, a production database or professional software engineering experience.

## Learning Objectives

During this chapter, I practiced how to:

- Create empty and populated dictionaries
- Store information as key-value pairs
- Access values using dictionary keys
- Add new records to a dictionary
- Update values associated with an existing key
- Search safely with the `get()` method
- Iterate over keys, values and complete items
- Delete records from a dictionary
- Organize dictionary operations inside functions
- Import functions into a main Python module
- Create and access tuples
- Understand tuple immutability
- Use tuples as dictionary keys
- Use `enumerate()` to access an index and an element during iteration
- Combine dictionaries, lists and tuples in small programs

## Dictionaries

A dictionary stores data as **key-value pairs**.

```python
users = {
    "chaves": ["Chaves from 8", "24/12/2017", "Reception_01"],
    "quico": ["Quico das Flores", "20/17/2017", "Xray_03"]
}
```

In this example:

- `"chaves"` and `"quico"` are dictionary keys
- Each key is associated with a list containing user information
- A key provides direct access to its corresponding value

## Creating an Empty Dictionary

An empty dictionary can be created with curly brackets:

```python
users = {}
```

New information can then be added by assigning a value to a key:

```python
users["florinda"] = [
    "Mrs. Florinda",
    "24/12/2017",
    "Xray_01"
]
```

## Accessing Values

A value can be accessed directly with its key:

```python
print(users["quico"])
```

The `get()` method can also be used:

```python
print(users.get("quico"))
```

When a key is not found, `get()` normally returns `None` instead of raising a `KeyError`.

## Updating Values

Assigning a new value to an existing key updates the stored record:

```python
users["quico"] = [
    "Quico das Flores",
    "21/12/2017",
    "Xray_04"
]
```

Dictionary keys must be managed carefully because assigning another value to the same key replaces the previous value.

## Iterating Over Dictionaries

### Keys

```python
for key in users.keys():
    print(key)
```

### Values

```python
for value in users.values():
    print(value)
```

### Keys and Values

```python
for key, value in users.items():
    print(key, value)
```

The `items()` method provides access to each key and its associated value during iteration.

## Searching for Records

A record can be searched by using a key provided by the user:

```python
search_key = input("Enter the username: ").upper()
result = users.get(search_key)

if result is not None:
    print(result)
else:
    print("User not found.")
```

This exercise combines:

- User input
- Key normalization
- Dictionary lookup
- Conditional statements
- Output messages

## Deleting Records

A dictionary record can be deleted with `del`:

```python
del users["quico"]
```

A key should be checked before deletion to avoid an error:

```python
if "quico" in users:
    del users["quico"]
```

## User-Management Operations

The chapter applied dictionaries to a small in-memory user-management program.

The main operations were conceptually similar to:

- **Create:** insert a user
- **Read:** search for or list users
- **Update:** replace information associated with an existing key
- **Delete:** remove a user

These operations resemble introductory CRUD concepts. However, the records exist only in memory and are lost when the program ends. This exercise is not a persistent database application.

## Functions and Modularization

Dictionary operations were separated into functions to improve organization and code reuse.

Functions in this stage may include responsibilities such as:

```text
ask for an option
insert a user
search for a user
delete a user
list registered users
```

A simplified function structure looks like this:

```python
def search_user(dictionary, key):
    return dictionary.get(key)
```

Separating operations into functions prepares the code for clearer modules and future maintenance.

## Modules

Functions can be stored in one Python file and imported into the main module.

```python
from functions import insert_user, search_user, delete_user
```

The main module is responsible for:

- Creating the main dictionary
- Displaying the menu
- Receiving the selected option
- Calling the corresponding function
- Controlling when the program ends

This structure introduces separation of responsibilities without claiming enterprise-level architecture.

## Tuples

A tuple is an ordered and immutable collection.

```python
ip_address = ("192.168", "1.10")
```

Tuple elements can be accessed by index:

```python
print(ip_address[0])
print(ip_address[1])
```

Unlike a list, a tuple cannot be modified after it is created:

```python
# This operation is not allowed:
# ip_address[0] = "10.0"
```

## Tuples as Dictionary Keys

Because tuples are immutable, they can be used as dictionary keys when their elements are also hashable.

```python
locations = {
    (10, 20): "Server room",
    (30, 40): "Reception"
}
```

A value can then be accessed using the complete tuple:

```python
print(locations[(10, 20)])
```

## Using `enumerate()`

The `enumerate()` function associates an index with each element during iteration.

```python
emails = [
    "user1@example.com",
    "user2@example.com"
]

for index, email in enumerate(emails):
    print(index, email)
```

Each iteration provides:

```text
(index, element)
```

This is useful when both the position and the value are needed.

## Data Structures Compared

### List

- Ordered
- Mutable
- Accessed mainly by numerical index
- Useful for collections that may change

### Dictionary

- Stores key-value pairs
- Mutable
- Accessed mainly by key
- Useful when each value needs a meaningful identifier

### Tuple

- Ordered
- Immutable
- Accessed by numerical index
- Useful for values that should not change

## Technical English

| Portuguese | English |
|---|---|
| Dicionário | Dictionary |
| Chave | Key |
| Valor | Value |
| Par chave-valor | Key-value pair |
| Consultar | Look up |
| Inserir | Insert |
| Atualizar | Update |
| Excluir | Delete |
| Listar | List |
| Registro | Record |
| Usuário | User |
| Tupla | Tuple |
| Imutável | Immutable |
| Índice | Index |
| Iteração | Iteration |
| Enumerar | Enumerate |
| Módulo | Module |
| Função | Function |
| Retorno | Return value |
| Dados em memória | In-memory data |
| Persistência | Persistence |

## Evidence Produced

This chapter produced introductory evidence of:

- Creating and populating Python dictionaries
- Working with key-value pairs
- Accessing records by key
- Using `get()` for dictionary lookup
- Adding, updating and deleting records
- Iterating with `keys()`, `values()` and `items()`
- Combining dictionaries with lists
- Organizing dictionary operations in functions
- Importing functions into a main module
- Creating and accessing tuples
- Understanding immutability
- Using tuples as dictionary keys
- Iterating with `enumerate()`
- Writing variables and console messages in English

## Technical Notes

- Dictionary keys should uniquely identify their associated values.
- Assigning a value to an existing key overwrites the previous value.
- Direct access with square brackets may raise `KeyError` when the key does not exist.
- The `get()` method can provide safer lookup behavior.
- In Python 3, `keys()`, `values()` and `items()` return dictionary view objects.
- The old `has_key()` method should not be used in Python 3.
- Tuples are immutable, but mutable objects stored inside a tuple may still change.
- The data used in these exercises exists only in memory and is not stored in a database.

## Chapter Progress

```text
[████████████████████] Chapter 4 completed
```

The practical learning stage covering dictionaries, tuples, functions and modular organization was completed.

## Connection to Software Development

The concepts from this chapter support future learning in:

- JSON objects
- API request and response data
- Configuration structures
- Data validation
- Database records
- Backend services
- Authentication data
- Structured application state
- Data transformation

Dictionaries are especially important in Python backend development because many API and JSON structures are represented through key-value data.

## Next Steps

- Continue to the next FIAP Nano Course chapter
- Practice solving dictionary problems independently
- Improve input validation and error handling
- Learn how to persist records in files and databases
- Compare dictionaries with classes and data models
- Continue separating responsibilities into functions and modules
- Add automated tests when testing concepts are introduced
- Update the main repository documentation after the complete course is finished

## Responsible Use of Course Materials

This repository contains my own code, explanations and learning evidence. FIAP PDFs, protected course content, personal information, credentials and assessment materials are not included.

## Author

**Jose da Silva Ramos Junior**  
Software Development Student at FIAP  
Building foundations in Python, backend development and financial technology.

---

<div align="center">

**Learning through practice, validation and continuous improvement.**

</div>
