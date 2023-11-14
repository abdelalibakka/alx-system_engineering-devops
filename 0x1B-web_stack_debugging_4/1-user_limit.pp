# comments
file { '/etc/security/limits.conf':
  content => template('your_module/limits.conf.erb'),
  notify  => Exec['reload_limits'],
}
# comments
exec { 'reload_limits':
  command     => 'pkill -HUP -u $USER systemd-logind',
  path        => '/usr/bin:/bin',
  refreshonly => true,
  subscribe   => File['/etc/security/limits.conf'],
}
