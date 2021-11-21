# convframe - PySide6 based framework for text conversion applications

Sometime you may need a simple text converter like:
  * Strip comments
  * Capitalize words
  * Remove leading / trailing spaces
  * Apply standardised formatting
  * etc.

Of course: you can do a lot with a great text editor like [Notepad++](https://notepad-plus-plus.org/) but there are cases when it's handy to have a somewhat standalone tool. In those cases you can build your own converter based on convframe. This gives you a GUI framework with an input and output field, file open and save options, drag and drop support, etc. In fact you only have to add the conversion code itself and get the GUI for 'free'.

## Usage
For a usage example, see [convframetemplate.py](https://github.com/bh1428/convframe/blob/master/convframetemplate.py). In short:
  * create a new class with `convframe.Converter` as base class
  * write your own implementation of the `convert` method which does the actual work:
    * the input (content of the _Input_ area when the user clicks the `[Convert]` button) is received via the `data` argument (str)
    * the result must be returned as a str(ing) and will be shown in the _Output_ text area
  * call `convframe.ConverterApp` with your class as it's `converter` argument
  * enter text in the _Input_ area
  * click the `[Convert]` button: the _Input_ area is converted and the result is shown in the _Output_ area

A minimal working implementation (which does nothing, i.e. returns the input as output) consists of:
```python
from convframe import ConverterApp, Converter

class DoNothing(Converter):
    def convert(self, data):
        return data

def main():
    ConverterApp(
        "Do Nothing",
        "This application does nothing",
        converter=DoNothing,
    )


if __name__ == "__main__":
    main()
```

In case you need configuration for your converter, you can implement / override these two methods of `convframe.Converter`:
```python
    def get_options_dialog(self):
        """Return an (optional) dialog (type=QLayout) for converter config."""
        return None

    def reset_options(self):
        """Reset the options in the (optional) dialog."""
        pass
```

The first method `get_options_dialog` is an easy way of adding configuration options via GUI elements to your converter application. See [convframetemplate.py](https://github.com/bh1428/convframe/blob/master/convframetemplate.py) for a basic usage example.

The second method `reset_options` hooks into the `[Reset]` button. If a user wants to reset the application to the initial state you can also reset your own options dialog. Again, see [convframetemplate.py](https://github.com/bh1428/convframe/blob/master/convframetemplate.py) for an example.

## Remarks
  * The framework is based on [PySide6](https://pypi.org/project/PySide6/) which has its own licensing conditions. Please pay close attention to those, depending on your application (and its distribution) you may need a license from them.
  * The project is primarily meant for Microsoft Windows. It will probably run on other operating systems, but this is not tested.
  * The development workflow for the package is based on a combination of [Visual Studio Code](https://code.visualstudio.com/) with the [Python extension](https://code.visualstudio.com/docs/languages/python), Python virtual environments (using [pip-tools](https://pypi.org/project/pip-tools/)) and `make` (if you need `make` for Windows: use the make from [GnuWin](http://gnuwin32.sourceforge.net/)).
