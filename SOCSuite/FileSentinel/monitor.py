import hashlib
import json
import os
import sys


def hash_file(file_path):

    with open(file_path, "rb") as f:
        data = f.read()

    hash = hashlib.sha256(data).hexdigest()

    return hash


def create_baseline(folder):
    hashes = {}
    for filename in os.listdir(folder):

        full_path = folder + "/" + filename

        if os.path.isfile(full_path):
            file_hash = hash_file(full_path)
            hashes[filename] = file_hash

    hashes_path = os.path.join(os.path.dirname(__file__), "hashes.json")
    with open(hashes_path, "w") as f:
        json.dump(hashes, f)

    return hashes


def check_integrity(folder):

    hashes_path = os.path.join(os.path.dirname(__file__), "hashes.json")
    with open(hashes_path, "r") as f:
        baseline = json.load(f)

    tampered = []

    for filename, old_hash in baseline.items():
        new_hash = hash_file(folder + "/" + filename)
        if new_hash != old_hash:
            tampered.append(filename)

    return tampered


def main():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = os.path.join(os.path.dirname(__file__), "test_folder")

    if "baseline" in sys.argv:
        create_baseline(folder)
        print("Baseline saved")
    else:
        tampered = check_integrity(folder)
        if tampered:
            print("ALERT")
        else:
            print("OK")


if __name__ == "__main__":
    main()
