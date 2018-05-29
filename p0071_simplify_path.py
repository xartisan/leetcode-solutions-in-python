class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dir_names = []

        cur_dir_name = ''
        for c in path:
            if not c == '/':
                cur_dir_name += c
                continue
            if not cur_dir_name:
                continue
            if cur_dir_name == '..':
                if dir_names:
                    dir_names.pop()
            elif cur_dir_name != '.':
                dir_names.append(cur_dir_name)
            cur_dir_name = ''
        if cur_dir_name:
            if cur_dir_name == '..':
                if dir_names:
                    dir_names.pop()
            elif cur_dir_name != '.':
                dir_names.append(cur_dir_name)
        return '/' + '/'.join(dir_names)
