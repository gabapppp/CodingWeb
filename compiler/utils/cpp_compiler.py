import os
from config import DOCKER_IMAGE, LOCAL_DIR, CONTAINER_DIR
import traceback


def cpp_runner(client, file_name, container_name, command_string, return_dict):
    try:
        local_directory = LOCAL_DIR + '/' + str(file_name)
        container_directory = CONTAINER_DIR + '/' + str(file_name)
        cpp_output_dir = LOCAL_DIR + '/' + container_name + 'temp'
        _file = open(cpp_output_dir, "w+")
        _file.close()

        container_run_command = 'docker run -d -it -v {0}:{1} --name {2} {3}'.format(local_directory,
                                                                                     container_directory,
                                                                                     container_name, DOCKER_IMAGE)
        os.system(container_run_command)

        container_id = client.containers.list(filters={'name': container_name})[0].short_id

        cpp_compile_command = 'docker exec -it {0} gcc {1} -o a.out'.format(container_id, str(file_name))
        system_compile_command = '{0} > {1}'.format(cpp_compile_command, cpp_output_dir)
        os.system(system_compile_command)

        with open(cpp_output_dir, 'r') as content_file:
            compile_output = content_file.read()

        if compile_output:
            os.remove(cpp_output_dir)
            return_dict['result'] = str(compile_output)
            return

        cpp_run_command = 'docker exec -it {0} {1}'.format(container_id, './a.out')
        system_run_command = '{0} > {1}'.format(cpp_run_command, cpp_output_dir)
        os.system(system_run_command) 

        run_output = open(cpp_output_dir, 'r').read()

        os.remove(cpp_output_dir)
        return_dict['result'] = str(run_output)
    except Exception as e:
        print (traceback.print_exc())
        return_dict['result'] = e.message