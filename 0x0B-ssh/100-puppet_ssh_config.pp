# Puppet to make changes to our configuration file
file_line { 'PasswordAuthentication':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no'    
}
file_line {'Configuration ssh':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school'    
}