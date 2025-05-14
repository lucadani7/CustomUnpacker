import logging
import os
import struct

from constants import Constants

"""Basic configuration of logging"""
logging.basicConfig(
    filename='logs.log',  # the file where the logs will be written
    filemode='a',  # append mode
    level=logging.DEBUG,  # logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # messages format
)

"""CustomUnpacker class with all the program functionalities:

   1. create_archive function, who creates an archive. The parameters are sources, who is a directory or a list of files, and archive_name, the name of
   the archive who is about to be created. Using auxiliar function add_in_archive, with parameters archive, file_path and header_format.

   2. list_archive function, who lists all the files from an archive. There is a single parameter, archive_path, where
   we give path of the archive we want to see its content. For less problems, giving archive absolute path is recommended.

   3. full_unpack function, who extracts all the files from the specified archive to a destination directory. First argument:
   archive_path, where we give path of the archive we want to see its content. For less problems, 
   giving archive absolute path is recommended. Second argument: destination_directory, directory where the files will be extracted.
   If the destination directory does not exist, it will be created.

   4. unpack function, who extracts all the files from the specified archive to a destination directory. First argument:
   archive_path, where we give path of the archive we want to see its content. For less problems, 
   giving archive absolute path is recommended. Second argument: files_list, who is the list of files we want to extract.
   If a file does not exist in the list, it will be skipped. If a file exists in the list, but not in the archive, the user will be warned.
   Last argument: destination_directory, directory where the files will be extracted.
   If the destination directory does not exist, it will be created.
"""


class CustomUnpacker:
    def create_archive(self, sources, archive_name):
        try:
            with open(archive_name, 'wb') as archive:
                logging.info(f"Creation of {archive_name} archive has been started.")
                print(f"Creation of {archive_name} archive has been started.")

            if isinstance(sources, str):
                sources = [sources]

            for source in sources:
                if os.path.isfile(source):  # if the source is a file, add it directly to archive
                    self.add_in_archive(archive, source, Constants.HEADER_FORMAT)
                elif os.path.isdir(source):  # if the source is a directory, process the files and add each file to archive
                    for root, _, files in os.walk(source):
                        for file in files:
                            absolute_path = os.path.join(root, file)
                            self.add_in_archive(archive, absolute_path, Constants.HEADER_FORMAT)
                else:
                    logging.warning(f"Source {source} is not a valid file or directory.")
                    print(f"Source {source} is not a valid file or directory.")

            logging.info(f"Archive {archive_name} has been created successfully.")
            print(f"Archive {archive_name} has been created successfully.")

        except Exception as e:
            logging.error(f"Error while creating the archive {archive_name}: {e}")
            print(f"Error while creating the archive {archive_name}: {e}")

    def add_in_archive(self, archive, file_path, header_format):
        try:
            file_name = os.path.basename(file_path).encode('utf-8').ljust(256, b'\x00')
            size = os.path.getsize(file_path)
            archive.write(struct.pack(header_format, file_name, size))

            with open(file_path, "rb") as file:
                archive.write(file.read())

            logging.info(f"File {file_path} has been successfully added to the archive.")
            print(f"File {file_path} has been successfully added to the archive.")

        except Exception as e:
            logging.error(f"Error while adding the archive {file_path}: {e}")
            print(f"Error while adding the archive {file_path}: {e}")
