# tslazer.py
# author: ef1500
import TwitterSpace
import argparse
import os

parser = argparse.ArgumentParser(description="Download Twitter Spaces at lazer fast speeds!", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--path", "-p", type=str, help="Path to download the space")

spaceID_group = parser.add_argument_group("Downloading from a Space ID/URL")
spaceID_group.add_argument("--space_id", "-s", type=str, help="Twitter Space ID or URL")

fileformat_options = """
    %%Ud	Host Display Name
    %%Un	Host Username
    %%Ui	Host User ID
    %%St	Space Title
    %%Si	Space ID
    """
spaceID_group.add_argument("--fileformat", "-f", type=str, help=f"File Format Options: {fileformat_options}")

dyn_group = parser.add_argument_group("Downloading from a dynamic or master URL")
dyn_group.add_argument("--dyn_url", "-d", type=str, help="Twitter Space Master URL or Dynamic Playlist URL")
dyn_group.add_argument("--filename", "-fn", type=str, help="Filename for the Twitter Space")

args = parser.parse_args()
if args.space_id != None and args.fileformat != None:
    if args.path == None:
        args.path = os.getcwd()
    TwitterSpace.TwitterSpace(space_id=args.space_id, filenameformat=args.fileformat, path=args.path)
if args.dyn_url != None and args.filename != None:
    if args.path == None:
        args.path = os.getcwd()    
    TwitterSpace.TwitterSpace(dyn_url=args.dyn_url, filename=args.filename, path=args.path)