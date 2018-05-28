class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        def gen_words():
            rv = []
            num_chars = 0
            for w in words:
                if rv and len(rv) - 1 + num_chars + 1 + len(w) > maxWidth:
                    yield num_chars, rv, False
                    rv.clear()
                    num_chars = 0
                rv.append(w)
                num_chars += len(w)
            yield num_chars, rv, True

        rv = []
        for count, ws, is_last in gen_words():
            if not is_last:
                spaces_num = maxWidth - count
                space_width = spaces_num // ((len(ws) - 1) or 1)
                extra_spaces = spaces_num % ((len(ws) - 1) or 1)
                tmp = []
                for i in range(1, len(ws)):
                    width = space_width + 1 if i <= extra_spaces else space_width
                    word_string = ws[i - 1] + ' ' * width
                    tmp.append(word_string)
                tmp.append(ws[-1])
                if (len(ws) == 1):
                    tmp.append(' ' * space_width)
                rv.append(''.join(tmp))
            else:
                row_string = ' '.join(ws)
                rv.append(row_string + ' ' * (maxWidth - len(row_string)))

        return rv
