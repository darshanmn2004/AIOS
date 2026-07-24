from tools.app_tools import open_app
from tools.web_tools import open_website, google_search
from tools.file_tools import create_folder, create_file
from tools.file_tools import (
    create_folder,
    create_file,
    write_file,
    read_file,
)

TOOLS = {
    "open_app": open_app,
    "open_website": open_website,
    "google_search": google_search,

    "create_folder": create_folder,
    "create_file": create_file,
    "write_file": write_file,
    "read_file": read_file,
}