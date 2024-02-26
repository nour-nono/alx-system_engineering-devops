file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
