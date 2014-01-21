==================
NREL Utility Wrapper 0.1
==================
Hannes Hapke
21/01/2014


README
------
This is a Python wrapper for NREL's utility API. 

It allows you to directly convert an address into
utility information (utility name, residential, 
commercial and industrial electricity costs).

License
------
MIT

Dependencies
------------
It has dependency on the json package, included with Python versions 2.7 and later.
requests library is also needed and will be installed by setuptools.

It is developed on Python 2.7 but should work on earlier versions. 
Not tested if it is also compatible with Python 3. Sorry.


Installation
------------
You can install this package using pip:

    pip install pynrelutility

or download the source from https://github.com/hanneshapke/pynrelutility and install

    python setup.py install

Also obtain a [free API key](https://developer.nrel.gov/signup) from NREL. 


Usage of the NREL Census Utility  API
-------------------------------------

    from pynrelutility import NRELUtilityWrapper, NRELUtilityResults
    ...
    address = 'YOUR ADDRESS'
    ...
    nrel_data = NRELUtilityWrapper(YOUR_NREL_API_KEY)
    nrel_response = nrel_data.get_nrel_utility_data(address)
    result = NRELUtilityResults(nrel_response) 
    ...
    result.utility_name # displays the names of all utilities at the location

The following attributes are currently supported:

    - utility_name
    - utility_name_list
    - commercial
    - residential
    - industrial


Contact Information
-------------------
Author: Hannes Hapke (renooble)
Twitter: @hanneshapke
Internet: https://github.com/hanneshapke/ 

For comments, issues, requests, please contact via Github at the above website


Changelog
---------
Version 0.1   > Project created, test.py and setup.py created



