# Deutsche Rentenversicherung Form Autofill (unofficial)

## Project Overview

This project aims to simplify the process of filling out forms from the Deutsche Rentenversicherung (German Pension
Insurance) by automatically pre-filling personal data. The script uses a dictionary to store user input and generates
multiple PDF forms for different family member combinations.
It fills 8 forms with up to ~140 form fields from ~30 well-structured user inputs.

## Features

* Downloads and automatically pre-fills personal data in forms V0800, V0805, and V0820
  * Form are for `Feststellung von Kindererziehungszeiten`and `Zuordnung der Kindererziehungszeit`
  * Official information can be found here: https://www.deutsche-rentenversicherung.de/DRV/DE/Rente/Familie-und-Kinder/Kindererziehung/kindererziehung_node.html
* Generates separate PDF forms for each combination that may be needed (mother/father/child1/child2)
* Easy to use: simply fill in the personal data dictionary and run the script

## Usage

* Clone the repository
* Install required dependencies: `pip install -r requirements.txt`
* Fill in the dictionary in `./rv_form_prefill/my_family_definition.py` with your personal information
* Run the script: `python -m rv_form_prefill.pre_fill_forms`
* Use the forms generated in forms_output to continue filling the remaining forms/printing

## Supported Forms

* V0800
* V0805
* V0820

## Form Combinations

The script generates the following 8 form combinations:

* V0800
    * for mother + child 1 + child 2
    * for father + child 1 + child 2
* V0805
    * Mother + Child 1
    * Mother + Child 2
    * Father + Child 1
    * Father + Child 2
* V0820
    * Mother/Father + Child1
    * Mother/Father + Child2

## Requirements

* Tested with linux
* pdftk installed and available in command line
* Python >=3.11 + requests >=2.32

## Note

This project is intended for personal use only and is not affiliated with the Deutsche Rentenversicherung. Please ensure
that you follow the official guidelines when submitting the forms.

## Contributing

Contributions are welcome! If you'd like to improve the script or add new features, please submit a pull request.

## License

This project is licensed under the MIT License. See LICENSE for details.
