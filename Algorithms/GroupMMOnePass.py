from mrjob.job import MRJob
import os
# import time


class GroupMatrixMultOnePass(MRJob):
    def configure_args(self):
        super(GroupMatrixMultOnePass, self).configure_args()
        self.add_passthru_arg('--size', type=int, default=12, help="matrix size")
        self.add_passthru_arg('--group', type=int, default=4, help="group number")

    def mapper(self, _, line):
        row, col, val = line.split()
        row = int(row)
        col = int(col)
        val = int(val)
        n = self.options.size
        band = self.options.group

        file_name = os.environ['map_input_file']

        if 'A' in file_name:
            for k in range(int(n / band)):
                yield (int(row / band), k), ('A', row, col, val)

        if 'B' in file_name:
            for k in range(int(n / band)):
                yield (k, int(col / band)), ('B', row, col, val)

    def reducer(self, key, values):
        '''
        KEY: block num(a_block, b_block)
        VALUE: [('A' or 'B', row, col, value), ..., (...)] // numbers in the block
        '''
        n = self.options.size
        band = self.options.group
        # load block number
        a_block, b_block = key[0], key[1]
        # the range of index which involving calculation
        min_i = band * a_block
        max_i = min(band * (1 + a_block) - 1, n)
        min_k = band * b_block
        max_k = min(band * (1 + b_block) - 1, n)

        a_value = {}
        b_value = {}
        for val in values:
            if val[0] == 'A':
                dict_key=str(val[1])+","+str(val[2])
                a_value[dict_key] = val[3]
            if val[0] == 'B':
                dict_key = str(val[1]) + "," + str(val[2])
                b_value[dict_key] = val[3]

        # compute/output result
        for i1 in range(max_i - min_i + 1):
            for k1 in range(max_k - min_k + 1):
                i = min_i + i1
                k = min_k + k1
                current_res = 0
                for j in range(n):
                    a_dict_key = str(i) + "," + str(j)
                    b_dict_key = str(j) + "," + str(k)
                    if a_dict_key in a_value.keys() and b_dict_key in b_value.keys():
                        current_res += a_value[a_dict_key] * b_value[b_dict_key]
                yield (i, k), current_res


if __name__ == '__main__':
    # start = time.time()
    GroupMatrixMultOnePass.run()
    # end = time.time()
    # print("Running Time:", start-end)
