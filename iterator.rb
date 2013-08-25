class OneArrayIterator
  def initialize(object)
    @object = object
  end
  
  def has_next?
    return false if @object.empty?
    return true unless @object[0].nil?
    OneArrayIterator.new(@object.drop(1)).has_next?
  end
  
  def next
    return nil if @object.empty?
    
    e = @object.shift
    return e unless e.nil?
    
    OneArrayIterator.new(@object).next
  end   
end

class TwoArrayIterator
  def initialize(object)
    @object = object
  end
  
  def has_next?
    return false if @object.empty?
    return true if OneArrayIterator.new(@object[0]).has_next?
    TwoArrayIterator.new(@object.drop(1)).has_next?
  end
  
  def next
    return nil if @object.empty?
    
    @object.shift if @object[0].empty?
    e = @object[0].shift
    return e unless e.nil?
    
    TwoArrayIterator.new(@object).next
  end
end

oa = OneArrayIterator.new([1,2,nil,3,nil])
while oa.has_next?
  puts oa.next
end
puts '-'
ta = TwoArrayIterator.new([[nil,3,nil,4,5],[nil,2,nil],[nil,nil],[5,6],[99,nil]])
while ta.has_next?
  puts ta.next
end
