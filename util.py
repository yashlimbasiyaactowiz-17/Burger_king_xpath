import os
import gzip
import json

""" USE FOR SINGLE FILE WITHOUT ZIP ( FOLDER )"""
def read_json(path: str):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.json'):
            full_path = os.path.join(path, file)
            try:
                content = open(full_path).read()
                yield json.loads(content)
            except Exception as e:
                print("Error in func:", read_json.__name__, '\nError: ', e)


""" USE FOR SINGLE FILE WITH ZIP ( FILES )"""
def read_json_zip_files(file_list: list):
    for file in file_list:
        try:
            content = gzip.open(file).read()
            yield json.loads(content)
        except Exception as e:
            print("Error in func:", read_json_zip_files.__name__, '\nError: ', e)


def read_html_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()