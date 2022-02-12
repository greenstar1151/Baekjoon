d1, d2, d3 = gets.chomp.split.map { |v| v.to_f }
a = (d1 + d2 - d3) / 2
b = (d1 - d2 + d3) / 2
c = (-d1 + d2 + d3) / 2

if a > 0 && b > 0 && c > 0
    puts 1
    puts "%.1f %.1f %.1f" % [a, b, c]
else
    puts -1
end
