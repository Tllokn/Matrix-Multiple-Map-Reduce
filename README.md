## Exp Group Matrix Mult

### How to run

Generate Matrix with size 100 (replaceable)

```shell
python GenerateMatrix.py 100
```

Run different shell scripts I provided to test different comparisons 

1.group size: `run_one_pass.sh` , `run_two_pass.sh`

2.number core instance: `num_core.sh`

3.instance type: `instance_type.sh`



## Exp: Time Analysis

### 1.Group Size 

I run the One-Pass and Two-Pass algorithm with group process with different group size.

The matrix size is always $100\times 100$, Core Instance Num:4, Instance Type: n1-standard-1

the group-size/band-width is 1,2,4,5,10,20,50

#### One-Pass

| Group Size | Running Time(s) |
| :--------: | :-------------: |
|     1      |       100       |
|     2      |       94        |
|     4      |       100       |
|     5      |       91        |
|     10     |       98        |
|     20     |       93        |
|     50     |       94        |

#### Two-Pass

| Group Size | Running Time(s) step1+step2 |
| :--------: | :-------------------------: |
|     1      |            87+90            |
|     2      |            86+91            |
|     4      |            87+91            |
|     5      |            87+91            |
|     10     |            85+89            |
|     20     |            91+90            |
|     50     |            97+98            |

### 2.Core Inatance Number

For this experiment I tried with one-pass algorithm, with matrix size $100\times 100$, group size=5, Instance Type: n1-standard-1

| Core Instance | Running Time(s) step1+step2 |
| :-----------: | :-------------------------: |
|       2       |             90              |
|       4       |             95              |
|       6       |             92              |
|       8       |     out of memory error     |
|      10       |     out of memory error     |

 - Insufficient 'DISKS_TOTAL_GB' quota. Requested 4500.0, available 4096.0.
 - Insufficient 'IN_USE_ADDRESSES' quota. Requested 9.0, available 8.0.

### 3.Instance Type

For this experiment I tried with one-pass algorithm, with matrix size $100\times 100$, group size=5, core instance number=4.

| Instance type  | Running Time(s) step1+step2 |
| :------------: | :-------------------------: |
| n1-standard-1  |             108             |
| t2d-standard-2 |             50              |
| t2d-standard-4 |             50              |
|  n1-highcpu-8  |     out of memory error     |
|    e2-micro    |     out of memory error     |

for n1-highcpu-8:

 - Insufficient 'CPUS' quota. Requested 33.0, available 24.0.
 - Insufficient 'CPUS_ALL_REGIONS' quota. Requested 33.0, available 32.0. 

for e2-micor

- 400 Machine type 'e2-micro' does not have enough memory. Minimum memory required is 3584 MB.







