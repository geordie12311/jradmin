#python script utilising nornir_scrapli plugin send_configs_from_file
#script is going to take the commands listed in jradmin_config.txt
#send them to all the hosts in the nornir hosts file. Note this specific
#example is to create a new user "jradmin" with restricted privileges
#so that user can only run show command scripts
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result
#importing send_configs_from_file from nornir_scrapli to send configuration commands from a file
nr = InitNornir(config_file="config.yaml")
#The above line is telling nornir where the config file is located

def send_configs(task):
    task.run(task=send_configs_from_file, file="jradmin_config.txt")
#above function is going to use the send_configs to send configuration commands from a file

results = nr.run(task=send_configs)
#above line is setting an object results that is aligned to the task output
print_result(results)
