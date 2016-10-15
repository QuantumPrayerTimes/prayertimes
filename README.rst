PrayerTimes
===========

.. image:: https://travis-ci.org/QuantumPrayerTimes/prayertimes.svg?branch=master
   :alt: Build
   
.. image:: https://www.quantifiedcode.com/api/v1/project/f73051bca854427c8405d28eabe6424c/badge.svg
   :target: https://www.quantifiedcode.com/app/project/f73051bca854427c8405d28eabe6424c
   :alt: Code issues
   
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
    
    # Date 02/25/2011
    # City Lat and Long : 43, -80
    # City UTC offset : -5 (you have to take into account DST)
    times = PT.get_times((2011, 2, 25), (43, -80), -5)

Configurations
==============

Resources
=========
* Homepage: https://github.com/QuantumPrayerTimes/prayertimes
* Source:

    - Browse at https://github.com/QuantumPrayerTimes/prayertimes

Please let me know if you like or use this module - it would make
my day!
