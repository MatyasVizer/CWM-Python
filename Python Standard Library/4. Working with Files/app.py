from pathlib import Path
from time import ctime  # creation time
import shutil


path = Path("D:\DEV\CWM Python\Modules and packages\ecommerce\__init__.py")
# path.exists()
# path.rename()
# path.unlink()
print(ctime(path.stat().st_ctime))

path.read_bytes()
print(path.read_text())

with open("__init__.py", "r") as file:  # old syntax
    ...

print(path.read_text())  # old syntax
path.write_text("...")
path.write_bytes()

source = Path("D:\DEV\CWM Python\Modules and packages\ecommerce\__init__.py")
target = Path() / "__init__.py"


target.write_text(source.read_text())  # old syntax
shutil.copy(source, target)  # new syntax
