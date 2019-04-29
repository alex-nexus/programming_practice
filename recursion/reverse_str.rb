def reverse_string(s)
  if s.chars.size == 0
    return s
  else
    return reverse_string(s.chars.last(s.chars.size-1).join) + s.chars.first
  end
end

s = "Computer Science"
puts(s.size)
# puts((s.chars.last(s.size-1) + [s.chars.first]).join)
puts(reverse_string(s))
