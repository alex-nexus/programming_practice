def power_sets(nums)
    return [[]] if nums.size == 0
        
    [nums] + nums.map do |num|
        power_sets(nums-[num])
    end.reduce(&:+).uniq    
end
