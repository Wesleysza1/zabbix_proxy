import subprocess

system = str(subprocess.check_output("cat /etc/*-release | grep PRETTY", shell=True))
so = system.lower()

if "ubuntu" in so:
    subprocess.call(["ansible-playbook", "ubuntu-zabbix-proxy.yaml", "-K"])
elif "debian" in so:
    subprocess.call(["ansible-playbook", "debian-zabbix-proxy.yaml", "-K"])
elif "redhat" in so: 
    subprocess.call(["ansible-playbook", "rhel-zabbix-proxy.yaml", "-K"])
elif "red hat" in so: 
    subprocess.call(["ansible-playbook", "rhel-zabbix-proxy.yaml", "-K"])
elif "centos" in so:
    subprocess.call(["ansible-playbook", "centos-zabbix-proxy.yaml", "-K"])
elif "suse" in so:
    subprocess.call(["ansible-playbook", "suse-zabbix-proxy.yaml", "-K"])
else:
    ("SO non supported")
