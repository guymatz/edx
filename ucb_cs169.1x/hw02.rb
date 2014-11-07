def hello(name)
  "Hello, #{name}"
end

def starts_with_consonant?(s)
  return false if s.empty?
  return false if s =~ /^[AEIOU]/i
  return false if s[0] !~ /[A-Z]/i
  return true
end

def binary_multiple_of_4?(s)
  return false if s.empty?
  return false if s !~ /^[01]*$/
  s.to_i(2) % 4 == 0 ? true : false
end

hello("Guy")
puts starts_with_consonant?('n is ok')
puts starts_with_consonant?('o is not ok')
puts binary_multiple_of_4?('1000')
puts binary_multiple_of_4?('1010')
puts binary_multiple_of_4?('a1010')
