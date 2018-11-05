from currency import convert

# Create a function called convert that takes a list called rates, a number called value, a string called from, and a string called current. Make sure than when you call convert with from and to being equal, the return value is the same as value.



def test_convert():
    assert convert([], 1, current = "USD", to = "USD") == 1

# DONE. The rates list should contain a list of tuples, with each tuple containing a currency code you can convert from, a currency code you can convert to, and a rate.

# DONE. [("USD", "EUR", 0.74)]
# This means that each dollar is worth 0.74 euros.

# DONE. value is the amount of currency, from is the current currency code, and to is the currency code you wish to convert to.

# Given the above rates, make sure that converting 1 dollar into euros returns the following value: 0.74.

# Next, test that you can convert currency with a value that is not 1.

# Next, test that converting 1 euro into dollars returns 1.35 (or an approximation).

# Create a new list of rates with two or more tuples. Make sure you can convert both ways with each rate. For example, with these rates:

# [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]
# Make sure you can convert from USD to EUR, EUR to USD, EUR to JPY, and JPY to EUR.

# Make sure that if you try to make a conversion you do not know about, a ValueError is raised with an appropriate message.
