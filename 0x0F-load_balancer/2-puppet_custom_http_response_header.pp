class nginx_custom_header {
    package { 'nginx':
        ensure => installed,
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => template('nginx_custom_header.erb'),
        require => Package['nginx'],
        notify  => Service['nginx'],
    }

    service { 'nginx':
        ensure    => running,
        enable    => true,
        subscribe => File['/etc/nginx/sites-available/default'],
    }
}

include nginx_custom_header