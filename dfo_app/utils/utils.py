import json
import os

# required for saving json files
dirname=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')) # added after restructuring files/folders

def get_session_json():
    json_fullpath=os.path.join(dirname,r"temp\session.json")
    if os.path.isfile(json_fullpath):
        data = json.load(open(json_fullpath))
    else:
        data={}
    return data


def save_session_json(session):
    json_fullpath=os.path.join(dirname,r"temp\session.json")
    json.dump(session, open(json_fullpath, 'w'),indent=4, sort_keys=True)
    return "None"
