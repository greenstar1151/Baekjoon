N = gets.chomp.to_i

votes = gets.chomp.split.map { |v| v.to_i }
vote_table = Array.new(N+1, 0)
for v in votes do 
    vote_table[v] += 1
end
vote_table = vote_table.drop(1)
max_vote = vote_table.max
if vote_table.count(max_vote) > 1
    puts 'skipped'
else
    puts vote_table.index(max_vote) + 1
end
