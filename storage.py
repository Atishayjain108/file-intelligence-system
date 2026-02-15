import json


def save_index(files, index, file_types):

    data = {
        "files": files,
        "index": index,
        "file_types": file_types
    }

    with open("file_index.json", "w") as f:
        json.dump(data, f)

    print("Index saved successfully.")


def load_index():

    try:

        with open("file_index.json", "r") as f:
            data = json.load(f)

        print("Index loaded successfully.")

        return data["files"], data["index"], data["file_types"]

    except:

        print("No saved index found.")

        return [], {}, {}
