screen insertion_sort_puzzle:

    image "images/insertion_sort/is_template.jpg"
    
    draggroup:
        # Group of draggable pieces, and the spots they can be dragged to.
        # Paper pieces
        for i in range(page_pieces_is):
            drag:
                drag_name i
                pos initial_line_coordinates_is[i]
                anchor (0.5, 0.5)
                focus_mask True
                drag_raise True
                image "images/insertion_sort/is_line%s.png" % (i + 1)

        # Snappable spots to drag to.
        for i in range(page_pieces_is):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop_is
                pos coordinate_lines_is[i]
                anchor (0.5, 0.5)
                focus_mask True
                image "images/insertion_sort/is_line%s.png" % (i + 1) alpha 0.0