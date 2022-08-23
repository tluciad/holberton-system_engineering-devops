# Puppet to make changes to our configuration file
file_line { 'PasswordAuthentication':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no'
    replace => true
}
file_line {'Configuration ssh':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school'
    replace => true
}