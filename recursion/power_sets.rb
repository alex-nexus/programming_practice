def power_sets(nums)
    return [[]] if nums.size == 0
        
    ss = [nums]
    nums.each do |num|
        ss += power_sets(nums-[num])        
    end
    ss.uniq
end

puts "#{power_sets([1,2,3])}"
puts "#{power_sets([1,2,3,4])}"
