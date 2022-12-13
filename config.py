# ----------------------  BASE PARAMETERS ---------------------- #
DOCKER_IMAGE = 'judge0/compilers'
LOCAL_DIR = '/home/hoainguyen/Desktop/IDEhub/idehub_be/storge'

# ----------------------  ADDITIONAL PARAMETERS ---------------------- #
#MEMORY_LIMIT = '8000k'  # the memory limit for the each docker container
AUTO_REMOVE = False # remove the docker container when it has completed the execution
FILE_OPEN_MODE = 'rw' #read only : use rw for read write
CONTAINER_DIR = '' # the container directory where code execution take place
CONTAINER_TIMEOUT = 600 # number of seconds the container is allowed to run