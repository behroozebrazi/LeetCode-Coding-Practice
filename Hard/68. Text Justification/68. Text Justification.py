# https://leetcode.com/problems/text-justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        oneRowWords = []
        oneRowWordsLength = 0

        for word in words:
            # Create a row
            if  oneRowWordsLength + len(word) + len(oneRowWords) > maxWidth:
                totalSpaceLength = maxWidth - oneRowWordsLength
                numberOfDistances = len(oneRowWords) - 1

                # Add space between the words
                oneRow = ""
                while numberOfDistances > 0:
                    space = floor(totalSpaceLength / numberOfDistances)
                    oneRow = ' ' * space + oneRowWords[numberOfDistances] + oneRow
                    totalSpaceLength -= space
                    numberOfDistances -= 1

                # Add the first (last) word to the row; reset and update values
                oneRow = oneRowWords[0] + oneRow
                oneRowWordsLength = 0
                oneRowWords = []
                result.append(oneRow + ' ' * (maxWidth - len(oneRow)))

            oneRowWords.append(word)
            oneRowWordsLength += len(word)

        if oneRowWords:
            lastRow = " ".join(oneRowWords) + ' ' * (maxWidth - oneRowWordsLength - len(oneRowWords) + 1)
            result.append(lastRow)

        return result