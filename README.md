# Webdriver Package

Create a webdriver, focus on Chrome webdriver.

If webdriver is outdated ill search for a new one and download.
Download url files and rename download files. 


## TODO

* Add unit test.


## Example Usage

### How to Install

```shell
  # ./ChromeDriver
  pip install -e .
```

### Usage

```python
from src import chrome_driver

driver = chrome_driver.ChromeDriver(
  "temp",
  True,
  None,
  "_software",
  "application/pdf"
)

driver.create_driver()
```


Change Log
----------

* 0.1.0
  * Change: Start production.
* 0.1.9
  * Change: Download a new version of chromedriver if current oudated.
* 0.2.0
  * Change: Refactor code to add upload package to pypi

Meta
----

Author: [Frederico Gago](https://www.linkedin.com/in/frederico-gago-5849281aa/)

E-Mail: fredyisaac@gmail.com

&copy; 2022 by Frederico Gago
