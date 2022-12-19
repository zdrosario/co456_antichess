# Antichess

**Name:** *Zaira del Rosario*

**Student ID:** `20813836`

**User ID:** `zzdelros`

**Course:** CO 456, Fall 2022, David Jao

# Libaries Used

This uses the `python-chess` libary. The docs are available
[here](https://python-chess.readthedocs.io/en/latest/) and the source is
[here](https://github.com/niklasf/python-chess/). `python-chess` is available
under the GPL-3.0 license.

# Build / Run Instructions

This program uses `python3`, and it was built and tested on version 3.8.10.
To install dependencies, run the following from the project's root directory:

```
pip install -r requirements.txt
```

The program can be invoked using the `antichess.sh`. Note that the shell script
uses the `python3` command and expects it to be available. E.g., from the
project's root directory:

```
./antichess.sh white
```

If you get a `Permission denied` error, add permissions to execute the file then
try again:
```
chmod u+x ./antichess.sh
```

The program can also be ran with python3 directly. E.g.:

```
python3 ./src/main.py white
```
