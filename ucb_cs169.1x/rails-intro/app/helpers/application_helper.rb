module ApplicationHelper
  def sortable(column, ctitle = nil, id = nil)
    ctitle ||= column.titleize
    css_class = column == sort_column ? "hilite" : nil
    direction = column == sort_column && sort_direction == "asc" ? "desc" : "asc"
    logger.debug("css_class = #{css_class}")
    logger.debug("column = #{column}")
    logger.debug("sort_column = #{sort_column}")
    logger.debug("sort_direction = #{sort_direction}")
    logger.debug("direction = #{direction}")
    link_to ctitle, {:sort => column, :direction => direction}, {:class => css_class, :id => column + '_header'}
  end
end
