'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in (social_graph[from_member])["following"] and from_member in (social_graph[to_member])["following"]:
        relationship_status = "friends"
    elif to_member in (social_graph[from_member])["following"]:
        relationship_status = "follower"
    elif from_member in (social_graph[to_member])["following"]:
        relationship_status = "followed by"
    else:
        relationship_status = "no relationship"
    return relationship_status

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for column in range(len(board)):
        if column+2 <= len(board)-1:
            for row in range(len(board)):
                if (board[row])[column] == (board[row])[column+1] == (board[row])[column+2] != "": 
                    result = (board[row])[column]
                    break
                else:
                    result = "NO WINNER"

    if result == "NO WINNER":              
        for row in range(len(board)):
            if row+2 <= len(board)-1:
                for column in range(len(board)):
                    if (board[row])[column] == (board[row+1])[column] == (board[row+2])[column] != "": 
                        result = (board[row])[column]
                        break
                    else:
                        result = "NO WINNER"
                        
    if result == "NO WINNER":
        for column in range(len(board)):
            if column+2 <= len(board)-1 and row+2 <= len(board)-1:
                for row in range(len(board)):
                    if (board[row])[column] == (board[row+1])[column+1] == (board[row+2])[column+2] != "":
                        result = (board[row])[column]
        
            elif ((column <= len(board)-1) and (column-2 >= 0)) and row+2 <= len(board)-1:
                for row in range(len(board)):
                    if (board[row])[column] == (board[row+1])[column-1] == (board[row+2])[column-2] != "":
                        result = (board[row])[column]
        
            elif column+2 <= len(board)-1 and ((row <= len(board)-1) and (row-2 >= 0)):
                for row in range(len(board)):
                    if (board[row])[column] == (board[row-1])[column+1] == (board[row-2])[column+2] != "":
                        result = (board[row])[column]
        
            elif ((column <= len(board)-1) and (column-2 >= 0)) and ((row <= len(board)-1) and (row-2 >= 0)):
                for row in range(len(board)):
                    if (board[row])[column] == (board[row-1])[column-1] == (board[row-2])[column-2] != "":
                        result = (board[row])[column]
        
            else:
                result = "NO WINNER"
    return result

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circular route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    total_time = 0
    current_stop = first_stop

    while True:
        for (start, end), data in route_map.items():
            if start == current_stop:
                total_time = total_time + data['travel_time_mins']
                current_stop = end
                if current_stop == second_stop:
                    return total_time
                break