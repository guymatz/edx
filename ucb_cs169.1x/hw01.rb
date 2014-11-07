#!/usr/bin/env ruby

def sum(nums = [])
  if nums.length() == 0
    return 0
  else
    total = 0
    nums.each do |n|
      total += n
    end
    return total
  end
end

def max_2_sum(nums = [])
  if nums.length() == 0
    return 0
  elsif nums.length() == 1
    return nums[0]
  else
    nums.sort!.reverse!
    return nums[0] + nums[1]
  end
end

def sum_to_n?(nums = [],total)
  if nums.length() < 2
    return false
  end
  
  nums.each_with_index do |n1, i1|
    nums.each_with_index do |n2, i2|
      if n1 == n2
        next
      end # end if
      return true if n1 + n2 == total
    end # nums second
  end # nums first
  return false
end # def

#puts sum([])
#puts sum([0,1,2,3,4])
#puts max_2_sum([])
#puts max_2_sum([5])
#puts max_2_sum([0,1,2,3,4])
#puts sum_to_n?([], 9)
#puts sum_to_n?([4], 9)
#puts sum_to_n?([0,1,2,3,4], 5)
#puts sum_to_n?([0,1,2,3,4], 8)
