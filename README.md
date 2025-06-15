# PrayerTimes

Pray Times is an Islamic project aimed at providing an open-source library for calculating Muslim prayer times.
The first version of Pray Times was released in early 2007. The code is currently used in a wide range of Islamic websites and applications.
🔗 http://praytimes.org/

- **User's Manual:** http://praytimes.org/manual
- **Calculation Formulas:** http://praytimes.org/calculation

**Compatible with Python 3.x**
**Improved version: PEP8 compliant, bugs fixed, and ready to use**

---

## Features

- Various methods of time calculation
- Global location support
- Local prayer time calculation (no internet required)
- Multiple time formats
- Time adjustments
- No external dependencies

---

## Prerequisites

Make sure you have the following installed:

- [Git](http://git-scm.com/)
- [Python 3.x](https://www.python.org/)

---

## Installation

```bash
git clone https://github.com/QuantumPrayerTimes/prayertimes.git
cd prayertimes
python setup.py install
```

---

## Usage

### Available Calculation Methods

| Method    | Description                                   |
|-----------|-----------------------------------------------|
| MWL       | Muslim World League                           |
| ISNA      | Islamic Society of North America              |
| Egypt     | Egyptian General Authority of Survey          |
| Makkah    | Umm al-Qura University                        |
| Karachi   | University of Islamic Sciences, Karachi       |
| Tehran    | Institute of Geophysics, University of Tehran |
| Jafari    | Shia Ithna Ashari (Jafari)                    |
| UOIF      | Union of Islamic Organizations of France      |
| Singapore | Majlis Ugama Islam Singapura                  |
| Turkey    | Diyanet İşleri Başkanlığı                     |

---

### Using Today's Date

```python
from prayertimes import PrayTimes
import datetime

today = datetime.datetime.today()

# Using ISNA method
pt = PrayTimes(method='ISNA')

# Get times using UTC offset
times = pt.get_times(today, (43, -80), -5)

# Or using a timezone string
times = pt.get_times(today, (43, -80), "America/New_York")
```

---

### Using a Specific Date

```python
from prayertimes import PrayTimes

pt = PrayTimes(method='ISNA')

# February 25, 2011 at location (43, -80)
times = pt.get_times((2011, 2, 25), (43, -80), -5)
```

---

### Available Time Formats

| Format | Description                     | Example |
|--------|---------------------------------|---------|
| 24h    | 24-hour format                  | 16:45   |
| 12h    | 12-hour format with suffix      | 4:45 pm |
| 12hNS  | 12-hour format no suffix        | 4:45    |
| Float  | Decimal hours (floating point)  | 16.75   |

---

### Changing Time Format

```python
from prayertimes import PrayTimes

pt = PrayTimes('ISNA')

# Set 12-hour format
pt.time_format = '12h'

times = pt.get_times((2011, 2, 25), (43, -80), -5)
```

---

### Asr Methods

| Method   | Description                                                |
|----------|------------------------------------------------------------|
| Standard | Shafii, Maliki, Jafari, Hanbali (shadow factor = 1)        |
| Hanafi   | Hanafi school of thought (shadow factor = 2)               |

---

### Midnight Methods

| Method   | Description                          |
|----------|--------------------------------------|
| Standard | Mean time from Sunset to Sunrise     |
| Hanafi   | Mean time from Maghrib to Fajr       |

---

### Higher Latitude Methods

| Method      | Description                        |
|-------------|------------------------------------|
| None        | No adjustments                     |
| NightMiddle | Middle of the night                |
| OneSeventh  | 1/7th of the night                 |
| AngleBased  | Angle-based (recommended)          |

---

### Modifying Settings

```python
from prayertimes import PrayTimes

pt = PrayTimes(method='ISNA')

# Use Hanafi method for Asr
pt.adjust({'asr': 'Hanafi'})

times = pt.get_times((2011, 2, 25), (43, -80), -5)
```

---

### Tuning Prayer Times

```python
from prayertimes import PrayTimes

pt = PrayTimes(method='ISNA')

# Add/subtract minutes to specific times
pt.tune({
    'fajr': +10,
    'dhuhr': -10,
    'asr': -10,
    'maghrib': -10,
    'isha': +10,
    'midnight': +5,
    'sunrise': -2,
    'sunset': +9,
    'imsak': +15
})

times = pt.get_times((2011, 2, 25), (43, -80), -5)
```

---

## Resources

- **Homepage:** [https://github.com/QuantumPrayerTimes/prayertimes](https://github.com/QuantumPrayerTimes/prayertimes)
- **Source:** [Browse Repository](https://github.com/QuantumPrayerTimes/prayertimes)

---

## Issues

Have suggestions or run into problems?
👉 [Open an issue](https://github.com/QuantumPrayerTimes/prayertimes/issues) or submit a pull request!
