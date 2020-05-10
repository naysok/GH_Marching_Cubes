import math
import util

ut = util.Util()


class Metaball_2d():

    
    def calc_value(self, pt, center, volume, amp):
        
        ### Calc Metaball
        xx = math.pow((center[0] - pt[0]), 2)
        yy = math.pow((center[1] - pt[1]), 2)

        return float(volume * math.exp(-1 * amp * (xx + yy)))


    def calc_grid(self, grid_list, center, volume, amp):
        
        values = []
        
        for i in xrange(len(grid_list)):
            p = grid_list[i]
            values.append(self.calc_value(p, center, volume, amp))
        
        return values


    def calc_grids(self, grid, centers, volumes, amp):

        ### Flatten Array (Array 2d >> Array 1d)
        list_grid = ut.flatten_array(grid)

        ### Calc Values
        grid_calc = []

        for i in xrange(len(centers)):
            c = centers[i]
            v = volumes[i]
            r = self.calc_grid(list_grid, c, v, amp)
            grid_calc.append(r)

        ### Blend
        grid_blended = ut.sum_elements_array(grid_calc)

        ### Unflatten Array (Array 1d >> Array 2d)
        v_grid = ut.un_flatten_array(grid_blended)

        return v_grid