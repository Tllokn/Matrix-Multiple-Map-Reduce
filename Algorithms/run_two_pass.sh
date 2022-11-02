for group in 1 2 4 5 10 20 50
do
  python GroupMMTwoPass.py -r dataproc --num-core-instance 4 --instance-type n1-standard-1 tmp/MA.txt tmp/MB.txt --size 100 --group $group
done
