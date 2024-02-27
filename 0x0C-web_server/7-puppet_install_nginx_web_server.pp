# nginx_setup.pp

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx is running
service { 'nginx':
  ensure     => running,
  enable     => true,
  require    => Package['nginx'],
}

# Ensure Nginx is listening on port  80
firewall { 'nginx':
  port   =>  80,
  proto  => tcp,
  action => accept,
}

# Create a simple index.html with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => '<html><body><h1>Hello World!</h1></body></html>',
  require => Package['nginx'],
}

# Set up a  301 redirect for /redirect_me
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Ensure the site is enabled
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Template for the Nginx site configuration
define nginx::site (
  $server_name,
  $root,
  $redirect_uri,
) {
  file { "/etc/nginx/sites-available/${server_name}":
    ensure  => file,
    content => template('nginx/site.erb'),
    notify  => Service['nginx'],
  }
}

# Create a site with the  301 redirect
nginx::site { 'default':
  server_name => 'localhost',
  root        => '/var/www/html',
  redirect_uri => '/redirect_me',
}

server {
    listen  80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;

    server_name noureldeen.tech;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a  404.
        try_files $uri $uri/ =404;
    }

    # Other locations...
}

server {
    listen  80;
    server_name <%= @server_name %>;

    location / {
        root <%= @root %>;
        try_files $uri $uri/ =404;
    }

    location <%= @redirect_uri %> {
        return  301 /;
    }

    # Other locations...
}
