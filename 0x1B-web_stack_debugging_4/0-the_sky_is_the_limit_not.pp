#the_sky_is_the_limit_not

exec { 'Ulimit nginx':
  command => 'sudo echo "ULIMIT=\"-n 4096\"" >> /etc/default/nginx',
  path    => '/bin/',
}

-> exec { 'restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
