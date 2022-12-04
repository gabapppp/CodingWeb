import subprocess
import sys
import os


def execute_python_code(path, input):
    tmp = subprocess.run([sys.executable, path],
                         input=input, capture_output=True, text=True)
    if tmp.stderr != "":
        return {"error": tmp.stderr, "status": "error"}
    return {"output": tmp.stdout, "status": "completed"}


def execute_cpp_code(path, input):
    if not os.path.exists("./tmp"):
        os.mkdir("tmp")
    name = "" + path.split('/')[1] + "-" + path.split('/')[2]
    name = "".join(name.split('.')[:-1])
    subprocess.call(["g++", path, "-o", "./tmp/"+name+".out"])
    tmp = subprocess.run("./tmp/"+name+".out", input=input,
                         capture_output=True, text=True)
    if tmp.stderr != "":
        return {"error": tmp.stderr, "status": "error"}
    return {"output": tmp.stdout, "status": "completed"}
