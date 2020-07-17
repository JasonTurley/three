# three.py
A package dedicated to the love of 3. 

This is silly personal project inspired by the equally silly JavaScript library [five.js](https://github.com/jackdclark/five) by [Jack Clark](https://github.com/jackdclark/).

## How to install
To install the library, simply clone or fork the repository. I am working on releasing this as a pip package for easier download in the future.
```
git clone https://github.com/JasonTurley/three
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

## Development setup
All the code needed is contained within:
```
three.py
```

*An automated test suite is under-construction!*

## How to contribute
Contributions are encouraged and welcomed!

1. Fork the repo 
2. Create a branch for your new feature (```git checkout -b feature/my-cool-feature```)
3. Commit your changes (```git commit -am feature/my-cool-feature```)  
4. Push to the branch (```git push origin feature/my-cool-feature```)
5. Create a new Pull Request

## Meta
Distributed under the MIT license. See [LICENSE.txt](https://github.com/JasonTurley/three/edit/master/LICENSE.txt) for more information.
