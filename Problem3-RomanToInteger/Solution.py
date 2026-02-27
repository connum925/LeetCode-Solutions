class Solution(object):
    def romanToInt(self, s):
        """
        Automaton Turing maching SPECIFIC STATES
        q0 -> (I:1),(V:5),(X:6),(L:9),(C:10),(D:13),(M:14)
        1 -> (V:2),(X:3),(I:4),(any:SUM 1)
        2 -> SUM 4
        3 -> SUM 9
        4 -> SUM 1
        5 -> SUM 5
        6 -> (L:7),(C:8),(ANY:SUM 10)
        7 -> SUM 40
        8 -> SUM 90
        9 -> SUM 50
        10 -> (D:11),(M:12),(ANY:SUM 100)
        11 -> SUM 400
        12 -> SUM 900
        13 -> SUM 500
        14 -> SUM 1000
        15 -> SUM 2


        Automaton Turing maching
        q0 -> I,V,X,L,C,D,M
        I -> V,X,qf
        V -> qf
        X -> L,C,qf
        L -> qf
        C -> D,M,qf
        D -> qf
        M -> qf
        :type s: str
        :rtype: int
        """
        # Initialize automaton state and result accumulator
        state = 0
        result = 0
        
        # Process each roman numeral character
        for letter in s:
            state, result = self.process_letter(letter, state, result)
        
        # Handle pending values at end of string
        if state == 1:
            result += 1  # Unprocessed 'I'
        elif state == 6:
            result += 10  # Unprocessed 'X'
        elif state == 10:
            result += 100  # Unprocessed 'C'
        return result
        
    def process_letter(self, letter, state, result):
        # State 0: Initial state, process new character
        if state == 0:
            if letter == "I":
                return 1, result  # Wait for possible IV or IX
            elif letter == "V":
                return 0, result + 5
            elif letter == "X":
                return 6, result  # Wait for possible XL or XC
            elif letter == "L":
                return 0, result + 50
            elif letter == "C":
                return 10, result  # Wait for possible CD or CM
            elif letter == "D":
                return 0, result + 500
            elif letter == "M":
                return 0, result + 1000

        # State 1: Previous character was 'I'
        if state == 1:
            if letter == "V":
                return 0, result + 4  # IV = 4
            elif letter == "X":
                return 0, result + 9  # IX = 9
            elif letter == "I":
                return 1, result + 1  # Consecutive 'I'
            else:
                result += 1  # Add pending 'I' and reprocess
                return process_letter(letter, 0, result)
        
        # State 6: Previous character was 'X'
        elif state == 6:
            if letter == "L":
                return 0, result + 40  # XL = 40
            elif letter == "C":
                return 0, result + 90  # XC = 90
            elif letter == "X":
                return 6, result + 10  # Consecutive 'X'
            else:
                result += 10  # Add pending 'X' and reprocess
                return process_letter(letter, 0, result)
        
        # State 10: Previous character was 'C'
        elif state == 10:
            if letter == "D":
                return 0, result + 400  # CD = 400
            elif letter == "M":
                return 0, result + 900  # CM = 900
            elif letter == "C":
                return 10, result + 100  # Consecutive 'C'
            else:
                result += 100  # Add pending 'C' and reprocess
                return process_letter(letter, 0, result)
        
        return state, result