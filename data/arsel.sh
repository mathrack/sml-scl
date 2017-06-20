#!/bin/bash -
set -e
module load gcc/4.9.0
#
ind=0
for i in {1..7} # T1 ... T6 Ux
do
   for j in {11..28} # f f**2 f**3 f**4 dfdz 6-components-diss(xx-yy-zz-xy-xz-yz) 6-domponents-variance-dissipation(x4-y4-z4-x2y2-x2z2-y2z2) dissipation-correlation
   do
      ind=`expr $ind + 1`;
      file[ind]='fort.'${i}'1'${j};
   done
done
#
echo "Processing files with arsel"
#
for j in "${file[@]}"
do
  echo "   - files ${j}"
  touch mean sig t0;
  for i in {1..181}
  do
    awk -v i=$i '{ print $i}' ../${j} | /home/r4/flageul/dns_iztok/ar/arsel --subtract-mean > tmp;
    more tmp | head -n8 | tail -n1 | cut -c12- >> mean;
    more tmp | head -n9 | tail -n1 | cut -c12- >> sig;
    more tmp | head -n15 | tail -n1 | cut -c12- >> t0;
  done
  paste yy mean sig t0 > ${j}.stat
  rm mean sig t0 tmp
done
#
echo "   - fort.44";
for i in {3..6}
do
  touch mean sig t0;
  awk -v i=$i '{ print $i}' ../fort.44 | /home/r4/flageul/dns_iztok/ar/arsel --subtract-mean > tmp;
  more tmp | head -n8 | tail -n1 | cut -c12- >> mean;
  more tmp | head -n9 | tail -n1 | cut -c12- >> sig;
  more tmp | head -n15 | tail -n1 | cut -c12- >> t0;
  paste mean sig t0 > fort.44.${i}.stat
  rm mean sig t0 tmp
done
#
echo "Done, terminus."
