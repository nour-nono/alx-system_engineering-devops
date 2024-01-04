#!/usr/bin/env ruby
#script that accepts one argument and pass it to a regular expression matching
#must match School
puts ARGV[0].scan(/hb(t{1,5})n/).join
