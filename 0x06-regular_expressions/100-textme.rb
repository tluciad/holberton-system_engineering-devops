#!/usr/bin/env ruby
#Your script should output: [SENDER],[RECEIVER],[FLAGS]
message = ARGV[0].scan(/\[from:(.+?)\]|\[to:(.+?)\]|\[flags:(.+?)\]/)
list = [message[0].compact, message[1].compact, message[2].compact]
puts list.join(',')