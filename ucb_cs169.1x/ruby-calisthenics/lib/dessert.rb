class Dessert
  attr_accessor :name, :calories
  def initialize(name, calories)
    @name = name
    @calories = calories
  end
  def healthy?
    @calories < 200
  end
  def delicious?
    true
  end
end

class JellyBean < Dessert
  attr_accessor :flavor
  def initialize(flavor)
    @name = flavor + ' jelly bean'
    @flavor = flavor
    @calories = 5
  end
  def delicious?
    return false if @flavor == 'licorice'
    true
  end
end
