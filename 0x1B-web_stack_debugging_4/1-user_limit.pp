# Enable the user holberton

# Increase file limits for holberton user using augeas
augeas { 'holberton_file_limits':
  context => '/files/etc/security/limits.conf',
  changes => [
    'set holberton hard nofile 50000',
    'set holberton soft nofile 50000',
  ],
  onlyif  => 'match user[. = "holberton"] size > 0 and (match user[. = "holberton"]/nofile[. = "5"] size > 0 or match user[. = "holberton"]/nofile[. = "4"] size > 0)',
}

# This ensures that the user holberton exists before making changes
User['holberton'] -> Augeas['holberton_file_limits']
