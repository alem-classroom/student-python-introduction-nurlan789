def size_of_str(str):
    # return size of string
    return len(str)


def concat_strings(first, second):
    # return concatination of first and second strings
    return first+second

def duplicate_string(str, copy):
    # return new string which is copy of str copy times
    # example -> duplicate_string('s', 2) == 'ss'
    s = str*copy
    return s

def reverse(str):
    # return reverse of the string
    return str[::-1]

def is_substring(str, substr):
    # return true if substr is the substring of str, false otherwise
    if(substr in str):
        return "true"
    else:
        return "false"
