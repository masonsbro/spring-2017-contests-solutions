limits = (1..10).map{|x| 10*x}
limits.each do |limit|
    File.open("test/#{limit}.in", 'w') do |file|
        file.write("#{limit}\n")
        limit.times do
            ct = rand(1..1000)
            file.write("#{ct}\n")
            sample = (1..65535).to_a.sample(ct)
            file.write("#{sample.join(' ')}\n")
        end
    end
end
