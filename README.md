# three.py
A package dedicated to the love of 3. 

This is silly personal project inspired by the equally silly JavaScript library [five.js](https://github.com/jackdclark/five) by [Jack Clark](https://github.com/jackdclark/).


![THREE](https://www.clker.com/cliparts/3/1/p/f/N/4/tow-md.png)

## How to install
Using pip:
```
pip install love-three
```

Alternatively, you can clone the repo:
```
git clone https://github.com/JasonTurley/three.git
```

## Usage examples
Begin by importing the three module into your code.
```
>>> import three
```

The module can be used to perform:

**arithmetic**
```
>>> three.three() + three.three() 
6
```
```
>>> three.squared()
9
```
```
>>> three.cubed()
27
```

**boolean expressions**
```
>>> a = 2
>>> if three.is_three(a):
...     print("a equals three :)")
... else:
...     print("a does not equal three :(")
... 
a does not equal three :(
```

**filter, map, and reduce**
```
>>> values = [1, None, 3, "beans", False, 3]
>>> three.filter(values)
[3, 3]
>>> three.map(values)
[3, 3, 3, 3, 3, 3]
>>> three.reduce(values)
3   
```

**novelty and humor**
```
>>> three.leches()
['Condensed', 'Evaporated', 'Heavy cream']
```
```
>>> three.stooges()
['Larry', 'Curly', 'Moe']
```

**date and time**
```
>>> three.hours_from_now()
'17:45:00'
```
```
>>> three.days_from_now()
'06 October 2020'
```

## Development setup
All the code needed is contained within:
```
three.py
```

### Run tests
From the root (three) directory:
```
python3 -m unittest discover -s tests
```

## How to contribute
Contributions are encouraged and welcomed!

See [CONTRIBUTING.md](https://github.com/JasonTurley/three/blob/master/CONTRIBUTING.md)

## Meta
Distributed under the MIT license. See [LICENSE.txt](https://github.com/JasonTurley/three/edit/master/LICENSE.txt) for more information.
