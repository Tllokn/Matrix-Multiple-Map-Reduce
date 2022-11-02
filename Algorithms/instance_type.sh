python GroupMMOnePass.py -r dataproc --num-core-instance 4 --instance-type n1-standard-1 tmp/MA.txt tmp/MB.txt --size 100 --group 5
python GroupMMOnePass.py -r dataproc --num-core-instance 4 --instance-type t2d-standard-2 tmp/MA.txt tmp/MB.txt --size 100 --group 5
python GroupMMOnePass.py -r dataproc --num-core-instance 4 --instance-type t2d-standard-4 tmp/MA.txt tmp/MB.txt --size 100 --group 5
python GroupMMOnePass.py -r dataproc --num-core-instance 4 --instance-type n1-highcpu-8 tmp/MA.txt tmp/MB.txt --size 100 --group 5
python GroupMMOnePass.py -r dataproc --num-core-instance 4 --instance-type e2-micro tmp/MA.txt tmp/MB.txt --size 100 --group 5
