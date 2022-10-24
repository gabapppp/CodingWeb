import subprocess
import sys


def execute_python_code(source_code, input):
    tmp = subprocess.run([sys.executable, "-c", source_code], input=input, capture_output=True, text=True)
    if tmp.stderr != "":
        return {"error": tmp.stderr, "status": "error"}
    return {"output": tmp.stdout, "status": "completed"}


def execute_cpp_code(source_code, input):
    f = open("code.cpp", "w")
    f.write(source_code)
    f.close()
    subprocess.call(["g++", "code.cpp"])
    tmp = subprocess.run("./a.out", input=input, capture_output=True, text=True)
    if tmp.stderr != "":
        return {"error": tmp.stderr, "status": "error"}
    return {"output": tmp.stdout, "status": "completed"}
