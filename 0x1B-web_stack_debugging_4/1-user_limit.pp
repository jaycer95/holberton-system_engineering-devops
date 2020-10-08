# Increase user limit
exec { 'file change':
command  => 'sudo echo "fs.file-max = 65536" >> /etc/sysctl.conf',
provider => shell,
}
exec { 'apply the limit':
command  => 'sudo sysctl -p',
provider => shell,
}
