# config

class Standards:
    """
    bound is on the number's left. so, range between bounds like this:
    bound0 <= range < bound1
    """
    outer_bound = 12
    inner_bound = (4, 8)
    thick_len = 4
    thin_len = 4
    distance_matrix = ((8, 7, 6, 5, 4, 4, 4, 4, 5, 6, 7, 8),
                       (7, 6, 5, 4, 3, 3, 3, 3, 4, 5, 6, 7),
                       (6, 5, 4, 3, 2, 2, 2, 2, 3, 4, 5, 6),
                       (5, 4, 3, 4, 1, 1, 1, 1, 4, 3, 4, 5),
                       (4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4),
                       (4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4),
                       (4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4),
                       (4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4),
                       (5, 4, 3, 4, 1, 1, 1, 1, 4, 3, 4, 5),
                       (6, 5, 4, 3, 2, 2, 2, 2, 3, 4, 5, 6),
                       (7, 6, 5, 4, 3, 3, 3, 3, 4, 5, 6, 7),
                       (8, 7, 6, 5, 4, 4, 4, 4, 5, 6, 7, 8))

    def set_wild(self):
        self.outer_bound = 14
        self.inner_bound = (5, 9)
        self.thick_len = 6
        self.thin_len = 6
        self.distance_matrix = ((10, 9, 8, 7, 6, 5, 5, 5, 5, 6, 7, 8, 9, 10),
                                (9, 8, 7, 6, 5, 4, 4, 4, 4, 5, 6, 7, 8, 9),
                                (8, 7, 6, 5, 4, 3, 3, 3, 3, 4, 5, 6, 7, 8),
                                (7, 6, 5, 4, 3, 2, 2, 2, 2, 3, 4, 5, 6, 7),
                                (6, 5, 4, 3, 4, 1, 1, 1, 1, 4, 3, 4, 5, 6),
                                (5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4, 5),
                                (5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4, 5),
                                (5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4, 5),
                                (5, 4, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 4, 5),
                                (6, 5, 4, 3, 4, 1, 1, 1, 1, 4, 3, 4, 5, 6),
                                (7, 6, 5, 4, 3, 2, 2, 2, 2, 3, 4, 5, 6, 7),
                                (8, 7, 6, 5, 4, 3, 3, 3, 3, 4, 5, 6, 7, 8),
                                (9, 8, 7, 6, 5, 4, 4, 4, 4, 5, 6, 7, 8, 9),
                                (10, 9, 8, 7, 6, 5, 5, 5, 5, 6, 7, 8, 9, 10))


standards = Standards()
