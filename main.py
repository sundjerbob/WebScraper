

import corner
from cornerdatabase import CornerDatabase


def main():
    database = CornerDatabase()
    corner.start(database)
    database.print_data()


main()
