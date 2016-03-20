from fabric.api import *
from fabric.context_managers import *
from fabric.contrib import *

def prepare():
    sudo("wget http://nginx.org/keys/nginx_signing.key")
    sudo("apt-key add nginx_signing.key")
    distribution = sudo("echo $(lsb_release -sc)")
    filename = "/etc/apt/sources.list.d/nginx-stable.list"
    pckg1 = "deb http://nginx.org/packages/ubuntu/ " + distribution + " nginx"
    pckg2 = "deb-src http://nginx.org/packages/ubuntu/ " + distribution + " nginx"
    files.append(filename, pckg1, True)
    files.append(filename, pckg2, True)

@task
def install():
    prepare()
    sudo("apt-get -y update")
    sudo("apt-get install -y nginx")
 
