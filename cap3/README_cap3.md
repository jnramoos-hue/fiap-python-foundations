<div align="center">

# Chapter 3: Lists, Functions and Modules

![Python](https://img.shields.io/badge/Python-Lists%20%26%20Functions-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FIAP](https://img.shields.io/badge/FIAP-Nano%20Course-ED145B?style=for-the-badge)
![Chapter](https://img.shields.io/badge/Chapter-03-6C63FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-2EA44F?style=for-the-badge)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=900&color=3776AB&center=true&vCenter=true&width=760&lines=Working+with+Python+lists;Organizing+code+with+functions;Learning+modules+and+code+reuse)](https://git.io/typing-svg)

</div>

## About This Chapter

Chapter 3 of the FIAP Python Foundations Nano Course introduced lists, nested lists, functions and modules.

The exercises in this chapter evolved from storing related data in separate lists to organizing equipment records inside nested lists. The final stage separated the inventory operations into reusable functions and imported them into a main module.

> This chapter represents foundational hands-on practice. It does not represent advanced Python knowledge or professional software engineering experience.

## Learning Objectives

During this chapter, I practiced how to:

- Create empty and populated lists
- Add elements with `append()`
- Iterate over lists with `for`
- Access list elements by index
- Work with multiple related lists
- Search for an item inside a list
- Update an element stored in a list
- Remove an item from a list
- Organize related data with nested lists
- Use `len()`, `min()`, `max()` and `sum()`
- Create reusable functions with `def`
- Pass data through parameters and arguments
- Return a value with `return`
- Separate responsibilities into modules
- Import functions into a main module

## Topics Practiced

### Lists

Lists allow multiple values to be stored in a single data structure.

```python
inventory = []
inventory.append("Router")
inventory.append("Printer")
```

### Indexes

Python lists use zero-based indexing. The first element is located at index `0`.

```python
equipment = ["Router", 4500.00, 123456, "IT"]

print(equipment[0])
print(equipment[1])
```

The equipment records used in this chapter follow this structure:

```text
Index 0: Equipment name
Index 1: Equipment value
Index 2: Serial number
Index 3: Department
```

### Multiple Lists

The first inventory exercises stored related information in separate lists:

```python
equipment = []
values = []
serial_numbers = []
departments = []
```

An index was used to access the related information in each list.

### Searching Lists

A `for` loop and a conditional statement were used to locate equipment by name.

```python
search = input("Enter the name of the equipment you want to search for: ")

for index in range(0, len(equipment)):
    if search == equipment[index]:
        print("Value..: ", values[index])
        print("Serial.: ", serial_numbers[index])
```

### Nested Lists

The inventory was then reorganized as a list containing other lists.

```python
inventory = [
    ["Router", 4500.00, 123456, "IT"],
    ["Printer", 880.00, 122377, "HR"]
]
```

Each internal list represents one equipment record.

```python
for element in inventory:
    print("Name.........: ", element[0])
    print("Value........: ", element[1])
    print("Serial.......: ", element[2])
    print("Department...: ", element[3])
```

### Updating Values

The exercises included a simulated 10% depreciation applied to an equipment value.

```python
element[1] = element[1] * 0.9
```

This calculation was used only as an educational programming exercise.

### Removing Elements

Equipment could be located by serial number and removed from the inventory.

```python
if element[2] == serial_number:
    inventory.remove(element)
```

## Functions and Modularization

The inventory operations were separated into functions to reduce repetition and improve code organization.

The functions developed in this chapter were:

- `fill_inventory()`
- `display_inventory()`
- `find_by_name()`
- `depreciate_by_name()`
- `delete_by_serial()`
- `summarize_values()`

Example:

```python
def display_inventory(inventory):
    for element in inventory:
        print("Name.........: ", element[0])
        print("Value........: ", element[1])
        print("Serial.......: ", element[2])
        print("Department...: ", element[3])
```

## Modules

The functions were stored in a separate Python file and imported into the main module.

```python
from function_identification import *
```

The main module creates the list and calls the required functions:

```python
mylist = []

fill_inventory(mylist)
display_inventory(mylist)
find_by_name(mylist)
depreciate_by_name(mylist, 20)
print(delete_by_serial(mylist))
display_inventory(mylist)
summarize_values(mylist)
```

This exercise introduced the idea of separating reusable operations from the main program flow.

## Files Developed

The practical work for this chapter includes files related to:

```text
cap3/
├── multiple_lists_and_indexes.py
├── multiple_lists_and_search.py
├── nested_lists.py
├── function_identification.py
└── main_module.py
```

The repository preserves the directory structure used during the course and in PyCharm.

## Technical English

| Portuguese | English |
|---|---|
| Lista | List |
| Elemento | Element |
| Índice | Index |
| Lista aninhada | Nested list |
| Pesquisa | Search |
| Equipamento | Equipment |
| Inventário | Inventory |
| Número serial | Serial number |
| Função | Function |
| Parâmetro | Parameter |
| Argumento | Argument |
| Valor de retorno | Return value |
| Módulo | Module |
| Pacote | Package |
| Importação | Import |
| Reutilização de código | Code reuse |
| Modularização | Modularization |

## Evidence Produced

This chapter produced introductory evidence of:

- Creating and modifying Python lists
- Iterating over collections
- Accessing values through indexes
- Searching and updating stored data
- Working with nested data structures
- Dividing code into functions
- Passing lists as function arguments
- Returning a message from a function
- Importing functions into another Python file
- Using English variable names and console messages

## Technical Notes

- List indexes begin at `0`.
- The inventory structure depends on consistent index positions.
- The equipment value is stored at index `1`.
- The serial number is stored at index `2`.
- The exercises use `float` for values as part of the course practice.
- The exercises use `int` for serial numbers, although real identifiers may also contain letters or leading zeros.
- Input comparisons are case-sensitive unless the input is normalized.
- The code reflects the concepts introduced at this stage of the course.

## Current Progress

```text
[████████████████████] Chapter 3 completed
```

The practical exercises for lists, nested lists, functions and modules were implemented and reviewed.

## Next Steps

- Continue to the next course chapter
- Practice dictionaries and structured data
- Improve input validation in future exercises
- Continue using functions to avoid repeated code
- Review explicit imports in future project revisions
- Add tests after testing concepts are introduced
- Update the main repository documentation as the course progresses

## Responsible Use of Course Materials

This repository contains my own code and learning evidence. FIAP PDFs, protected course content, personal information, credentials and assessment materials are not included.

## Author

**Jose da Silva Ramos Junior**  
Software Development Student at FIAP  
Developing foundations in Python, backend development and financial technology.

---

<div align="center">

**Learning through practice, validation and continuous improvement.**

</div>
