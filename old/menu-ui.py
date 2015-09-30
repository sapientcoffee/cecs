

# https://pypi.python.org/pypi/Menu/1.4
# sudo easy_install https://pypi.python.org/packages/source/M/Menu/Menu-1.4.tar.gz

import menu
#from menu import Menu
import cecs

# mainMenu = menu.Menu('title',update=updateFunction)
#
# mainMenu.submenu = menu.Menu('title',update=updateFunction)
#
# options = [{"name":"firstOption","function":firstFunc},
#            {"name":"secondOption","function":secondFunc},
#            {"name":"thirdOption","function":thirdFunc}]
# mainMenu.addOptions(options)
#
# mainMenu.open()


title = "ROBS TEST MENU"

mainMenu = menu.Menu(title,update=updateFunction)

mainMenu.explicit()
options = [{"name":"firstOption","function":firstFunc},
           {"name":"secondOption","function":secondFunc},
           {"name":"thirdOption","function":thirdFunc}]
mainMenu.addOptions(options)

mainMenu.clearOptions()

mainMenu.implicit()
options = [("firstOption",firstFunc),
           ("secondOption",secondFunc),
           ("thirdOption",thirdFunc)]
mainMenu.addOptions(options)
mainMenu.open()
