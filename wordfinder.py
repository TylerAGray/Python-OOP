import random

class WordFinder:
    """Class to find random words from a list of words read from a file."""
    
    def __init__(self, filepath):
        """
        Initialize the WordFinder with the path to the file containing words.
        
        >>> wf = WordFinder("words.txt")
        235887 words read
        """
        # Load words from the file and store them in the instance
        self.words = self.load_words(filepath)
        # Print the number of words read
        print(f"{len(self.words)} words read")

    def load_words(self, filepath):
        """Load words from a file and return a list of words."""
        # Read the file and return a list of non-empty, stripped lines
        with open(filepath) as file:
            return [line.strip() for line in file if line.strip()]

    def random(self):
        """
        Return a random word from the list of words.
        
        Note: Since the output is random, we cannot predict it. 
        However, we can check that the returned word is in the list.
        
        >>> wf = WordFinder("words.txt")
        235887 words read
        >>> word = wf.random()
        >>> word in wf.words
        True
        """
        # Return a randomly chosen word from the list of words
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("words.txt")
    235887 words read

    >>> word = swf.random()
    >>> word in swf.words
    True

    >>> word = swf.random()
    >>> word in swf.words
    True

    >>> word = swf.random()
    >>> word in swf.words
    True
    """
    
    def load_words(self, filepath):
        """Load words from a file, ignoring blank lines and comments."""
        # Read the file and return a list of non-empty, non-comment, stripped lines
        with open(filepath) as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]

    def random(self):
        """
        Return a random word from the list of words, ensuring each word is unique.
        
        This overrides the parent method to ensure words are not repeated until all
        words have been used once.
        
        >>> swf = SpecialWordFinder("words.txt")
        235887 words read
        >>> word = swf.random()
        >>> word in swf.words
        True
        >>> word = swf.random()
        >>> word in swf.words
        True
        >>> word = swf.random()
        >>> word in swf.words
        True
        """
        # Initialize a set to track used words if it doesn't exist
        if not hasattr(self, "_used_words"):
            self._used_words = set()
        
        # Reset the used words set if all words have been used
        if len(self._used_words) == len(self.words):
            self._used_words = set()
        
        # Choose a random word that hasn't been used yet
        word = random.choice(self.words)
        while word in self._used_words:
            word = random.choice(self.words)
        
        # Add the word to the set of used words and return it
        self._used_words.add(word)
        return word
