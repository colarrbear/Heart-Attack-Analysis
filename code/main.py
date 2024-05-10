"""Main of the program. Used to run the program"""
from controllers import HDController


def main():
    """Main function"""
    controller = HDController()
    controller.run()


if __name__ == "__main__":
    main()
