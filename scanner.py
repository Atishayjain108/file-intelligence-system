import os
from storage import save_index, load_index


class FileScanner:

    def __init__(self):

        self.files, self.index, self.file_types = load_index()


    def scan_folder(self, folder_path):

        print("\nScanning folder:", folder_path)

        self.files = []
        self.index = {}
        self.file_types = {}

        for root, dirs, files in os.walk(folder_path):

            for file in files:

                full_path = os.path.join(root, file)

                self.files.append(full_path)

                file_name = file.lower()

                if file_name not in self.index:
                    self.index[file_name] = []

                self.index[file_name].append(full_path)

                extension = file.split(".")[-1].lower()

                if extension not in self.file_types:
                    self.file_types[extension] = 0

                self.file_types[extension] += 1

        save_index(self.files, self.index, self.file_types)

        print("Scan complete.")
        print("Total files indexed:", len(self.files))


    def search_file(self, search_term):

        search_term = search_term.lower()

        results = []

        for file_name in self.index:

            if search_term in file_name:
                results.extend(self.index[file_name])

        return results


    def show_statistics(self):

        print("\nFILE STATISTICS")
        print("----------------")

        print("Total files:", len(self.files))

        print("\nFile types:")

        for file_type in self.file_types:
            print(file_type, ":", self.file_types[file_type])


    def show_all_files(self):

        for file in self.files:
            print(file)
