# kleene 

Converts a list of values into an xor regex.
For example,
["left", "right", "up", "down"]
returns the regex equivalent of:
"left" xor "right" xor "up" xor "down"

This was just some nerdy fun years ago.  The intent was to build a library of translations into regex.

## Future plans

- [ ] Move future plans to issues
- [ ] Add shared resources here

## Important disclaimer

I have more interesting work!  See my Hello, World root readme.


### Getting Started

Clone this repository and use the `kleene` class to generate regular expressions from lists of strings or numbers. You can run the provided examples in `kleene.py` or use the class in your own Python scripts. To verify everything works, you can also run the included tests.

### Prerequisites

- Python 3.6 or higher
- No additional libraries are required (only standard library modules like `re` and `unittest` are used)

### Installing

1. Clone the repository:
   ```bash
   git clone https://github.com/ErikPohl444/kleene.git
   cd kleene
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. No further installation steps are necessary; you can use the code directly.


## Running the tests

I will explain how to test the system here using the automated tests.

## Contributing

For now, I'd be excited to receive pull requests.  I don't have rules for contributing right now.

## Authors

* **Erik Pohl** - *Initial work* - 

Also see the list of github contributors.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to everyone who has motivated me to learn more.
