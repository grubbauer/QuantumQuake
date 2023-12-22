CustColo
========

CustColo is the module used for the logging system via colorama.
Its located in the resources/modules directory under the name 
"CustColo.py".


## Structure

The structure of the library is very simple.
It uses 5 functions that display colors with
the names "debug", "info", "warning", "error" and "critical".


### Explanation of code

Every fuction is the same as the other except the name and 
the color. Here is an example

def debug(arg):                                             # *
    import colorama                                         # **
    colorama.init()                                         # ***
    print(f"{colorama.Fore.CYAN}DEBUG: {arg}")              # *** *

#### Explanation of code elements

##### *
Defines the fuction and asks for the argument arg

##### **
Imports colorama because its necesary for the colors

##### ***
Initialises colorama

##### *** *
Prints the message to the console. Uses the "colorama.Fore.{x}" element.

### Example of code to run

#### *main.py*

import resources.modules.CustColo as CustColo
CustColo.debug("Example usage")

