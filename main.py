from time import sleep 

 
def main():
    seconds = 0
    minutes = 0
    hours = 0
 
    lines = ["|", "/", "—", "\\", "|"]
    line_index = 0

    while True:
        # To clear the terminal.
        print("\033c")
        # Print time and a cool line to show progress.
        print(
                f"Total time: {hours:02d}:{minutes:02d}:{seconds:02d} {lines[line_index]}")
        seconds += 1
        # This will add 1 to line index to update the line.
        line_index += 1
        
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1

        if line_index == 4:
            line_index = 0

        sleep(1)

                                                                                                       
main() 
