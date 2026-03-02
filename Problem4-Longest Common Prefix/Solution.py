def recorrer_por_posicion(strs):
    # Find the length of the shortest string
    # Handle empty input
    if not strs:
        return ""
    
    # Find shortest string length to avoid index out of bounds
    min_length = min(len(s) for s in strs)
    List = []
    result = ""
    
    # Check each character position across all strings
    for i in range(min_length):
        count = 0
        for string in strs:
            if count == 0:
                # Store first string's character as reference
                List.append(string[i])
                count += 1
            else:
                # Compare current character with reference
                if string[i] != (List[-1]):
                    # Mismatch found, remove reference and exit loop
                    List.pop()
                    break
        
        # If character matched across all strings, add to result
        if List:
            result += List.pop()
        else:
            # No more common characters, return current result
            return result
    
    return result

# Example
strs = ["carnaval","caro","cara"]
recorrer_por_posicion(strs)