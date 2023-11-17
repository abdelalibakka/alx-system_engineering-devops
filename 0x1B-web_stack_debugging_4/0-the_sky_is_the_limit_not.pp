# Increase the ULIMIT for Nginx
file { '/etc/default/nginx':
  ensure  => file,
  content => template('path/to/nginx_config.erb'),
  require => Exec['nginx_config_change'],
}

exec { 'nginx_config_change':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
  notify  => Exec['nginx_restart'],
}

# Restart Nginx if the configuration has changed
exec { 'nginx_restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
  refreshonly => true,
}

# Usage of template('path/to/nginx_config.erb') assumes that you have an ERB template
# at 'path/to/nginx_config.erb' that contains the desired content for the nginx config.
