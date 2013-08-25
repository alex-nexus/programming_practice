#given a set of integers, generate the power sets

def power_set(input_set)
  return [[]] if input_set.empty?   	 
  num = input_set.shift 
  o = [] 
  power_set(input_set).each do |set|
    o.push [num]+set
    o.push set 
  end
  o
end

input_set = [1,2,3]
input_set = input_set.uniq
o = power_set(input_set)

puts o.inspect
puts o.count
