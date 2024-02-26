# ssh use the private key ~/.ssh/school
file { 'ssh_config':
  ensure  => file,
  path => '/etc/ssh/ssh_config',
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
