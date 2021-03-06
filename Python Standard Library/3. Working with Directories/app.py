from pathlib import Path

path = Path("D:\DEV\CWM Python\Modules and packages\ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# generator object doesn't store value in memory

for p in path.iterdir():
    print(p)

# posixpath is standard in unix
# windowspath


paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("**/*.py")]  # recursive **/
py_files = [p for p in path.rglob("*.py")]  # or rglob
print(py_files)
