#Kill a process using puppet
exec {'killmenow':
command => '/usr/bin/pkill killmenow'
}
