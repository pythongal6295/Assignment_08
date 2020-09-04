#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# KKauffman, 2020-Aug-30, added code to class CD and FileIO, began Main code
# KKauffman, 2020-Sept-01, continued building Main code, updated docstrings
# KKauffman, 2020-Sept-02, took out dictionaries to use list of CD objects,
#   updated functions to work with a list of objects, updated docstrings
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        CD ID, title, and artist are added to a list of CD objects

    """

    #Fields
    #Constructor 
    def __init__(self, cd_id, cd_title, cd_artist):
    
        #Attributes
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    #Properties
    @property
    def cd_id(self):
        return self.__cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_id.setter
    def cd_id(self, new_cd_id):
        self.__cd_id == new_cd_id

            
    @cd_title.setter
    def cd_title(self, new_cd_title):
        self.__cd_title == new_cd_title
    
    @cd_artist.setter
    def cd_artist(self, new_cd_artist):
        self.__cd_artist == new_cd_artist

    #Methods

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    #Properties
    
    #Methods
    @staticmethod
    def save_inventory(file_name, table):
        """Function to write data to file
        
        Takes each row from list of CD objects and separates the items in it by a comma
        and adds a \n at the end
        
        Args:
            file_name (string): name of file data is saved to
            table (lists of CD Objects)
            
        Returns: print statement confirming save is complete
        
        """
        objFile = open(strFileName, 'w')
        for row in table:
            objFile.write(str(row.cd_id) + ',' + row.cd_title + ',' + row.cd_artist + '\n')
        objFile.close()
        return print('\nYour data has been saved.')
    

    @staticmethod
    def load_inventory(file_name, table):
        """Method to load data from file to a list of CD objects

        Reads the data from file identified by file_name into a list of objects

        Args:
            file_name (string): name of file used to read the data from
            table (list of CD objects): holds the data during runtime

        Returns:
            table
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                cd_info = CD(int(data[0]), data[1], data[2]) #define ID, title, and artist as objects
                table.append(cd_info)
            objFile.close()
        except IOError:
        #If function can't find the file, then this code will execute
            print('\nCD Inventory file does not yet exist. Creating a new file now.')
            objFile = open(file_name, 'w')
            objFile.close()
        return table

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output
        
        Displaying menu options
        Displaying current CD inventory
        Collecting user menu choice 
        Collecting user informatin about a CD
    """
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('\nCD Inventory Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')
        
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table 

        Returns:
            None.

        """
        print()
        print('------- The Current Inventory: -------')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by: {})'.format(str(row.cd_id), row.cd_title, row.cd_artist))
        print('--------------------------------------')
        print()
        
    @staticmethod
    def user_inputs():
        """Function to gather the user's inputs for CD ID, CD Title, and CD Artist
        
        Arg: none
        
        Return: a tuple of the three user inputs (entryID, entryTitle, entryArtist)
        
        """
        #Will catch if the user enters an noninteger for the ID. Loop will continue to prompt them.
        entryID = ''
        while True:
            try:
                entryID = int(input('Enter ID: ').strip())
                break
            except ValueError:
                print('\nOops! You must enter an integer for the CD ID.')
                continue
        
        entryTitle = input('What is the CD\'s title? ').strip()
        entryArtist = input('What is the Artist\'s name? ').strip()
        return (entryID, entryTitle, entryArtist)

# -- Main Body of Script -- #

print('\nWelcome to your CD Inventory!')

# 1. When program starts, load the currently saved Inventory into a list of CD objects
lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects) 

# 2. start main loop

while True:
    # 2.1 Display Menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()
    # show user current inventory
        # 3.4 process display current inventory
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user add data to the inventory
        # 3.3 process add a CD
    elif strChoice == 'a':
        
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID, strTitle, strArtist = IO.user_inputs() #Assigned return to variables and unpacked this tuple
        
        # 3.3.2 Add item to the table
        #Arguments are unpacked tuple from IO.user_inputs() and instantiated as objects
        cd_info = CD(int(strID), strTitle, strArtist)
        lstOfCDObjects.append(cd_info) #Add CD object to list of CD Objects
        continue  # start loop back at top.
    
    # let user save inventory to file
        # 3.6 process save inventory to file
    elif strChoice == 's':
        
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        
        # 3.6.2 Process choice
        if strYesNo == 'y':
            
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # let user load inventory from file
        # 3.2 process load inventory
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled\n')
        if strYesNo.lower() == 'yes':
            print('\nreloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('\ncanceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.\n')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user exit program
        # 3.1 process exit first
    elif strChoice == 'x':
        break
    else:
        print('General Error')
