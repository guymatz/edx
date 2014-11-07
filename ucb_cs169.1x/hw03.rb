#!/usr/bin/env ruby
#
class BookInStock

    attr_accessor :isbn, :price
    def initialize(isbn, price)
        @isbn = isbn
        @price = price

        raise ArgumentError if @isbn.empty?
        raise ArgumentError if @price <= 0.0

    end

    def price_as_string
        "$#{'%.2f' % @price}"
    end

end

b = BookInStock.new('23423wfwr', 22.9)
puts b.price_as_string
puts b.isbn
