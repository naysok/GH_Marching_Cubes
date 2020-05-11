import util
ut = util.Util()

import Rhino.Geometry as rg


class Geometry():


    def point3d_to_xy(self, point_3d_list):

        pts = []

        for i in xrange(len(point_3d_list)):
            # print(point_3d_list[i])
            p = point_3d_list[i]
            pp = [p[0], p[1]]
            pts.append(pp)
        
        return pts


    def draw_line(self, line_pts):
        
        ps = line_pts[0]
        pe = line_pts[1]
        p_start = rg.Point3d(ps[0], ps[1], ps[2])
        p_end = rg.Point3d(pe[0], pe[1], pe[2])
       
        return rg.Line(p_start, p_end)


    def draw_lines(self, lines_pts):
        
        lines = []
        
        for i in xrange(len(lines_pts)):
            pts = lines_pts[i]
            lines.append(self.draw_line(pts))
        
        return lines