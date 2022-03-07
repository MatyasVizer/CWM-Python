import subprocess


# these are obsolete
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen  # process open class

# new syntax
try:
    completed = subprocess.run(["false"],
                               capture_output=True,
                               text=True,
                               check=True)
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
except subprocess.CalledProcessError as ex:
    print(ex)
