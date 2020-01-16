# eighteeneff
An exercise in looking up the second lowest cost silver plan, as one does.

# How to run this

* Youl'll need to have Python 3 installed on an machine running Apple OS X. (Only tested on 10.13.6, ymmv)
* Download a .zip version, using the green "Clone or download" button above and to the right.
* Unzip that sucker, switch into the `eighteeneff-master` directory, open your `Terminal` app and type:
```
$ python main.py
```
* You should see a list of ZIP codes and accompanying second lowest cost silver plan as per the data in `data/zips.csv`, the source of truth for this app.

# How to run the tests

* While in the `eighteeneff-master` directory, from the `Terminal` type:

```
$ python -m unittest test
```
* You shoud see:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.059s

OK

```
* That is all!