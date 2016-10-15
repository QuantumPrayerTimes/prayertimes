PrayerTimes
===========

.. image:: https://travis-ci.org/QuantumPrayerTimes/prayertimes.svg?branch=master
    :alt: Build
    
.. image:: https://coveralls.io/repos/github/QuantumPrayerTimes/prayertimes/badge.svg?branch=master
    :target: https://coveralls.io/github/QuantumPrayerTimes/prayertimes?branch=master

.. image:: https://landscape.io/github/QuantumPrayerTimes/prayertimes/master/landscape.svg?style=flat
    :target: https://landscape.io/github/QuantumPrayerTimes/prayertimes/master
    :alt: Code Health
    
.. image:: https://codecov.io/gh/QuantumPrayerTimes/prayertimes/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/QuantumPrayerTimes/prayertimes

.. image:: https://codeclimate.com/github/QuantumPrayerTimes/prayertimes/badges/coverage.svg
   :target: https://codeclimate.com/github/QuantumPrayerTimes/prayertimes/coverage
   :alt: Test Coverage

Pray Times, an Islamic project aimed at providing an open-source library for calculating Muslim prayers times.
The first version of Pray Times was released in early 2007. The code is currently used in a wide range of Islamic websites and applications. (http://praytimes.org/)
  
User's Manual:
http://praytimes.org/manual

Calculation Formulas:
http://praytimes.org/calculation

Compatibility:
Compatible with Python 2.x and 3.x

**This is an improved version PEP8 compliant, bugs fixed and ready to use.**

Features:
=========

* Various methods of time calculation
* Supporting all locations around the world
* Local calculation of prayer times (no connection to Internet is needed)
* Multiple time formats
* Adjusting prayer times
 
Prerequisites
=============

You will need the following software properly installed on your computer.

* `Git <http://git-scm.com/>`__
* `Python 2.x or 3.x <https://www.python.org/>`__

Installation
============

Clone the repo and run :

.. code:: python

    git clone https://github.com/QuantumPrayerTimes/prayertimes.git
    cd prayertimes
    python setup.py install

Usage
=====

Available calculation methods :
  
::

    +=========+===============================================+
    | Method  | Description                                   |
    +=========+===============================================+
    | MWL     | Muslim World League                           |
    +---------+-----------------------------------------------+
    | ISNA    | Islamic Society of North America              |
    +---------+-----------------------------------------------+
    | Egypt   | Egyptian General Authority of Survey          |
    +---------+-----------------------------------------------+
    | Makkah  | Umm al-Qura University                        |
    +---------+-----------------------------------------------+
    | Karachi | University of Islamic Sciences, Karachi       |
    +---------+-----------------------------------------------+
    | Tehran  | Institute of Geophysics, University of Tehran |
    +---------+-----------------------------------------------+
    | Jafari  | Shia Ithna Ashari (Jafari)                    |
    +---------+-----------------------------------------------+

Using today date :
  
.. code:: python

    from prayertimes import PrayTimes
    import datetime
    
    today = datetime.date.today()
    
    # Using ISNA calculation method
    PT = PrayTimes('ISNA')
    
    # Date today
    # City Lat and Long : 43, -80
    # City UTC offset : -5 (you have to take into account DST)
    times = PT.get_times(today, (43, -80), -5)

Using a special date :

.. code:: python

    from prayertimes import PrayTimes
    
    # Using ISNA calculation method
    PT = PrayTimes('ISNA')
    
    # Date 02/25/2011
    # City Lat and Long : 43, -80
    # City UTC offset : -5 (you have to take into account DST)
    times = PT.get_times((2011, 2, 25), (43, -80), -5)

Available time format :

::

    +=========+==============================+=========+
    | Format | Description                   | Example |
    +=========+==============================+=========+
    | 24h    | 24-hour time format           | 16:45   |
    +--------+-------------------------------+---------+
    | 12h    | 12-hour time format           | 4:45 pm |
    +--------+-------------------------------+---------+
    | 12hNS  | 12-hour format with no suffix | 4:45    |
    +--------+-------------------------------+---------+
    | Float  | Floating point number         | 16.75   |
    +--------+-------------------------------+---------+

Modify time format :

.. code:: python

    from prayertimes import PrayTimes
    
    # Using ISNA calculation method
    PT = PrayTimes('ISNA')
    
    # Change time format
    PT.time_format = '12h'
    
    times = PT.get_times((2011, 2, 25), (43, -80), -5)

Available settings :

::

    Asr methods
    +==========+========================================================+
    | Method   | Description (More Info)                                |
    +==========+========================================================+
    | Standard | Shafii, Maliki, Jafari and Hanbali (shadow factor = 1) |
    +----------+--------------------------------------------------------+
    | Hanafi   | Hanafi school of tought (shadow factor = 2)            |
    +----------+--------------------------------------------------------+
    
    Midnight methods
    +==========+======================================+
    | Method   | Description                          |
    +==========+======================================+
    | Standard | The mean time from Sunset to Sunrise |
    +----------+--------------------------------------+
    | Hanafi   | The mean time from Maghrib to Fajr   |
    +----------+--------------------------------------+
    
    Higher latitudes methods
    +=============+======================================+
    | Method      | Description (More Info)              |
    +=============+======================================+
    | None        | No adjustments                       |
    +-------------+--------------------------------------+
    | NightMiddle | The middle of the night method       |
    +-------------+--------------------------------------+
    | OneSeventh  | The 1/7th of the night method        |
    +-------------+--------------------------------------+
    | AngleBased  | The angle-based method (recommended) |
    +-------------+--------------------------------------+


Modify settings :

.. code:: python

    from prayertimes import PrayTimes
    
    # Using ISNA calculation method
    PT = PrayTimes('ISNA')
    
    # Change asr settings
    PT.adjust({'asr': 'Hanafi'})
    
    times = PT.get_times((2011, 2, 25), (43, -80), -5)

Tune prayer times :

.. code:: python

    from prayertimes import PrayTimes
    
    # Using ISNA calculation method
    PT = PrayTimes('ISNA')
    
    # Tune the times
    PT.tune({'fajr': +10, 'dhuhr': -10, 'asr': -10, 'maghrib': -10, 
             'isha': +10, 'midnight': 5, 'sunrise': -2, 'sunset': +9, 
             'imsak': +15})
    
    times = PT.get_times((2011, 2, 25), (43, -80), -5)

Resources
=========
* Homepage: https://github.com/QuantumPrayerTimes/prayertimes
* Source:

    - Browse at https://github.com/QuantumPrayerTimes/prayertimes


Issues
======

If you have any issues or improvements, do not hesitate to create an
issue or submit a pull request.
