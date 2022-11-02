from mrjob.job import MRJob
from mrjob.job import MRStep
import os


class  GroupMatrixMultTwoPass(MRJob):
    def configure_args(self):
        super( GroupMatrixMultTwoPass, self).configure_args()
        self.add_passthru_arg('--size', type=int, default=12, help="matrix size")
        self.add_passthru_arg('--group', type=int, default=4, help="group number")

    def mapper1(self, _, line):
        i, j, val = line.split()
        row = int(i)
        col = int(j)
        val = int(val)
        n = self.options.size
        band = self.options.group

        file_name = os.environ['map_input_file']

        if 'A' in file_name:
            yield int(col / band), ('A', row, col, val)

        if 'B' in file_name:
            yield int(row / band), ('B', row, col, val)

    def reducer1(self, j, values):
        listA = []
        listB = []
        for val in values:
            if val[0] == 'A':
                listA.append(val)
            if val[0] == 'B':
                listB.append(val)

        for itemA in listA:
            for itemB in listB:
                if itemA[2] == itemB[1]:
                    yield (itemA[1], itemB[2]), int(itemA[3] * itemB[3])

    def mapper2(self, j, value):
        yield j, value

    def reducer2(self, key, value):
        yield key, sum(value)

    def steps(self):
        return [
            MRStep(mapper=self.mapper1,
                   reducer=self.reducer1),
            MRStep(mapper=self.mapper2,
                   reducer=self.reducer2),
        ]


if __name__ == '__main__':
     GroupMatrixMultTwoPass.run()
