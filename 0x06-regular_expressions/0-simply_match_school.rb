#!/usr/bin/env ruby
# Check if the command-line argument matches the regular expression
if ARGV[0] =~ /School/
  puts ARGV[0]
else
  puts ""
end
