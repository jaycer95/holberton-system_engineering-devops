#the_sky_is_the_limit_not

exec { 'Ulimit nginx':
  command => 'sudo echo "ULIMIT=\"-n 4096\"" >> /etc/default/nginx ; sudo service nginx restart',
  provider => shell,
}
