#author: Alex Chen
#date: 2013.4.2
#this divider uses binary search to estimate the quotient of division
class Divider
  def initialize(n, d)
    #raise exception if denominator is 0
    raise 'd cannot be zero' if d == 0

    @n = n
    @d = d

    #to start the estimation, the high is the absolute value of numerator itself, 
    #the low is zero, and the orientation of the binary search, is of the same sign of the denominator
    @high = (d > 0) ? n : -n
    @low = 0 #the low always start with 0        
  end

  def resursive_divide
    #if denominator is i or -1, there is no need to estimate, 
    #the quotient is the numerator with its sign being product with the denominator
    return [@n*@d, 0] if @d.abs == 1
    
    #estimate quotient by halving the sum of low and high
    q = (@low+@high)/2

    #calculate the remainder, the difference between numerator and the product of denominator and quotient
    r = @n-@d*q
    
    #return if the remainder is smaller than the denominator
    return [q, r] if r.abs < @d.abs && r * @d >= 0

    #half the estimation range by either make quotient the new low, or the new high.
    if @n * r > 0
      @low = q
    else
      @high = q
    end

    #calling divide recursively with the new low or new high
    return self.resursive_divide
  end
  
  def iterative_divide
    #if denominator is i or -1, there is no need to estimate, 
    #the quotient is the numerator with its sign being product with the denominator
    return [@n*@d, 0] if @d.abs == 1
    
    q = (@low+@high)/2
    r = @n-@d*q
    
    while r.abs >= @d.abs || r * @d < 0
      #estimate quotient by halving the sum of low and high
      q = (@low+@high)/2

      #calculate the remainder, the difference between numerator and the product of denominator and quotient
      r = @n-@d*q
      
      if @n * r > 0
        @low = q
      elsif 
        @high = q
      end      
    end
    
    return [q, r]  
  end
 
  def self.test(boundary=20)
    errors = []
    begin
      (quotient, remainder) = Divider.new(6, 0).iterative_divide
      errors << "didn't raise exception when dividing by zero."
    rescue      
    end
    
    begin
      (quotient, remainder) = Divider.new(6, 0).resursive_divide
      errors << "didn't raise exception when dividing by zero."
    rescue      
    end
        
    i = 0
    #testing 2 approaches, ranges for both denominator and numerator 
    [:resursive_divide, :iterative_divide].each do |method|
      (-boundary..boundary).each do |n|
        (-boundary..boundary).each do |d|        
          i+=1
          next if d == 0 #skip the case denominator is zero, which is tested above already
          (quotient, remainder) = Divider.new(n, d).send(method)
          puts "#{method}:#{n} / #{d} = #{quotient} ... #{remainder}"       
          
          #error if denominator * quotient + remainder is not equal to numerator
          if n != d * quotient + remainder  
            errors << "#{n} / #{d} != #{quotient} ... #{remainder}"
          end 
          
          #error if denominator * remainder are not of the same sign
          if d * remainder < 0
            errors << "#{n} / #{d} = #{quotient} ... #{remainder} but #{d} and #{remainder} have different signs"
          end         
        end
      end
    end
    
    puts errors
    puts "#{errors.count.to_s} failure out of #{i} cases"
  end
end

Divider.test