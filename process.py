log_file = open("um-server-01.txt") # Opens the file "um-server-01.txt" when the variable "log_file" is called


def sales_reports(log_file): #Begins defining the function "sales_reports" that takes in the parameter "log_file"
    for line in log_file: # Begins a for loop so that a thing happens for each line in log_file
        line = line.rstrip() #Removes any trailing spaces at the end of each line
        day = line[0:3] # Sets the variable "day" as the first 4 charaters of each line
        if day == "Mon": # Begins defining an operation to take place if the variable "day" matches the value "Mon"
            print(line) # Tells Python to display the above-defined "line" variable if the conditions on line 8 are met


sales_reports(log_file) # Calls the sales_reports function for the log_file parameter (does all the stuff mentioned abovegit)
