from scanner import FileScanner


scanner = FileScanner()


while True:

    print("\nOptions:")
    print("1. Scan new folder")
    print("2. Search file")
    print("3. Show statistics")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        folder = input("Enter folder path: ")

        scanner.scan_folder(folder)

    elif choice == "2":

        term = input("Enter search term: ")

        results = scanner.search_file(term)

        if results:
            print("\nFiles found:")
            for file in results:
                print(file)
        else:
            print("No files found.")

    elif choice == "3":

        scanner.show_statistics()

    elif choice == "4":

        break

    else:

        print("Invalid choice")
