# Python 3: Mutable, Immutable... Everything is an Object!

![Python Objects](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

## Introduction
When starting with Python, you quickly learn a fundamental truth: "everything is an object." Unlike some programming languages that separate primitive data types from objects, Python treats absolutely everything—integers, strings, lists, and even functions—as an object under the hood. This design makes Python incredibly flexible but requires a solid understanding of how these objects live and behave in memory.

## id and type
To inspect objects, Python gives us two handy built-in functions: `type()` and `id()`. The `type()` function tells you the class an object belongs to. The `id()` function acts as the object's fingerprint, returning its unique memory address. 
```python
a = 89
print(type(a))  # Output: <class 'int'>
print(id(a))    # Output: 10105856

Mutable Objects
Mutable objects are objects that can be changed after they are created. Common examples include list, dict, and set. When you modify a mutable object, its memory address (id) remains exactly the same. You are altering the object in place.
my_list = [1, 2, 3]
print(id(my_list)) # Example Output: 14013589
my_list.append(4)
print(id(my_list)) # Same Output: 14013589

Immutable Objects
On the flip side, immutable objects cannot be modified once created. Examples include int, float, str, and tuple. If you try to update the value of an immutable object, Python doesn't change it; instead, it creates a brand-new object in memory with a completely new id.
text = "Hello"
print(id(text)) # Output: 2001150
text += " World"
print(id(text)) # Output: 3005890 (Different ID!)

Why does it matter and how Python treats them
Understanding mutability is crucial because it affects how variables reference memory. If two variables point to the same mutable object (e.g., a = b = [1, 2]), changing a will also secretly change b! For immutable objects, Python sometimes uses memory optimization (like pre-allocating small integers from -5 to 256). Since they can't be changed, it is safe for multiple variables to share the same immutable object in memory without side effects.
How arguments are passed to functions
Python uses a mechanism called "call by object reference." When you pass a mutable object to a function, the function gets a reference to the actual object. If the function modifies it (like adding an item to a list), the original list outside the function changes too. However, if you pass an immutable object (like an integer) and the function tries to change it, Python creates a new local copy, leaving the original variable completely untouched.