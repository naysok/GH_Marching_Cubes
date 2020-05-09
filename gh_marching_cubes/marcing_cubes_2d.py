import util, transform
ut = util.Util()
tr = transform.Transform()


class Marching_Cubes_2d():


    def check_threshold(self, pts4, threshold):

        pts4_tf = []
        count = 0

        for i in range(4):

            if pts4[i] < threshold:
                pts4_tf.append(0)
            else:
                pts4_tf.append(1)
                count += 1

        return pts4_tf, count


    def line_one(self, p0, p1, p3):

        vector_s = tr.vector_amp(tr.vector_2pt(p0, p1), 0.5)
        vector_e = tr.vector_amp(tr.vector_2pt(p0, p3), 0.5)

        point_s = tr.point_move(p0, vector_s)
        point_e = tr.point_move(p0, vector_e)

        return [point_s, point_e]


    def line_two_neighboring(self, p0, p1, p2, p3):

        vector_s = tr.vector_amp(tr.vector_2pt(p1, p2), 0.5)
        vector_e = tr.vector_amp(tr.vector_2pt(p0, p3), 0.5)

        point_s = tr.point_move(p1, vector_s)
        point_e = tr.point_move(p0, vector_e)

        return [point_s, point_e]


    def line_two_not_neighboring_a(self, p0, p1, p2, p3):

        line = []

        line.append(self.line_one(p0, p2, p1))
        line.append(self.line_one(p3, p1, p2))

        return line


    def line_two_not_neighboring_b(self, p0, p1, p2, p3):

        line = []

        line.append(self.line_one(p1, p0, p3))
        line.append(self.line_one(p2, p3, p0))

        return line


    def line_three(self, p0, p1, p3):

        vector_s = tr.vector_amp(tr.vector_2pt(p0, p3), 0.5)
        vector_e = tr.vector_amp(tr.vector_2pt(p0, p1), 0.5)

        point_s = tr.point_move(p0, vector_s)
        point_e = tr.point_move(p0, vector_e)

        return [point_s, point_e] 


    def calc_one(self, pts4, thr4):

        ### calc cell
        if thr4 == [1, 0, 0, 0]:
            return self.line_one(pts4[0], pts4[2], pts4[1])
        elif thr4 == [0, 0, 1, 0]:
            return self.line_one(pts4[2], pts4[3], pts4[0])
        elif thr4 == [0, 0, 0, 1]:
            return self.line_one(pts4[3], pts4[1], pts4[2])
        elif thr4 == [0, 1, 0, 0]:
            return self.line_one(pts4[1], pts4[0], pts4[3])


    def calc_two(self, pts4, thr4):

        ### calc cell
        if thr4 == [1, 0, 1, 0]:
            return self.line_two_neighboring(pts4[0], pts4[2], pts4[3], pts4[1])
        elif thr4 == [0, 0, 1, 1]:
            return self.line_two_neighboring(pts4[2], pts4[3], pts4[1], pts4[0])
        elif thr4 == [0, 1, 0, 1]:
            return self.line_two_neighboring(pts4[3], pts4[1], pts4[0], pts4[2])
        elif thr4 == [1, 1, 0, 0]:
            return self.line_two_neighboring(pts4[1], pts4[0], pts4[2], pts4[3])
        elif thr4 == [1, 0, 0, 1]:
            return self.line_two_not_neighboring_a(pts4[0], pts4[1], pts4[2], pts4[3])
        elif thr4 == [0, 1, 1, 0]:
            return self.line_two_not_neighboring_b(pts4[0], pts4[1], pts4[2], pts4[3])


    def calc_three(self, pts4, thr4):

        ### calc cell
        if thr4 == [1, 0, 1, 1]:
            return self.line_three(pts4[1], pts4[0], pts4[3])
        elif thr4 == [0, 1, 1, 1]:
            return self.line_three(pts4[0], pts4[2], pts4[1])
        elif thr4 == [1, 1, 0, 1]:
            return self.line_three(pts4[2], pts4[3], pts4[0])
        elif thr4 == [1, 1, 1, 0]:
            return self.line_three(pts4[3], pts4[1], pts4[2])


    def calc_marcing_cubes(self, pts4, thr4, threshold):

        """
        01
        23
        """
        
        ### Threshold
        thr4_tf, count = self.check_threshold(thr4, threshold)
        # print(thr4_tf)
        # print("count : {}".format(count))

        ### Calc
        result = []

        if count == 1:
            result.append(self.calc_one(pts4, thr4_tf))
        elif count == 2:
            l = self.calc_two(pts4, thr4_tf)
            if len(l[0]) == 2: 
                result.append(l[0])
                result.append(l[1])
            else:
                result.append(l)
        elif count == 3:
            result.append(self.calc_three(pts4, thr4_tf))

        return result

