for core in 2 4 6 8 10
do
  python GroupMMOnePass.py -r dataproc --num-core-instance $core --instance-type n1-standard-1 tmp/MA.txt tmp/MB.txt --size 100 --group 5
done
