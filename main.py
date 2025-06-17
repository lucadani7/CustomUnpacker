import argparse
import sys

from custom_unpacker import CustomUnpacker

parser = argparse.ArgumentParser(description="Execute all the functions from CustomUnpacker class")
subparsers = parser.add_subparsers(dest="command", help="Command which you want to execute")

"""Command for creating an archive."""
create_parser = subparsers.add_parser("create_archive", help="Create archive with specified files.")
create_parser.add_argument("-s", "--sources", nargs="+", required=True, help="Files list or directory with archive.")
create_parser.add_argument("-a", "--archive", required=True, help="Archive name who is about to be created.")

"""Command for listing an archive content."""
list_parser = subparsers.add_parser("list_content", help="List archive content.")
list_parser.add_argument("-p", "--path", required=True, help="Archive path.")

"""Command for extracting an archive content."""
unpack_all_parser = subparsers.add_parser("full_unpack", help="Extract all the files from an archive.")
unpack_all_parser.add_argument("-p", "--path", required=True, help="Archive path.")
unpack_all_parser.add_argument("-d", "--destination", required=True, help="Destination directory.")

"""Command for extracting some specified files from an archive."""
unpack_parser = subparsers.add_parser("unpack", help="Extract some specified files from an archive.")
unpack_parser.add_argument("-p", "--path", required=True, help="Archive path.")
unpack_parser.add_argument("-f", "--files", nargs="+", required=True, help="Files list who is / are about to be extracted.")
unpack_parser.add_argument("-d", "--destination", required=True, help="Destination directory.")

unpacker = CustomUnpacker()
print("Welcome to CustomUnpacker!")

while True:
    cmd_input = input("\nType a command (type 'quit' to quit or 'help' to see available commands): ").strip()
    if cmd_input.lower() == "quit":
        print("You chose to quit the program. Goodbye!")
        sys.exit(0)
    if cmd_input in ["help", "--help", "-h"]:
        parser.print_help()
        print("\nAdditional commands:")
        print("  help                Show this help message")
        print("  quit                Quit the program")
        continue
    try:
        args = parser.parse_args(cmd_input.split())
        match args.command:
            case "create_archive":
                unpacker.create_archive(args.sources, args.archive)
            case "list_content":
                unpacker.list_content(args.path)
            case "full_unpack":
                unpacker.full_unpack(args.path, args.destination)
            case "unpack":
                unpacker.unpack(args.path, args.files, args.destination)
    except SystemExit:
        print(f"Error: Command '{cmd_input}' is not recognized.")
        parser.print_help()
        print("\nAdditional commands:")
        print("  help                Show this help message")
        print("  quit                Quit the program")
        continue
