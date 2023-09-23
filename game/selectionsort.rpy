screen selection_sort_puzzle:

    image "images/selection_sort/ss_template.jpg"
    
    draggroup:
        # Group of draggable pieces, and the spots they can be dragged to.
        # Paper pieces
        for i in range(page_pieces_ss):
            drag:
                drag_name i
                pos initial_line_coordinates_ss[i]
                anchor (0.5, 0.5)
                focus_mask True
                drag_raise True
                image "images/selection_sort/ss_line%s.png" % (i + 1)

        # Snappable spots to drag to.
        for i in range(page_pieces_ss):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop_ss
                pos coordinate_lines_ss[i]
                anchor (0.5, 0.5)
                focus_mask True
                image "images/selection_sort/ss_line%s.png" % (i + 1) alpha 0.0