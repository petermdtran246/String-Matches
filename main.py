# Define function
def matches(str1, str2):
    # Initialize the match_count
    match_count = 0

    # Determine the length of shorter string
    min_length = min(len(str1),len(str2))

    # Iterate to the length of the shorter string
    for i in range(min_length):
        if str1[i] == str2[i]:
            match_count += 1
    return match_count

str1 = input('Enter your 1st word: ').lower()
str2 = input('Enter your 2nd word: ').lower()

# Call the function
print('Number of string matches:', matches(str1, str2))


