# Data Engineering Coding Challenges

## Problem 1: Fixed-Width File Parse
- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

### How to run
```
# pull the docker image
docker pull ghcr.io/lorne-luo/code_kata/problem1:latest

# run docker container, the generated files will copied into you current local path
docker run -v .:/app/problem1/data ghcr.io/lorne-luo/code_kata/problem1

# check result files
cat generated.txt
cat parsed.csv
```

### How to setup
```
# checkout the repo
git clone git@github.com:lorne-luo/code-kata.git
cd code-kata

# create virtual environment
python3 -m venv venv
. venv/bin/activate

# run test
cd problem1
pytest

# run main
python main.py

```

### Note
To make code smell good and easy to review:
- used [black](https://github.com/psf/black) to format the code
- used [flake8](https://github.com/PyCQA/flake8) to check code style
- used [isort](https://github.com/PyCQA/isort) to sort import statements
- Created Github Action pipeline to publish the Docker images

## Problem 2

### Data processing

- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform

## To be finished