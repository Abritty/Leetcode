def valid_anagram(s, t)
    return false if s.length != t.length

    count = Hash.new(0)

    s.each_char { |char| count[char] += 1 }
    t.each_char { |char| count[char] -= 1 }

    count.values.all? { |v| v == 0 }
end

# Example usage
puts valid_anagram("anagram", "nagaram") # Output: true
puts valid_anagram("rat", "car")         # Output: false
