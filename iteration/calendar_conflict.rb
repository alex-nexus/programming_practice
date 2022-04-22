# frozen_string_literal: true

def detect_conflicts(events)
  i = 0
  loop do
    event = events[i]
    puts('TRY:' + event.to_s)
    j = i + 1
    next_event = events[j]

    while next_event && (event.last > next_event.first)
      if no_overlap?(event, next_event)
        j += 1
        next_event = events[j]
      else
        return true
      end
    end

    i += 1
  end
  false
end

def no_overlap?(event1, event2)
  (event1.last <= event2.first) || (event2.last <= event1.first)
end

events = [
  [3, 5], [1, 2], [4, 6], [7, 10], [8, 11], [10, 12], [13, 14], [13, 14]
]

events = [
  [3, 5], [1, 2], [5, 6], [7, 10], [10, 11], [11, 12], [13, 14], [13, 15]
]

# puts(no_overlap?([3 , 5], [1, 2]))
puts(detect_conflicts(events))
