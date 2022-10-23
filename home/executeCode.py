import subprocess
import sys


def execute_python_code(source_code, input):
    tmp = subprocess.run([sys.executable, "-c", source_code], stdin=input, capture_output=True, text=True)
    if tmp.stderr != "":
        return {"error": tmp.stderr, "status": "error"}
    return {"output": tmp.stdout, "status": "complete"}


def execute_cpp_code(source_code, input):
    f = open("code.cpp", "a")
    f.write(source_code)
    f.close()
    subprocess.call(["g++", "code.cpp"])
    tmp = subprocess.run("./a.out", shell=True, stdin=input, capture_output=True, text=True)
    if tmp.stderr != "":
        return {"error": tmp.stderr, "status": "error"}
    return {"output": tmp.stdout, "status": "complete"}
