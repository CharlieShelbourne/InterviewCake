class WordReversal(object):
    """
    Reverses the order strings in a list, in place in O(n) time and O(1) memory 
    
    Methods
    -----------
    Public: 
    word_reversal

    Private:
    string_reversal

    """

    def word_reversal(self, message: list):
        if ' ' not in message:
            return
        
        self._string_reversial(message, 0, len(message)-1)

        start_ind = 0
        for i, char in enumerate(message):
            if char == " ":
                self._string_reversial(message, start_ind, i-1)
                start_ind = i+1
            self._string_reversial(message, start_ind, len(message)-1)
    
    @staticmethod
    def _string_reversial(string : list, start : int, end : int): # function is inplace
        """reverses list of list of strings (chars). Uses O(1) memory and O(n) time"""
        if len(string) < 2:
            return

        while end > start:
            string[start],  string[end] = string[end], string[start]
            start += 1
            end -=1



message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
word_reversal(message)
print(message)
