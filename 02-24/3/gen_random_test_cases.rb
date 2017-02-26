limits = (1..4).map{|x| 10**x}
[10**4].each do |limit|
    [true, false].each do |easy|
        easy_str = if easy then 'easy' else 'hard' end
        File.open("test/#{easy_str}.in", 'w') do |file|
            file.write("#{limit}\n")
            limit.times do
                width  = rand(1..12)
                height = rand(1..12)
                depth  = rand(1..12)

                top    = if easy then 10**3 else 10**7 end
                bot    = if easy then 1 else 10**6 end
                n      = rand(bot..top)
                file.write("#{width} #{height} #{depth} #{n}\n")
            end
        end
    end
end
