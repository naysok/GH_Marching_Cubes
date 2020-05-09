class Util():


    def point3d_to_point2d(self, p_3d_list):

        p_2d_list = []

        for i in xrange(len(p_3d_list)):
            p_3d = p_3d_list[i]
            p_2d = [p_3d[0], p_3d[1]]
            p_2d_list.append(p_2d)

        return p_2d_list