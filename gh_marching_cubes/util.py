import math


class Util():


    def print_matrix_info(self, mat):
        return ("{} x {}".format(len(mat), len(mat[0])))


    def split_list(self, l, n):

        # https://www.python.ambitious-engineer.com/archives/1843
        # http://y0m0r.hateblo.jp/entry/20140405/1396674065 
        for idx in range(0, len(l), n):
            yield l[idx:idx + n]


    def zip_matrix(self, mat):

        ### https://note.nkmk.me/python-list-transpose/
        return [list(x) for x in zip(*mat)]


    def flatten_array(self, array_):
        
        elms = []
        
        for i in xrange(len(array_)):
            sub = array_[i]
            for j in xrange(len(sub)):
                elms.append(sub[j])

        return elms


    def un_flatten_array(self, list_):

        num = int(math.sqrt(len(list_)))
        # print("sqrt : {}".format(num))

        array_2d = list(self.split_list(list_, num))
        # print("i_count : {}".format(len(array_2d)))
        # print("j_count : {}".format(len(array_2d[0])))

        return array_2d


    def point3d_to_point2d(self, p_3d_list):

        p_2d_list = []

        for i in xrange(len(p_3d_list)):
            p_3d = p_3d_list[i]
            p_2d = [p_3d[0], p_3d[1]]
            p_2d_list.append(p_2d)

        return p_2d_list


    def gen_array_2d(self, count):

        pts = []
        step = 1.0 / (count-1)

        for i in xrange(count):
            sub = []
            for j in xrange(count):
                sub.append([j * step, i* step, 0])
            pts.append(sub)
        
        return pts


    def sum_elements_array(self, array_):

        array_flip = self.zip_matrix(array_)
        
        result = []
        for i in xrange(len(array_flip)):
            result.append(sum(array_flip[i]))

        return result