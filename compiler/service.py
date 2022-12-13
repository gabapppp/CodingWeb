from compiler.utils.python_compiler import python_runner
from compiler.utils.java_compiler import java_runner
from compiler.utils.cpp_compiler import cpp_runner
from compiler.utils.shell_compiler import shell_runner


commands = {
    'python': {
        2: 'python',
        3: 'python3'
    },
    'java': {
        8: 'javac'
    },
    'cpp': {
        1:'gcc'
    },
    'shell':{
        2:'bash'
    }

}


extensions = {
    'python': '.py',
    'java': '.java',
    'cpp':'.cpp',
    'shell':'.sh'
}

def get_command(language, version):
    if language not in commands:
        return False, 'Invalid language.'
    if version not in commands[language]:
        return False, 'Invalid version.'

    return True, commands[language][version]


def get_extension(language):
    return extensions[language]

def get_target_method(language):
    if language == 'python':
        return python_runner
    elif language == 'java':
        return java_runner
    elif language == 'cpp':
        return cpp_runner
    elif language == 'shell':
        return shell_runner
