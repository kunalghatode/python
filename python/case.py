color = input("Enter color : ")
match color:
    case 'red' | 'RED':
        print("RED")
    case 'blue':
        print("BLUE")
    case _:
        print("Invalid color")

