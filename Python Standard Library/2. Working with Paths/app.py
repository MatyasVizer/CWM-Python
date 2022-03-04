from pathlib import Path

Path(r"C:\Program Files\Microsoft")
Path("usr/local/bin")
Path()  # object that represents the current folder
path = Path("ecommmerce/__init__.py")
Path() / Path("ecommmerce/__init__.py")  # combining paths
Path() / "ecommmerce" / "__init__.py"  # combining strings to paths
Path.home()  # returns the home directory of the current user

path.exists()
path.is_file()
path.is_dir()
print(path.name)  # full filename
print(path.stem)  # without the extension
print(path.suffix)  # extension
print(path.parent)  # parent of the path
new_path = path.with_name("file.txt")
new_path2 = path.with_suffix(".txt")
print(new_path)
print(path.absolute())
