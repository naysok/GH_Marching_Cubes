class Transform():


    def vector_2pt(self, pt_start, pt_end):
        vx = pt_end[0] - pt_start[0]
        vy = pt_end[1] - pt_start[1]
        
        ### Point 3d
        if len(pt_start) == 3:
            vz = pt_end[2] - pt_start[2]
            return [vx, vy, vz]

        ### Point 2d
        else:
            return [vx, vy]


    def vector_amp(self, vector, amp_value):
        vx = vector[0] * amp_value
        vy = vector[1] * amp_value
        
        ### Vector 3d
        if len(vector) == 3:
            vz = vector[2] * amp_value
            return [vx, vy, vz]

        ### Vector 2d
        else:
            return [vx, vy]


    def point_move(self, point, vector):

        px = point[0] + vector[0]
        py = point[1] + vector[1]
        
        ### Calc 3d
        if len(point) == 3:
            pz = point[2] + vector[2]
            return [px, py, pz]

        ### Calc 2d
        else:
            return [px, py]