module FunWithStrings
  def palindrome?
    s = ''
    # Strip out non-alpha chars
    self.each_char do |c|
        if c.upcase != c.downcase
            s += c
        end
    end
    0.upto(s.length / 2) do |n|
        return false if s[n].downcase != s[-n-1].downcase
    end
  end

  def count_words
    return {} if self.empty?
    tmp_hash = {}
    self.gsub!(/[^\w ]/, '')
    self.downcase.split.each do |w|
        tmp_hash[w] ? tmp_hash[w] += 1 : tmp_hash[w] = 1
    end
    return tmp_hash
  end

  def is_anagram?(other)
    one = self
    two = other
    #puts "Checking #{one} against #{two}"
    one.each_char do |c|
      if not two.nil? and two.include?(c)
        two.sub(c, '')
      else
        return false
      end
    end
    two.each_char do |c|
      if not one.nil? and one.include?(c)
        one.sub(c, '')
      else
        return false
      end
    end
    #puts "#{two} = #{one}"
    return true
  end

  def anagram_groups
    return [] if self.empty?
    anagram_list = []
    words = self.split
    words.each_index do |i|
        next if (words[i].empty? or words[i].nil?)
        tmp_list = []
        tmp_list << words[i]
        # last word in list, nothing else to check
        if i == words.length
            return anagram_list
        end
        (i+1).upto(words.length) do |j|
            if words[i].is_anagram?(words[j])
                tmp_list << words[j]
                words[j] = ''
            end
        end
        anagram_list << tmp_list
    end
    return anagram_list
  end
end

# make all the above functions available as instance methods on Strings:

class String
  include FunWithStrings
end
