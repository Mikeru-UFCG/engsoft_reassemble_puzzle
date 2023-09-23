init python:

    def setup_bs_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(5):
            start_x = 100
            start_y = 570
            end_x = 800
            end_y = 900
            rand_loc= (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_line_coordinates_bs.append(rand_loc) # Add the random locations to a list so we can use them
    
    def setup_is_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(8):
            start_x = 100
            start_y = 570
            end_x = 800
            end_y = 900
            rand_loc= (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_line_coordinates_is.append(rand_loc) # Add the random locations to a list so we can use them

    def setup_ss_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(10):
            start_x = 100
            start_y = 570
            end_x = 800
            end_y = 900
            rand_loc= (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_line_coordinates_ss.append(rand_loc) # Add the random locations to a list so we can use them

    def piece_drop_bs (dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to
        global finished_pieces_bs
        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to
            finished_pieces_bs += 1
            if finished_pieces_bs == page_pieces_bs:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("bubble_sort_complete")
    
    def piece_drop_is (dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to
        global finished_pieces_is
        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to
            finished_pieces_is += 1
            if finished_pieces_is == page_pieces_is:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("insertion_sort_complete")
    
    def piece_drop_ss (dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to
        global finished_pieces_ss
        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to
            finished_pieces_ss += 1
            if finished_pieces_ss == page_pieces_ss:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("selection_sort_complete")
