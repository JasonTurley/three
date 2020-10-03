# Contributing to Three
First off, thanks for taking the time to contribute!

Below is a set of guidelines for contributing. These are mostly guidelines, not set rules. Use your best judgement and feel free to propose changes to this document.

## Pull Request Process
1. Fork this repo to your GitHub account
2. Clone your version of the repo with ```git clone https://github.com/<your_user_name>/three.git```
3. Create a new descriptively named branch with ```git checkout -b new-branch```
4. Make any local changes and **add test cases if changing app functionality**
5. Commit changes with ```git commit -m "my descriptive commit message"
6. Push changes to your current branch with ```git push --set-upstream origin new-branch```
7. Configure a remote for the fork with ```git remote add upstream https://github.com/<your_user_name>/three.git``` (this is to avoid conflicts)
8. Sync the fork with ```git fetch upstream```, switch to local master branch with ```git checkout master```, and then merge changes with ```git merge upstream/master```
9. Finally, create a Pull Request

### Tests
Add tests to the file ```three/tests/tests.py```

Follow the same style and format as the other test cases.

From the root directory run tests with 
```
python3 -m unittest discover -s tests
```

## Style Guide
The coding style for this repo is inspired by [pep8](https://www.python.org/dev/peps/pep-0008/). In general, follow the style and format of the current code.
Read the document if you'd like, but the key takeaways are:

* use lowercase or lower_case_with_underscores for functions and local variables
```python
def my_cool_function():
  n = 2
  some_lame_var = "hi"
  
  return some_lame_var * n
```

* use UPPERCASE or UPPERCASE_WITH_UNDERSCORES for "constant" values
```
MAX_LIMIT = 3000
...
```

* use CapitalizedWords (aka CamelCase) for class names
```
class MyFavClass:
  ...
  ...
```

Check out the full [pep8 style guide](https://www.python.org/dev/peps/pep-0008/).
