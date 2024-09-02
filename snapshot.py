import copy
steps = []
length = 0


class snapshot:
    def __init__(self, init, size, color_count, dad=None):
        self.init = init
        self.dad = dad
        self.childs = []
        self.size = size
        self.color_count = color_count
        self.weight = self.calc_weight()

        self.is_winner()

        if self.dad is None:
            self.create_childs()
            self.choose()

    def create_childs(self):
        current = copy.deepcopy(self.init)
        for i in range(len(current)):
            has_empty = False
            if len(current[i]) > 0 and (len(set(current[i])) != 1 or self.recognize_tube_with_the_same_color(i, current[i][0])):
                for j in range(len(current)):
                    if len(current[j]) != 0 or has_empty == False:
                        self.forward(current, i, j)
                        if self.init != current:
                            new_child = snapshot(current, self.size, self.color_count, dad=self)
                            self.childs.append(new_child)
                            current = copy.deepcopy(self.init)
                    if len(current[j]) == 0 and has_empty == False:
                        has_empty = True

    def forward(self, current, i, j):
        if current[i] != current[j] and \
                len(current[j]) < self.size and \
                len(current[i]) > 0 and \
                (len(current[j]) == 0 or current[i][0] == current[j][0]) and \
                self.count_same(current[i]) <= self.size - len(current[j]):
            temp = current[i].pop(0)
            current[j].insert(0, temp)
            self.forward(current, i, j)

    def recognize_tube_with_the_same_color(self,i, color):
        for tube in self.init:
            if tube is not self.init[i] and len(tube) > 0 and len(set(tube)) == 1 and tube[0] == color:
                return True

    def count_same(self, tube):
        count = 0
        for value in tube:
            if value != tube[0]:
                return count
            else:
                count += 1
        return count

    def choose(self):
        if len(self.childs) == 0:
            return
        self.childs.sort(key=lambda child: child.weight, reverse=True)
        for child in self.childs:
            if child.init not in steps:
                global length
                length += 1
                steps.append(child.init)
                child.create_childs()
                child.choose()
                steps.remove(child.init)


    def calc_weight(self):
        one_color = []
        bottom = set()
        count = 0
        for i in range(len(self.init)):
            if len(self.init[i]) > 0:
                bottom.add(self.init[i][len(self.init[i]) - 1]) # calc how much different bottoms colors
                if len(set(self.init[i])) == 1: # just one color
                    if self.init[i][0] in one_color and 0 <= len(set(self.dad.init[i])) <= 1:
                        return -1 # split one color to 2 tubes is bad idea
                    else:
                        one_color.append(self.init[i][0])

                    count += 3**len(self.init[i])

                    tube_color = self.init[i][0]
                    for tube in self.init: # add one for this color oon the top of other tubes
                        if len(tube) != 0 and tube is not self.init[i] and tube[0] == tube_color:
                            count += 1


                else: # more than one color
                    for j in range(1,len(self.init[i])):
                        if self.init[i][j] == self.init[i][0]:
                            count += 1
                        else:
                            break

        count += len(bottom)

        return count



    def is_winner(self):
        for tube in self.init:
            if len(set(tube)) > 1 or 0 < len(tube) < self.size:
                return
        steps.append(self.init)
        print("Winner!!")
        exit(0)
